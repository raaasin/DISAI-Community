
# Talk To CSV using Agentic Approach

### Steps with Logic:

1. **Upload Files**: Users can upload CSV, XLS, or XLSX files using the file uploader widget.
2. **Save Uploaded File**: The uploaded files are saved locally, and Pandas dataframes are created from them.
3. **Query Processing**:
   - Users can input queries.
   - Upon clicking the "Query" button, the system processes the input using an agentic approach.
   - The system generates a response based on the query using the LangChain experimental agents and the OpenAI language model.
   - If the query mentions charts or graphs, the system saves them locally and includes the file names in the response.
4. **Display Response**: The system displays the generated response or any saved charts or graphs.

### Functions:

1. **save_chart(query)**:

   - Appends text to the query to save any generated charts or graphs locally.
2. **save_uploaded_file(uploaded_file)**:

   - Saves the uploaded file locally.
   - Creates Pandas dataframes from the uploaded files.
   - Initializes LangChain experimental agents with OpenAI for query processing.
3. **load_dataframe()**:

   - Loads dataframes from CSV, XLS, or XLSX files present in the directory.
4. **run_query(agent, query_)**:

   - Processes the user query using LangChain agents and OpenAI language model.
   - Decodes intermediate processing steps for logging and understanding.
   - Stores the conversation history including questions, responses, and processing steps.
5. **decode_intermediate_steps(steps)**:

   - Extracts and decodes intermediate processing steps for logging and understanding.
6. **get_convo()**:

   - Retrieves conversation history from a JSON file.
7. **store_convo(query, response_, response)**:

   - Stores the conversation history including questions, responses, and processing steps in a JSON file.

### Architecture Flowchart:

```
+------------------------------------------+
|                  UI Layer                |
|               (Streamlit)                |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|              Service Layer               |
|  (LangChain Experimental Agents, OpenAI) |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|               Model Layer                |
|    (Pandas, LangChain, OpenAI Model)     |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|              Storage Layer               |
|    (Local Storage, JSON, CSV, XLSX)      |
+------------------------------------------+
```

This architecture depicts the UI layer built with Streamlit, the service layer utilizing LangChain experimental agents and OpenAI, the model layer employing Pandas, LangChain, and OpenAI model, and the storage layer utilizing local storage, JSON, CSV, and XLSX files.
