from textblob import TextBlob

text = input()  # -> Temporarily created before taking mood from prompt

current_mood = TextBlob(text).polarity  # -> analyze current mood from text

mood = "Natural"

if current_mood > 0:
    mood = "Happy"
elif current_mood < 0:
    mood = "Sad"

print(mood)