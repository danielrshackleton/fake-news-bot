import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def analyze(article_text):
    # df = pd.read_csv('C:\\Users\\danie\\Downloads\\news.csv')
    df = pd.read_csv('data_set\\train.csv')

    # Change the labels
    df.loc[(df['label'] == 1), ['label']] = 'FAKE'
    df.loc[(df['label'] == 0), ['label']] = 'REAL'

    labels = df.label
    x_train, x_test, y_train, y_test = train_test_split(df['text'], labels, test_size=0.25, random_state=7)

    # Initialize a TfidfVectorizer, vectorize the text
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.75)

    # Fit and transform train set, transform test set
    tfidf_train = tfidf_vectorizer.fit_transform(x_train.values.astype('U'))
    tfidf_test = tfidf_vectorizer.transform(x_test.values.astype('U'))

    # Initialize a PassiveAggressiveClassifier and fit training sets
    pac = PassiveAggressiveClassifier(max_iter=50)
    pac.fit(tfidf_train, y_train)

    # Predict on the test set and calculate accuracy
    y_pred = pac.predict(tfidf_test)
    score = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {round(score * 100, 2)}%')

    vec_new = tfidf_vectorizer.transform([article_text])
    y_pred1 = pac.predict(vec_new)

    str = f'There is a good chance that this article is {y_pred1[0].lower()}'
    return str


