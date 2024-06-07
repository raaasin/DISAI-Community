# DISAI Webagent Documentation

## Overview

DISAI Webagent is a Streamlit chat agent powered by the DSAI Framework. It allows users to interact with an AI agent connected to the internet using OpenAI's GPT-3.5-turbo model and DuckDuckGo Search. Users can input queries or prompts, and the agent provides responses based on the context from internet search results and the provided input.

## Steps with Logic

1. **Streamlit App Initialization**:

   - Initialize the Streamlit app and create the UI elements, such as titles and sidebars.
2. **OpenAI API Key Input**:

   - Users provide their OpenAI API key through a sidebar text input.
3. **Search Function**:

   - Define a function to search the internet using DuckDuckGo Search and retrieve search results based on user input.
4. **Response Generation Function**:

   - Define a function to generate responses using OpenAI's GPT-3.5-turbo model based on the context from internet search results and the provided prompt.
5. **Chat Interface**:

   - Display the chat interface using Streamlit's `chat_input` and `chat_message` components.
6. **Message Handling**:

   - Handle user input and display messages from both the user and the assistant.
7. **Message Processing**:

   - Process user input, search the internet for context, and generate responses.
8. **Display Response**:

   - Display the generated response in the chat interface.

## Function Explanations

### `search(input_query)`

Searches the internet using DuckDuckGo Search based on the user input query and retrieves search results.

### `get_response(context, prompt)`

Generates a response using OpenAI's GPT-3.5-turbo model based on the provided context from internet search results and the user prompt.

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
|   (DuckDuckGo Search, OpenAI API)       |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|               Model Layer                |
|          (GPT-3.5-turbo model)          |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|              Storage Layer               |
|           (Not applicable)               |
+------------------------------------------+
```

### Detailed Layer Descriptions

- **UI Layer**:

  - **Technology**: Streamlit
  - **Components**: Sidebar for OpenAI API key input, chat interface for user interaction and message display.
- **Service Layer**:

  - **Technologies**: DuckDuckGo Search for internet search, OpenAI API for response generation.
  - **Functions**: Searching internet for context, generating responses based on context and prompts.
- **Model Layer**:

  - **Technologies**: OpenAI's GPT-3.5-turbo model.
  - **Functions**: Generating responses based on provided context and prompts.
- **Storage Layer**:

  - **Technologies**: Not applicable.
  - **Functions**: Not applicable.

This architecture enables seamless interaction between users and the AI agent, providing relevant responses based on internet search results and user input.
