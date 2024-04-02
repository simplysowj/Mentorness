import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from constant import *
from PIL import Image
import openai
from langchain.chat_models import ChatOpenAI

from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms import Gemini
from IPython.display import Markdown, display
from llama_index import ServiceContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index.prompts import PromptTemplate
#import chromadb
import os

import streamlit as st
import os
import pathlib
import textwrap



import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# -----------------  chatbot  ----------------- #
# Set up the OpenAI key
openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
openai.api_key = (openai_api_key)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\style\style.css")

genai.configure(api_key=openai_api_key)

# load the file

file_path = r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\bio.txt"

documents = SimpleDirectoryReader(input_files=[file_path]).load_data()


#db = chromadb.PersistentClient(path="./embeddings/chroma_db")
#chroma_collection = db.get_or_create_collection("quickstart")
pronoun = info["Pronoun"]
name = info["Name"]
## Function to load OpenAI model and get respones





def ask_bot(input_text):
    model = genai.GenerativeModel('gemini-pro')
    


    response = model.generate_content(input_text)
    
    
    return response.text

##initialize our streamlit app

#st.set_page_config(page_title='Template' ,layout="wide",page_icon='👧🏻')














# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("After providing OpenAI API Key on the sidebar, you can send your questions and hit Enter ", key="input")
    return input_text

#st.markdown("Chat With Me Now")
user_input = get_text()

if user_input:
  #text = st.text_area('Enter your questions')
  if not openai_api_key:
    st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
  else:
    st.info(ask_bot(user_input))

# -----------------  loading assets  ----------------- #
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)
st.sidebar.markdown(info['Github'],unsafe_allow_html=True)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# loading assets
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")

#st.sidebar.image(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\images\profile.jpg", width=150, caption="Profile Picture")
# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#000080','#007fff','00004c',f"<br><p style='color:#ffffff;font-size: 50px;font-family: Daydream, sans-serif;'>Hi, I'm {full_name}😊</p>", info["Intro"])
    st.write("")
    st.write(info['About'])


    
with col2:
    st_lottie(lottie_gif, height=280, key="data")
        


# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)