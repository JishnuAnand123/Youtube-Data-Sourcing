from pytube import YouTube
#from pydub import AudioSegment
import pandas as pd
from moviepy.editor import *
import os
import subprocess
import openpyxl


excel_data="/home/admin1/Documents/Data_by_Pradeep/Inferencing/UK_English_Batch_1/Batch_1.3.xlsx"
save_path="/home/admin1/Documents/Data_by_Pradeep/Inferencing/UK_English_Batch_1/Batch_1.3/mp3/"


def read_xlsx_file(file_path):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    # for row in data:
    #     print(row)
    workbook.close()
    return data

def alternate_downloader(link,file_tag):
    #os.system('/home/admin1/anaconda3/bin/yt-dlp -f mp4 {}'.format(link))  # Output template for the MP3 file

    command = ['yt-dlp', '-x', '--audio-format', 'mp3', '-o', file_tag, link]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)    


def download_from_youtube():
 
    videos_in_dir=os.listdir(save_path)
    data=read_xlsx_file(excel_data)

    #print(excel_data)
    #print(excel_data["Audio Link"])
    for i in data:
        link=i[1]
        file_name=''.join(c for c in i[0] if c.isalpha())
        file_tag=save_path+'/'+file_name
        try:
            output
            alternate_downloader(link,file_tag)
        except:
            print('error')

download_from_youtube()