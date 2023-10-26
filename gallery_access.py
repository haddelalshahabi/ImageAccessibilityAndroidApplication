from plyer import filechooser


def list_all_folders():
    """
    Access and list all folders in the gallery.
    """
    # This will open a file chooser. Depending on how your gallery is structured, you might need to adjust.
    paths = filechooser.choose_dir(multiple=True)
    return paths


def navigate_to_folder(folder_name):
    """
    Navigate to a specific folder.
    """
    # Placeholder logic
    print(f"Navigating to folder: {folder_name}")


def get_images_from_folder(folder_path):
    """
    Get all images from a specific folder.
    """
    # Placeholder logic
    # In a real-world scenario, you'd return a list of all image files in the folder.
    images = []
    return images
