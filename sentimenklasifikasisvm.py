import pandas as pd
import numpy as np
from scipy.sparse import hstack
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
import joblib

def svmBasedClassification():

    # tweets = pd.read_csv("data\\matilampu-label.csv")
    # tweets = pd.read_csv("data\\tweetclean600-only.csv", sep="|")
    tweets = pd.read_csv("data\\backup\\tweets333-only.csv", sep="|")
    # tweets = pd.read_csv("data\\backup\\tweets333-only-withattribute.csv", sep="|")
    tweets = tweets.drop_duplicates()
    tweets = tweets.dropna()
    list(tweets.columns.values)

    sentiment_counts = tweets.sentimen.value_counts()
    number_of_tweets = tweets.id.count()
    print(sentiment_counts)

    from nltk.probability import FreqDist

    fdist = FreqDist(tweets[(tweets.sentimen == 'negatif')])
    print(fdist.most_common(50))


    # count_vectorizer = CountVectorizer(ngram_range=(1,2))
    count_vectorizer = TfidfVectorizer()

    vectorized_data = count_vectorizer.fit_transform(tweets.clean_tweet)
    indexed_data = hstack((np.array(range(0,vectorized_data.shape[0]))[:,None], vectorized_data))



    def sentiment2target(sentiment):
        return {
            'negatif': 0,
            'netral': 1,
            'positif' : 2
        }[sentiment]

    targets = tweets.sentimen.apply(sentiment2target)


    from sklearn.model_selection import train_test_split
    data_train, data_test, targets_train, targets_test = train_test_split(indexed_data, targets, test_size=0.4, random_state=0)
    data_train_index = data_train[:,0]
    data_train = data_train[:,1:]
    # print(data_train[0:2])
    data_test_index = data_test[:,0]
    data_test = data_test[:,1:]

    from sklearn import svm
    from sklearn.multiclass import OneVsRestClassifier
    clf = OneVsRestClassifier(svm.SVC(gamma=0.01, C=100., probability=True, class_weight='balanced', kernel='rbf'))
    # clf = OneVsRestClassifier(svm.SVC(gamma=0.01, C=100., probability=True, class_weight='balanced', kernel='linear'))
    clf_output = clf.fit(data_train, targets_train)
    filename = 'model.sav'
    pickle.dump(clf_output, open(filename, 'wb'))

    print(clf.score(data_test, targets_test))

    y_pred = clf.predict(data_test)
    print("Predict test data :\n"+str(y_pred))
    print("Accuracy: ",accuracy_score(targets_test, y_pred))
    print("Recall: ",recall_score(targets_test, y_pred, average='weighted'))
    print("Presisi: ",precision_score(targets_test, y_pred, average='weighted'))
    print("F1 score: ",f1_score(targets_test, y_pred, average='weighted'))


    sentences = count_vectorizer.transform([
        "Negara kita ngutang buat bngun infrastruktur yang udah dipake masyarakat, terus masyarakatnya ngeluh karena negara ngutang, setiap negara itu pasti ngutang,  utang bisa dibayar kalo negara dapet penghasilan. Penghasilan negara itu ya dari pajak",
        "Negara kita ngutang sehingga harga mahal dan masyarakat tercekik dan ngeluh",
        "Prabowo-Sandi Sepakat Tak Ambil Gaji karena Negara Sedang Susah",
        "Calon presiden Jokowi menjelaskan program Kartu Pra Kerja akan memberikan insentif dalam kurun waktu tertentu, bukan berarti memberikan gaji secara cuma-cuma bagi masyarakat yang belum berpenghasilan."
    ])
    print(clf.predict_proba(sentences))

def get_classPredictionSVM(tweetList):
    tweets = pd.read_csv("data\\backup\\tweets333-only.csv", sep="|")
    # tweets = pd.read_csv("data\\backup\\tweets333-only-withattribute.csv", sep="|")
    tweets = tweets.drop_duplicates()
    tweets = tweets.dropna()

    count_vectorizer = TfidfVectorizer()
    count_vectorizer.fit_transform(tweets.clean_tweet)

    filename = "model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    sentence = count_vectorizer.transform(tweetList)
    classifier = loaded_model.predict(sentence)
    return classifier

def sentimenSVMClassifier(classSVM):
    if classSVM == 0:
        return 'negatif'
    elif classSVM == 1:
        return 'netral'
    else:
        return 'positif'



if __name__ == '__main__':
    tweet = "Negara kita ngutang buat bngun infrastruktur yang udah dipake masyarakat, terus masyarakatnya ngeluh karena negara ngutang, setiap negara itu pasti ngutang,  utang bisa dibayar kalo negara dapet penghasilan. Penghasilan negara itu ya dari pajak"
    get_classPredictionSVM(tweet)


    # svmBasedClassification()