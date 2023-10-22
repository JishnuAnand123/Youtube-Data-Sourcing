import os
from re import L
from selenium import webdriver
import pandas as pd
from tkinter import *
    

def initialize_app(path,video_num_initial):
    create_file()
    names,urls,runtimes=get_video_details(path)
    #print("start",video_num_initial)
    #print("open url")
    #print("App_gui")
    #print(urls)
    App_gui=create_tkinter_gui(names,urls,runtimes,video_num_initial,len(urls))
    #print("class")
    App_gui.attributes('-topmost',True)
    App_gui.mainloop()
    #print("Printed gui")

def create_file():
    if "Excel Files" not in os.listdir("./"):
        os.makedirs("./Excel Files")

    if "manual_accent.xlsx" not in os.listdir("./Excel Files"):
            df=pd.DataFrame(columns=["Audio Name","Audio Link","Run Time","Accent"])
            df.to_excel("./Excel Files/manual_accent.xlsx")

def create_tkinter_gui(names,urls,run_times,video_num_initial,video_num_last):
    root1=Tk()
    root1.geometry("300x400")
    class gui:
        def __init__(self,master,names,urls,run_times,video_num_initial,video_num_last):
            frame=Frame(master)
            frame.pack()

            self.lst_accent=Listbox(root1,height=13,width=10)
            self.lst_accent.pack()
            self.lst_accent.insert(1,"British uk")
            self.lst_accent.insert(2,"Irish")
            self.lst_accent.insert(3,"Scottish")
            self.lst_accent.insert(4,"Welsh")
            self.lst_accent.insert(5,"Geordie")
            self.lst_accent.insert(6,"Scouse")
            self.lst_accent.insert(7,"Yorkshire")
            self.lst_accent.insert(8,"Cockney")
            self.lst_accent.insert(9,"Brummie")
            self.lst_accent.insert(10,"Estuary English")
            self.lst_accent.insert(11,"Not sure")
            self.lst_accent.insert(12,"None")

            self.index_lbl=Label(root1,text=f"Video Number: {video_num_initial}",height=5,width=15)
            self.index_lbl.pack()
            self.lbl_accent=Label(root1,text="None")
            self.lbl_accent.pack()

            self.accept_btn = Button(root1, text="Confirm", command=lambda: [self.append_accent(self.names[self.current_idx],self.urls[self.current_idx],self.run_times[self.current_idx],self.lst_accent.get(self.lst_accent.curselection()[0])),self.increment_current(),self.next_website(self.urls[self.current_idx]) if not self.check_last() else self.index_lbl.config(text="All urls searched.")])
            self.accept_btn.pack()

            self.current_idx=video_num_initial
            self.last_idx=video_num_last-1
            self.webDriver=webdriver.Chrome()

            self.names=names
            self.run_times=run_times
            self.urls=urls
            self.accent="none"
            

            #print(self.urls)
            #print(self.current_idx)
            #print(self.webDriver)
            #print(self.check_last())

            self.lst_accent.bind("<<ListboxSelect>>", lambda event: self.update_accent(self.lst_accent.get(self.lst_accent.curselection()[0])))

        
            self.open_website()

        def update_accent(self,accent):
            print("update")
            self.lbl_accent.config(text=accent)


        def check_last(self):
            print("check")
            if self.current_idx>=self.last_idx:
                return True
            return False    
        
        def increment_current(self):
            self.current_idx+=1

        def next_website(self,url):
            print("next")
            print(self.webDriver)
            self.webDriver.get(url)

        def open_website(self):
            print("open")
            self.webDriver.get(self.urls[self.current_idx])

        def append_accent(self,name,url,run_time,accent):
            if "None" not in accent:
                name_lst,url_lst,run_time_lst,accent_lst=[name],[url],[run_time],[accent]
                print(run_time_lst)
                print(type(run_time))
                data={"Audio Name":name_lst,"Audio Link":url_lst,"Run Time":run_time_lst,"Accent":accent_lst}
                #print("data frame creation:")
                df1=pd.DataFrame(data)
                with pd.ExcelWriter("./Excel Files/manual_accent.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                    df1.to_excel(writer, sheet_name="Sheet1",header=None,startrow=writer.sheets["Sheet1"].max_row,index=False)         
                   

    e=gui(root1,names,urls,run_times,video_num_initial,video_num_last)
            
    return root1

def get_video_details(path):
    df=pd.read_excel(path)
    names=df["Audio Name"].tolist()
    urls=df["Audio Link"].tolist()
    run_times=df["Run Time"].tolist()
    return names,urls,run_times

def initialize_driver():
    web_driver = webdriver.Chrome()
    #web_driver.attributes('-topmost',True)
    return web_driver

def open_url(web_driver,url):
    web_driver.get(url)