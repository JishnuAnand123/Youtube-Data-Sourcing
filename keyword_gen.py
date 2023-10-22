import openai
import pandas as pd
import os


def open_ai_prompt(subject):
    os.mkdir("./urls_sheets")
    openai.api_key ="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" #create an api key on openai website

    messages = [ {"role": "system", "content": 
                "100 {} keywords".format(subject)} ]

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    reply_split=reply.splitlines()
    messages.append({"role": "assistant", "content": reply})
    reply_insert=[]
    for i in reply_split:
        reply_insert.append(i[3:])
    columns=["keywords"]
    df=pd.DataFrame(reply_insert,columns=columns)
    df.to_excel('./urls_sheets/Keywords.xlsx')
