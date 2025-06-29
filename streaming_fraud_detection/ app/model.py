import pickle

# Load pre-trained fraud detection model (RandomForest)
with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_transaction(features):
    # features is a list or numpy array of model inputs
    prediction = model.predict([features])[0]
    prob = model.predict_proba([features])[0][1]
    return prediction, prob

