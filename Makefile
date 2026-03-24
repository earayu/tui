.PHONY: help install dev test lint format

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies (uv sync)
	uv sync

dev: ## Run TUI app with Textual dev console (Ctrl+Shift+D)
	uv run textual run --dev tui.app:PlaygroundApp

run: ## Run TUI app (no dev console)
	uv run python -m tui

test: ## Run tests
	uv run pytest tests/ -v

lint: ## Ruff check + format check
	uv run ruff check tui/ tests/
	uv run ruff format --check tui/ tests/

format: ## Auto-fix and format
	uv run ruff check --fix tui/ tests/
	uv run ruff format tui/ tests/
