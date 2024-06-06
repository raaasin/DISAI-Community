import streamlit as st
from duckduckgo_search import DDGS
from dotenv import load_dotenv
import google.generativeai as genai

st.sidebar.title("DISAI Webagent")
# Input Google Gemini API key here
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")
if api_key:
    genai.configure(api_key=api_key)

    def search(input_query):
        results = DDGS().text(input_query, max_results=10)  
        return str(results)

    def get_response(context, prompt):
        full_prompt = f"Here is the context, reply according to my internet search: {context}\n{prompt}"
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(full_prompt)
        return response.text

    st.title("💬 DISAI Webagent")
    st.caption("🚀 A Streamlit chat agent powered by DSAI Framework")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hi I am your LLM web agent connected to the internet. AMA! 😊"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        with st.spinner("Searching internet for the context..."):
            context = search(prompt)
        with st.spinner("Generating response..."):
            msg = get_response(context, prompt)
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
