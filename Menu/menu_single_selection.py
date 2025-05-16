from Menu.menu import CMenu


class CMenuSingleSelection(CMenu):

    def show_menu(self):
        CMenu.show_menu(self)
        for i in range(len(self.menu_list)):
            print("[X] " + self.menu_list[i]) if i == self.position else print("[ ] " + self.menu_list[i])
        print("[X] " + self.exit) if len(self.menu_list) == self.position else print("[ ] " + self.exit)

    def select_option(self):
        CMenu.select_option(self)
        return self.exit if self.position == len(self.menu_list) else self.menu_list[self.position]