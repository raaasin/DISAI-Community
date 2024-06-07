import os
import streamlit as st
from functions import *
import openai
from streamlit_chat import message
from streamlit_image_select import image_select
from dotenv import load_dotenv
import re
load_dotenv()

API_KEY= os.environ['OPENAI_API_KEY'] 

def get_text(n):
    input_text= st.text_input('', '', key="input{}".format(n))
    return input_text 

def show_data(tabs, df_arr):
    for i, df_ in enumerate(df_arr):
        print(i, len(df_))
        with tabs[i]:
            st.dataframe(df_)

def main():
    st.title("Talk To CSV using Agentic Approach")
    openai_key = API_KEY
    uploaded_file = st.file_uploader("Choose files to upload (csv, xls, xlsx)", type=["csv", "xls", "xlsx"], accept_multiple_files=True)
    agent = ''
    if uploaded_file:
        for file in uploaded_file:
            agent, selected_df, selected_df_names = save_uploaded_file(file)
        st.session_state["tabs"].clear()
        for df_name in selected_df_names:
            st.session_state.tabs.append(df_name)
        #tabs = st.tabs([s.center(9,"\u2001") for s in st.session_state["tabs"]])
        #show_data(tabs, selected_df)
    
    x = 0
    user_input = get_text(x)
    if st.button('Query'):
        x+=1
        print(user_input, len(user_input))
        with st.spinner('Processing...'):
            response, thought, action, action_input, observation = run_query(agent, user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        pattern = r"'([^']+\.png)'"
        match = re.search(pattern, response)
        if match:
            filename = match.group(1)
            st.image(filename)
        else:
            st.write(response)


if __name__ == "__main__":
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []
    
    if 'tabs' not in st.session_state:
        st.session_state['tabs'] = []

    main()