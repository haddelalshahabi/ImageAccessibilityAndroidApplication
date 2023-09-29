from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from voice_commands import VoiceCommands
from gallery_access import GalleryAccess

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
class MainApp(App):

    def build(self):
        # When the app starts, give the user a voice prompt
        voice_prompt("Welcome to the Image Accessibility App. Swipe right to open the gallery or say 'Open Gallery'.")

        # Start listening to voice commands
        listen_to_user()

        return MainLayout()

class MainApp(App):

    def build(self):
        return MainLayout()

    def handle_voice_command(self):
        captured_command = capture_voice_command()
        action = interpret_command(captured_command)

        if action == "open_gallery":
            # Code to open the gallery
            self.root.open_gallery(None)  # Assuming your open_gallery method in MainLayout doesn't require the 'instance' argument
        elif action == "describe_image":
            # Code to describe the currently displayed image
            pass
        elif action == "show_help":
            # Code to show help instructions
            pass
        # ... additional actions based on other voice commands

if __name__ == "__main__":
    app = MainApp()
    app.run()

"""