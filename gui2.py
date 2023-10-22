from tkinter import *
from tkinter.filedialog import askdirectory, askopenfilename
import keyword_gen
import scrapper
import filter
import youtube_api
import pandas as pd
import asyncio
import urlhtml
import soupParser
import manual_filter

def main_page():
    root=Tk()
    root.title("Main Page")
    root.geometry("500x400")
    lb_space=Label(root,text="").pack()
    btn_new=Button(root,text="new subject/location",command=subject_page,padx=10,pady=10).pack()
    lb_space=Label(root,text="").pack()
    btn_name=Button(root,text="name filter",command=name_fil_page,padx=10,pady=10).pack()
    lb_space=Label(root,text="").pack()
    btn_tags=Button(root,text="get tags and urls",command=tags_page,padx=10,pady=10).pack()
    lb_space=Label(root,text="").pack()
    btn_time=Button(root,text="time filter",command=time_fil_page,padx=10,pady=10).pack()
    lb_space=Label(root,text="").pack()
    btn_manual_filter=Button(root,command=manual_fil_page,text="filter videos manually",padx=10,pady=10).pack()
    #btn_manual=Button(root,text="manual filter",command=manual_fil_page).pack()
    root.mainloop()

def subject_page():
    top=Toplevel()
    top.title("subject page")
    top.geometry("800x300")

    lb_space=Label(top,text="  ")
    lb_space.grid(row=0,column=0)


    lb_sub=Label(top,text="  subject  ")
    lb_sub.grid(row=1,column=0)
    e_sub=Entry(top,width=25,borderwidth=5)
    e_sub.grid(row=1,column=1)

    lb_space=Label(top,text="")
    lb_space.grid(row=2,column=0)

    '''
    btn_browse=Button(top,text="Browse previous",command=lambda:[e_browse.insert(0,browse())])
    btn_browse.grid(row=3,column=0)
    e_browse=Entry(top,width=25,borderwidth=5)
    e_browse.grid(row=3,column=1)

    
        '''
    lb_space=Label(top,text="")
    lb_space.grid(row=4,column=0)

    
    btn_get_keywords=Button(top,text="get keyword",command=lambda:[gen_keywords(e_sub.get())])
    btn_get_keywords.grid(row=3,column=1)

    '''
    btn_browse=Button(top,text="Browse folder",command=lambda:[e_browse2.insert(0,browse_fol())])
    btn_browse.grid(row=6,column=0)
    e_browse2=Entry(top,width=25,borderwidth=5)
    e_browse2.grid(row=6,column=1)
    e_button_fol=Button(top,text="add folder values",command=lambda:[filter.add_fol_vals(e_browse2.get())])
    e_button_fol.grid(row=6,column=2)
    '''


    lb_space=Label(top,text="        ") 
    lb_space.grid(row=1,column=4)

    lb_loc=Label(top,text="location  ")
    lb_loc.grid(row=1,column=5)
    
    lb_space=Label(top,text="        ") 
    lb_space.grid(row=6,column=0)

    btn_get_url=Button(top,text="get urls and filter by location",command=lambda:[get_urls("keyword","./urls_sheets/keywords.xlsx",clicked.get(),e_browse.get())])
    btn_get_url.grid(row=7,column=6)


    btn_browse=Button(top,text="Browse previous",command=lambda:[e_browse.insert(0,browse())])
    btn_browse.grid(row=3,column=5)
    e_browse=Entry(top,width=25,borderwidth=5)
    e_browse.grid(row=3,column=6)


    btn_browse=Button(top,text="Browse folder",command=lambda:[e_browse2.insert(0,browse_fol())])
    btn_browse.grid(row=5,column=5)
    e_browse2=Entry(top,width=25,borderwidth=5)
    e_browse2.grid(row=5,column=6)
    e_button_fol=Button(top,text="add folder values",command=lambda:[filter.add_fol_vals(e_browse2.get())])
    e_button_fol.grid(row=5,column=7)


    clicked=StringVar()
    listbox = OptionMenu(top, clicked , "United Kingdom","United States","Australia")
    listbox.grid(row=1,column=6)
    
    listbox.insert(1,"United Kingdom")
    listbox.insert(2,"United States")
    listbox.insert(3,"Australia")

    lb_space=Label(top,text="")
    lb_space.grid(row=4,column=0)


def name_fil_page():
    top=Toplevel()
    top.title("filter name")
    top.geometry("800x300")

    lb_space=Label(top,text="   ")
    lb_space.grid(row=0,column=0)

    lb_keys=Label(top,text="enter keys to keep  ")
    lb_keys.grid(row=1,column=1)
    e_excel1=Entry(top,width=25,borderwidth=5)
    e_excel1.grid(row=1,column=2)

    lb_space=Label(top,text="")
    lb_space.grid(row=2,column=0)

    lb_loc=Label(top,text="select excel  ")
    lb_loc.grid(row=3,column=1)
    bt_browse=Button(top,text="Browse",command=lambda:[e_loc1.insert(0,browse())])
    bt_browse.grid(row=3,column=3)
    e_loc1=Entry(top,width=25,borderwidth=5)
    e_loc1.grid(row=3,column=2)

    lb_space=Label(top,text="")
    lb_space.grid(row=4,column=0)

    btn_get_keywords=Button(top,text="filter keys",command=lambda:[filt_name(e_loc1.get(),e_excel1.get())])
    btn_get_keywords.grid(row=5,column=2)

    lb_keys=Label(top,text="   ")
    lb_keys.grid(row=1,column=4)

    lb_keys=Label(top,text="enter keys to keep  ")
    lb_keys.grid(row=1,column=5)
    e_excel2=Entry(top,width=25,borderwidth=5)
    e_excel2.grid(row=1,column=6)


    lb_loc=Label(top,text="select excel  ")
    lb_loc.grid(row=3,column=5)
    bt_browse=Button(top,text="Browse",command=lambda:[e_loc2.insert(0,browse())])
    bt_browse.grid(row=3,column=6)
    e_loc2=Entry(top,width=25,borderwidth=5)
    e_loc2.grid(row=3,column=7)

    btn_get_keywords=Button(top,text="filter tags",command=lambda:[filt_tag_name(e_loc2.get(),e_excel2.get())])
    btn_get_keywords.grid(row=5,column=5)




