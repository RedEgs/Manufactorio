import pygame, json, os, sys

from engine.app import *
from engine.libs import SceneService as SceneService

from tkinter import *

import scenes.main_menu as main_menu
import scenes.difficulty_select as d_select
import scenes.map_select as m_select
import scenes.tower_select as t_select
import scenes.main_game as main_game
import scenes.map_editor as map_editor
import scenes.user_login as user_login
import scenes.network_test as network_test
import scenes.example_scene as example_scene


class Main(App):
    def __init__(self):
        super().__init__()
    
    def set_user(self, user):
        self.user = user

    def load_scenes(self):
        self.scenes.load_scenes([network_test.Network_Test("network_test", self),
                                 map_editor.Map_Editor("map_editor", self),
                                 main_game.Main_Game("main_game", self),
                                 t_select.Tower_Select("tower_select", self),
                                 m_select.Map_Select("map_select", self),
                                 d_select.Difficulty_Select("difficulty_select", self),
                                 main_menu.Menu("main_menu", self),
                                 user_login.User_Login("user_login", self),
                                 example_scene.Example_Scene("example_scene", self)])
        self.scenes.set_scene("example_scene")  
         
        
        

        
        
        

    

if __name__ == "__main__":
    main = Main()
    main.run()
