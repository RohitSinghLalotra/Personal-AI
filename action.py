import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather1

def Action (data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant";

    elif "hello" in user_data or "hey" in user_data:
        text_to_speech.text_to_speech("Hy , sir How i can help you")
        return "Hy , sir How i can help you";

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir";

    elif "whom i am talking" in user_data:
        text_to_speech.text_to_speech("you are talking to zaya")
        return "you are talking to zaya";

    elif "time now" in user_data:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(current_time)
        text_to_speech.text_to_speech(current_time)
        return current_time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok  sir")
        return "ok sir";

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech('gaana.com is now ready for you')
        return 'gaana.com is now ready for you';

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech('youtube.com is now ready for you')
        return 'youtube.com is now ready for you';

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech('google.com is now ready for you')
        return 'google.com is now ready for you';

    elif "weather" in user_data:
        ans = weather.get_weather.get_weather()
        text_to_speech.text_to_speech(ans)
        return ans;




    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand";