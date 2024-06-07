
# Agentic Website Chat

This is a Streamlit web application designed to provide conversational responses based on a user's input query. It utilizes LangChain for language processing and interaction.

#### How to Use:

1. **Insert The website URL:**

   - Input field where the user can enter the URL of the website they want to extract information from.
2. **Ask a question (query/prompt):**

   - Text input for the user to ask a question or provide a prompt for the system.
3. **Submit Query:**

   - Button to submit the user's query for processing.

#### Steps with Logic:

1. **Website Data Extraction:**

   - The application extracts data from the provided website URL using a `WebBaseLoader`.
   - The extracted data is then split into smaller chunks using a `CharacterTextSplitter` to facilitate processing.
2. **Embedding and Vector Storage:**

   - OpenAI embeddings are generated for the extracted documents.
   - These embeddings are stored in a Chroma vector store for efficient retrieval.
3. **Retrieval and Response:**

   - A retrieval-based question-answering (QA) model is employed to find relevant responses to the user's query.
   - LangChain's `RetrievalQA` is utilized, with a specified LLM model (`gpt-3.5-turbo`) and a retrieval mechanism based on the previously generated embeddings.
   - The response to the user's query is displayed on the web interface.

#### Functions:

1. **`main()` Function:**
   - The main function orchestrating the entire application flow.
   - It sets up the Streamlit interface and handles user inputs.
   - Upon submission of a query, it triggers the data extraction, processing, retrieval, and response generation.

#### Architecture Flowchart:

```
+---------------------------------------------+
|                 UI Layer                    |
|               (Streamlit)                   |
+---------------------------------------------+
                    |
                    v
+---------------------------------------------+
|              Service Layer                  |
|         (LangChain, OpenAI API)             |
+---------------------------------------------+
                    |
                    v
+---------------------------------------------+
|              Model Layer                    |
|        (RetrievalQA, ChatOpenAI)            |
+---------------------------------------------+
                    |
                    v
+---------------------------------------------+
|             Storage Layer                   |
|           (Chroma Vector Store)             |
+---------------------------------------------+
```

This architecture showcases the flow of data and operations through different layers of the application, including the user interface, service layer, model layer, and storage layer.
