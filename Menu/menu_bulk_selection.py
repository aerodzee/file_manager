from Menu.menu import CMenu


class CMenuBulkSelection(CMenu):

    def __init__(self, menu_name, menu_list, exit_menu=False):
        CMenu.__init__(self, menu_name, menu_list, exit_menu)
        self.selection = []

    def show_menu(self):
        CMenu.show_menu(self)
        for i in range(len(self.menu_list)):
            if i in self.selection:
                print("[\033[4mX\033[0m] " + self.menu_list[i]) if i == self.position else print("[X] " + self.menu_list[i])
            else:
                print("[\033[4m \033[0m] " + self.menu_list[i]) if i == self.position else print("[ ] " + self.menu_list[i])
        print("[\033[4m-\033[0m] " + self.exit) if len(self.menu_list) == self.position else print("[-] " + self.exit)

    def select_option(self):
        CMenu.select_option(self)
        if self.position == len(self.menu_list):
            return
        if self.position in self.selection:
            self.selection.remove(self.position)
        else:
            self.selection.append(self.position)
        self.select_option()
