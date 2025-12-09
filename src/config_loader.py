import tomllib
from pathlib import Path

CONFIG_PATH = Path("config/settings.toml")

def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError("settings.toml not found")

    with CONFIG_PATH.open("rb") as f:
        return tomllib.load(f)