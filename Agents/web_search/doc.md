
# Websearch Agent:

### Steps and Logic:

1. Import necessary modules: `utils`, `streamlit`, and components from `langchain`.
2. Define a class `InternetChatbot`.
3. Initialize the OpenAI model and configure it using the `utils.configure_openai()` function.
4. Define a function `setup_agent()` within the `InternetChatbot` class to set up the conversational agent.
   - Define a tool for DuckDuckGoSearch.
   - Pull a prompt from `hub`.
   - Initialize an OpenAI instance with specific parameters.
   - Create an agent with the defined tools, prompt, and OpenAI instance.
5. Define the `main()` function within the `InternetChatbot` class.
   - Call `setup_agent()` to initialize the agent and memory.
   - Display a chat input box using `st.chat_input()` for user queries.
   - If a user query is entered:
     - Display the user's message.
     - Invoke the agent with the user's query and display the response.

### Functions Explanation:

- `InternetChatbot.__init__()`: Initializes the `InternetChatbot` class and sets up the OpenAI model.
- `InternetChatbot.setup_agent()`: Sets up the conversational agent with tools, prompt, OpenAI model, and memory.
- `InternetChatbot.main()`: Main function to run the websearch agent, invoking the conversational agent with user queries.
- `utils.enable_chat_history(func)`: Decorator function to manage chat history, clearing it when the current page changes.
- `utils.display_msg(msg, author)`: Adds a message to the chat history.
- `utils.configure_openai()`: Configures the OpenAI model, allowing the selection of different models through Streamlit sidebar.

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
|         (langchain, langchain_openai,    |
|         langchain_community)             |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|               Model Layer                |
|         (OpenAI, DuckDuckGo)            |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|              Storage Layer               |
|        (Session State in Streamlit)      |
+------------------------------------------+
```

This architecture diagram represents the layers involved in the application:

- **UI Layer**: Utilizes Streamlit for the user interface.
- **Service Layer**: Incorporates various modules from `langchain` and `langchain_community`.
- **Model Layer**: Involves OpenAI for language processing and DuckDuckGo for web search.
- **Storage Layer**: Manages session state within Streamlit.
