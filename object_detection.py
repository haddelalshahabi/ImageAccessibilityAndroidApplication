def detect_objects(image_path):
    # Mock logic: Use a TensorFlow model for object detection
    # Here, you would load your model and run the image through it.
    detected_objects = ["dog", "cat", "ball"]  # Sample objects
    return detected_objects


def get_image_description(objects):
    # Convert detected objects into a description
    return ", ".join(objects)
