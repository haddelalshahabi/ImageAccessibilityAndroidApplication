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
