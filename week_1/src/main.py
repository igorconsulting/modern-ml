from config import Config, KaggleValidator
from extract import DataExtractor

if __name__ == "__main__":
    # Load configurations
    config = Config()
    
    print(f"Environment: {config.env}")
    print(f"Kaggle JSON Path: {config.kaggle_json_path}")
    print(f"Datasets Directory: {config.datasets_dir}")
    print(f"Competition Name: {config.competition_name}")

    try:
        # Validate credentials
        KaggleValidator.validate_file_exists(config.kaggle_json_path)
        KaggleValidator.validate_json_content(config.kaggle_json_path)
        print("Kaggle configuration is valid!")

        # Extract data
        extractor = DataExtractor(config.competition_name, config.datasets_dir)
        extractor.run()

    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"Error: {e}")

