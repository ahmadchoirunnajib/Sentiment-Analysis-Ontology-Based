import pandas as pd
from sklearn import metrics

def calculatePerformanceLexiconAndSVM():
    df = pd.read_csv("data\\backup\\tweets333-lexicon-svm-quartil-rB-0.00468-rT0.019266.csv",index_col="id", sep="|")
    trueValues = list(df['sentimen'])
    predLexValues = list(df['sentimen_lexicon'])
    predSVMValues = list(df['sentimen_class_svm'])

    print("Performance measure Lexicon Based : \n")
    print(metrics.confusion_matrix(trueValues, predLexValues))
    print(metrics.classification_report(trueValues, predLexValues, digits=3))

    print("Performance measure SVM: \n")
    print(metrics.confusion_matrix(trueValues, predSVMValues))
    print(metrics.classification_report(trueValues, predSVMValues, digits=3))

if __name__ == '__main__':
    calculatePerformanceLexiconAndSVM()