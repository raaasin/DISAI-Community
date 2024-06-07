# DISAI Graph Generator Documentation

## Overview

This Streamlit application, DISAI Graph Generator, allows users to upload CSV, Excel, or SQLite database files, interactively query the data using OpenAI's GPT-3.5-turbo model, and visualize the results with Matplotlib.

## Steps with Logic

1. **Streamlit App Initialization**:

   - Initialize the Streamlit app and create the UI elements, such as titles and sidebars.
2. **API Key Input**:

   - Users provide their OpenAI API key through a sidebar text input.
3. **File Upload**:

   - Users can upload a CSV, Excel, or SQLite database file.
4. **File Handling**:

   - Depending on the file type, the app processes the file:
     - For CSV/Excel: Load into a DataFrame, save as CSV, and gather metadata.
     - For SQLite: Save the file and extract the database schema.
5. **User Query Input**:

   - Users input their query or prompt in the main text input field.
6. **Prompt Creation and Response**:

   - Create a dynamic prompt based on the uploaded data or database schema.
   - Use the OpenAI API to generate a response to the user's query.
7. **Code Execution and Visualization**:

   - If the response contains Python code for Matplotlib, execute the code to generate a graph.
   - Display the generated graph or query results in the Streamlit app.

## Function Explanations

### `save_csv_file(df)`

Saves a DataFrame to a CSV file named "data.csv".

### `get_csv_metadata(df)`

Gathers metadata from a DataFrame, including column names, data types, null values, and example data.

### `get_db_schema(db_path)`

Extracts the schema from an SQLite database, including table names and column names.

### `create_prompt(schema)`

Creates a prompt string for the OpenAI model based on the database schema, providing examples for SQL query generation.

### `get_response(question, prompt, api_key)`

Uses the OpenAI API to get a response to a user query based on the provided prompt.

### `read_sql_query(sql, db_path)`

Executes an SQL query on an SQLite database and returns the results.

### `main()`

Defines the main logic of the Streamlit app, including UI elements, file handling, query processing, and result visualization.

## Architecture Flowchart

```plaintext
+------------------------------------------+
|                  UI Layer                |
|               (Streamlit)                |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|              Service Layer               |
|            (OpenAI API, Pandas)          |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|               Model Layer                |
|     (OpenAI GPT-3.5-turbo, Matplotlib)   |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|              Storage Layer               |
|       (CSV Files, SQLite Database)       |
+------------------------------------------+
```

### Detailed Layer Descriptions

- **UI Layer**:

  - **Technology**: Streamlit
  - **Components**: File uploader, API key input, text input for user queries, display areas for results and graphs.
- **Service Layer**:

  - **Technologies**: OpenAI API for natural language processing, Pandas for data manipulation.
  - **Functions**: Handling API requests, processing uploaded data, and preparing prompts.
- **Model Layer**:

  - **Technologies**: OpenAI GPT-3.5-turbo for generating responses, Matplotlib for plotting graphs.
  - **Functions**: Generating SQL queries and Python code for visualization based on user input and data.
- **Storage Layer**:

  - **Technologies**: CSV files for storing uploaded data, SQLite database for database uploads.
  - **Functions**: Saving and retrieving data, managing file storage.

This architecture ensures a smooth flow of data from user inputs to API calls, data processing, and visualization, providing a seamless interactive experience.
