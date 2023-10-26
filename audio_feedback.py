from plyer import tts  # Use Plyer for TTS


def start_app_voice_guide():
    """
    Function to provide voice guidance using Google Talk.
    """
    voice_output("Welcome to Audio Vision. I will guide you through the process.")


def voice_output(message):
    """
    Function to output voice messages.
    """
    tts.speak(message)
