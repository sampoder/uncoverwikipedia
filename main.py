import wikipedia
import re
from replit import db
from flask import Flask, render_template, request
app = Flask(__name__)
import random


def ireplace(old, repl, text):
    return re.sub('(?i)'+re.escape(old), lambda m: repl, text)

def generate():
  articles = []

  while len(articles) < 10:
    try:
      title = wikipedia.random()
      content = wikipedia.page(title=title).content
      sentences = []
      for paragraph in content.splitlines():
        for sentence in paragraph.split('.'):
          if title in sentence.strip():
            sentenceToAdd = sentence.strip() + "."
            for titleWord in title.split(' '):
              sentenceToAdd = ireplace(titleWord, "█".join(["█"*len(titleWord) for q in range(1)]), sentenceToAdd)
            sentences.append(sentenceToAdd)
          else:
            for titleWord in title.split(' '):
              if " " + titleWord in sentence.strip() or titleWord + " " in sentence.strip():
                sentenceToAdd = sentence.strip() + "."
                for titleWord in title.split(' '):
                  sentenceToAdd = ireplace(titleWord, "█".join(["█"*len(titleWord) for q in range(1)]), sentenceToAdd)
                sentences.append(sentenceToAdd)
      if len(list(dict.fromkeys(sentences))) >= 4:
        sentencesTuple = tuple(list(dict.fromkeys(sentences)))  
        print("Welcome to the squad " + title + "!")
        db[title] = sentencesTuple
    except:
      print("Exception occured.")

  print(articles)

  for article in articles:
    print(article["title"])
    print("\n")
    for sentence in article["sentences"]:
      print(sentence)
      print("\n")
    print("---")
    print("\n")

@app.route('/')
def index():
    return render_template('index.html', animated = True)

@app.route('/home')
def home():
    return render_template('index.html', animated = False)

@app.route('/play')
def about(): 
  keys = db.keys()
  choosen = random.sample(keys, 4)
  randomIndex = random.randint(0,3)
  value = db[choosen[randomIndex]]
  streak = ""
  if 'streak' in request.args:
    streak = request.args.get('streak')
  else:
    streak = "0"
  return render_template('play.html', value=value, choosen=choosen, correct=choosen[randomIndex], streak=streak, nextStreak = int(streak)+1)
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it