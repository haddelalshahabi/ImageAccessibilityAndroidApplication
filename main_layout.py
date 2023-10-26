from kivy.uix.boxlayout import BoxLayout


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Assuming you have a method to check if it's the user's first time
        if self.is_first_time_user():
            self.show_tutorial()
        # Here you can add other UI components to your main layout

    def is_first_time_user(self):
        # Mock logic, should be replaced with actual logic to check if it's the user's first time
        return True
