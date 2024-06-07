# DISAI Talk to Website Documentation

## Overview

DISAI Talk to Website is a Streamlit application that allows users to interact with website content using the Google Gemini API and OpenAI's generative model. Users can input a website link, provide a prompt, and receive AI-generated responses based on the content of the website and the provided prompt.

## Steps with Logic

1. **Streamlit App Initialization**:

   - Initialize the Streamlit app and create the UI elements, such as titles and sidebars.
2. **Google Gemini API Key Input**:

   - Users provide their Google Gemini API key through a sidebar text input.
3. **Website Link Input**:

   - Users input the link of the website they want to search.
4. **Content Extraction**:

   - Extract the text content from the provided website link using the `newspaper` library.
5. **Prompt Input**:

   - Users input the prompt for the AI model to generate a response.
6. **Response Generation**:

   - Use the Google Gemini API and OpenAI's generative model to generate a response based on the website content and the provided prompt.
7. **Display Response**:

   - Display the generated response in the Streamlit app.

## Function Explanations

### `extract_text_from_url(url)`

Extracts text content from a given website URL using the `newspaper` library.

### `main()`

Defines the main logic of the Streamlit app, including UI elements, API key input, website link input, content extraction, prompt input, response generation, and response display.

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
|    (Google Gemini API, newspaper)        |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
|               Model Layer                |
|       (OpenAI Generative Model)          |
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
  - **Components**: Sidebar for API key input, text inputs for website link and prompt, display area for generated response.
- **Service Layer**:

  - **Technologies**: Google Gemini API for content analysis, `newspaper` library for content extraction.
  - **Functions**: Extracting content from websites, interfacing with the Gemini API.
- **Model Layer**:

  - **Technologies**: OpenAI's generative model (part of Google Gemini API).
  - **Functions**: Generating responses based on provided content and prompts.
- **Storage Layer**:

  - **Technologies**: Not applicable.
  - **Functions**: Not applicable.

This architecture enables users to interact with website content and generate AI-based responses seamlessly, enhancing their browsing experience and access to information.
