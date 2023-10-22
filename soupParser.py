from bs4 import BeautifulSoup

def Parser(html,urls_present):
    #if request is used use
    #html.text
    base_url="https://www.youtube.com"
    title_list,video_url_list=[],[]
    soup = BeautifulSoup(html, 'lxml')
    titles = soup.findAll('a', id='video-title')
    video_urls = soup.findAll('a', id='video-title')

    for j,title in enumerate(titles):
        new_title=title.text.replace("\n","")
        title_list.append(new_title)
        new_video_url="".join([base_url,video_urls[j].get('href')])
        #print(new_video_url)
        video_url_list.append(new_video_url)

    return title_list,video_url_list,urls_present

def Parse_channel_name(html):

    i=html.find("/@")
    name=""
    while html[i]!='"':
        name="".join([name,html[i]])
        i+=1         
    return name 

def check_loc_parser(html,location):
    if location in html:
        return 1
    else:
        return 0
    

def get_tags_parser(htmls):
    tags_final=[]
    for html in htmls:
        html=BeautifulSoup(html,"html.parser")
        tags=html.find_all("meta",property="og:video:tag")
        for tag in tags:
            tags_final.append(tag["content"])    
    return tags_final        
    
