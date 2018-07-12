import pygame
import pygame.midi
import time

pygame.midi.init()

player = pygame.midi.Output(0)
player.set_instrument(0)

while True:
    text = input('Введите текст: ')
    if text == 'exit':
        break
    note = []
    for x in text:
        note.append(ord(x)-50)
    print(note)
    for n in note:
    # n -=50
        player.note_on(n,127)
        time.sleep(0.2)
        player.note_off(n,127)



player.close()

