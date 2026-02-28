
import colorama
import json
import os
import init
import sn
import platform
import time
from _logging import Log
import sys
import os_command


_Log = Log()
try:
        with open("setting.json", "r") as f:
                settings = json.load(f)
        path_now = settings["path_now"]
        IS_COMMAND_HISTORY_OPEN = settings["command_history"]
        IS_COMMAND_HISTORY_WRITE_TO_FILE = settings["command_history_write_to_file"]
        COMMAND_HISTORY_FILE_PATH = settings["command_history_file_path"]

except Exception as e:
        _Log.log(_Log.INFO, "初始化失败...")
        if platform.system() == "Windows":
                init.Init_Windows()
        else:
                pass
        with open("setting.json", "r") as f:
                settings = json.load(f)
        path_now = settings["path_init"]
        IS_COMMAND_HISTORY_OPEN = settings["command_history"]
        IS_COMMAND_HISTORY_WRITE_TO_FILE = settings["command_history_write_to_file"]
        COMMAND_HISTORY_FILE_PATH = settings["command_history_file_path"]        
        


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

def get_time():
        return time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())

class terminal():
        def __init__(self,path_init = "C:\\"):
                global command_history_filename,path_now


                self.system_command_handler = os_command.SystemCommandExecutor()
                self.system_command_handler.set_working_directory(path_init)

                path_now = path_init
                os.system(f"cd {path_now}")
                history_dir = os.path.abspath(COMMAND_HISTORY_FILE_PATH)
                os.makedirs(history_dir, exist_ok=True)  # 确保目录存在
                command_history_filename = f"{history_dir}/{get_time()}.txt" 
                with open(command_history_filename, "w") as f:
                        f.write(f"""
__ _  _   _____              _          _ 
/ __| \| | |_   _|__ _ _ _ __ (_)_ _ __ _| |
\__ \ .` |   | |/ -_) '_| '  \| | '_/ _` | |
|___/_|\_|   |_|\___|_| |_|_|_|_|_| \__,_|_|
______________________________________________
TIME: {get_time()} 
SYS : {sys.platform} {platform.uname()}
COMMAND HISTORY:
"""
                        )
        def welcome(self):
                try:
                        with open("version.json", "r") as f:
                                version = json.load(f)
                except Exception as e:
                        _Log.log(level= _Log.Error,text= "版本文件不存在！")

                print(f"""
__ _  _   _____              _          _ 
/ __| \| | |_   _|__ _ _ _ __ (_)_ _ __ _| |
\__ \ .` |   | |/ -_) '_| '  \| | '_/ _` | |
|___/_|\_|   |_|\___|_| |_|_|_|_|_| \__,_|_|
________________________________________________

{platform.uname()[1]}

""" + "\n" + YELLOWFORE + BOLD + f"SnTerminal {version['version']}" + RESETALL +"\n")

        def handle_input(self,path_run = path_now) -> str:
                """
                
                """
                
                input_command = input(
                        YELLOWFORE +"$ " + RESETALL +
                        GREENFORE + BOLD + f"{path_run} " + RESETALL +
                        BOLD + "> " + RESETALL)

                if IS_COMMAND_HISTORY_OPEN == True:
                        COMMAND_INPUT_HISTORY.append(input_command)
                        
                if IS_COMMAND_HISTORY_WRITE_TO_FILE == True:
                        with open(command_history_filename, "a") as f:
                                f.write(f"[ {get_time()} : input -> {path_run}] {input_command} \n")
                return input_command
        def handle_sys_command(self,command:str):
                try:

                        output_ = os.system(command)
                        if IS_COMMAND_HISTORY_OPEN == True:
                                COMMAND_OUTPUT_HISTORY.append(output_)

                        if IS_COMMAND_HISTORY_WRITE_TO_FILE == True:
                                with open(command_history_filename, "a") as f:
                                        f.write(f"[ {get_time()} : output ] {output_} \n")
                        print(output_)
                except Exception as e:
                        _Log.log(level= _Log.Error,text= e)
                        _Log.log_file(level= _Log.Error,text= e,file= command_history_filename)
        
        def run_command(self,command):
                pass

        def handle_sn_command(self,command:str,path_run = path_now):
                Sn_handle = sn.sn_command(path_run)
                Sn_handle.handle_command(command)

        def handle_command(self,command:str ,path_run = path_now):

                try:
                        if command.split()[0] == "sn":
                                self.handle_sn_command(command)
                        elif command.split()[0] == "cd":
                                try:
                                        path_now = command.split()[1]
                                        self.system_command_handler.set_working_directory(path_now)
                                except Exception as e:
                                        print(e)
                                        _Log.log(level= _Log.Error,text= e)
                                        _Log.log_file(level= _Log.Error,text= e,file= command_history_filename)

                        else:
                                self.system_command_handler.execute_command(command)
                                if IS_COMMAND_HISTORY_OPEN == True:
                                        COMMAND_OUTPUT_HISTORY.append(self.system_command_handler.get_command_history()[-1])
                                        _Log.log_file(level= _Log.INFO,text= self.system_command_handler.get_command_history()[-1],file= command_history_filename)


                except Exception as e:
                        if command == "":
                                pass
                        else:
                                print(e)

        def run(self,path_run = path_now):
                while True:
                        command = self.handle_input(path_run)
                        self.handle_command(command)

if __name__ == "__main__":
        test = terminal()
        test.welcome()
        test.run()