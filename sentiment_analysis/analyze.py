from textblob import TextBlob


def user_mood(user_text):

    if not user_text.strip():  # -> if user didn't type anything
        print("Please enter a valid response.")
        exit()

    current_mood = TextBlob(user_text).polarity  # -> analyze current mood from text

    # -> update based on input text from user
    if current_mood > 0.5:
        return "Very Happy"
    elif 0 < current_mood <= 0.5:
        return "Happy"
    elif 0 > current_mood >= -0.5:
        return "Slightly Sad"
    elif -0.5 > current_mood >= -1:
        return "Very Sad"
    else:
        return "Neutral"

