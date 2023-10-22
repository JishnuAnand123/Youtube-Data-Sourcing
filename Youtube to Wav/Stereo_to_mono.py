from pydub import AudioSegment
import os
import sys

input_path=sys.argv[1]
output_path=sys.argv[2]
#print(output_path)

def change_properties(file, filename,out_path):
    #info = AudioSegment.from_mp3(file)
    info = AudioSegment.from_file(file)

    info = info.set_frame_rate(16000)
    info = info.set_channels(1)
    #, 

    # file = file.replace(".mp3", ".wav")
    # info.export(r"C:\Users\Dell\Desktop\\audios\\"+"audio-"+str(num)+".wav", format="wav", bitrate="256k") 
    info.export(out_path+'/'+filename[:-4]+'.wav', format="wav",bitrate="256k")
    print("Successfully changed")


#path="/home/admin1/Documents/Data_by_Pradeep/Aus_Eng_Batch_3_7hrs/AU_en_Batch_3_Jun_03-Part2/"
files = os.listdir(input_path)  
#print(files) 
for f in files:
    print(f)
    #wav_name=''.join(c for c in f if c.isalpha())
    #print(wav_name)
    file_path=input_path+'/'+f
    change_properties(file_path,f,output_path) 