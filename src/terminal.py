import colorama
import json
import os
import init

try:
        with open("settings.json", "r") as f:
                settings = json.load(f)
        path_now = settings["path_now"]
        IS_COMMAND_HISTORY_OPEN = settings["command_history"]
        IS_COMMAND_HISTORY_WRITE_TO_FILE = settings["command_history_write_to_file"]
        COMMAND_HISTORY_FILE_PATH = settings["command_history_file_path"]

except Exception as e:
        init.Init()
        


# 颜色定义
BLACKFORE = colorama.Fore.BLACK
BLUEFORE = colorama.Fore.BLUE
CYANFORE = colorama.Fore.CYAN
GREENFORE = colorama.Fore.GREEN
MAGENTAFORE = colorama.Fore.MAGENTA
REDFORE = colorama.Fore.RED
WHITEFORE = colorama.Fore.WHITE
YELLOWFORE = colorama.Fore.YELLOW
RESETFORE = colorama.Fore.RESET

BLACKBACK = colorama.Back.BLACK
BLUEBACK = colorama.Back.BLUE
CYANBACK = colorama.Back.CYAN
GREENBACK = colorama.Back.GREEN
MAGENTABACK = colorama.Back.MAGENTA
REDBACK = colorama.Back.RED
WHITEBACK = colorama.Back.WHITE
YELLOWBACK = colorama.Back.YELLOW
RESETBACK = colorama.Back.RESET

BOLD = colorama.Style.BRIGHT
NORMAL = colorama.Style.NORMAL
DIM = colorama.Style.DIM
RESETALL = colorama.Style.RESET_ALL

COLOR_DICT = {
        0 : BLACKFORE,
        1 : BLUEFORE,
        2 : CYANFORE,
        3 : GREENFORE,
        4 : MAGENTAFORE,
        5 : REDFORE,
        6 : WHITEFORE,
        7 : YELLOWFORE,
        8 : RESETFORE,
        9 : BLACKBACK,
        10 : BLUEBACK,
        11 : CYANBACK,
        12 : GREENBACK,
        13 : MAGENTABACK,
        14 : REDBACK,
        15 : WHITEBACK,
        16 : YELLOWBACK,
        17 : RESETBACK,
        18 : BOLD,
        19 : NORMAL,
        20 : DIM,
        21 : RESETALL
}



if IS_COMMAND_HISTORY_OPEN == True:
        COMMAND_INPUT_HISTORY = []
        COMMAND_OUTPUT_HISTORY = []



class terminal():
        def __init__(self,path_now = "C:\\"):
                self.path_now = path_now
        def welcome(self):
                try:
                        with open("version.json", "r") as f:
                                version = json.load(f)
                except Exception as e:
                        print(e)
                print("""
        __ _  _   _____              _          _ 
        / __| \| | |_   _|__ _ _ _ __ (_)_ _ __ _| |
        \__ \ .` |   | |/ -_) '_| '  \| | '_/ _` | |
        |___/_|\_|   |_|\___|_| |_|_|_|_|_| \__,_|_|
        ________________________________________________
        """ + "\n" + YELLOWFORE + BOLD + f"SnTerminal {version['version']}" + RESETALL)

        def handle_input(self,path_now) -> str:
                input_command = input(
                        YELLOWFORE +"$ " + RESETALL +
                        GREENFORE + BOLD + f"{path_now} " + RESETALL +
                        BOLD + "> " + RESETALL)
                if IS_COMMAND_HISTORY_OPEN == True:
                        COMMAND_INPUT_HISTORY.append(input_command)
                        
                if IS_COMMAND_HISTORY_WRITE_TO_FILE == True:
                        with open(COMMAND_HISTORY_FILE_PATH, "a") as f:
                                f.write(input_command + "\n")
                return input_command
        def handle_sys_command(self,command:str):
                try:
                        output_ = os.system(command)
                        if IS_COMMAND_HISTORY_OPEN == True:
                                COMMAND_OUTPUT_HISTORY.append(output_)

                        if IS_COMMAND_HISTORY_WRITE_TO_FILE == True:
                                with open(COMMAND_HISTORY_FILE_PATH, "a") as f:
                                        f.write(output_ + "\n")
                        print(output_)
                except Exception as e:
                        print(e)
        
        def run_command(self,command):
                pass

        def handle_sn_command(self,command:str):
                self.run_command(command)

        def handle_command(self,command:str):
                if command.split()[0] == "sn":
                        self.handle_sn_command(command)
                else:
                        self.handle_sys_command(command)

        def run(self):
                while True:
                        command = self.handle_input(self.path_now)
                        self.handle_command(command)

if __name__ == "__main__":
        test = terminal()
        test.welcome()
        test.run()