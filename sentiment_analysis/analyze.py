from textblob import TextBlob


def user_mood():
    text = input("Type your current mood -> ")  # -> Temporarily created before taking mood from prompt

    if not text.strip():  # -> if user didn't type anything
        print("Please enter a valid response.")
        exit()

    current_mood = TextBlob(text).polarity  # -> analyze current mood from text

    mood = "Natural"  # -> initial mood

    # -> update based on input text from user
    if current_mood > 0.5:
        mood = "Very Happy"
    elif 0 < current_mood <= 0.5:
        mood = "Slightly Happy"
    elif 0 > current_mood >= -0.5:
        mood = "Slightly Sad"
    elif -0.5 > current_mood >= -1:
        mood = "Very Sad"

    return mood
