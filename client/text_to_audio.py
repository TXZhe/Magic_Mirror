from gtts import gTTS
import time
import pygame

pygame.mixer.init()

def speak(texture):
    tts = gTTS(text=texture, lang="en")
    tts.save("audio.mp3")
    file=r'audio.mp3'
    #pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    '''
    time.sleep(20)
    pygame.mixer.music.stop()
    '''
def stopmusic():
    pygame.mixer.music.stop()

if __name__ == '__main__':
	speak("easy peasy, lemon squeezy")
