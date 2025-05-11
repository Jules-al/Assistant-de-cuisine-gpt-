import streamlit as st
import os
import sys
from openai import OpenAI

# Ajouter le répertoire parent au chemin Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

# Initialiser le client OpenAI
client = OpenAI(api_key=config.OPENAI_API_KEY)

# Liste des questions prédéfinies
QUESTIONS = [
    "Comment préparer une ratatouille ?",
    "Quelle est la différence entre une quiche et une tarte ?",
    "Comment faire une crème brûlée ?",
    "Qu'est-ce que le cassoulet ?",
    "Comment faire une tarte Tatin ?",
    "Qu'est-ce que la bouillabaisse ?",
    "Comment faire un coq au vin ?",
    "Qu'est-ce que le gratin dauphinois ?",
    "Comment faire une mousse au chocolat ?",
    "Qu'est-ce que le pot-au-feu ?"
]

def get_model_response(prompt, model_id):
    """Obtient une réponse du modèle fine-tuné."""
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "Vous êtes un assistant spécialisé en cuisine française."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur lors de l'appel au modèle: {str(e)}"

def main():
    st.title("🍳 Assistant Cuisine Française")
    st.write("Posez vos questions sur la cuisine française !")

    # Champ pour l'ID du modèle
    model_id = st.text_input("Entrez l'ID du modèle fine-tuné :")

    # Sélection de la question
    selected_question = st.selectbox(
        "Choisissez une question :",
        QUESTIONS
    )

    # Champ pour une question personnalisée
    custom_question = st.text_input("Ou posez votre propre question :")

    # Bouton pour obtenir la réponse
    if st.button("Obtenir la réponse"):
        if not model_id:
            st.error("Veuillez entrer l'ID du modèle fine-tuné")
            return

        # Utiliser la question personnalisée si elle existe, sinon utiliser la question sélectionnée
        question = custom_question if custom_question else selected_question
        
        with st.spinner("Le modèle réfléchit..."):
            response = get_model_response(question, model_id)
            
            # Afficher la réponse dans un conteneur stylisé
            st.markdown("### Réponse :")
            st.markdown(response)

if __name__ == "__main__":
    main() 