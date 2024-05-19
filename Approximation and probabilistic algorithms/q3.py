"""
Создайте программу, которая использует алгоритм машинного обучения (например, метод опорных векторов или случайный лес)
для классификации изображений с целью автоматической идентификации объектов на фотографиях. Программа должна обучаться
на размеченном наборе изображений и предсказывать класс объектов на новых изображениях.
"""

"""
pip install numpy
pip install scikit-learn
pip install keras
pip install tensorflow
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.datasets import cifar10
import numpy as np

def load_data():
    """ Загрузка и предварительная обработка данных CIFAR-10. """
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    # Нормализация данных
    X_train = X_train.reshape(X_train.shape[0], -1) / 255.0
    X_test = X_test.reshape(X_test.shape[0], -1) / 255.0
    y_train = y_train.ravel()
    y_test = y_test.ravel()
    return X_train, X_test, y_train, y_test

def train_classifier(X_train, y_train):
    """ Обучение классификатора случайного леса. """
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    return clf

def evaluate_classifier(clf, X_test, y_test):
    """ Оценка точности классификатора. """
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Точность классификации: {accuracy:.2f}")

def main():
    X_train, X_test, y_train, y_test = load_data()
    clf = train_classifier(X_train, y_train)
    evaluate_classifier(clf, X_test, y_test)

if __name__ == "__main__":
    main()
