import sys, os, random, time, math
import psutil 
import pygame
from pygame.locals import *
class interface:
    def __init__(self, size):
        self.size = size
        self.screen = None
        self.clock = None
        
    def load_module(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size, HWSURFACE | DOUBLEBUF)
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

        pygame.display.set_caption('Neural Interface') 

    def await_input(self):
        return
        
    def return_output(self):
        return

    def display(self):
        return
