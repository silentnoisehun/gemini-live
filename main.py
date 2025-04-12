import os
from flask import Flask, send_file, request, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        api_key = request.cookies.get('gemini_api_key')
        if api_key:
            return send_file('gemini-live.html')
        else:
            # HTML for form
            html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Gemini Live Voice to Text Realtime: Enter API Key</title>
    <!-- By Jim Salsman, April 2025. Released under the free MIT License. -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h2>Gemini Live Voice to Text Realtime</h2>
    <p>Enter your (free!) Gemini API key from:
    <a href="https://aistudio.google.com/apikey" target="_blank"
        style="text-decoration: none;">aistudio.google.com/apikey</a></p>
    <form method="POST">
        <input type="text" size="33" name="api_key" required>
        <button type="submit">Submit</button>
    </form>
    <p>
        <small>
            <b>Privacy policy:</b> Your API key is stored in a cookie which
            is only accessible from the HTML JavaScript at this domain, which
            runs only in your browser. It will never be stored anywhere else.
            If you don't trust this,
            <a href="https://github.com/jsalsman/gemini-live" target="_blank"
            style="text-decoration: none;">fork the code on GitHub</a> to run
            it on your own server. By <a href="mailto:jim@talknicer.com"
            style="text-decoration: none;">Jim Salsman</a>, April 11, 2025.
        </small>
    </p>
</body>
</html>
"""
            return html_content
    elif request.method == 'POST':
        api_key = request.form.get('api_key')
        response = redirect("/")
        response.set_cookie('gemini_api_key', api_key,
            max_age=31_536_000)  # one year
        return response

def main():
    app.run(port=int(os.environ.get('PORT', 80)))
