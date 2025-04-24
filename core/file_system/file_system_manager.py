import json
from pathlib import Path


class FileSystemManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileSystemManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return
        self._initialized = True

        self.project_root = Path(__file__).resolve().parents[2]
        self.config_dir = self.project_root / "core" / "config"
        self.data_dir = self.config_dir / "_data"
        self.users_file = self.data_dir / "users.json"

    def ensure_directories(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def get_user_json_path(self) -> Path:
        return self.users_file

    def export_to_json(self, data: list[dict], filename: Path = None):
        self.ensure_directories()

        with open(filename or self.users_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
