# DIGIOTAI Graph Generator Application

## Overview

This documentation provides a detailed overview of the DIGIOTAI Graph Generator application built using Streamlit. The application allows users to upload CSV, Excel, or SQLite database files, generate metadata, and interact with the Google Gemini AI model to create SQL queries and Matplotlib plots.

## Steps with Logic

1. **Import Libraries**:

   - Import necessary libraries including `streamlit`, `pandas`, `sqlite3`, and `google.generativeai`.
2. **Define Functions**:

   - Define helper functions to save CSV files, gather metadata, retrieve database schema, create prompts, generate responses using the Google Gemini model, and execute SQL queries.
3. **Streamlit Application Structure**:

   - Set up the Streamlit interface with a sidebar for API key input and file upload options.
   - Handle different file types (CSV, Excel, and SQLite databases) and process them accordingly.
   - Generate metadata for CSV and Excel files and display SQL query results for database files.
   - Utilize the Google Gemini model to generate SQL queries and Matplotlib plot code based on user input.
4. **Run the Streamlit Application**:

   - Call the `main()` function to run the Streamlit application.

## Functions Explanation

### `save_csv_file(df)`

- **Purpose**: Save the DataFrame to a CSV file.
- **Parameters**:
  - `df` (pandas.DataFrame): DataFrame to be saved.
- **Returns**: None

### `get_csv_metadata(df)`

- **Purpose**: Gather metadata about the CSV file.
- **Parameters**:
  - `df` (pandas.DataFrame): DataFrame from which metadata is extracted.
- **Returns**:
  - `metadata` (dict): Dictionary containing columns, data types, null values, and example data.

### `get_db_schema(db_path)`

- **Purpose**: Retrieve the schema of the SQLite database.
- **Parameters**:
  - `db_path` (str): Path to the SQLite database file.
- **Returns**:
  - `schema` (dict): Dictionary containing the table names and their columns.

### `create_prompt(schema)`

- **Purpose**: Create a prompt dynamically for generating SQL queries based on the database schema.
- **Parameters**:
  - `schema` (dict): Database schema information.
- **Returns**:
  - `prompt` (str): Generated prompt for the AI model.

### `get_response(question, prompt, api_key)`

- **Purpose**: Load the Google Gemini Model and provide responses to queries.
- **Parameters**:
  - `question` (str): User's question.
  - `prompt` (str): Prompt to guide the AI model.
  - `api_key` (str): API key for accessing the Google Gemini model.
- **Returns**:
  - `response` (str): Generated response from the AI model.

### `read_sql_query(sql, db_path)`

- **Purpose**: Retrieve query results from the database.
- **Parameters**:
  - `sql` (str): SQL query to be executed.
  - `db_path` (str): Path to the SQLite database file.
- **Returns**:
  - `rows` (list): List of rows returned by the query.

### `main()`

- **Purpose**: Define and run the Streamlit application.
- **Parameters**: None
- **Returns**: None

## Flowchart of Architecture

```plaintext
+------------------------------------------+
|                  UI Layer                |
|               (Streamlit)                |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|              Service Layer               |
|        (Google Gemini API, Pandas)       |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|               Model Layer                |
| (Google Gemini Generative Model, Matplotlib) |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|              Storage Layer               |
|       (CSV Files, SQLite Database)       |
+------------------------------------------+
```
