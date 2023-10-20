from kivy.app import App
from main_layout import MainLayout
from audio_feedback import start_app_voice_guide

class AudioVisionApp(App):
    def build(self):
        start_app_voice_guide()  # Start Google Talk to guide users
        return MainLayout()

if __name__ == '__main__':
    AudioVisionApp().run()

"""
class MainApp(App):
    user_type = None  # "blind" or "deaf"

    def build(self):
        layout = BoxLayout()
        # Add widgets for gallery, voice recognition, etc.

        # Listen for voice commands
        command = VoiceCommands.on_voice_command()
        if command == "open gallery":
            self.user_type = "blind"
            GalleryAccess.navigate_images("next", "voice")
        # ... handle other commands ...

        return layout
        
        if __name__ == "__main__":
    MainApp().run()

"""



