from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

