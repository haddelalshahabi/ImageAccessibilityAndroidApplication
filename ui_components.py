from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from gallery_access import open_filechooser  # Assuming you have a function named open_filechooser in gallery_access.py

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
