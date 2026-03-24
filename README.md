# tui

用 **Textual** 做终端界面实验：布局、组件、表格、日志等，方便以后扩展成更完整的 TUI 工具。

## 环境

- Python **3.12+**（与 [treadstone](https://github.com/earayu/treadstone) 对齐）
- 依赖管理：**uv**

```bash
make install   # 或: uv sync
make dev       # Textual 开发模式（可开控制台）
make run       # 普通运行: python -m tui
```

## 常用命令

| 命令        | 说明        |
| ----------- | ----------- |
| `make dev`  | `textual run --dev`，调样式/布局方便 |
| `make test` | pytest      |
| `make lint` | ruff        |

安装后也可：`uv run tui`。
