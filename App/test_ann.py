from tensorflow.keras.models import load_model

model = load_model("Models/ann_recommender.h5")

print(model.output_shape)
print(model.input_shape)