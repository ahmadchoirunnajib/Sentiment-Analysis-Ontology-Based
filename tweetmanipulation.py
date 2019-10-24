import pandas as pd
import sentimenlexicon, ontology
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
from collections import Counter
import random
from sklearn import metrics
import utils, sentimenlexicon, sentimenklasifikasisvm

def selectLabelledTweets():
    pd.options.mode.chained_assignment = None
    # read excel
    df = pd.read_excel("data\\Sampel600.xlsx")
    # select only the used table
    dfClean = df[['class', 'attribute', 'sentimen', 'tweet_asli', 'tweet']]

    # remove unlabelled tweet
    dfClean['clean_tweet'] = dfClean['tweet_asli'].apply(lambda row: utils.cleanAllTweet(row))

    dfClean = dfClean.dropna()
    dfClean = dfClean.drop_duplicates()

    # dfClean['sentimen_new'] = dfClean.apply(lambda row: sentimen.klasfikasibaru(row), axis=1)
    dfClean['attribute_new'] = dfClean['tweet_asli'].apply(lambda row: ontology.attributeClassifier(row))
    # dfClean['sentimen_new'] = df.apply(lambda row: sentimen.klasfikasibaru(row), axis=1)
    dfClean = dfClean.dropna()
    dfClean = dfClean.drop_duplicates()
    # save into csv
    dfClean.to_csv("data\\tweetclean600-lambda.csv", index_label="id", sep="|")
    print(dfClean.shape)

    dfOnlyTweeAndClass = dfClean[['sentimen', 'clean_tweet']]
    # dfOnlyTweeAndClass = dfClean[['sentimen_new', 'clean_tweet']]
    dfOnlyTweeAndClass.to_csv("data\\tweetclean600-only.csv", index_label="id", sep="|")

def infoDataset():
    # df = pd.read_csv("data\\tweetclean600-lambda.csv", index_col="id", sep="|")
    # df = pd.read_csv("data\\backup\\tweets333.csv", index_col="id", sep="|")

    #show best model based 351
    # df = pd.read_csv("data\\backup\\tweetclean600-lambda-e916-lk548-ksj351.csv", index_col="id", sep="|")
    # sentiment_counts = df.attribute_new.value_counts()
    # print("Jumlah distinct : \n"+str(sentiment_counts))

    #get describe
    df = pd.read_csv("data\\backup\\tweets333-only-withlbscore.csv", index_col="id", sep="|")
    print("Describe :")
    print(str(df['sentimen_score_lb'].describe()))

    # df = pd.read_csv("data\\backup\\tweets333-only-withlbscore-new.csv", index_col="id", sep="|")
    # print("Describe :")
    # print(str(df.sentimen_new.value_counts()))

def mappingDataset333():
    df = pd.read_csv("data\\backup\\tweets333-only-withlbscore.csv", index_col="id", sep="|")


def assignNewClassifier():
    df = pd.read_csv("data\\backup\\tweets333-only-withlbscore.csv", index_col="id", sep="|")

    mean = df['sentimen_score_lb'].mean()
    std = df['sentimen_score_lb'].std()
    max = df['sentimen_score_lb'].max()
    quartilBawah = -0.004680
    quartilAtas = 0.019266
    stdper3 = std/3
    # rangeBottom = 0 - stdper3
    # rangeTop = stdper3
    rangeBottom = quartilBawah
    rangeTop = quartilAtas
    key = "quartil"

    print("Nilai "+key+" Range Bottom = "+str(rangeBottom)+" -- Range Top"+str(rangeTop))

    df['sentimen_lexicon'] = df['sentimen_score_lb'].apply(lambda row: sentimenlexicon.sentimenLexiconClassifier(row, rangeBottom, rangeTop))
    df['sentimen_class_svm_raw'] = sentimenklasifikasisvm.get_classPredictionSVM(list(df['clean_tweet']))
    df['sentimen_class_svm'] = df['sentimen_class_svm_raw'].apply(lambda row: sentimenklasifikasisvm.sentimenSVMClassifier(row))
    df.to_csv("data\\backup\\tweets333-lexicon-svm-"+key+"-rB"+str(rangeBottom)+"-rT"+str(rangeTop)+".csv", index_label="id", sep="|")

