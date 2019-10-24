import pandas as pd
import os
import sentimenlexicon
import nltk
from collections import Counter
import random
import utils

def attributeClassifier(tweet):

    tweet = utils.cleanAllTweet(tweet)

    try:
        listToken = nltk.word_tokenize(tweet)
        counterToken = Counter(listToken)

        counterKesejahteraan = counterToken["kesejahteraan"]+counterToken["miskin"]+counterToken["kemiskinan"]+counterToken["kaya"]+counterToken["kekayaan"]+counterToken["harta"]+counterToken["aset"]+counterToken["biaya hidup"]+counterToken["biaya"]+counterToken["daya beli"]+counterToken["sejahtera"]
        counterEkonomi = counterToken["ekonomi"]+counterToken["harga"]+counterToken["inflasi"]+counterToken["pajak"]+counterToken["pertumbuhan"]+counterToken["terjangkau"]+counterToken["murah"]+counterToken["mahal"]
        counterLapanganKerja = counterToken["lapangan kerja"]+counterToken["pekerjaan"]+counterToken["pengangguran"]+counterToken["nganggur"]+counterToken["phk"]+counterToken["gaji"]+counterToken["penghasilan"]+counterToken["tunjangan"]+counterToken["kerja"]
        counterAll = [counterEkonomi, counterKesejahteraan, counterLapanganKerja]
        maxCount = max(counterAll)
        indexPosition = counterAll.index(maxCount)

        attEkonomi = "ekonomi"
        attKesejahteraan = "kesejahteraan"
        attLapanganKerja = "lapangan kerja"
        listAttribute = [attEkonomi, attKesejahteraan, attLapanganKerja]
        listAttributeEkoLK = [attEkonomi, attLapanganKerja]
        listAttributeKsjLK = [attEkonomi, attLapanganKerja]

        if(counterEkonomi == counterKesejahteraan):
            return listAttribute[random.randint(0,1)]
        elif(counterEkonomi == counterLapanganKerja):
            return listAttributeEkoLK[random.randint(0,1)]
        elif(counterKesejahteraan == counterLapanganKerja):
            return listAttributeKsjLK[random.randint(0, 1)]
        else:
            return listAttribute[indexPosition]
    except Exception as e:
        print("Tweet error = "+tweet)
        print("Error = "+str(e))

if __name__ == '__main__':
    print("Ontology")

    ## jadikan satu file chunks

    # dfs = []
    # for filename in os.listdir("data"):
    #     dfs.append(pd.read_csv("data\\" + filename, sep="|"))
    #
    # # Concatenate all data into one DataFrame
    # big_frame = pd.concat(dfs, ignore_index=True)
    # big_frame.to_csv("data\\allchunk.csv", header=True, index=False, sep="|")

    # df = pd.read_csv("data/allchunk.csv", sep="|")
    # dfEkonomi = df[df['tweet'].str.contains("ekonomi|harga|pertumbuhan|lapangan kerja|pekerjaan|penghasilan|gaji|pajak|pengangguran|nganggur|kemiskinan|kesejahteraan")==True]
    # # dfInsfrastruktur = df[df['tweet'].str.contains("ekonomi|pembangunan|harga|pertumbuhan|lapangan kerja|pengangguran|nganggur|kemiskinan|kesejahteraan")==True]
    # # print(dfEkonomi.shape)
    # for index, row in dfEkonomi.iterrows():
    #     attribute = attributeClassifier(str(row['tweet_asli']))
    #     stringToWrite = attribute[0]+"|"+attribute[1]+"|"+str(sentimen.get_sentimen(str(row['tweet_asli'])))+"|"+row['tweet_asli']+"|"+row['tweet']+"\n"
    #     print("Index = "+str(index)+" Adding "+attribute[0]+"|"+attribute[1]+"|"+row['tweet'])
    #     # print(str(row['tweet_asli'])+" - "+str(row['tweet']))
    #     with open("ekonomi_score.csv", "a+", encoding="utf-8") as text_file:
    #         text_file.write(stringToWrite)
    #
    #     # if index == 300:
    #     #     break




