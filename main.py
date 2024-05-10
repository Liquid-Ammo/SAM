import google.generativeai as genai
import json
import base64
from manage import combine, topic, save
import pathlib
import pprint
import requests
import mimetypes

# Set your API key
API_KEY = "AIzaSyDb6snPbG15Rk8_8zlBAf1N1AlSMolS2Uk"

# Configure the client library by providing your API key.
genai.configure(api_key=API_KEY)

model = "gemini-1.5-pro-latest"  # @param {isTemplate: true}
contents_b64 = "W10="  # @param {isTemplate: true}
generation_config_b64 = "eyJ0ZW1wZXJhdHVyZSI6MSwidG9wX3AiOjAuOTUsInRvcF9rIjowLCJtYXhfb3V0cHV0X3Rva2VucyI6ODE5Miwic3RvcF9zZXF1ZW5jZXMiOltdfQ=="  # @param {isTemplate: true}
safety_settings_b64 = "W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d"  # @param {isTemplate: true}
user_input_b64 = ""  # @param {isTemplate: true}

contents = json.loads(base64.b64decode(contents_b64))
generation_config = json.loads(base64.b64decode(generation_config_b64))
safety_settings = json.loads(base64.b64decode(safety_settings_b64))
user_input = base64.b64decode(user_input_b64).decode()
stream = False

while True:
    print("SAM : Smart Artificial Male")
    print()
    us_in1 = int(
        input(
            """Select Subject : 
  1)Mathematics
  2)Physics
  3)Chemistry
  4)Biology
  """
        )
    )
    print()
    asd = topic(us_in1)
    a = str("Select Chapter :\n " + asd + "\n")
    us_in2 = int(input(a))
    print()
    us_in3 = int(
        input(
            """Request : 
  1)Questions with answers 
  2)Notes
  3)Summary
  4)All
  """
        )
    )
    print()
    ven = asd.split("\n")
    chap = ven[us_in2 - 1]

    cha = ""
    run = False
    j = 0
    for i in chap:
        if i.isdigit():
            run = True
        if run:
            if i.isdigit():
                continue
            if j < 1:
                j += 1
            else:
                cha += str(i)

    user_input = str(combine(cha, us_in3))

    gemini = genai.GenerativeModel(model_name=model)
    chat = gemini.start_chat(history=contents)
    response = chat.send_message(user_input, stream=stream)

    a = response.text
    print(a)
    save(a, cha, us_in3)

    response.prompt_feedback
    response.candidates
    a = str("Press enter to continue : ")
    if a != "":
        break
