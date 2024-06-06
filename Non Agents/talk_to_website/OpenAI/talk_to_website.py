import streamlit as st
from duckduckgo_search import DDGS
from dotenv import load_dotenv
from openai import OpenAI


st.sidebar.title("DISAI Webagent")
#input openAI key here
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
if api_key:
    client = OpenAI(api_key=api_key)
    def search(input_query):
        results = DDGS().text(input_query, max_results=10)  
        return str(results)

    def get_response(context, prompt):

        full_prompt = f"Here is the context , reply with according to my internet search{context}\n{prompt}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Internet search agent, you search internet and tell asnwers according to the context."},
                {"role": "user", "content": full_prompt}
            ]
        )
        return response.choices[0].message.content
        

    st.title("💬 DISAI Webagent ")
    st.caption("🚀 A streamlit chat agent powered by DSAI Framework")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hi I am your Llm web agent connected to internet. AMA! 😊"}]

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
        #print(chat_history)
