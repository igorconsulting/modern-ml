import subprocess
import os
import zipfile

class DataExtractor:
    """
    Handles data downloanding from Kaggle competitions using the Kaggle CLI.
    """

    def __init__(self, competition_name: str, output_dir: str):
        """
        Initialize downloader with competition name and output directory.
        """
        self.competition_name = competition_name
        self.output_dir = output_dir
        self.zip_file_path = os.path.join(self.output_dir, f"{self.competition_name}.zip")

    def download(self):
        """
        Download competition data using Kaggle CLI.
        """
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        if os.path.isfile(self.zip_file_path):
            print(f"Data already downloaded at {self.zip_file_path}")
            # Unzip competition data
            return

        # Download competition data
        subprocess.run(
            [
                "kaggle",
                "competitions",
                "download",
                "-c",
                self.competition_name,
                "-p",
                self.output_dir,
            ]
        )

    def unzip_data(self):
        """
        Unzip competition data.
        """
        # Get all zip files in the output directory
        zip_files = [f for f in os.listdir(self.output_dir) if f.endswith(".zip")]

        # Unzip each file
        for zip_file in zip_files:
            with zipfile.ZipFile(os.path.join(self.output_dir, zip_file), "r") as zip_ref:
                zip_ref.extractall(self.output_dir)
                os.remove(os.path.join(self.output_dir, zip_file))

    def run(self):
        """
        Run the data extraction process.
        """
        try:
            self.download()
            self.unzip_data()
        except Exception as e:
            print(f"Error: {e}")
