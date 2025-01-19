import os
import json
from pathlib import Path


class Config:
    """
    Centralized configuration class for the project.
    """

    # Private attributes
    _KAGGLE_CONFIG_DIR = os.getenv("KAGGLE_CONFIG_DIR", str(Path.home() / ".kaggle"))
    _DATASETS_DIR = os.getenv("DATASETS_DIR", str(Path.home() / "github-projects/modern-ml/week_1/data/raw"))
    _COMPETITION_NAME = os.getenv("KAGGLE_COMPETITION", "neo-bank-non-sub-churn-prediction")
    _ENV = os.getenv("ENV", "development").lower()

    def __init__(self):
        """
        Initialize configuration.
        """
        self.kaggle_json_path = os.path.join(self._KAGGLE_CONFIG_DIR, "kaggle.json")

    @property
    def datasets_dir(self) -> str:
        """
        Directory where datasets will be downloaded.
        """
        return self._DATASETS_DIR

    @property
    def competition_name(self) -> str:
        """
        Kaggle competition name.
        """
        return self._COMPETITION_NAME

    @property
    def env(self) -> str:
        """
        Current application environment.
        """
        return self._ENV


class KaggleValidator:
    """
    Utility class for validating Kaggle configuration and credentials.
    """

    @staticmethod
    def validate_file_exists(file_path: str):
        """
        Validates that the file exists at the given path.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(
                f"Kaggle credentials not found at {file_path}. "
                "Ensure KAGGLE_CONFIG_DIR is set correctly or the file exists."
            )

    @staticmethod
    def validate_json_content(file_path: str):
        """
        Validates that the JSON file contains the required fields: 'username' and 'key'.
        """
        try:
            with open(file_path, "r") as file:
                credentials = json.load(file)

            # Check required keys
            if "username" not in credentials or "key" not in credentials:
                raise ValueError(
                    f"Kaggle credentials file at {file_path} is missing required fields: 'username' and 'key'."
                )
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {file_path}.")