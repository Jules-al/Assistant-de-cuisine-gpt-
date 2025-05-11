# Assistant Cuisine Française avec GPT-3.5

Ce projet utilise le fine-tuning de GPT-3.5 pour créer un assistant spécialisé en cuisine française. L'application est construite avec Streamlit et permet aux utilisateurs de poser des questions sur la cuisine française.

## Fonctionnalités

- Fine-tuning de GPT-3.5 sur un jeu de données de recettes françaises
- Interface utilisateur Streamlit intuitive
- Questions prédéfinies sur la cuisine française
- Possibilité de poser des questions personnalisées
- Réponses détaillées avec instructions de préparation

## Prérequis

- Python 3.8 ou supérieur
- Compte OpenAI avec accès à l'API
- Clé API OpenAI

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-username/assistant-cuisine-francaise.git
cd assistant-cuisine-francaise
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurez votre clé API :
   - Créez un fichier `.env` à la racine du projet
   - Ajoutez votre clé API : `OPENAI_API_KEY=votre_clé_api_ici`

## Utilisation

1. Fine-tuning du modèle :
```bash
python src/fine_tune.py
```

2. Lancer l'application Streamlit :
```bash
streamlit run src/app.py
```

3. Dans l'application :
   - Entrez l'ID du modèle fine-tuné
   - Sélectionnez une question prédéfinie ou posez votre propre question
   - Cliquez sur "Obtenir la réponse"

## Structure du projet

```
.
├── data/
│   └── training_data.jsonl
├── src/
│   ├── app.py
│   ├── fine_tune.py
│   └── use_model.py
├── .env
├── .gitignore
├── config.py
├── LICENSE
├── README.md
└── requirements.txt
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 