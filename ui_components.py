class Settings():
    def __init__(self):
        self.settings = {
            "audio_voice": True,
            "object_detection": True,
            "text_description": True
        }

    def toggle_setting(self, setting_name):
        if setting_name in self.settings:
            self.settings[setting_name] = not self.settings[setting_name]


"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from audio_feedback import voice_prompt

class DecisionLayout(BoxLayout):
    def __init__(self, chosen_image_path, **kwargs):
        super(DecisionLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Display the chosen image
        self.image_widget = Image(source=chosen_image_path)
        self.add_widget(self.image_widget)

        # Guidance for the user
        self.guidance_label = Label(text="Swipe Left for Detection, Swipe Right for Description", size_hint_y=0.2)
        self.add_widget(self.guidance_label)

        # Voice guidance
        voice_prompt("Swipe left if you want image detection. Swipe right if you want a description of the image.")

        # Bind the swipe gestures
        Window.bind(on_touch_move=self.on_touch_move)

    def on_touch_move(self, instance, touch):
        # Detect left swipe for image detection
        if touch.dx < -40:
            self.detect_image()

        # Detect right swipe for image description
        elif touch.dx > 40:
            self.describe_image()

    def detect_image(self):
        # Logic to perform object detection on the chosen image
        pass

    def describe_image(self):
        # Logic to get a description of the chosen image
        pass

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Define the open_gallery method
        self.add_widget(Button(text="Open Gallery", on_press=self.open_gallery))
        # Add more UI elements here

    def open_gallery(self, instance):
        # Logic to open the gallery
        filepath = open_filechooser()
        # Do something with the filepath
"""