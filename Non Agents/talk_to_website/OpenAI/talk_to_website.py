import streamlit as st
from duckduckgo_search import DDGS
from dotenv import load_dotenv
from openai import OpenAI
from newspaper import Article


st.sidebar.title("DISAI Talk to Website")
#input openAI key here
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
if api_key:
    client = OpenAI(api_key=api_key)
    website_link = st.text_input("Enter the website link to search",type="default")

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
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"You are an expert in analyzing website content and answering questions based on the provided content. Here is the context: {content}"},
                        {"role": "user", "content": prompt}
                    ]
                )
            st.write(response.choices[0].message.content)

