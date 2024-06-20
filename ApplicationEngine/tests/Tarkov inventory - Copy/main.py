# Main project file
import pygame, sys, os, random
import pyredengine as pyr

import scenes.example_scene as example_scene


class Item:
    def __init__(self, position: pygame.Vector2) -> None:
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.position = position
        self.path = "gun.png"
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image.get_rect(center= position )
        self.image.fill((0, 255, 0))
        
    def draw(self, display: pygame.Surface):
        display.blit(self.image, self.image.get_rect(center=self.position))

    

class MainGame():
    def __init__(self, parent) -> None:
        pygame.init()

        self._init_display()
        self.clock = pygame.time.Clock()
        self.run = True
        self.mouse_pos = (0,0) 
        self.mouse_rect = pygame.Rect(self.mouse_pos[0], self.mouse_pos[1], 10, 10)
        
        self.dragging = False
        
        self.draw_buffer = []
        self.rect_buffer = []
        
        for i in range(3):
            item = Item((random.randint(0, 1280), random.randint(0, 720)))
            self.draw_buffer.append(item)
            self.rect_buffer.append(item.image.get_rect(center=item.position))
        
        
        
    def _init_display(self): # Don't touch 
        """Initialises the display to be rendered within the viewport window of the engine"""
        self._hwnd = None
        if len(sys.argv) > 1:
            self._hwnd = int(sys.argv[1])
            os.environ['SDL_WINDOWID'] = str(self._hwnd)
        
        self.display_width = 1280
        self.display_height = 720
        
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-1000, -1000)
        self.display = pygame.display.set_mode((self.display_width, self.display_height), pygame.NOFRAME)
        pygame.display.set_caption("Pygame Window")
        
    def _send_event(self, type, key = None, mouse_x = None, mouse_y = None):
        """Manages event handling between viewport window and the game"""
    
        if type == 1:
            event = pygame.event.Event(pygame.KEYDOWN, key=key)
            pygame.event.post(event)
        elif type == 2:
            last_pos = (mouse_x, mouse_y)
            
            if last_pos:
                rel_x = mouse_x - last_pos[0]
                rel_y = mouse_y - last_pos[1]
            else:
                rel_x, rel_y = 0, 0

            last_pos = (mouse_x, mouse_y)
                        
            event = pygame.event.Event(pygame.MOUSEMOTION, {'pos': (mouse_x, mouse_y), 'rel': (rel_x, rel_y), 'buttons': pygame.mouse.get_pressed()})
            pygame.event.post(event)
            pygame.mouse.set_pos(mouse_x, mouse_y)
        
    def handle_events(self):
        """Handles custom user events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEMOTION: 
                self.mouse_pos = event.pos

            
    def update(self):
        """Put all your custom logic here"""
        
        self.mouse_rect.center = self.mouse_pos





















    def draw(self):
        """Custom drawing logic here"""
        import math
        
        
        self.display.fill((255, 255, 255))
        for i in self.draw_buffer:
            i.draw(self.display)

        for r in self.rect_buffer:
            if self.mouse_rect.colliderect(r):
                if pygame.mouse.get_pressed(1):
                    pygame.draw.rect(self.display, (255, 0, 0), self.mouse_rect, 10)
        
        
        pygame.draw.rect(self.display, (255, 0, 0), self.mouse_rect, 10)
        
        
        pygame.display.flip()
    
    def run_game(self):
        """Handles the running of the game"""
        
        while self.run: # Don't touch
            self.clock.tick()
            self.handle_events()
            self.update()
            self.draw()
            
            yield self.display

        pygame.quit()
        sys.exit()
        
    def close_game(self):
        self.run = False
        pygame.quit()
    
