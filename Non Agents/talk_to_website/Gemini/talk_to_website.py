import streamlit as st
from duckduckgo_search import DDGS
from dotenv import load_dotenv
from newspaper import Article
import google.generativeai as genai

st.sidebar.title("DISAI Talk to Website")
# Input Google Gemini API key here
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    website_link = st.text_input("Enter the website link to search", type="default")

    def extract_text_from_url(url):
        article = Article(url)
        article.download()
        article.parse()
        return article.text

    if website_link:
        prompt = st.text_area("Enter the prompt for the webagent")
        if prompt:
            with st.spinner("Extracting content from the website"):
                content = extract_text_from_url(website_link)
            with st.spinner("Generating response"):
                response = model.generate_content(
                    f"You are an expert in analyzing website content and answering questions based on the provided content. Here is the context: {content}\n{prompt}"
                )
            st.write(response.text)
