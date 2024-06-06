import streamlit as st
import pandas as pd
import sqlite3
from dotenv import load_dotenv
import os
from openai import OpenAI

# Function to save CSV file
def save_csv_file(df):
    df.to_csv("data.csv", index=False)

# Function to gather metadata about the CSV file
def get_csv_metadata(df):
    metadata = {
        "columns": df.columns.tolist(),
        "data_types": df.dtypes.to_dict(),
        "null_values": df.isnull().sum().to_dict(),
        "example_data": df.head().to_dict()
    }
    return metadata

# Function to get database schema
def get_db_schema(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    schema = {}
    for table in tables:
        table_name = table[0]
        cur.execute(f"PRAGMA table_info({table_name});")
        columns = cur.fetchall()
        schema[table_name] = [col[1] for col in columns]
    conn.close()
    return schema

# Function to create prompt dynamically for SQL queries
def create_prompt(schema):
    schema_str = "The database schema is as follows:\n"
    for table, columns in schema.items():
        schema_str += f"Table {table} with columns {', '.join(columns)}.\n"
    return f"You are an expert in converting English questions to SQL query! {schema_str}\nFor example,\nExample 1 - How many entries of records are present in STUDENT?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ; \nExample 2 - Tell me all the students studying in Data Science class in STUDENT?, the SQL command will be something like this SELECT * FROM STUDENT where CLASS='Data Science'; also the sql code should not have ``` in beginning or end and sql word in output"

# Function to load Google Gemini Model and provide queries as response
def get_response(question, prompt, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# Function to retrieve query from the database
def read_sql_query(sql, db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define Streamlit app
def main():
    st.title("DIGIOTAI GRAPH GENERATOR")

    st.sidebar.title("OpenAI API Key")
    st.sidebar.write("You can find your API key at https://platform.openai.com/account/api-keys")
    OPENAI_API_KEY = st.sidebar.text_input("API Key", type="password")
    
    if OPENAI_API_KEY:
        client = OpenAI(api_key=OPENAI_API_KEY)
        st.sidebar.title("Upload File")
        uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx", "db"])
        
        if uploaded_file is not None:
            file_type = uploaded_file.name.split('.')[-1]
            
            if file_type == 'csv':
                df = pd.read_csv(uploaded_file)
                save_csv_file(df)
                st.sidebar.success("CSV file uploaded successfully!")

                csv_metadata = get_csv_metadata(df)
                metadata_str = ", ".join(csv_metadata["columns"])

                st.subheader("Enter your query:")
                user_query = st.text_input("")

                if user_query:
                    prompt_eng = (
                        f"You are graphbot. If the user asks to plot a graph, you only reply with the Python code of Matplotlib to plot the graph and save it as graph.png. "
                        f"The data is in data.csv and its attributes are: {metadata_str}. If the user does not ask for a graph, you only reply with the answer to the query. "
                        f"The user asks: {user_query}"
                    )

                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt_eng}
                        ]
                    )

                    generated_content = st.empty()
                    all_text = ""

                    for choice in response.choices:
                        chunk_message = choice.message.content if choice.message else ''
                        all_text += chunk_message
                        generated_content.text(all_text)

                    code_start = all_text.find("```python") + 9
                    code_end = all_text.find("```", code_start)
                    code = all_text[code_start:code_end]

                    generated_content.code(code, language="python")

                    if 'import matplotlib' in code:
                        try:
                            exec(code)
                            st.image("graph.png")
                        except Exception as e:
                            prompt_eng = f"There has occurred an error while executing the code, please take a look at the error and strictly only reply with the full python code do not apologize or anything just give the code {str(e)}"
                            response = client.chat.completions.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system", "content": "You are a helpful assistant."},
                                    {"role": "user", "content": prompt_eng}
                                ]
                            )
                            all_text = ""
                            for choice in response.choices:
                                chunk_message = choice.message.content if choice.message else ''
                                all_text += chunk_message
                                generated_content.text(all_text)

                            code_start = all_text.find("```python") + 9
                            code_end = all_text.find("```", code_start)
                            code = all_text[code_start:code_end]

                            generated_content.code(code, language="python")
                            try:
                                exec(code)
                                st.image("graph.png")
                            except Exception as e:
                                st.error("Failed to generate the chart. Please try later.")

            elif file_type == 'xlsx':
                df = pd.read_excel(uploaded_file)
                save_csv_file(df)
                st.sidebar.success("Excel file uploaded successfully!")

                csv_metadata = get_csv_metadata(df)
                metadata_str = ", ".join(csv_metadata["columns"])

                st.subheader("Enter your query:")
                user_query = st.text_input("")

                if user_query:
                    prompt_eng = (
                        f"You are graphbot. If the user asks to plot a graph, you only reply with the Python code of Matplotlib to plot the graph and save it as graph.png. "
                        f"The data is in data.csv and its attributes are: {metadata_str}. If the user does not ask for a graph, you only reply with the answer to the query. "
                        f"The user asks: {user_query}"
                    )

                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt_eng}
                        ]
                    )

                    generated_content = st.empty()
                    all_text = ""

                    for choice in response.choices:
                        chunk_message = choice.message.content if choice.message else ''
                        all_text += chunk_message
                        generated_content.text(all_text)

                    code_start = all_text.find("```python") + 9
                    code_end = all_text.find("```", code_start)
                    code = all_text[code_start:code_end]

                    generated_content.code(code, language="python")

                    if 'import matplotlib' in code:
                        try:
                            exec(code)
                            st.image("graph.png")
                        except Exception as e:
                            prompt_eng = f"There has occurred an error while executing the code, please take a look at the error and strictly only reply with the full python code do not apologize or anything just give the code {str(e)}"
                            response = client.chat.completions.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system", "content": "You are a helpful assistant."},
                                    {"role": "user", "content": prompt_eng}
                                ]
                            )
                            all_text = ""
                            for choice in response.choices:
                                chunk_message = choice.message.content if choice.message else ''
                                all_text += chunk_message
                                generated_content.text(all_text)

                            code_start = all_text.find("```python") + 9
                            code_end = all_text.find("```", code_start)
                            code = all_text[code_start:code_end]

                            generated_content.code(code, language="python")
                            try:
                                exec(code)
                                st.image("graph.png")
                            except Exception as e:
                                st.error("Failed to generate the chart. Please try later.")

            elif file_type == 'db':
                db_path = f"uploaded_file_{uploaded_file.name}"
                with open(db_path, 'wb') as f:
                    f.write(uploaded_file.getbuffer())
                st.sidebar.success("Database file uploaded successfully!")

                db_schema = get_db_schema(db_path)
                prompt = create_prompt(db_schema)

                st.subheader("Enter your query:")
                user_query = st.text_input("")

                if user_query:
                    sql_query = get_response(user_query, prompt, OPENAI_API_KEY)
                    st.subheader("Generated SQL Query:")
                    st.code(sql_query, language="sql")

                    try:
                        result = read_sql_query(sql_query, db_path)
                        st.subheader("Query Result:")
                        st.write(result)
                    except Exception as e:
                        st.error(f"Failed to execute the query: {str(e)}")
        else:
            st.sidebar.info("Please upload a file first.")
    else:
        st.sidebar.warning("Please enter your OpenAI API key.")

if __name__ == "__main__":
    main()
