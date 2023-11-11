from pytube import YouTube
import pygame
import os

def download_youtube_video(url, output_path='temp_video.mp4'):
    yt = YouTube(url)
    ys = yt.streams.filter(only_audio=True).first()
    ys.download(output_path)

def play_audio(video_path):
    pygame.mixer.init()
    pygame.mixer.music.load(video_path)
    pygame.mixer.music.play()

def main():
    youtube_url = input("Enter the YouTube URL: ")
    
    # Download YouTube video as audio
    download_youtube_video(youtube_url)

    # Play the downloaded audio
    play_audio('temp_video.mp4')

    input("Press Enter to stop playback...")

    # Stop playback and remove temporary file
    pygame.mixer.music.stop()
    os.remove('temp_video.mp4')

if __name__ == "__main__":
    main()
video_path = 'C:\\Users\\Asus\\Documents\\Testing and Learning VSCode\\temp_video.mp4'
pygame.mixer.music.load(video_path)
