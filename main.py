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
    <title>Gemini Live Voice to Text Realtime Stream: Enter API Key</title>
</head>
<body>
    <h2>Gemini Live Voice to Text Realtime Stream</h2>
    <p>Enter your (free!) Gemini API key from
    <a href="https://aistudio.google.com/apikey" target="_blank"
        >aistudio.google.com/apikey</a></p>
    <form method="POST">
        <input type="text" size="33" name="api_key" required>
        <button type="submit">Submit</button>
    </form>
    <p><small><b>Privacy policy:</b> Your API key is stored in a cookie which
        is only accessible from the HTML JavaScript at this domain, which runs
        only in your browser. It will never be stored anywhere else.</small>
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