def time_fil_page():
    top=Toplevel()
    top.title("filter time")
    top.geometry("500x300")

    lb_space=Label(top,text="    ")
    lb_space.grid(row=0,column=0)

    lb_loc=Label(top,text="select excel  ")
    lb_loc.grid(row=1,column=1)
    bt_browse=Button(top,text="Browse",command=lambda:[e_loc.insert(0,browse())])
    bt_browse.grid(row=1,column=3)
    e_loc=Entry(top,width=25,borderwidth=5)
    e_loc.grid(row=1,column=2)

    lb_space=Label(top,text="")
    lb_space.grid(row=2,column=0)

    btn_get_keywords=Button(top,text="filter time",command=lambda:[filt_time(e_loc.get())])
    btn_get_keywords.grid(row=3,column=2)

def tags_page():
    top=Toplevel()
    top.title("tags")
    top.geometry("500x300")

    lb_space=Label(top,text=" ")
    lb_space.grid(row=0,column=0)

    lb_loc=Label(top,text="select excel  ")
    lb_loc.grid(row=1,column=1)
    e_loc=Entry(top,width=25,borderwidth=5)
    e_loc.grid(row=1,column=2)
    bt_browse=Button(top,text="Browse",command=lambda:[e_loc.insert(0,browse())])
    bt_browse.grid(row=1,column=3)

    lb_space=Label(top,text="         ")
    lb_space.grid(row=1,column=4)

    btn_get_keywords=Button(top,text="  get urls  ",command=lambda:[get_urls("tags","./urls_sheets/tags.xlsx",clicked.get(),"")])
    btn_get_keywords.grid(row=3,column=6)

    lb_location=Label(top,text="enter location  ")
    lb_location.grid(row=1,column=5)

    clicked=StringVar()
    location=OptionMenu(top,clicked,"United Kingdom","United States","Australia")
    location.grid(row=1,column=6)



    lb_space=Label(top,text="")
    lb_space.grid(row=2,column=0)

    btn_get_keywords=Button(top,text="  get tags  ",command=lambda:[get_tags(e_loc.get())])
    btn_get_keywords.grid(row=3,column=2)


def manual_fil_page():
    top=Toplevel()
    '''
    top.title("manually filter")
    lb_loc=Label(top,text="select excel")
    lb_loc.grid(row=0,column=0)
    bt_browse=Button(top,text="Browse",command=lambda:[e_loc.insert(0,browse())])
    bt_browse.grid(row=0,column=1)
    e_loc=Entry(top,width=25,borderwidth=5)
    e_loc.grid(row=0,column=2)
    '''

    '''
    lb_loc=Label(top,text="enter the name of excel sheet")
    lb_loc.grid(row=1,column=0)
    bt_browse=Button(top,text="Browse",command=lambda:[e_loc.insert(0,browse())])
    bt_browse.grid(row=1,column=1)
    e_loc=Entry(top,width=25,borderwidth=5)
    e_loc.grid(row=1,column=2)
    '''

    '''
    lb_loc=Label(top,text="enter number of url to start from")
    lb_loc.grid(row=2,column=0)
    e_loc=Entry(top,width=25,borderwidth=5)
    e_loc.grid(row=2,column=1)
    '''

    space_label=Label(top,text="    ")
    space_label.grid(row=0,column=0)

    space_label=Label(top,text="    ")
    space_label.grid(row=0,column=1)

    space_label=Label(top,text="    ")
    space_label.grid(row=0,column=2)

    btn_get_keywords=Button(top,command=manual_filt_yn,text="filter manually(Y/N)")
    btn_get_keywords.grid(row=1,column=1)

    btn_get_keywords=Button(top,command=manual_filt_accent,text="filter manually(Accent)")
    btn_get_keywords.grid(row=1,column=2)


def manual_filt_yn():
    manual_filter.yes_no_main()

def manual_filt_accent():
    manual_filter.accent_filter_main()   



def browse():
    path=askopenfilename()
    return path

def browse_fol():
    path=askdirectory()
    return path

def gen_keywords(subject):
    keyword_gen.open_ai_prompt(subject)

def get_urls(key_used,folder_path,location,previous):
    scrapper.url_scrapper_and_filter(key_used,folder_path,location,previous)  

def filt_name(path,keys):
    filter.keep_by_name(path,keys)

def filt_tag_name(path,tags):
    filter.filt_tag_name(path,tags)    

def filt_time(path):
    youtube_api.youtube_api_duration(path)


def get_tags(path):
    df=pd.read_excel(path)
    urls=df["Audio Link"].tolist() 
    htmls=asyncio.run(urlhtml.get_html_async(urls))
    tags=soupParser.get_tags_parser(htmls)
    data={"tag":tags}
    df=pd.DataFrame(data)
    df.to_excel("./urls_sheets/tags.xlsx")


          
    
