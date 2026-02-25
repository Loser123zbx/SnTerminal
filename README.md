# SnTerminal

SnTerminal 是一个基于 Python 开发的终端模拟器，支持命令历史记录、别名管理以及图形化界面操作。该项目旨在提供一个轻量级且易于扩展的终端工具，适用于 Windows 系统。

# （处于测试与开发阶段）

## 📦 功能特性

- ✅ 命令历史记录（可选择是否保存到文件）
- ✅ 自定义命令别名
- ✅ 图形化界面支持（使用 wxPython）
- ✅ 多标签页终端窗口

## 🛠️ 技术栈

- **语言**: Python 3.x
- **GUI 框架**: wxPython
- **依赖库**: 
  - `colorama`（终端颜色支持）
  - `wx`（图形界面）
  - `json`（配置文件读写）

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/Loser123zbx/SnTerminal.git
cd SnTerminal/src
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 初始化项目

首次运行时会自动创建必要的配置文件和目录：

```bash
python init.py
```

### 4. 启动终端

#### 命令行模式：

```bash
python terminal.py
```

#### 图形界面模式：

```bash
python gui.py
```

## 🧪 测试

目前项目尚未添加单元测试，后续计划引入 `pytest` 进行测试覆盖。

## 📝 To-Do List

以下是未来计划完成的任务：

- [ ] 添加更多内置命令
- [ ] 支持跨平台（Linux/macOS）
- [ ] 增强图形界面功能（如主题切换、字体设置）
- [ ] 优化性能，减少内存占用
- [ ] 编写详细的用户文档和开发者指南
- [ ] 支持多语言界面（国际化）
- [ ] 增加命令补全功能

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库  
2. 创建你的分支 (`git checkout -b feature/AmazingFeature`)  
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)  
4. 推送到分支 (`git push origin feature/AmazingFeature`)  
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---

### 项目结构说明

```
SnTerminal/
├── src/
│   ├── _logging.py         # 日志记录模块
│   ├── init.py             # 项目初始化脚本
│   ├── sn.py               # 核心命令处理逻辑
│   ├── terminal.py         # 命令行终端主程序
│   ├── gui.py              # 图形界面主程序
│   ├── setting.json        # 配置文件
│   └── version.json        # 版本信息
└── README.md
```

### 配置文件说明

- [setting.json](file://f:\SnTerminal\src\setting.json): 包含路径初始化、命令历史记录开关等配置项。
- `command_alias.json`: 存储用户自定义的命令别名。
- [command_history](file://f:\SnTerminal\src\gui.py#L144-L163): 记录用户输入的历史命令。

### 示例用法

#### 添加命令别名

在终端中输入以下命令：

```bash
sn alias add ls dir
```

这将为 `dir` 命令创建一个别名 `ls`。

#### 查看命令历史

启用命令历史记录后，可以通过图形界面或直接查看 `command_history` 文件获取历史记录。

---

如有任何问题或建议，请随时提交 Issue！