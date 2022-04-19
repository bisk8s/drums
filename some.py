import pygame
from pygame.locals import *
import os

sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# join the filepath and the filename
hihat = os.path.join(sourceFileDir, 'hihat_closed.mp3')
hihatopen = os.path.join(sourceFileDir, 'hihat_open.mp3')
snare = os.path.join(sourceFileDir, 'snare.mp3')
kick = os.path.join(sourceFileDir, 'kick.mp3')
tomsml = os.path.join(sourceFileDir, 'tom_small.mp3')
tommed = os.path.join(sourceFileDir, 'tom_medium.mp3')

EVENTS = []

FREQ = 44100   # same as audio CD
BITSIZE = 16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30  # how often to check if playback has finished


def playsound(sound):
    """
    Play sound through default mixer channel in blocking manner.
    This will load the whole sound into memory before playback
    """
    sound.play()
    return sound


def main():
    pygame.init()

    if pygame.joystick.get_count() > 1:
        print("You didn't plug in a joystick. FORSHAME!")
        return

    try:
        pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
    except pygame.error as exc:
        print("Could not initialize sound system: %s" % exc)
        return 1

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    sound0 = pygame.mixer.Sound(tomsml)
    sound1 = pygame.mixer.Sound(tommed)
    sound2 = pygame.mixer.Sound(hihat)
    sound3 = pygame.mixer.Sound(snare)
    sound4 = pygame.mixer.Sound(kick)

    # The main game loop
    current_sound = None
    while True:
        for event in pygame.event.get():
            # print event
            if event.type == JOYBUTTONDOWN:
                if current_sound != None:
                    # current_sound.stop()
                    pass
                print("Button down: ", event.button)
                if event.button == 4:
                    current_sound = playsound(sound4)
                if event.button == 3:
                    current_sound = playsound(sound3)
                if event.button == 2:
                    current_sound = playsound(sound2)
                if event.button == 1:
                    current_sound = playsound(sound1)
                if event.button == 0:
                    current_sound = playsound(sound0)
            if event.type == JOYBUTTONUP:
                print("Button up: ", event.button)
            if event.type == JOYHATMOTION:
                print("Hat: ", event.value)


main()
