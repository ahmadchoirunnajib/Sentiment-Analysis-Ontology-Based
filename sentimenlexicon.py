# @author : Nur Aini Rakhmawati
# sentimen bahasa Indonesia
import pandas as pd
import nltk
from nltk.tag import CRFTagger
import re, math
import numpy
import random
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
import utils

def get_scores(dframe):
    count =0
    totalpositive =0.0
    totalnegative =0.0
    for index,row in dframe.iterrows():
        totalpositive = totalpositive + row['pos']
        totalnegative = totalnegative + row['neg']
        count =count + 1
    if count > 0:
        return((totalpositive-totalnegative)/count)
    else:
        return 0

def klasfikasibaru(tweet):
    try:
        negatif = ['buruk', 'cebong', 'kampret', 'goblok', 'dungu', 'bobrok']
        postitif = ['setuju', 'bagus', 'dukung', '']

        print("Nilainya = "+str(tweet[2]))
        sentimen = ['negatif', 'positif', 'netral']
        if str(tweet[2]) == 'nan':
            return sentimen[random.randint(0,2)]
        elif tweet[2] is not None:
            return tweet[2]
        elif any(x in tweet[5] for x in negatif):
            return 'negatif'
        elif any(x in tweet[5] for x in postitif):
            return 'positif'
        else:
            return 'netral'
    except:
        return 'netral'

def get_sentimen(doc):
    ct = CRFTagger()
    ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')

    # doc=remove_hashtag(doc)
    # doc=clean_tweet(doc)
    doc = utils.cleanAllTweet(doc)
    #print(doc)
    #pisah perkalimat
    sentences = nltk.sent_tokenize(doc)
    #pisah per kata
    stokens = [nltk.word_tokenize(sent) for sent in sentences]
    #tag indonesia
    taggedlist = ct.tag_sents(stokens)
    # print(taggedlist)

    #sentiword Indonesia
    barasa=pd.read_csv('barasa-ID.txt',delimiter='\t',encoding='utf-8',header=0, names=['syn', 'goodness', 'lemma', 'pos','neg','dummy'])
    score_list=[]
    negasi=""
    for idx,taggedsent in enumerate(taggedlist):
        score_list.append([])
        for idx2,t in enumerate(taggedsent):
            newtag=''
           
            if t[1].startswith('NN'):
                newtag='n'
            elif t[1].startswith('JJ'):
                newtag='a'
            elif t[1].startswith('VB'):
                newtag='v'
            elif t[1].startswith('R'):
                newtag='r'
            elif t[1].startswith('NEG'):
                negasi=t[0]
            else:
                newtag=''       
            if(newtag!=''):    
                if(negasi!=""):
                    kalimat=negasi + ' ' + t[0]
                    negasi=""
                else:
                    kalimat=t[0]
                lemmas=barasa[barasa['lemma'].str.contains(kalimat,na=False)]
                score_list[idx].append(get_scores(lemmas))
    #sentence_sentiment=[]
    totalscore=0.0
    for score_sent in score_list:
        scoresentnow=sum([word_score for word_score in score_sent])/len(score_sent)
        #sentence_sentiment.append(score_sent)
        totalscore=scoresentnow+totalscore
    sentimenScore = totalscore/len(score_list)
    print("Score sentimen = "+str(sentimenScore))
    return sentimenScore

