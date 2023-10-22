import pandas as pd
import httpx
import asyncio




def get_urls_keywords(folder_name,location):
    #print("get_urls_keywords")
    tags=pd.read_excel(folder_name)
    if "keywords" in folder_name:
        tags=tags["keywords"].tolist()
    else:
        tags=tags["tag"]
    #keyword=pd.read_excel("keywords.xlsx")
    #keyword=keyword["keywords"].tolist()
    #tags=list(set(tags)-set(keyword))
    #print(keywrds_df["keywords"])
    url=[]
    loc=""
    base_link='https://www.youtube.com/results?search_query='
    if location=="United Kingdom":
        print("true")
        loc="uk"
    elif location=="Australia":
        loc="australia"
    elif location=="United States":
        loc="US"        
    else:
        print("false")    

    for words in tags:
        #print(words)
        wrd="".join([base_link,words])
        wrd="".join([wrd," {}".format(loc)])
        url.append(wrd)
    return url 