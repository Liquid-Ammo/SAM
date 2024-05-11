from flask import Flask, render_template, request
from main import chatbot   # Assuming you have a function to generate question papers
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

@app.route('/input', methods=['POST'])
def generate_paper():
  subject = request.form['subject']
    
  

  

  
  chapter = request.form['chapter']
  question_type = request.form['question_type']
    # Call the question paper generator function with the inputs
    #question_paper = chatbot(subject, chapter, question_type)
  return render_template('paper.html', question_paper=question_paper)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080)
