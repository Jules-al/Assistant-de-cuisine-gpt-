import os
import json
import sys
from openai import OpenAI
from tqdm import tqdm

# Ajouter le répertoire parent au chemin Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

# Initialiser le client OpenAI
client = OpenAI(api_key=config.OPENAI_API_KEY)

def prepare_training_data(file_path):
    """Vérifie et prépare les données d'entraînement."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Vérifier que le contenu est bien en UTF-8
            content.encode('utf-8')
            lines = content.splitlines()
    except UnicodeDecodeError:
        raise ValueError("Le fichier n'est pas encodé en UTF-8")
    
    # Vérifier le format des données
    for line in lines:
        try:
            data = json.loads(line)
            if not all(key in data for key in ['messages']):
                raise ValueError("Format de données invalide")
        except json.JSONDecodeError:
            raise ValueError("Format JSON invalide")
    
    return lines

def upload_training_file(file_path):
    """Télécharge le fichier d'entraînement vers OpenAI."""
    try:
        # Lire le contenu du fichier
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Créer le fichier directement avec l'API OpenAI
        response = client.files.create(
            file=content.encode('utf-8'),
            purpose='fine-tune'
        )
        return response.id
    except Exception as e:
        print(f"Erreur lors de l'upload du fichier: {str(e)}")
        raise

def create_fine_tuning_job(training_file_id):
    """Crée un job de fine-tuning."""
    try:
        response = client.fine_tuning.jobs.create(
            training_file=training_file_id,
            model=config.FINE_TUNING_PARAMS['model'],
            hyperparameters={
                "n_epochs": config.FINE_TUNING_PARAMS['n_epochs'],
                "batch_size": config.FINE_TUNING_PARAMS['batch_size'],
                "learning_rate_multiplier": config.FINE_TUNING_PARAMS['learning_rate_multiplier']
            }
        )
        return response.id
    except Exception as e:
        print(f"Erreur lors de la création du job: {str(e)}")
        raise

def main():
    try:
        # Vérifier et préparer les données
        print("Préparation des données d'entraînement...")
        prepare_training_data(config.TRAINING_FILE)
        
        # Télécharger le fichier d'entraînement
        print("Téléchargement du fichier d'entraînement...")
        training_file_id = upload_training_file(config.TRAINING_FILE)
        
        # Créer le job de fine-tuning
        print("Création du job de fine-tuning...")
        job_id = create_fine_tuning_job(training_file_id)
        
        print(f"Job de fine-tuning créé avec succès! ID: {job_id}")
        print("Vous pouvez suivre la progression sur le dashboard OpenAI.")
        
    except Exception as e:
        print(f"Une erreur est survenue: {str(e)}")

if __name__ == "__main__":
    main() 