from os import name
from tkinter.font import names
import pandas as pd
import soupParser
import urlhtml
import filter
import soupParser
import get_keywords_tags
from selenium import webdriver
import asyncio



def url_scrapper_and_filter(key_used,folder_path,location,previous):

    previous_len=0
    if key_used=="keyword":
        if previous=="":    
            urls_present=set()
            df=pd.DataFrame(columns=["Audio Name","Audio Link"])
            df.to_excel("./urls_sheets/1.xlsx")

        else:
            print(previous)
            df=pd.read_excel(previous)
            urls_present=df["Audio Name"].tolist()
            name=df["Audio Link"].tolist()
            previous_len=len(name)
            data={"Audio Name":urls_present,"Audio Link":name}
            urls_present=set(urls_present)
            df=pd.DataFrame(data)
            df.to_excel("./urls_sheets/1.xlsx")

    else:
        df=pd.read_excel("./urls_sheets/1.xlsx")
        urls_present=set(df["Audio Name"].tolist())  
        df=pd.DataFrame(columns=["Audio Name","Audio Link"])
        df.to_excel("./urls_sheets/1.xlsx")
        
    urls=get_keywords_tags.get_urls_keywords(folder_path,location)
    #urls=urls[0:2]
    print(urls)
    driver=webdriver.Chrome()
    '''
    if key_used=="keyword":
        urls_present=set()
    else:
        df=pd.read_excel("./urls_sheets/keywords_urls.xlsx")
        urls_present=set(df["Audio Link"].tolist())  
        '''  
    for loop,url in enumerate(urls):
        print(loop)
        print(url)

        video_urls=[]
        titles=[]
        video_urls1=[]

        html=urlhtml.get_youtube_html(driver,url)

        titles,video_urls,urls_present=soupParser.Parser(html,urls_present)


        for u in video_urls:
            if "&pp=" in u:
                video_urls1.append(u[0:u.index("&pp=")])
            else:
                video_urls1.append(u) 
            #print(video_urls1)       


        video_urls=video_urls1

        titles,video_urls,urls_present=filter.filt(titles,video_urls,urls_present)


        data={"Audio Name":titles,"Audio Link":video_urls}
        df=pd.DataFrame(data)

        
        with pd.ExcelWriter("./urls_sheets/1.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
            df.to_excel(writer, sheet_name="Sheet1",header=None,startrow=writer.sheets["Sheet1"].max_row)
        
    print("get channel")

    
    df=pd.read_excel("./urls_sheets/1.xlsx")
    video_names_tot=df["Audio Name"].tolist() 
    video_urls_tot=df["Audio Link"].tolist()
    video_names_tot=video_names_tot[previous_len:]
    video_urls_tot=video_urls_tot[previous_len:]
    df=pd.DataFrame(columns=["Audio Name","Audio Link"])
    if key_used=="keyword":
        df.to_excel("./urls_sheets/keywords_urls.xlsx")
    else:
        df.to_excel("./urls_sheets/urls.xlsx")

    driver.close()    

    url_len=len(video_urls_tot)
    start=0
    end=1000

    while url_len>=0:
        try:
            if url_len<1000:
                end=url_len
            video_urls=video_urls_tot[start:end]
            video_names=video_names_tot[start:end]
            print(video_urls)
            print("video url: ",len(video_urls))
            print("video name: ",len(video_names))
            print("start: ",start)
            print("end: ",end)

            start=end
            end=end+1000
            url_len=url_len-1000


            channel_names=[]
            channel_htmls=asyncio.run(urlhtml.get_html_async(video_urls))

            for channel_html in channel_htmls:
                channel_names.append(soupParser.Parse_channel_name(channel_html))

            channel_urls=[]

            for channel_name in channel_names:
                channel_urls.append("https://www.youtube.com{}/about".format(channel_name))

            print("get location")    

            about_html=asyncio.run(urlhtml.get_html_async(channel_urls))

            location_bool=[]

            for i in about_html:
                location_bool.append(soupParser.check_loc_parser(i,location))    
            #print("loc bool len: ",len(location_bool))

            video_names,video_urls=filter.filt_by_loc(video_names,video_urls,location_bool)

            data={"Audio Name":video_names,"Audio Link":video_urls}
            df1=pd.DataFrame(data)
            print("num of videos: ",len(video_names))

            if key_used=="keyword":
                with pd.ExcelWriter("./urls_sheets/keywords_urls.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                    df1.to_excel(writer, sheet_name="Sheet1",header=None,startrow=writer.sheets["Sheet1"].max_row)
            else:
                with pd.ExcelWriter("./urls_sheets/urls.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                    df1.to_excel(writer, sheet_name="Sheet1",header=None,startrow=writer.sheets["Sheet1"].max_row)           
                video_names=[]
                video_urls=[]

        except Exception as error:
            print(error)
    
    if key_used=="tags":
        print()
        print("append")
        df=pd.read_excel("./urls_sheets/keywords_urls.xlsx")
        names=df["Audio Name"].tolist()
        audio_url=df["Audio Link"].tolist()
        data={"Audio Name":names,"Audio Link":audio_url}
        df=pd.DataFrame(data)
        #df1=pd.read_excel("./urls_sheets/urls.xlsx")
        with pd.ExcelWriter("./urls_sheets/urls.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
            df.to_excel(writer, sheet_name="Sheet1",header=None,startrow=writer.sheets["Sheet1"].max_row)
      


