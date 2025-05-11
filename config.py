import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration de l'API OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Paramètres de fine-tuning
FINE_TUNING_PARAMS = {
    "model": "gpt-3.5-turbo",  # Modèle disponible pour le fine-tuning
    "n_epochs": 1,     # Réduit à 1 époque pour diminuer les coûts
    "batch_size": 1,   # Taille du batch
    "learning_rate_multiplier": 0.1  # Multiplicateur du taux d'apprentissage
}

# Chemins des fichiers
DATA_DIR = "data"
TRAINING_FILE = os.path.join(DATA_DIR, "training_data.jsonl")
VALIDATION_FILE = os.path.join(DATA_DIR, "validation_data.jsonl") 