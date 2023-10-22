from operator import imod
from pdb import run
import time
from typing_extensions import runtime
import googleapiclient.discovery 
import pandas as pd
import os
import filter





def youtube_api_duration(path):
    
    df=pd.read_excel(path)
    urls=df["Audio Link"].tolist()
    names=df["Audio Name"].tolist()
    
    #urls=["https://www.youtube.com/watch?v=YJDkma1aBGo"]
    #print(url.index("="))
    duration=[]
    for num,url in enumerate(urls):
        run_time=""
        print(num)
        iden=""
        equal_index=url.index("=")
        iden=url[equal_index+1:]
        api_key="AIzaSyAhgfK7awYI9D3B_sYnCaBw4CQlJr6uxbM"
        youtube=googleapiclient.discovery.build("youtube","v3", developerKey=api_key)
        req=youtube.videos().list(id=iden,part="contentDetails")
        res=req.execute()
        time_unfil=res["items"][0]["contentDetails"]["duration"]
        time_unfil=time_unfil[2:]
        l=len(time_unfil)
        hr,min,sec="","",""
        print(time_unfil)
        if "H" in time_unfil:
            if "M" in time_unfil and "S" in time_unfil:
                hr=time_unfil[0]
                min=time_unfil[time_unfil.index("H")+1:time_unfil.index("M")]
                sec=time_unfil[time_unfil.index("M")+1:time_unfil.index("S")]
                if len(min)==1:
                    min="0"+min
                if len(sec)==1:
                    sec="0"+sec
                run_time=hr+":"+min+":"+sec

            elif "S" in time_unfil:
                hr=time_unfil[0]
                sec=time_unfil[time_unfil.index("H")+1:time_unfil.index("S")]
                if len(sec)==1:
                    sec="0"+sec

                run_time=hr+":00"+":"+sec

            elif "M" in time_unfil:
                hr=time_unfil[0]
                min=time_unfil[time_unfil.index("H")+1:time_unfil.index("M")]
                if len(min)==1:
                    min="0"+min
                run_time=hr+":"+min+":00"
                            

        elif "M" in time_unfil and "S" in time_unfil:
            min=time_unfil[0:time_unfil.index("M")]
            sec=time_unfil[time_unfil.index("M")+1:time_unfil.index("S")]
            if len(min)==1:
                min="0"+min
            if len(sec)==1:
                sec="0"+sec
            run_time="00:"+min+":"+sec

        elif "M" in time_unfil:
            min=time_unfil[0:time_unfil.index("M")]
            if len(min)==1:
                 run_time="00:0"+min+":00"
            else:
                run_time="00:"+min+":00"


        elif "S" in time_unfil:
            sec=time_unfil[0:time_unfil.index("S")]
            if len(sec)==1:
                run_time="00:00:0"+sec
            else:
                run_time="00:00:"+sec

        else:
            run_time=time_unfil           
        print(run_time)
        duration.append(run_time)
           
        
    data={"Audio Name":names,"Audio Link":urls,"Run Time":duration}
    df1=pd.DataFrame(data)
    filter.filter_time(names,urls,duration,path)
#print(res)
#print()
#print(res["items"][0]["contentDetails"]["duration"])
