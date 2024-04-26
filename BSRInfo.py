import os
import pygame
import time
from numpy import interp
from colors import *

class bsrInfo:
    screen = None

    def __init__(self):
        self.menu_btn_height = 60
        self.menu_btn_width = 60

        os.putenv('SDL_VIDEODRIVER', 'fbcon')
        pygame.display.init()

        self.size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        self.pygame = pygame

        # Remove mouse cursor
        pygame.mouse.set_visible(False)

        # Blank out screen at Init
        self.screen.fill((0, 0, 0))
        pygame.font.init()
        pygame.display.update()

    # def test(self):
    #     red = (255, 0, 0)
    #     pygame.draw.rect(self.screen, red, pygame.Rect(30, 30, 60, 60))
    #     pygame.display.update()

    # INNER CLASS METRIC #############################################################################################
    class Metric():
        def __init__(self, bi, label, location, min, max, unit, font_name=None, font_size=30, graph=False):
            self.bsrinfo = bi
            self.label = label
            self.location = location
            self.min = min
            self.max = max
            self.value = max
            self.unit = unit
            self.font_name = font_name
            self.font_size = font_size
            self.font = pygame.font.Font(self.font_name, self.font_size)
            self.lbl_surface = None
            self.lbl_width = None
            self.lbl_height = None
            self.graph = graph
            self.graph_height = 15

            # Draw Label
            self.lbl_surface = self.font.render(self.label+" ", 1, white)
            self.lbl_width = self.lbl_surface.get_width()
            self.lbl_height = self.lbl_surface.get_height()
            self.bsrinfo.screen.blit(self.lbl_surface, self.location)
            
            # get full width and height of label and value
            vsurf = self.font.render(str(self.max) + self.unit, 1, (0, 0, 0))
            self.val_width = vsurf.get_width()
            self.val_height = vsurf.get_height()
            self.full_width = self.lbl_width + self.val_width

            pygame.display.update()

        def clearValue(self):
            # Clear Value
            pygame.draw.rect(self.bsrinfo.screen, (0, 0, 0), pygame.Rect(self.location[0] + self.lbl_width, self.location[1], self.val_width, self.val_height))
            

            # Clear Graph
            if self.graph:
                pygame.draw.rect(self.bsrinfo.screen, (0, 0, 0), pygame.Rect(self.location[0], self.location[1] + self.lbl_height + 2, self.full_width, self.graph_height))
                # pygame.draw.rect(bsrinfo.screen, (0, 0, 0), pygame.Rect(self.location[0], self.location[1] + self.lbl_height + 2, self.full_width, self.graph_height), 1)

            pygame.display.update()

        def update(self, value, color=white):
            self.clearValue()
            val = value + self.unit
            self.val_surface = self.font.render(val, 1, color)
            self.bsrinfo.screen.blit(self.val_surface, (self.location[0]+self.lbl_width, self.location[1]))

            # Draw Graph
            if self.graph:
                pygame.draw.rect(self.bsrinfo.screen, amber, pygame.Rect(self.location[0], self.location[1] + self.lbl_height + 2, self.full_width, self.graph_height), 1)

                m = interp(value,[self.min, self.max], [0, self.full_width])
                pygame.draw.rect(self.bsrinfo.screen, amber, pygame.Rect(self.location[0], self.location[1] + self.lbl_height + 2, m, self.graph_height))

            pygame.display.update()