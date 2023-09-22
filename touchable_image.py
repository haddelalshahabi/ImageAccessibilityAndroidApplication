from kivy.uix.image import Image
from object_detection import ImageCaptioning
from audio_feedback import voice_prompt

class TouchableImage(Image):
    def __init__(self, **kwargs):
        super(TouchableImage, self).__init__(**kwargs)
        # Initialize the ImageCaptioning class to get descriptions
        self.captioning = ImageCaptioning()

    def on_touch_down(self, touch):
        # Check if the image was touched
        if self.collide_point(*touch.pos):
            self.describe_image(self.source)

    def describe_image(self, img_path):
        # Get the description using the AI model
        description = self.captioning.get_image_description(img_path)
        # Use voice_prompt to give audio feedback to the user
        voice_prompt(description)


"""
from object_detection import detect_objects
from gallery_access import text_to_speech



class TouchableImage(Image):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            detected_objects = detect_objects(self.source)
            touched_object = self.identify_touched_object(touch.pos, detected_objects)

            if touched_object:
                feedback_message = f"You touched a {touched_object}."
                text_to_speech(feedback_message)

            return True
        return super(TouchableImage, self).on_touch_down(touch)

    def identify_touched_object(self, touch_position, detected_objects_with_boxes):
        x_touch, y_touch = touch_position

        for obj_name, bounding_box in detected_objects_with_boxes.items():
            x1, y1, x2, y2 = bounding_box
            if x1 <= x_touch <= x2 and y1 <= y_touch <= y2:
                return obj_name  # Returns the name of the object that was touched

        return None
"""