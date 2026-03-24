# tui

用 **Textual** 做终端界面实验：布局、组件、表格、日志等，方便以后扩展成更完整的 TUI 工具。

## 环境

- Python **3.12+**（与 [treadstone](https://github.com/earayu/treadstone) 对齐）
- 依赖管理：**uv**

```bash
make install   # 或: uv sync（会装 dev 组，含 textual-dev）
make dev       # `textual run --dev`（需 dev 依赖里的 textual-dev）
make run       # 普通运行: python -m tui
```

Textual 8 主包不附带 `textual` 可执行文件；**textual-dev** 提供 `textual run`、`textual console` 等，已写入 dev 依赖。

## 常用命令

| 命令        | 说明        |
| ----------- | ----------- |
| `make dev`  | `textual run --dev`，热重载 / 开发选项 |
| `make test` | pytest      |
| `make lint` | ruff        |

安装后也可：`uv run tui`。
