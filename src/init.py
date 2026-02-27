import os

def Init_Windows():
    # 创建必要的目录
    base_dir = "C:\\Program Files (x86)\\SnTerminal"
    os.makedirs(base_dir, exist_ok=True)  # 确保目录存在

    # 写入 setting.json 文件
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

if __name__ == "__main__":
    Init_Windows()