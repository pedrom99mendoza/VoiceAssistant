import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


# Hear our microphone and return the audio as text
def transform_audio_in_text():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("You can talk")
        audio = r.listen(origen)

    try:
        pedido = r.recognize_google(audio)
        print(f"You said: {pedido}")
        return pedido

    except sr.UnknownValueError:
        print("Excuse me, I did not understand what you said")
        return "Waiting"
    except sr.RequestError:
        print("Excuse me, the service isn't available")
        return "Waiting"
    except:
        print("Excuse me, something went wrong")
        return "Waiting"


# function assistant voice
def talk(message):
    engine = pyttsx3.init()
    engine.setProperty("voice", id1)
    engine.say(message)
    engine.runAndWait()


def ask_date():
    day = datetime.date.today()
    print(day)
    week = day.weekday()
    print(week)

    calendar1 = {0: "Monday",
                 1: "Tuesday",
                 2: "Wednesday",
                 3: "Thurday",
                 4: "Friday",
                 5: "Saturday",
                 6: "Sunday"}

    talk(f"Today is {calendar1[week]}")


def ask_hour():
    hour = datetime.datetime.now()
    hour = f"Son las {hour.hour} horas, {hour.minute} minutos y {hour.second} segundos"
    print(hour)
    talk(hour)


def hi():
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        moment = "Good night"
    elif 6 <= hour.hour < 13:
        moment = "Good morning"
    else:
        moment = "Good afternoon"

    talk(
        f"{moment}, I'm you voice Assistant")


def ask_things():
    hi()
    start = True
    while start:
        pedido = transform_audio_in_text().lower()
        if "youtube" in pedido:
            talk("One moment, let's open Youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "google" in pedido:
            talk("Okey, i'm opening google")
            webbrowser.open("https://google.com")
            continue
        elif "hoy" in pedido:
            ask_date()
            continue
        elif "hora" in pedido:
            ask_hour()
            continue
        elif "wikipedia" in pedido:
            talk("searching in wikipedia")
            pedido = pedido.replace("wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            talk("wikipedia dice que: ")
            talk(resultado)
        elif "internet" in pedido:
            talk("searching in google")
            pedido = pedido.replace("internet", "")
            pywhatkit.search(pedido)
            continue
        elif "chiste" in pedido:
            talk(pyjokes.get_joke("es"))
        elif "adios" in pedido:
            talk("perfect, see you soon")



ask_things()