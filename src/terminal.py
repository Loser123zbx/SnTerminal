
import colorama
import json
import os
import init
import sn
import platform
import time
from _logging import Log
import sys
import subprocess
from datetime import datetime
from typing import Dict


_Log = Log()
try:
        with open("setting.json", "r") as f:
                settings = json.load(f)
        path_now = settings["path_now"]
        IS_COMMAND_HISTORY_OPEN = settings["command_history"]
        IS_COMMAND_HISTORY_WRITE_TO_FILE = settings["command_history_write_to_file"]
        COMMAND_HISTORY_FILE_PATH = settings["command_history_file_path"]
        TERMINAL_ENCODING = settings["terminal_encoding"]

except Exception as e:
        _Log.log(_Log.ERROR, "初始化失败...")
        if platform.system() == "Windows":
            pass
        else:
                pass
        with open("setting.json", "r") as f:
                settings = json.load(f)
        path_now = settings["path_init"]
        IS_COMMAND_HISTORY_OPEN = settings["command_history"]
        IS_COMMAND_HISTORY_WRITE_TO_FILE = settings["command_history_write_to_file"]
        COMMAND_HISTORY_FILE_PATH = settings["command_history_file_path"]        
        TERMINAL_ENCODING = settings["terminal_encoding"]
        


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
        """
        
        """
        def __init__(self,path_init = "C:\\"):
                global command_history_filename,path_now



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
                        with open("version.txt", "r") as f:
                                version = f.read()
                except Exception as e:
                        version = "Unknown"
                        _Log.log(level= _Log.Error,text= "版本文件不存在！")

                print(f"""
 __ _  _   _____              _          _                          
/ __| \| | |_   _|__ _ _ _ __ (_)_ _ __ _| |
\__ \ .` |   | |/ -_) '_| '  \| | '_/ _` | |                                        {BLUEBACK + "Sn Terminal" + RESETALL}
|___/_|\_|   |_|\___|_| |_|_|_|_|_| \__,_|_|                                        TIME: {get_time()}
________________________________________________                                    SYSTEM: {platform.uname()[0]}{platform.uname()[2]}({platform.uname()[3]})
                                                                                    COMPUTER: {platform.uname()[1]}
                                                                                    User: {os.getlogin()}

""" + "\n" + YELLOWFORE + BOLD + f"SnTerminal {version}" + RESETALL +"\n")

        def handle_input(self, path_run = path_now) -> str:
                """
                输入处理函数
                :param path_run: 当前执行目录
                :return: 输入的字符串
                """
                try:
                        # 标准化路径显示
                        display_path = path_run.replace("//", "/").replace("\\", "/")
                        
                        input_command = input(
                        YELLOWFORE + "$ " + RESETALL +
                        GREENFORE + BOLD + f"{display_path} " + RESETALL +
                        BOLD + "> " + RESETALL
                        )

                        if IS_COMMAND_HISTORY_OPEN == True:
                                COMMAND_INPUT_HISTORY.append(input_command)
                        
                        if IS_COMMAND_HISTORY_WRITE_TO_FILE == True:
                                with open(command_history_filename, "a") as f:
                                        f.write(f"[ {get_time()} : input -> {path_run}] {input_command} \n")
                        return input_command
                        
                except KeyboardInterrupt:
                        # 重新抛出，让 run() 方法处理
                        raise
        def handle_sys_command(self,command:str):
                """
                系统命令处理函数
                :param command: 命令字符串
                """
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
                        _Log.log_file(level= _Log.ERROR,text= e,file= command_history_filename)

        def handle_sn_command(self,command:str,path_run = path_now):
                """
                Sn命令处理函数
                :param command: 命令字符串
                :param path_run: 运行路径
                """
                Sn_handle = sn.sn_command(path_run)
                Sn_handle.handle_command(command)

        def handle_command(self,command:str ,path_run = path_now,print_output: bool = True) -> Dict[str, str]:
                try:
                        # 启动子进程
                        process = subprocess.Popen(
                                command,
                                shell=True,
                                cwd=path_run,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                text=True,
                                encoding=TERMINAL_ENCODING,
                                errors='ignore'
                        )
                        
                        output = ""
                        
                        # 逐行读取输出并实时打印
                        for line in process.stdout:
                                output += line
                                if print_output:
                                        print(line, end='')
                        
                        # 等待进程结束并获取返回码
                        return_code = process.wait()
                        
                        # 根据返回码决定时间戳
                        if return_code == 0:
                                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                return {timestamp: output}
                        else:
                                return {"0": output}
                        
                except Exception as e:
                        error_msg = f"执行异常：{str(e)}"
                        if print_output:
                                print(error_msg)
                                return {"0": error_msg}

        def run(self,path_run = path_now):
                """
                控制台运行函数
                :param path_run: 运行路径
                """
                while True:
                        command = self.handle_input(path_run)
                        self.handle_command(command)

if __name__ == "__main__":
        try:
                test = terminal()
                test.welcome()
                test.run()
        except KeyboardInterrupt:
                print(f"\n{YELLOWFORE}程序被用户中断{RESETALL}")
        except Exception as e:
                _Log.log(level=_Log.ERROR, text=f"启动失败：{str(e)}")
                print(f"{REDFORE}启动失败：{str(e)}{RESETALL}")
        finally:
                print(f"{GREENFORE}感谢使用 SnTerminal{RESETALL}")