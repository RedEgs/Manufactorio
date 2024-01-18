import pytweening, pygame, sys, os
import random

import engine.libs.Formatter as formatter
import engine.libs.Utils as utils
import engine.libs.EntityService as EntityService 
import engine.libs.SceneService as SceneService 
import engine.libs.GuiService as GuiService 
import engine.libs.TweenService as TweenService


class Menu(SceneService.Scene):
    def __init__(self, scene_name, app):
        super().__init__(scene_name, app)
        self.app = app

        GuiService.ImageElement((formatter.get_center(1280, 720)), "cctd/resources/main_menu/background.png") # Background
        GuiService.ImageElement((243, 189), "cctd/resources/main_menu/logo.png")

        mod_button = GuiService.ButtonElement((48,48), ["cctd/resources/main_menu/mod_button.png"], [self.play_button])
        self.play_button = GuiService.ButtonElement((204, 396), ["cctd/resources/main_menu/play_button.png"], [self.play_button])
        option_button = GuiService.ButtonElement((166, 526), ["cctd/resources/main_menu/options_button.png"], [self.play_button])
        quit_button = GuiService.ButtonElement((159, 641), ["cctd/resources/main_menu/quit_button.png"], [self.play_button])

    def play_button(self):
        self.app.scenes.switch_scene("options")
    
    def on_enter(self):
        super().on_enter()
     
    def update(self):
        pass
        
    def draw(self):
        self.app.get_screen().fill((0))  
      
