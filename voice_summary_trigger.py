import os
import time
import pygame

def play_voice_summary():
    pygame.mixer.init()
    pygame.mixer.music.load("voices/ali_summary.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    play_voice_summary()