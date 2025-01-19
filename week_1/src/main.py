from config import Config, KaggleValidator

if __name__ == "__main__":
    # Inicializa a configuração
    config = Config()

    print(f"Environment: {config.env}")
    print(f"Kaggle JSON Path: {config.kaggle_json_path}")
    print(f"Datasets Directory: {config.datasets_dir}")
    print(f"Competition Name: {config.competition_name}")

    try:
        # Validações específicas
        KaggleValidator.validate_file_exists(config.kaggle_json_path)
        KaggleValidator.validate_json_content(config.kaggle_json_path)
        print("Kaggle configuration is valid!")
    except (FileNotFoundError, ValueError) as e:
        print(f"Configuration error: {e}")
