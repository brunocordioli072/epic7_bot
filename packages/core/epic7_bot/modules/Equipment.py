import logging
import math
import asyncio
from epic7_bot.utils.runInParallel import runInParallel
from epic7_bot.core.DeviceManager import DeviceManager
from epic7_bot.core.MathUtils import MathUtils
from epic7_bot.modules.Module import Module
from epic7_bot.templates.EquipmentTemplates import EquipmentTemplates


class Equipment(Module):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.EquipmentTemplates = EquipmentTemplates()


    #def inventory_full(self):
        #if self.ScreenManager.match_color_on_screen_area(
                #x1=629, y1=175, x2=960, y2=224, template=self.EquipmentTemplates.inventory_full, percentage=0.6) is True:
            #logging.info(f"Inventory full, finishing crafting")
            #return False
        #return True
    
    
    def craft_and_extract_blues(self):
        
        self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
            x1=365, y1=785, x2=562, y2=828, action="Click on arrange button")

        if self.ScreenManager.match_color_on_screen_area(
                x1=164, y1=262, x2=264, y2=362) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                x1=164, y1=262, x2=264, y2=362, action="Click on equipment")
            
        if self.ScreenManager.match_color_on_screen_area(
                x1=490, y1=262, x2=590, y2=362) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                x1=490, y1=262, x2=590, y2=362, action="Click on equipment")

        if self.ScreenManager.match_color_on_screen_area(
                x1=814, y1=262, x2=914, y2=362) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                x1=814, y1=262, x2=914, y2=362, action="Click on equipment")
            
        if self.ScreenManager.match_color_on_screen_area(
                x1=1139, y1=262, x2=1239, y2=362) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                x1=1139, y1=262, x2=1239, y2=362, action="Click on equipment")
            
        if self.ScreenManager.match_color_on_screen_area(
                x1=164, y1=408, x2=264, y2=508) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                x1=164, y1=408, x2=264, y2=508, action="Click on equipment")
            
        if self.ScreenManager.match_color_on_screen_area(
                x1=490, y1=408, x2=590, y2=508) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
               x1=490, y1=408, x2=590, y2=508, action="Click on equipment")

        if self.ScreenManager.match_color_on_screen_area(
                x1=814, y1=408, x2=914, y2=508) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                x1=814, y1=408, x2=914, y2=508, action="Click on equipment")
            
        if self.ScreenManager.match_color_on_screen_area(
                x1=1139, y1=408, x2=1239, y2=508) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                x1=1139, y1=408, x2=1239, y2=508, action="Click on equipment")

        if self.ScreenManager.match_color_on_screen_area(
                x1=490, y1=553, x2=590, y2=653) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                x1=490, y1=553, x2=590, y2=653, action="Click on equipment")
            
        if self.ScreenManager.match_color_on_screen_area(
                x1=814, y1=553, x2=914, y2=653) is True:
            self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
                x1=814, y1=553, x2=914, y2=653, action="Click on equipment")

        self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
            x1=1096, y1=779, x2=1332, y2=832, action="Click on extract button")
        
        self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
            x1=822, y1=627, x2=1031, y2=683, action="Click on extract button")      
        
        self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
            x1=274, y1=783, x2=482, y2=833, action="Click on cancel button")    

        self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
            x1=928, y1=786, x2=1234, y2=826, action="Click on craft again button")

        self.ScreenManager.random_click_on_area_and_check_change_on_area_retry(
            x1=758, y1=623, x2=1034, y2=658, action="Click on craft button")

        self.craft_and_extract_blues()    

    def start_crafting(self):
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=1024, y1=508, x2=1191, y2=579, action="Click on Craft x10 button")
        
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=750, y1=624, x2=1027, y2=658, action="Click on Craft button")

        self.craft_and_extract_blues()

    #def start_crafting_from_lobby(self):
        #self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        #self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
        #    x1=270, y1=225, x2=341, y2=284, action="Click on Sanctuary")
        
        #self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
        #    x1=1122, y1=686, x2=1307, y2=765, action="Click on Steel Workshop")
        
        #self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
        #    x1=430, y1=457, x2=559, y2=595, action="Click on Crafting")
        
        #tbd - add choose hunt to craft and equipment type (boots,equipments,etc..)

        #self.start_crafting()
