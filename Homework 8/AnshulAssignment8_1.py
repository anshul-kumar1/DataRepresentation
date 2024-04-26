import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from nltk.stem import WordNetLemmatizer
import nltk
import math
import string
import random
nltk.download('punkt')
nltk.download('wordnet')
random.seed(350)

def pre_process(file):
    stop_words = ["the", "and", "of", "in", "a", "to", "is", "it", "you", "for", "on", "with", "this", "that", "are", "as", "be"]
    lemmatizer = WordNetLemmatizer()
    data = pd.read_csv(file)
    data.dropna(subset=['CATEGORY', 'CONTENT', 'SUMMARY'], inplace=True)

    def apply_func(f):
        token = []
        clean = f.translate(str.maketrans('', '', string.punctuation))
        final = ''.join(letter for letter in clean if letter.isalnum() or letter.isspace())
        t = final.split()
        for char in t:
            b = char.lower()
            if b not in stop_words:
                token.append(b)

        token = [lemmatizer.lemmatize(word) for word in token]
        return token

    data['After_Filter_Content'] = data['CONTENT'].apply(apply_func)

    return data

df = pre_process('dataset.csv').sample(n=2000)

def tf(element, doc):
    count = doc.count(element)
    if count == 0:
        return 0
    return count / len(doc)


def idf(t, check):
    count = 0
    for i in check:
        if t in i:
            count += 1
    if count == 0:
        return 0
    return math.log(len(check) / count)


def tf_idf(content):
    all = set()
    for elem in content:
        for word in elem:
            all.add(word)
    idf_dict = dict()
    for word in all:
        idf_dict[word] = idf(word, content)

    numeric = []

    tf_idf_dict = dict()
    for m in content:
        for n in m:
            score=idf_dict[n]*tf(n,m)
            tf_idf_dict[n] = score
        numeric.append(score)
    return numeric

vectors = tf_idf(df['After_Filter_Content'].tolist())
vectors = pd.DataFrame(vectors).fillna(0)

tf_vec = TfidfVectorizer(max_features=5000)

X = tf_vec.fit_transform(df['After_Filter_Content'].astype(str))
y = df['CATEGORY']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

reg = LogisticRegression()
reg.fit(X_train, y_train)
log_reg_predicted = reg.predict(X_test)
print("Accuracy Logistic Regression:")
print(accuracy_score(y_test, log_reg_predicted))
print("Summary - Logistic Regression:")
print(classification_report(y_test, log_reg_predicted))

svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
svm_predicted = svm.predict(X_test)
print("Accuracy SVM:")
print(accuracy_score(y_test, svm_predicted))
print("Summary SVM:")
print(classification_report(y_test, svm_predicted))