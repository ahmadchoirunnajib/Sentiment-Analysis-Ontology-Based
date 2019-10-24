import pandas as pd


def mergeNewClassifierWithSentimenLexiconAndSVM():
    df = pd.read_csv("data\\backup\\tweets333-concenate.csv", index_col="id", sep="|")
    dfSentimen = pd.read_csv("data\\backup\\tweets333-lexicon-svm-quartil-rB-0.00468-rT0.019266.csv", index_col="id", sep="|")
    dfSentimen['attribute'] = df['attribute']
    dfSentimen.to_csv("data\\backup\\tweets333-concenate.csv", sep="|", index_label="id")

def countLexiconSentimenMapping():
    print("Mapping Lexicon : ")
    df = pd.read_csv("data\\backup\\tweets333-concenate.csv", index_col="id", sep="|")
    dfEkonomiPositif = df[(df['sentimen_lexicon'] == "positif") & (df['attribute'] == "ekonomi")]
    dfEkonomiNetral = df[(df['sentimen_lexicon'] == "netral") & (df['attribute'] == "ekonomi")]
    dfEkonomiNegatif = df[(df['sentimen_lexicon'] == "negatif") & (df['attribute'] == "ekonomi")]
    print("Ekonomi - negatif = "+str(dfEkonomiNegatif['sentimen_lexicon'].count()))
    print("Ekonomi - Netral = "+str(dfEkonomiNetral['sentimen_lexicon'].count()))
    print("Ekonomi - Positif = "+str(dfEkonomiPositif['sentimen_lexicon'].count()))


    df = pd.read_csv("data\\backup\\tweets333-concenate.csv", index_col="id", sep="|")
    dfLKPositif = df[(df['sentimen_lexicon'] == "positif") & (df['attribute'] == "lapangan kerja")]
    dfLKNetral = df[(df['sentimen_lexicon'] == "netral") & (df['attribute'] == "lapangan kerja")]
    dfLKNegatif = df[(df['sentimen_lexicon'] == "negatif") & (df['attribute'] == "lapangan kerja")]
    print("LK - negatif = "+str(dfLKNegatif['sentimen_lexicon'].count()))
    print("LK - Netral = "+str(dfLKNetral['sentimen_lexicon'].count()))
    print("LK - Positif = "+str(dfLKPositif['sentimen_lexicon'].count()))


    df = pd.read_csv("data\\backup\\tweets333-concenate.csv", index_col="id", sep="|")
    dfKsjPositif = df[(df['sentimen_lexicon'] == "positif") & (df['attribute'] == "kesejahteraan")]
    dfKsjNetral = df[(df['sentimen_lexicon'] == "netral") & (df['attribute'] == "kesejahteraan")]
    dfKsjNegatif = df[(df['sentimen_lexicon'] == "negatif") & (df['attribute'] == "kesejahteraan")]
    print("Ksj - negatif = "+str(dfKsjNegatif['sentimen_lexicon'].count()))
    print("Ksj - Netral = "+str(dfKsjNetral['sentimen_lexicon'].count()))
    print("Ksj - Positif = "+str(dfKsjPositif['sentimen_lexicon'].count()))

def countSVMSentimenMapping():
    print("Mapping SVM : ")
    df = pd.read_csv("data\\backup\\tweets333-concenate.csv", index_col="id", sep="|")
    dfEkonomiPositif = df[(df['sentimen_class_svm'] == "positif") & (df['attribute'] == "ekonomi")]
    dfEkonomiNetral = df[(df['sentimen_class_svm'] == "netral") & (df['attribute'] == "ekonomi")]
    dfEkonomiNegatif = df[(df['sentimen_class_svm'] == "negatif") & (df['attribute'] == "ekonomi")]
    print("Ekonomi - negatif = "+str(dfEkonomiNegatif['sentimen_class_svm'].count()))
    print("Ekonomi - Netral = "+str(dfEkonomiNetral['sentimen_class_svm'].count()))
    print("Ekonomi - Positif = "+str(dfEkonomiPositif['sentimen_class_svm'].count()))


    df = pd.read_csv("data\\backup\\tweets333-concenate.csv", index_col="id", sep="|")
    dfLKPositif = df[(df['sentimen_class_svm'] == "positif") & (df['attribute'] == "lapangan kerja")]
    dfLKNetral = df[(df['sentimen_class_svm'] == "netral") & (df['attribute'] == "lapangan kerja")]
    dfLKNegatif = df[(df['sentimen_class_svm'] == "negatif") & (df['attribute'] == "lapangan kerja")]
    print("LK - negatif = "+str(dfLKNegatif['sentimen_class_svm'].count()))
    print("LK - Netral = "+str(dfLKNetral['sentimen_class_svm'].count()))
    print("LK - Positif = "+str(dfLKPositif['sentimen_class_svm'].count()))


    df = pd.read_csv("data\\backup\\tweets333-concenate.csv", index_col="id", sep="|")
    dfKsjPositif = df[(df['sentimen_class_svm'] == "positif") & (df['attribute'] == "kesejahteraan")]
    dfKsjNetral = df[(df['sentimen_class_svm'] == "netral") & (df['attribute'] == "kesejahteraan")]
    dfKsjNegatif = df[(df['sentimen_class_svm'] == "negatif") & (df['attribute'] == "kesejahteraan")]
    print("Ksj - negatif = "+str(dfKsjNegatif['sentimen_class_svm'].count()))
    print("Ksj - Netral = "+str(dfKsjNetral['sentimen_class_svm'].count()))
    print("Ksj - Positif = "+str(dfKsjPositif['sentimen_class_svm'].count()))


if __name__ == '__main__':
    # mergeNewClassifierWithSentimenLexiconAndSVM()
    countLexiconSentimenMapping()
    countSVMSentimenMapping()