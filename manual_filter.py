import video_check_yn
import video_check_accent
from tkinter import *
from tkinter.filedialog import askopenfilename

def browse():
    path=askopenfilename()
    return path


def yes_no_main():
    root=Tk()
    lb_sel=Label(root,text="select excel")
    lb_sel.grid(row=0,column=0)
    e_browse=Button(root,text="browse",command=lambda:[e_loc.insert(0,browse())])
    e_browse.grid(row=0,column=1)
    e_loc=Entry(root,width=25,borderwidth=5)
    e_loc.grid(row=0,column=2)

    lb_video_num=Label(root,text="select video number to start from")
    lb_video_num.grid(row=1,column=0)
    e_video_num=Entry(root,width=25,borderwidth=5)
    e_video_num.grid(row=1,column=1)
    btn_new=Button(root,text="Start manual check",command=lambda:[video_check_yn.check_video(e_loc.get(),e_video_num.get())])
    btn_new.grid(row=2,column=0)
    print("started")
    root.mainloop()


def accent_filter_main():
    root=Tk()
    lb_sel=Label(root,text="select excel")
    lb_sel.grid(row=0,column=0)
    e_browse=Button(root,text="browse",command=lambda:[e_loc.insert(0,browse())])
    e_browse.grid(row=0,column=1)
    e_loc=Entry(root,width=25,borderwidth=5)
    e_loc.grid(row=0,column=2)

    lb_video_num=Label(root,text="select video number to start from")
    lb_video_num.grid(row=1,column=0)
    e_video_num=Entry(root,width=25,borderwidth=5)
    e_video_num.grid(row=1,column=1)
    btn_new=Button(root,text="Start manual check",command=lambda:[video_check_accent.initialize_app(e_loc.get(),0) if e_video_num.get() == "" else video_check_accent.initialize_app(e_loc.get(),int(e_video_num.get()))])
    btn_new.grid(row=2,column=0)
    print("started")
    root.mainloop()   

