import os
import sys
from openai import OpenAI

# Ajouter le répertoire parent au chemin Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def get_model_response(prompt, model_id):
    """Obtient une réponse du modèle fine-tuné."""
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "Vous êtes un assistant utile."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur lors de l'appel au modèle: {str(e)}"

def main():
    # Demander l'ID du modèle fine-tuné
    model_id = input("Entrez l'ID du modèle fine-tuné: ")
    
    while True:
        # Demander le prompt à l'utilisateur
        prompt = input("\nEntrez votre prompt (ou 'quit' pour quitter): ")
        
        if prompt.lower() == 'quit':
            break
        
        # Obtenir et afficher la réponse
        response = get_model_response(prompt, model_id)
        print("\nRéponse du modèle:")
        print(response)

if __name__ == "__main__":
    main() 