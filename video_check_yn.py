import os
from re import L
from selenium import webdriver
import keyboard
import pandas as pd
import time



def keypress_wait():
    '''waits for keyboard y , n or e key press to accept video, reject video or exit program.
        keys are only accepted once website opens
        returns a boolean value(True for accepted, False for rejected)    
    '''
    #while True:
    if keyboard.read_key() == "y":
        #print("You pressed y")
        return True
        
    elif keyboard.read_key() == "n":
        #print("you pressed n")
        return False

    elif keyboard.read_key() == "e":
        #print("you quit the program")
        return


def open_website(driver,url):    
    print("   driver   ")
    driver.get(url)
    #time.wait(1)
    #youtube_video_player = driver.find_elements_by_class_name("video-stream html5-main-video")
    #action = ActionChains(driver)
    val=keypress_wait()
    return val



def check_video(path,video_num):
    try:
        #urls=["https://www.youtube.com/watch?v=xXPBQc7utLY",
        #    "https://www.youtube.com/watch?v=Tu9rS8JA50Q","https://www.youtube.com/watch?v=cdZbEnDA7VU"]
        driver = webdriver.Chrome()
        print("0")
        print(os.listdir("./"))
        if "manual_check_us_healthcarepart2.xlsx" not in os.listdir("./"):  
            #manual_check_us_generalpart1.xlsx
            print("1")
            df=pd.DataFrame(columns=["Audio Name","Audio Link","Run Time"])
            df.to_excel("manual_check_us_healthcarepart2.xlsx")

        print("2")
        df=pd.read_excel(path)

        urls=df["Audio Link"].tolist()
        video_url_lst=[]
        video_names=df["Audio Name"].tolist()
        run_time=df["Run Time"].tolist()
        run_time_lst=[]
        video_names_lst=[]
        if video_num=="":
            video_num=0
        else:
            video_num=int(video_num)    
        for (num,url) in enumerate(urls):
            if num >=video_num:
                video_names_lst,video_url_lst,run_time_lst=[],[],[]
                try:
                    print(num)
                    print(video_names[num])
                    val=open_website(driver,url)
                    if val== None:
                        break
                    elif val:
                        run_time_lst.append(run_time[num])
                        video_url_lst.append(url)
                        video_names_lst.append(video_names[num])   
                except Exception as error:
                    print("error",num)
                    print(error)
                    continue       
            #print("num: ",num)  
        #print("data creation")       
            data={"Audio Name":video_names_lst,"Audio Link":video_url_lst,"Run Time":run_time_lst}
        #print("data frame creation:")
            df1=pd.DataFrame(data)
        #print("df: ",df1)
            with pd.ExcelWriter("./Excel Files/manual_yn.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                df1.to_excel(writer, sheet_name="Sheet1",header=None,startrow=writer.sheets["Sheet1"].max_row)         
        #print(video_lst)     
        #print("df1: ",df2)
        #print("vals: ",vals)
        #print(len(vals))
            
    except Exception as error:
        print(error)