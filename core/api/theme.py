from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC
import pickle

router = APIRouter()

# Load the trained model
with open("model/model_full.pkl", "rb") as model_file:
    multi_output_classifier = pickle.load(model_file)

# Load the vectorizer (you can load it from the 'vectorizer.pkl' file)
with open("model/vectorizer_full.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


class TextData(BaseModel):
    text: str


@router.post("/api/theme", tags=["theme"])
def get_theme_probabilities(text_data: TextData):
    # Preprocess the text data
    text = [text_data.text]
    x_text = vectorizer.transform(text)

    # Predict probabilities for each category using the trained model
    val_pred_probs = multi_output_classifier.predict_proba(x_text)

    # Convert the probability matrix to a dictionary with category names and their corresponding probabilities
    categories = ['personal', 'lifestyle', 'medical']
    output_probs = {category: prob[0, 1]
                    for category, prob in zip(categories, val_pred_probs)}

    return output_probs
