import os
import uuid
from werkzeug.utils import secure_filename
from moviepy.editor import VideoFileClip

def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def get_video_duration(file_path):
    try:
        clip = VideoFileClip(file_path)
        return clip.duration
    except Exception as e:
        print(f"Error processing video: {e}")
        return None

def save_uploaded_file(file, folder, allowed_extensions):
    if not allowed_file(file.filename, allowed_extensions):
        return None
    filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
    file_path = os.path.join(folder, filename)
    file.save(file_path)
    return file_path