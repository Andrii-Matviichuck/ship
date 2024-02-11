import pygame

class Alien():
    def __init__(self, SW):
     self.screen = SW.screen
     self.image = pygame.image.load('images/spirit_braeken')
     self.rect = self.image.get_rest()
     self.screen_rest = SW.screen.get_rect()



     self.y = float(self.rect.y)
def update_alien(self):
    if self.rect.bottom < self.screen_rect.bottom:
           self.y += self.alien_speed
    self.rect.y = self.y
def blit_alien(self):
    self.screen.blit(self.image, self.rect)
       