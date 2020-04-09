import pygame

file = '/home/jkligel/Downloads/tngtheme.mp3'
def play_music(file, volume=0.8):
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 2048

    pygame.mixer.init(freq,bitsize,channels,buffer)
    pygame.mixer.music.set_volume(volume)

    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(file)
        print('Music file {} loaded!'.format(file))
    except pygame.error:
        print('File {} not found! ({})'.format(file, pygame.get_error()))

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)

play_music(file)
