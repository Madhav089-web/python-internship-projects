import streamlit as st
import google.generativeai as genai
import os
import time
# chats=[]

genai.configure(api_key="Your-Api-Key")
model = genai.GenerativeModel('gemini-2.5-flash')
st.header("First Chatbot")

    
usermsg=st.chat_input("Give Any Prompt")
print(usermsg)
if(usermsg):
            
            
            #  chats.append([usermsg,""])
            #  print(chats)
    reponse=model.generate_content(usermsg)
    print(reponse.text)

                
            
    with st.chat_message("user") as human:
        st.write(usermsg)
    with st.chat_message("ai") as ai:
        st.write(reponse.text)
        time.sleep(5)
            
         


else:
    ...

