import os
from Menu.menu_single_selection import CMenuSingleSelection
from Menu.menu_bulk_selection import CMenuBulkSelection
from operator import methodcaller


class CTranscoder:

    name = "Transcoder"
    transcoder_menu = [
        "Transcode",
        "Select Files",
        "Load Preset",
        "Change Transcode Options",
        "Change Post-Transcode Options",
        "Print Selection"
    ]
    supported_files = [
        ".m4v",
        ".mp4",
        ".mkv",
        ".avi",
        ".mpg",
        ".mpeg"
    ]

    def __init__(self):
        print("Starting transcoder")
        self.transcode_menu = CMenuSingleSelection(CTranscoder.name, CTranscoder.transcoder_menu)
        self.transcode_menu.select_option()
        sel = self.transcode_menu.select_option()
        method = methodcaller(sel.lower().replace(' ', '_'))
        method(self)

    def select_preset(self):
        print()

    def load_preset(self):
        print()

    def change_transcode_options(self):
        print()

    def select_post_transcode_options(self):
        print()

    def select_files(self):
        print()

    def add_files(self):
        print()

    def remove_files(self):
        print()

    def print_selection(self):
        print()

    def print_progress_bar(self):
        print()

    def transcode(self):
        print()

    def post_transcode(self):
        print()


transcoder = CTranscoder()
