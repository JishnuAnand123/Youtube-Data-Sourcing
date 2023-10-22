import keyword
import time
from tkinter.font import names
from turtle import title
import pandas as pd
import os


def filt(titles,video_urls,urls_present):
    if "folder.xlsx" in os.listdir("./urls_sheets/"):
        df=pd.read_excel("./urls_sheets/folder.xlsx")
        fold=df["names"].tolist()
        print("titles_len:",len(titles))
        names_fold=[]
        for i in fold:
            names_fold.append(i.lower())
        names_fold=set(names_fold)
       

        name_n=[]
        link_n=[]

        titles_special=[]
        for i in titles:
            str="".join(letter for letter in i if letter.isalnum())
            titles_special.append(str.lower())

        print(titles_special)
        print(names_fold)      

        l=len(names_fold)
        for num,t in enumerate(titles_special):
            if l!=names_fold.add(t):
                name_n.append(titles[num])
                link_n.append(video_urls[num])
                l=len(names_fold) 

        titles=name_n
        video_urls=link_n
        print("len_titles_fil:",len(titles))           

        '''     
            
        for num,t in enumerate(titles_special):
            for i in names_fold:
                if i.lower()  not in t.lower():
                    name_n.append(titles[num])
                    link_n.append(video_urls[num])
                    #run_times_n.append(run_times_n2[num])
        titles=name_n
        video_urls=link_n
        print("titles_len_filt",len(titles))            
        '''
                 
    
    filter_keywords_name=["indian","malayalam","hindi","desi","india","pakisthan","pakistani","ayat","sunlife","US","sri"]



    name_n2=titles
    name_n=[]
    link_n2=video_urls
    link_n=[]
    #run_times_n2=run_times_n
    #run_times_n=[]
    #print(type(urls_present))
    l=len(urls_present)
    for num,t in enumerate(name_n2):
        #print(t)
        #print(type(t))
        urls_present.add(t)
        if l!=len(urls_present) :
            name_n.append(t)
            link_n.append(link_n2[num])
            #run_times_n.append(run_times_n2[num])
            l=len(urls_present)

    for num,t in enumerate(name_n2):
        #print(t)
        #print(type(t))
        urls_present.add(t)
        if l!=len(urls_present):
            name_n.append(t)
            link_n.append(link_n2[num])
            #run_times_n.append(run_times_n2[num])
            l=len(urls_present)        
            



    name_lwr_n=[x.lower() for x in name_n]
    name_n2=name_n
    name_n=[]
    link_n2=link_n
    link_n=[]

    for (num,name) in enumerate(name_lwr_n):
        flag=True
        for word in filter_keywords_name:
            if word in name:
                flag=False
                break
        if flag:
            name_n.append(name_n2[num])
            link_n.append(link_n2[num])
            #run_times_n.append(run_times_n2[num])

    name_n2=name_n
    name_n=[]
    link_n2=link_n
    link_n=[]        
    for num,n in enumerate(link_n2):
        if "shorts" in n:
            continue
        else:
            name_n.append(name_n2[num])
            link_n.append(link_n2[num])

    #print(name_n)
    #print(link_n)        
    return name_n,link_n,urls_present 

def filt_by_loc(video_names,video_urls,location_bool):
    video_names_n,video_urls_n=[],[]
    for num,i in enumerate(location_bool):
        if i:
            video_names_n.append(video_names[num])
            video_urls_n.append(video_urls[num])

    print("filt name: ",len(video_names_n))
    print("filt url: ",len(video_urls_n))        
    return video_names_n,video_urls_n  


def keep_by_name(path,keywords):
    df=pd.DataFrame(columns=["Audio Name","Audio Link"])
    names_final,urls_final=[],[]
    df=pd.read_excel(path)
    titles=df["Audio Name"]
    urls=df["Audio Link"]
    print(titles)
    keywords_lst=keywords.split(",")
    print(keywords)
    print(keywords_lst)
    for (title,url) in zip(titles,urls):
        for i in keywords_lst:
            if i in title.lower():
                names_final.append(title)
                urls_final.append(url)
                break 

    print(names_final)
    data={"Audio Name":names_final,"Audio Link":urls_final}            
    df=pd.DataFrame(data)
    df.to_excel(path)


def filter_time(names,urls,duration,path):
    duration_filt=[]
    names_filt=[]
    urls_filt=[]

    for (name,url,time) in zip(names,urls,duration):
        if type(time)==str:
            if time[0:5]=="00:00" or time[0:5]=="00:01": 
            #or time[0:5]=="00:02":
                continue
            else:
                duration_filt.append(time)
                names_filt.append(name)
                urls_filt.append(url)

        else:
            duration_filt.append("00:03:00")

            names_filt.append(name)
            urls_filt.append(url)
    data={"Audio Name":names_filt,"Audio Link":urls_filt,"Run Time":duration_filt}
    df=pd.DataFrame(data)
    path1="./urls_sheets/urls"
    df.to_excel(path) 


def filt_tag_name(path,keys):
    #df=pd.DataFrame(columns=["Audio Name","Audio Link"])
    tags_final=[]
    df=pd.read_excel(path)
    tags=df["tag"].tolist()
    key_lst=keys.split(",")
    print(path)
    #print(keywords)
    for tag in tags:
        for key in key_lst:
            if key.lower() in tag.lower():
                tags_final.append(tag)
                break
    tags_final=list(set(tags_final))            
    print(tags_final)
    data={"tag":tags_final}            
    df=pd.DataFrame(data)
    df.to_excel(path)


def add_fol_vals(path):
    names=os.listdir(path)
    name_final=[]
    for name in names:
        print(name[:-4])
        name_final.append(name[:-4])
    data={"names":name_final}
    df=pd.DataFrame(data)
    df.to_excel("./urls_sheets/folder.xlsx")    



               
