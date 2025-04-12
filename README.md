# Gemini Live Voice to Text Realtime Stream

This **Gemini Live Voice to Text Realtime Stream** running at [live.talknicer.com](https://live.talknicer.com) is a web application that provides a free, live, real-time voice-to-text large language model interaction experience using Google's new `js-genai` API. This project harnesses the power of Gemini 2.0 Flash Live in real-time to provide a seamless voice-driven experience for users, allowing them to chat with the model while reading the output instead of having to wait much longer for synthesized speech, which can't be skimmed. Google Search and Python code execution are available, along with both markdown and LaTeX output display. It runs entirely in the browser after the API key cookie is set, and was built in Firebase Studio with about 90% vibe coding and deployed on Google Cloud Run.

## Key features:
*   **Real-time Voice Input:** Sends speech directly to the model as you speak, providing immediate and blazingly fast responses.
*   **Google Search Integration**: The `gemini-2.0-flash-live-001` model performs Google searches on request for up to date information.
*   **Code Execution:** The model is able to execute python code to do complex computations for you.
*   **Interactive Conversation:** Allows users to engage in a continuous conversation with the model. Output is rendered correctly from both markdown and LaTeX.
*   **Single-Page Application (SPA):** The entire client-side logic resides within a single HTML file (`gemini-live.html`), simplifying deployment and enhancing user experience.
*   **Secure API Key Management:** Utilizes Flask to securely manage the API key by setting it as a cookie. The user is asked to provide their own key, preventing the need to hardcode an API key or run in to rate limits.
*   **Client-Side JavaScript:** The core functionality, including voice capture, transcription, and interaction with the js-genai API, is implemented in JavaScript, making the application highly responsive.
*   **Invalid API Key Detection:** If an incorrect API key is provided, the app invalidates the cookie and asks for the key again.

## Technology stack:
*   **JavaScript:** For client-side logic, voice recording, and LLM API interaction.
*   **Flask:** A lightweight web framework for setting the API key cookie and serving the HTML, entirely in `main.py`.
*   **HTML/CSS/JS:** The single `gemini-live.html` file contains the entire client application.

## Execution:
To run the server: `python -m flask --app main run` and then visit the endpoint from a browser where the API key cookie can be set.

## Requirements:
The server only needs `Flask` installed (`pip install flask`), but the client JavaScript uses Google's `js-genai`, `marked`, `katex`, and the `marked-katex-extension` libraries, none of which need to be installed.

## Documentation:
* https://ai.google.dev/gemini-api/docs/live
* https://googleapis.github.io/js-genai/main/index.html
* https://github.com/googleapis/js-genai

## License:
This project is licensed under the free MIT License.

By Jim Salsman, April 11, 2025.
