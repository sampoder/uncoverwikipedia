import wikipedia
import re
from replit import db
from flask import Flask, render_template, request
app = Flask(__name__)
import random


def ireplace(old, repl, text):
    return re.sub('(?i)'+re.escape(old), lambda m: repl, text)

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