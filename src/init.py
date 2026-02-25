import os

def Init():
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
        "command_history_file_path":"C:\\\\Program Files (x86)\\\\SnTerminal\\\\command_history",
        "command_alias_file_path":"C:\\\\Program Files (x86)\\\\SnTerminal\\\\command_alias.json"
}
"""
        )

    # 写入 command_alias.json 文件
    with open(os.path.join(base_dir, "command_alias.json"), "w") as f:
        f.write("")

    # 写入 command_history 文件
    with open(os.path.join(base_dir, "command_history"), "w") as f:
        f.write("")

if __name__ == "__main__":
    Init()