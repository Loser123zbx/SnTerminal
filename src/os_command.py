import subprocess
import os
from datetime import datetime
import ctypes

class SystemCommandExecutor:
        def __init__(self, working_directory=None):
                """
                初始化系统命令执行器
                :param working_directory: 初始工作目录，默认为当前目录
                """
                self.working_directory = working_directory or os.getcwd()
                self.history = []

                # 加载 DLL
                dll_path = os.path.join(os.path.dirname(__file__), 'os_command.dll')
                self.lib = ctypes.CDLL(dll_path)

                # 定义函数签名
                self.lib.init_executor.argtypes = [ctypes.c_char_p]
                self.lib.set_working_directory.argtypes = [ctypes.c_char_p]
                self.lib.execute_command.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
                self.lib.get_command_history.argtypes = []
                self.lib.save_history_to_file.argtypes = [ctypes.c_char_p]
                self.lib.cleanup.argtypes = []

                # 初始化执行器
                self.lib.init_executor(None)

        def set_working_directory(self, directory):
                """
                设置当前工作目录
                :param directory: 目标目录路径
                """
                self.lib.set_working_directory(directory.encode())

        def execute_command(self, command, capture_output=True, print_output=True):
                """
                执行系统命令
                :param command: 要执行的命令字符串
                :param capture_output: 是否捕获输出（默认 True）
                :param print_output: 是否实时打印输出到控制台（默认 True）
                :return: 包含 stdout、stderr 和 returncode 的字典
                """
                result = self.lib.execute_command(command.encode(), capture_output, print_output)
                self.history.append({
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "command": command,
                    "result": result
                })
                return result

        def get_command_history(self):
                """
                获取命令历史记录
                :return: 历史记录列表
                """
                return self.history

        def save_history_to_file(self, filename):
                """
                将命令历史保存到文件
                :param filename: 文件名
                """
                self.lib.save_history_to_file(filename.encode())

if __name__ == "__main__":
        executor = SystemCommandExecutor()
        executor.execute_command("dir")
        executor.set_working_directory("D:\\123_softs")
        executor.execute_command("dir /s")
        