import joblib

label_encoder = joblib.load(
    "Models/cnn_label_encoder.pkl"
)

print(label_encoder.classes_)