#modules required for TOS
from gtts import gTTS
import pyaudio
import os 

#module for html
from flask import Flask, render_template, request


#python script
mytext = input("Enter Text")
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("AI_Session.mp3")

#HTML script
app = Flask(__name__)
@app.route('/',methods = ['GET'])
def show_indexhtml():
    return render_template('index.html')

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        sent = request.form['Text']
        print ("Sentance is " + sent)
        return "Data sent. Please check your program log"

if __name__ == '__main__':
      app.run(debug=True)