def sentimenLexiconClassifier(score, rangeBottom, rangeTop):
    # mean = 0.007324
    # rangeBottom = mean - 0.027402
    # rangeBottom = -0.004680
    # rangeTop = mean + 0.027402
    # rangeTop = 0.019266
    if(rangeBottom <= score <= rangeTop):
        return 'netral'
    elif(score<rangeBottom):
        return 'negatif'
    else:
        return 'positif'




    #ekonomi
    # ekonomi = "ekonomi"
    # harga = "harga"
    # pertumbuhan = "pertumbuhan"
    # lapangankerja = "lapangan kerja"
    # pekerjaan = "pekerjaan"
    # penghasilan = "penghasilan"
    # gaji = "gaji"
    # pajak = "pajak"
    # pengangguran = "pengangguran"
    # nganggur = "nganggur"
    # kemiskinan = "kemiskinan"
    # kesejahteraan = "kesejahteraan"
    # entahapa = "entahapa"

    #infrastruktur
    # infrastruktur = "infrastruktur"
    # jembatan = "jembatan"
    # jalan = "jalan"
    # pembangunan = "pembangunan"
    # bandara = "bandara"
    # transportasi = "transportasi"
    # waduk = "waduk"
    # bendungan = "bendungan"
    # danadesa = "dana desa"
    #
    # if harga in tweet:
    #     return [ekonomi, harga]
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]
    # elif lapangankerja in tweet:
    #     return [ekonomi, lapangankerja]
    # elif pekerjaan in tweet:
    #     return [ekonomi,pekerjaan]
    # elif penghasilan in tweet:
    #     return [ekonomi,penghasilan]
    # elif gaji in tweet:
    #     return [ekonomi,gaji]
    # elif pajak in tweet:
    #     return [ekonomi,pajak]
    # elif pengangguran in tweet:
    #     return [ekonomi,pengangguran]
    # elif nganggur in tweet:
    #     return [ekonomi,nganggur]
    # elif kemiskinan in tweet:
    #     return [ekonomi,kemiskinan]
    # elif kesejahteraan in tweet:
    #     return [ekonomi,kesejahteraan]
    # else:
    #     return [ekonomi,ekonomi]

    #infrastruktur
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]
    # elif pertumbuhan in tweet:
    #     return [ekonomi,pertumbuhan]


if __name__ == '__main__':
    # import nltk
    # nltk.download('stopwords')

    # doc="@kamu Maaf saya mau menyampaikan layanan farmasi umum di rsud dr soetomo tidak maksimal karena pegawai sedikit waktu ditinggal sholat http://yes.com, antriannya menumpuk sampai 2 jam lebih hanya buat satu macam obat. Yang mengeluh bukan saya saja tapi banyak. Mohon penanganannya."
    # print(get_sentimen(doc))

    # doc = "cth step utk bangun indonesia masuk akal praktik bukti jokowi invest infrastruktur fasilitas sat era ekonomi ga lancar kirim sayur desa jala ga aspal"

    # doc = "Negara kita ngutang buat bngun infrastruktur yang udah dipake masyarakat, terus masyarakatnya ngeluh karena negara ngutang, setiap negara itu pasti ngutang,  utang bisa dibayar kalo negara dapet penghasilan. Penghasilan negara itu ya dari pajak"
    # print("Nilai senrimen = "+str(get_sentimen(doc)))

#baru=remove_hashtag("tes123 #halo !! pa ya httP://mau \n \r wawa")
#print(baru)
#print(clean_tweet(baru))
    # tweet = "Bantu majukan perekonomian bangsa bersama Pak Jokowi, yuk! https://twitter.com/BKNSquare/status/1113655944955588610Â â€ #Jokowi"
    # tweet = "Memang cebong tidak bisa kita menghendaki harga cabai sampai Rp 10.000, harga bawang sampai Rp 5.000, petaninya yang kasihan, kata Jokowi #2019JokowiKyaiMaruf #1PeriodeLagiUntukJokowi #PesonaBonoSurfing  https://twitter.com/tag_nusantara/status/1061795598209232896/photo/1 pic.twitter.com/NApI0SoReiÂ"
    # cleanTweet = klasfikasibaru(tweet)
    # print(cleanTweet)
    # for i in range(5):
    #     print(str(random.randint(0,2)))

    tweet = "@jokowi bantu majukan perekonomian bangsa pak jokowi https twitter com bknsquare status"
    print(utils.cleanAllTweet(tweet))


