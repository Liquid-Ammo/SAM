from flask import Flask, render_template, request
from chat import chatbot   # Assuming you have a function to generate question papers
import google.generativeai as genai
import json
import base64
from manage import combine, topic, save
import pathlib
import pprint
import requests
import mimetypes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/input', methods=['POST','GET'])
def Generate():
  while True:
    subject = request.form['firstField']
    chapter = request.form['secondField']
    question_type = request.form['thirdField']
    output=chatbot(subject,chapter,question_type)
    return render_template('index.html',out=output)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=80)
