import pytweening, pygame, json, sys, os

current_dir = os.path.dirname(os.path.realpath(__file__))
resources_dir = os.path.join(current_dir, '..', '..', 'resources')

from ..libs.gui import *
from ..libs.utils import *
from ..libs.scenes import *
from ..libs.map import *


class LobbyScene(Scene):
    def __init__(self, screen, registry, scene_director, scene_name):
        super().__init__(screen, scene_director, scene_name)

        self.screen = screen
        self.registry = registry
        self.scene_director = scene_director
        self.scene_name = scene_name
        
        self.map_director = MapDirector(screen)

        self.width, self.height = self.screen.get_size()
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        
        self.playButton = Button(
            self.center_x, self.center_y-500, os.path.join(resources_dir, "lobby", "endless_button_off.png"), os.path.join(resources_dir, "lobby", "endless_button_on.png"), self.playGame)
        self.background = pygame.image.load(
            os.path.join(resources_dir, "lobby", "background.png")).convert_alpha()

        self.towers_limit = 4
        self.hero_limit = 1
        
        self.amount_heros = 0
        self.amount_towers = 0
        
        

    def load_select_towers(self):
        towers_data = self.registry.get_towers_data()
        self.tower_items = []  
        self.tower_buttons = []
        self.tower_ids = []
        
        for tower_data in towers_data:   
            print("Loading Item")         
            image = pygame.image.load(os.path.join(current_dir, '..', '..', 'resources', 'lobby',f'tower_select_{check_rarity_color(tower_data["base_rarity"])}.png')).convert_alpha()
            cover = pygame.image.load(os.path.join(current_dir, '..', '..', 'towers', tower_data["id"], f'cover.png')).convert_alpha()
           
            cover_pos = cover.get_rect(center=(image.get_width()//2, image.get_height()//2))
            image.blit(cover, cover_pos)
            
            center_pos_x, center_pos_y = calculate_index_spacing_out(towers_data.index(tower_data), 163, 177, image.get_width(), image.get_height(), 44, 9, 4)
            corner_pos = calculate_index_spacing(towers_data.index(tower_data), 107, 110, image.get_width(), image.get_height(), 44, 9, 4)
            
            button = Button(center_pos_x, center_pos_y, os.path.join(current_dir, '..', '..', 'resources', 'lobby',f'tower_select_{check_rarity_color(tower_data["base_rarity"])}.png'), os.path.join(current_dir, '..', '..', 'resources', 'lobby',f'tower_select_{check_rarity_color(tower_data["base_rarity"])}.png'), lambda id=tower_data["id"]: self.select_tower(id))
            
            self.tower_ids.append(tower_data["id"])
            self.tower_buttons.append(button)
            self.tower_items.append((image, corner_pos))
            
        return self.tower_items, self.tower_buttons, self.tower_ids
            

    def select_tower(self, id):
        #index = self.tower_ids.index(id)
        string = self.registry.get_tower_dir(id)
        list = self.registry.selected_towers
          
        if len(list) <= self.towers_limit + self.hero_limit:    
            if is_in_list(string, list):
                print("Item already in list")
            else:
                if self.registry.get_tower_data(id)["base_rarity"] >= 4: # If card is a hero
                    if self.amount_heros >= self.hero_limit:
                        print("Hero already selected")
                    else:
                        self.registry.add_to_selected_towers(self.registry.get_tower_dir(id))
                        self.amount_heros += 1
                        print("selected hero")
                                            
                        if len(list) == self.towers_limit + self.hero_limit:
                            self.playButton.tween_pos((self.center_x, self.center_y-250), 1 ,0, pytweening.easeInOutQuad) 
                
                        
                elif self.amount_towers >= self.towers_limit:
                    print("Reached Normal Tower Limit")
                    
                    if len(list) == self.towers_limit + self.hero_limit:
                        self.playButton.tween_pos((self.center_x, self.center_y-250), 1 ,0, pytweening.easeInOutQuad) 
                
                else:
                    self.registry.add_to_selected_towers(self.registry.get_tower_dir(id))
                    self.amount_towers += 1
                    print("Selected Tower")
                    
                    if len(list) == self.towers_limit + self.hero_limit:
                        self.playButton.tween_pos((self.center_x, self.center_y-250), 1 ,0, pytweening.easeInOutQuad) 
        
        else:
              
            print("Reached Max Towers")
            
        print("Heroes: " + str(self.amount_heros))
        print("Towers: " + str(self.amount_towers))
        
       


    def playGame(self):
        self.scene_director.switch_scene("game_scene")

    def on_exit(self):
        return super().on_exit()

    def on_enter(self):
        self.towers, self.tower_buttons, self.tower_ids = self.load_select_towers()
    
    def events(self, event):
        self.playButton.handle_event(event)
        
        for button in self.tower_buttons:
            button.handle_event(event)

    def update(self):
        self.playButton.update()
        
        for button in self.tower_buttons:
            button.update()

    def draw(self):
        self.screen.fill(0)
        
        self.screen.blit(self.background, (0,0))
        self.playButton.draw(self.screen)
        
        for tower in self.towers:
            self.screen.blit(tower[0], tower[1]) 
                     
    def run(self, event):
        self.events(event)
        self.update()
        self.draw()

    def get_scene_info(self):
        return self.scene_name