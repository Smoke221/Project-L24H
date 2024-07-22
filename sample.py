from gtts import gTTS
from moviepy.editor import *
import os

# Ensure MoviePy can find ImageMagick
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"

# Function to convert text to speech using gTTS
def text_to_speech_gtts(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"Generated audio file {filename} for text: {text}")

# Function to create a video from an image and an audio file
def create_video(image_path, audio_path, output_path, text):
    # Load the image
    image_clip = ImageClip(image_path).set_duration(10)  # Set duration to match the audio length

    # Load the audio
    audio_clip = AudioFileClip(audio_path)

    # Set the audio to the image
    video_clip = image_clip.set_audio(audio_clip)

    # Add text
    txt_clip = TextClip(text, fontsize=24, color='white', bg_color='black', size=image_clip.size)
    txt_clip = txt_clip.set_pos('bottom').set_duration(10)

    # Composite video and text
    final_clip = CompositeVideoClip([video_clip, txt_clip])

    # Write the video file
    final_clip.write_videofile(output_path, fps=24)
    print(f"Created video file {output_path}")

# Function to automate video creation for multiple images and texts
def automate_video_creation(image_text_pairs, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i, (image_path, text) in enumerate(image_text_pairs):
        audio_path = os.path.join(output_folder, f"audio_{i}.mp3")
        video_path = os.path.join(output_folder, f"video_{i}.mp4")
        
        # Convert text to speech
        text_to_speech_gtts(text, audio_path)
        
        # Create video
        create_video(image_path, audio_path, video_path, text)
        
        print(f"Created video {i+1} at {video_path}")

# List of (image_path, text) pairs
image_text_pairs = [
    ("panda.jpg", "A cute panda eating bamboo."),
    ("001HPS_Emma_Watson_082.jpg", "A picture of Emma Watson clapping hands with a grin face from the movie Harry Potter.")
]

output_folder = "output_videos"
automate_video_creation(image_text_pairs, output_folder)
