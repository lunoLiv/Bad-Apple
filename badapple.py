import cv2 as cv
import numpy as np
import time
import sys, os
 
def filtragem(lista):
    lista = [sum(i) for linha in lista for i in linha]
    final = []
 
    for i in lista:
        if i >= 382:
            final.append(1)
        if i < 382:
            final.append(0)
    return final
 
def criar_string(lista):
    counter = 0
    string = ''
    for i in lista:
        if counter % 192 == 0 and counter != 0:
            string += '\n'
        if i == 1:
            string += 'A'
        if i == 0:
            string += ' '
    return string
 
apple = cv.VideoCapture('worst.mp4')
 
flag, frame = apple.read()
counter = 0
 
while flag:
    print(counter)
    flag, frame = apple.read()
    final = filtragem(frame.tolist())
    print(criar_string(final))
    time.sleep(0.01)
    os.system('cls')
    counter += 1
