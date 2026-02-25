import os
import _logging
import json

with open("setting.json", "r") as f:
        setting = json.load(f)
ALIAS_FILE_PATH = setting["command_alias_file_path"]


class sn_command:
        def __init__(self,path_now = "C:\\"):
                self.path_now = path_now

        def handle_command(self,command:str):
                """
        head command var1 var2 ...
        - >
        command , [var1,var2,...]
                """
                log = _logging.Log()
                command = command.split(" ")

                del command[0]
                if command[0] == "alias":
                        if command[1] == "add":
                                vars = command[1:]
                                self.handle_add_command_alias(vars)


        def handle_add_command_alias(self,vars:list):
                """
        [var1,var2] -> {command:alias}
        write to >> alias.json
                """
                log = _logging.Log()
                if len(var) == 2:
                        try:
                                with open(ALIAS_FILE_PATH, "r") as f:
                                        alias = json.load(f)

                                with open(ALIAS_FILE_PATH, "w") as f:
                                        alias[var[0]] = var[1]
                                        json.dump(alias,f)
                                        log.log(level = log.INFO,text = "Add command alias successfully")

                        except Exception as e:
                                log.log(level = log.ERROR,text = "Error: " + str(e))
                else:
                        log.log(level = log.WARNING,text = "If you give more than two parameters, the first parameter will be the command, and the second parameter will be the alias")
                


