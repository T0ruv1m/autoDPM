from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets"

def get_path(file_name: str) -> str:
    asset_path = ASSETS_DIR / file_name
    if not asset_path.exists():
        raise FileNotFoundError(f"Asset not found:{asset_path}")
    return str(asset_path)