from plyer import filechooser
import pyttsx3
import speech_recognition as sr

def open_filechooser():
    file_path = filechooser.open_file()
    return file_path

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def capture_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            return "Sorry, I did not get that."
        except sr.RequestError:
            return "API unavailable."