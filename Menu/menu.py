import os
import keyboard
from abc import ABC, abstractmethod


class CMenu(ABC):

    @staticmethod
    def clear():
        os.system('cls')

    def __init__(self, menu_name, menu_list, exit_menu=False):
        self.menu_name = menu_name
        self.menu_list = menu_list
        self.exit = "Exit" if exit_menu else "Back"
        self.position = 0
        keyboard.add_hotkey('up', self.up)
        keyboard.add_hotkey('down', self.down)

    @abstractmethod
    def show_menu(self):
        CMenu.clear()
        print(self.menu_name)

    def up(self):
        if self.position == 0:
            return
        self.position -= 1
        self.show_menu()

    def down(self):
        if self.position == len(self.menu_list):
            return
        self.position += 1
        self.show_menu()

    @abstractmethod
    def select_option(self):
        self.show_menu()
        keyboard.wait('return')




