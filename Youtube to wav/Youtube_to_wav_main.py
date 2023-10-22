from tkinter import *
import tkinter 
import pandas as pd
import subprocess
import os
from pydub import AudioSegment
from tkinter.filedialog import askopenfilename


def mp3_to_wav(file, filename,out_path):
    #info = AudioSegment.from_mp3(file)
    info = AudioSegment.from_file(file)

    info = info.set_frame_rate(16000)
    info = info.set_channels(1)

    # file = file.replace(".mp3", ".wav")
    # info.export(r"C:\Users\Dell\Desktop\\audios\\"+"audio-"+str(num)+".wav", format="wav", bitrate="256k") 
    info.export(out_path+'/'+filename[:-4]+'.wav', format="wav",bitrate="256k")
    print("Successfully changed")

def alternate_downloader(link,file_tag):
    #os.system('/home/admin1/anaconda3/bin/yt-dlp -f mp4 {}'.format(link))  # Output template for the MP3 file

    command = ['yt-dlp', '-x', '--audio-format', 'mp3', '-o', file_tag, link]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)  

def youtube_to_mp3(path,label2):
    df=pd.read_excel(path)
    video_name=df["Audio Name"].tolist()
    video_urls=df["Audio Link"].tolist()
    #video_name=video_name[:2]
    #video_urls=video_urls[:2]
    tot_len=len(video_urls)
    for num,(name,url) in enumerate(zip(video_name,video_urls)):
        save_path=f"./mp3 videos/{name}"
        label2.config(text=f"Downloading: {num} / {tot_len}")
        try:
            alternate_downloader(url,save_path)
        except:
            print('error')
    os.makedirs("./youtube wav")
    files=os.listdir("./mp3 videos/")
    output_file="./youtube wav/"
    tot_len=len(os.listdir("./mp3 videos/"))
    for num,file in enumerate(files):
        try:
            #label2.config(text=f"converting: {num} / {tot_len}")
            input_file=f"./mp3 videos/{file}"
            mp3_to_wav(input_file,file,output_file)
        except:
            print("error")            


def browse():
    path=askopenfilename()
    return path

def main():
    root=Tk()
    print("main")
    e_browse=Button(root,text="browse",command=lambda:[e_loc.insert(0,browse())])
    e_browse.grid(row=0,column=1)
    e_loc=Entry(root,width=25,borderwidth=5)
    e_loc.grid(row=0,column=2)
    label1 = Label(root, text="Status")
    label1.grid(row=1,column=0)
    label2=Label(root,text="")
    label2.grid(row=1,column=1)
    print("button")
    btn=Button(root,text="Download and convert",command=lambda:[youtube_to_mp3(e_loc.get(),label2)])
    btn.grid(row=2,column=1)
    print("1")
    print("main loop")
    root.mainloop()
    print("1")

if __name__=="__main__":
    main()