def assignNewClassifierSVM():
    df = pd.read_csv("data\\backup\\tweets333-only.csv", index_col="id", sep="|")
    df['sentimen_new'] = df['sentimen_score_lb'].apply(lambda row: sentimenlexicon.sentimenLexiconClassifier(row))
    df.to_csv("data\\backup\\tweets333-only-withlbscore-new.csv", index_label="id", sep="|")


def separateDataTrainTest():
    df = pd.read_csv("data\\tweetclean.csv", sep="|", index_col="id")
    # select sentimen netral
    dfNetral = df[df['sentimen'] == 'netral']
    print("Jumlah sentimen netral = " + str(dfNetral.shape[0]))
    # select sentimen positif
    dfPositif = df[df['sentimen'] == 'positif']
    print("Jumlah sentimen positif = " + str(dfPositif.shape[0]))
    # select sentimen negatif
    dfNegatif = df[df['sentimen'] == 'negatif']
    print("Jumlah sentimen negatif = " + str(dfNegatif.shape[0]))

    # pilih 0.7% dan 0.3% dari dataframe netral
    dfTrainNetral = dfNetral.iloc[0:int(0.7 * dfNetral.shape[0])]
    dfTestNetral = dfNetral.iloc[int(0.7 * dfNetral.shape[0]):dfNetral.shape[0]]
    print(str(dfTrainNetral.shape[0]) + "," + str(dfTestNetral.shape[0]))
    # pilih 0.7% dan 0.3% dari dataframe positif
    dfTrainPositif = dfPositif.iloc[0:int(0.7 * dfPositif.shape[0])]
    dfTestPositif = dfPositif.iloc[int(0.7 * dfPositif.shape[0]):dfPositif.shape[0]]
    print(str(dfTrainPositif.shape[0]) + "," + str(dfTestPositif.shape[0]))
    # pilih 0.7% dan 0.3% dari dataframe netral
    dfTrainNegatif = dfNegatif.iloc[0:int(0.7 * dfNegatif.shape[0])]
    dfTestNegatif = dfNegatif.iloc[int(0.7 * dfNegatif.shape[0]):dfNegatif.shape[0]]
    print(str(dfTrainNegatif.shape[0]) + "," + str(dfTestNegatif.shape[0]))

    # Gabung dataframe Train dan Test
    dfTrain = pd.concat([dfTrainNetral, dfTrainPositif, dfTrainNegatif])
    print("Data train = " + str(dfTrain.shape))
    dfTest = pd.concat([dfTestNetral, dfTestPositif, dfTestNegatif])
    print("Data tes = " + str(dfTest.shape))

    # save datarfame to csv
    dfTrain.to_csv("data\\tweetTrain.csv", sep="|", index_label=None)
    dfTest.to_csv("data\\tweetTest.csv", sep="|", index_label=None)

def generateWordCloud():
    print("Generating stopwords..")
    df = pd.read_csv("data\\tweetclean600-only.csv", index_col="id", sep="|")
    text = " ".join(tweet for tweet in df.clean_tweet)
    stopwords = ["uno","raja salman","coba","beda","program","digaji","sandiaga","mobile","legend","amin","negeri","game","esport","mobile legend","langsung","nggak", "bikin","pernyataan","paham","banget","hati","tusuk","pemerintah", "emang","kali","dukung","bangsa","gajinya","dunia","mati", "semoga","wowo","dipake","april","capres","salah arah", "masyarakat", "pake", "jokowi","presiden","milih","butuh","salah", "ambil","fokus","pilih","negara","beliau", "menang","periode", "negara","ambil","prabowo", "salah arah","udah", "sandi", "indonesia","orang","gak","prabowosandi","jokowimaruf","debat","rakyat","bilang","anak","janji","menghargai","tau","salah arah","mengambil","allah","pemimpin","terpilih"]
    wordcloud = WordCloud(stopwords=stopwords,background_color="white").generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def select350TweetsPerAttribute():
    df = pd.read_csv("data\\backup\\tweetclean600-lambda-e916-lk548-ksj351.csv", index_col="id", sep="|")
    dfEkonomi = df[df['attribute_new'] == "ekonomi"]
    dfEkonomi = dfEkonomi.iloc[0:350]
    dfLapanganKerja = df[df['attribute_new'] == "lapangan kerja"]
    dfLapanganKerja = dfLapanganKerja.iloc[0:350]
    dfKesejahteraan = df[df['attribute_new'] == "kesejahteraan"]
    dfKesejahteraan = dfKesejahteraan.iloc[0:350]

    allFrames = [dfEkonomi, dfLapanganKerja, dfKesejahteraan]
    result = pd.concat(allFrames)
    result.to_csv("data\\backup\\tweets333.csv", sep="|", index_label="id")

    dfOnlyTweeAndClass = result[['sentimen', 'clean_tweet']]
    dfOnlyTweeAndClass.to_csv("data\\backup\\tweets333-only.csv", index_label="id", sep="|")

    dfOnlyTweeAndClassAndAttribute = result[['sentimen', 'attribute_new', 'clean_tweet']]
    dfOnlyTweeAndClassAndAttribute.to_csv("data\\backup\\tweets333-only-withattribute.csv", index_label="id", sep="|")

