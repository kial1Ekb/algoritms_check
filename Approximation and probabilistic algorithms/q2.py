"""
Разработайте программу, которая использует вероятностный алгоритм для классификации изображений. Программа должна
принимать изображение, применять вероятностный метод и определять к какому классу объектов изображения относится.
"""

import numpy as np
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions


def load_and_preprocess_image(img_path):
    """Загрузка и предварительная обработка изображения."""
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded_dims)


def classify_image(model, img_array):
    """Классификация изображения с использованием модели."""
    preds = model.predict(img_array)
    return decode_predictions(preds, top=3)[0]


def main(img_path):
    """Основная функция для загрузки изображения, классификации и вывода результатов."""
    model = MobileNet(weights='imagenet')
    img_array = load_and_preprocess_image(img_path)
    predictions = classify_image(model, img_array)

    print("Predictions:")
    for pred in predictions:
        # pred - это кортеж (код класса, название класса, вероятность)
        print(f"{pred[1]}: {pred[2] * 100:.2f}%")


if __name__ == "__main__":
    img_path = input("Введите путь к изображению: ")
    main(img_path)
