import os       
import platform
import _logging

def Init_Windows():

        try:
                with open("setting.json", "w") as f:
                    f.write(
                        """
                        {
                                "path_init":"C://",
                                "command_history":true,
                                "command_history_write_to_file":true,
                                "command_history_file_path":"command_history/",
                                "command_alias_file_path":"command_alias.json"
                        }
                        """
                        )

                # 写入 command_alias.json 文件
                with open("command_alias.json", "w") as f:
                         f.write("")

                # 创建 command_history 文件夹
                os.makedirs(("command_history"), exist_ok=True)
                os.makedirs(("Log"), exist_ok=True)
        except Exception as e:
                print(e)
    

def Init_Linux():
        try:
                with open("setting.json", "w") as f:
                        f.write(
                        """
                        {
                                "path_init":"~/",
                                "command_history":true,
                                "command_history_file_path":"command_history/",
                                "command_alias_file_path":"command_alias.json"
                        }
                        """)
                        # 写入 command_alias.json 文件
                        with open("command_alias.json", "w") as f:
                                f.write("")

                        # 创建 command_history 文件夹
                        os.makedirs(("command_history"), exist_ok=True)
                        os.makedirs(("Log"), exist_ok=True)
        except Exception as e:
                print(e)
    
        
def Init():
        _log = _logging.Log()
        _log.log(Log.INFO, "正在初始化...")
        try:
                if platform.system() == "Windows":
                    Init_Windows()
                elif platform.system() == "Linux":
                    Init_Linux()
                else:
                    _log.Log(Log.ERROR, "不支持的操作系统")
                    sys.exit()

                _log.log(Log.INFO, "初始化完成")

        except Exception as e:
                _log.log(Log.ERROR, "初始化失败")

if __name__ == "__main__":
        Init_Windows()