def calculateLexiconBasedScore():
    df = pd.read_csv("data\\backup\\tweets333-only-withattribute.csv", index_col="id", sep="|")
    df['sentimen_score_lb'] = df['clean_tweet'].apply(lambda row: sentimenlexicon.get_sentimen(row))
    df.to_csv("data\\backup\\tweets333-only-withattribute-withlbscore.csv", sep="|", index_label="id")



if __name__ == '__main__':
    #pilih tweet yg sudah dilabeli
    # selectLabelledTweets()

    # generate wordcloud
    generateWordCloud()

    #pisahkan dataset untuk training dan testing
    # separateDataTrainTest()

    #get info dataset
    # infoDataset()

    #assignClassifier
    # assignNewClassifier()

    #select350tweets
    # select350TweetsPerAttribute()

    #calculate sentimen score lexicon based
    # calculateLexiconBasedScore()


    #tes
    # tweet = "pengamat ekonomi prestasi angka kemiskinan era jokowi terendah sejarah"
    # tweet = sentimen.cleanAllTweet(tweet)
    # listToken = nltk.word_tokenize(tweet)
    # counterToken = Counter(listToken)
    #
    # counterKesejahteraan = counterToken["kesejahteraan"] + counterToken["miskin"] + counterToken["kemiskinan"] + \
    #                        counterToken["kaya"] + counterToken["kekayaan"] + counterToken["harta"] + counterToken[
    #                            "aset"] + counterToken["biaya hidup"] + counterToken["biaya"] + counterToken["daya beli"]
    # counterEkonomi = counterToken["ekonomi"] + counterToken["harga"] + counterToken["inflasi"] + counterToken["pajak"] + \
    #                  counterToken["pertumbuhan"] + counterToken["terjangkau"] + counterToken["murah"] + counterToken[
    #                      "mahal"]
    # counterLapanganKerja = counterToken["lapangan kerja"] + counterToken["pekerjaan"] + counterToken["pengangguran"] + \
    #                        counterToken["nganggur"] + counterToken["phk"] + counterToken["gaji"] + counterToken[
    #                            "penghasilan"] + counterToken["tunjangan"]
    # counterAll = [counterEkonomi, counterKesejahteraan, counterLapanganKerja]
    # print("List = "+str(counterAll))
    # maxCount = max(counterAll)
    # print("Max = "+str(maxCount))
    # indexPosition = counterAll.index(maxCount)
    # print("Index max = "+str(indexPosition))
    #
    # attEkonomi = "ekonomi"
    # attKesejahteraan = "kesejahteraan"
    # attLapanganKerja = "lapangan kerja"
    # listAttribute = [attEkonomi, attKesejahteraan, attLapanganKerja]
    # listAttributeEkoLK = [attEkonomi, attLapanganKerja]
    # listAttributeKsjLK = [attKesejahteraan, attLapanganKerja]
    #
    # if (counterEkonomi == counterKesejahteraan):
    #     print("Masuk")
    #     print(str(listAttribute[random.randint(0, 1)]))
    # elif (counterEkonomi == counterLapanganKerja):
    #     print(str(listAttributeEkoLK[random.randint(0, 1)]))
    # elif (counterKesejahteraan == counterLapanganKerja):
    #     print(str(listAttributeKsjLK[random.randint(0, 1)]))
    # else:
    #     print(str(listAttribute[indexPosition]))










