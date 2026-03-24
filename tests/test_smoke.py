from __future__ import annotations

import pytest
from textual.widgets import DataTable

from tui.app import PlaygroundApp


@pytest.mark.asyncio
async def test_app_mounts() -> None:
    app = PlaygroundApp()
    async with app.run_test():
        table = app.query_one("#demo-table", DataTable)
        assert table.row_count == 12
