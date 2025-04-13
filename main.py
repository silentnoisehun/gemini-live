#import os
from flask import Flask, send_file, request, redirect, Response

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
<html><head>
    <!-- By Jim Salsman, April 2025. Released under the free MIT License. -->
    <meta charset="UTF-8">
    <title>Gemini Live Voice to Text Realtime: Enter API Key</title>
    <meta name="description" content="Gemini Live voice-to-text realtime stream">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <style>
        body {
          background-color: lightgreen;
          font-family: sans-serif;
          text-align: center;
        }
        a { text-decoration: none; }
        .description, .privacy {
          width: 80%;
          margin: 0 auto;
          text-align: left;
        }
    </style>
</head><body>
    <h2>Gemini Live Voice to Text Realtime</h2>
    <p>Enter your (free!) Gemini API key from:
    <a href="https://aistudio.google.com/apikey" target="_blank"
        style="text-decoration: none;">aistudio.google.com/apikey</a></p>
    <form method="POST">
      <input type="text" size="33" name="api_key" required>
      <button type="submit">Submit</button>
    </form><br>
    <p class="description">
        This is a web application that allows you to interact with 
        Google's Gemini 2.0 Flash Live large language model using your
        voice in real-time. It's based on Google's js-genai API to run
        entirely in the browser, providing a seamless, voice-driven
        experience. Key features include Google Search, Python code
        execution (including image display from e.g. matplotlib),
        image upload (including from the camera on mobile), and text
        output rendered in markdown and LaTeX. The <a
        href="https://github.com/jsalsman/gemini-live" target="_blank"
        >source code is free on GitHub</a> under the MIT License.
        Voice to text interactions are advantageous because most people
        read about twice as fast as synthetic speech typically talks;
        while text can be skimmed, interrupting speech leaves what
        might have been said as an often frustrating mystery.
    </p><br>
    <p class="privacy">
        <b>Privacy policy:</b> Your API key is stored in a cookie which
        is only accessible from the HTML JavaScript at this domain, which
        runs only in your browser. It will never be stored anywhere else.
        If you don't trust this, fork the code on GitHub to run it on
        your own server. By <a href="mailto:jim@talknicer.com"
        >Jim Salsman</a>, April 11, 2025.
    </p>
</body></html>"""
            return html_content
    elif request.method == 'POST':
        api_key = request.form.get('api_key')
        response = redirect("/")
        response.set_cookie('gemini_api_key', api_key,
            max_age=31_536_000)  # one year
        return response

@app.route('/favicon.ico')
def favicon():
    return send_file('favicon.ico', mimetype='image/x-icon')

@app.route('/robots.txt')
def robots():
    return Response("User-agent: *\nAllow: /\n", mimetype='text/plain')

#app.run(port=int(os.environ.get('PORT', 80)), debug=...)
