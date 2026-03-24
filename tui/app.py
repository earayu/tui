"""Textual demo: tabs, grid, table, log, progress — starting point for TUI experiments."""

from __future__ import annotations

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Grid, Vertical
from textual.widgets import (
    DataTable,
    Footer,
    Header,
    Label,
    ProgressBar,
    RichLog,
    Static,
    TabbedContent,
    TabPane,
)


class PlaygroundApp(App[None]):
    """Sandbox TUI for trying Textual widgets and layouts."""

    TITLE = "TUI Playground"
    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
        Binding("d", "toggle_dark", "Theme", show=True),
    ]
    CSS_PATH = "app.tcss"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with TabbedContent():
            with TabPane("概览", id="tab-overview"):
                yield Vertical(
                    Static(
                        "用 [bold cyan]Tab[/] 切换标签；[bold]q[/] 退出；[bold]d[/] 切换深色/浅色。",
                        id="intro",
                    ),
                    Label("色块网格（Grid + CSS 变量）"),
                    Grid(
                        Static(" Panel A ", classes="cell cell-a"),
                        Static(" Panel B ", classes="cell cell-b"),
                        Static(" Panel C ", classes="cell cell-c"),
                        Static(" Panel D ", classes="cell cell-d"),
                        id="color-grid",
                    ),
                    Label("进度条"),
                    ProgressBar(total=100, show_eta=False, id="demo-pb"),
                    classes="tab-body",
                )
            with TabPane("表格", id="tab-table"):
                yield Vertical(
                    DataTable(cursor_type="row", zebra_stripes=True, id="demo-table"),
                    classes="tab-body",
                )
            with TabPane("日志", id="tab-log"):
                yield Vertical(
                    RichLog(highlight=True, markup=True, id="demo-log"),
                    classes="tab-body",
                )
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#demo-pb", ProgressBar).progress = 65

        table = self.query_one("#demo-table", DataTable)
        table.add_columns("列 A", "列 B", "说明")
        for i in range(12):
            table.add_row(f"行 {i}", str(i * i), "演示数据")

        log = self.query_one("#demo-log", RichLog)
        log.write("[green]就绪[/] — Rich markup 在 RichLog 里可用。")
        for line in range(1, 6):
            log.write(f"事件 #{line}")
