from kivy.core.audio import SoundLoader

def voice_prompt(message):
    sound = SoundLoader.load('path_to_audio_file.mp3')
    if sound:
        sound.play()


voice_prompt("Welcome to the Image Accessibility App. Swipe right to open the gallery or say 'Open Gallery'.")

"""import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
"""
