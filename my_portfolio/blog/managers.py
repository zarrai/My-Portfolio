import os

def post_filename(instance, filename):
    """
    upload files to the project folder with specific name in the media directory
    """
    extension = "." + filename.split(".")[-1] if "." in filename else ""
    try:
        title = instance.title
    except:
        title = instance.id
    kind = instance._meta.model.__name__.lower()
    return os.path.join('posts', f"{kind}-{title.lower()}{extension}".replace(" ", "_"))