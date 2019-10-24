import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def remove_hashtag(tweet):
    katas = tweet.split()
    katasbersih=""
    for kata in katas:
        if  kata.startswith('#') == False:
            katasbersih=katasbersih+' '+kata
    return katasbersih

def removeUrl(tweet):
    doc = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*','',tweet, flags=re.MULTILINE)
    doc = re.sub(r'\b(\w*pic.twitter.com\w*)\b.*','',doc, flags=re.MULTILINE)
    doc = re.sub(r'[\d-]','',doc, flags=re.MULTILINE)
    doc = doc.replace("rp","")
    return doc

def clean_tweet(tweet):
     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def removeStopWords(tweet):
    tokens = word_tokenize(tweet)
    stopwordsk = stopwords.words('indonesian')
    newStopwords = ["gitu","gt","bkn","karna","ttg","nggak","ngga","utk","udah","asem","anjay","lah","kh","kok","si","hi","yg","kl","klo","kalo","tdk","tp","sdh","jd","jgn","dr","krn","gw","jg","sy","org","gk","dg","ngak","bpk","d","dlm","rt","p","pa","hahaha","pak","nga","di","tu","lho","x","ni","wah","kan","g","woww","de","vu","nah","ya","ke","aja","nya","pada","kok","kiai","kyai","k.h","h","si","nih","lu","sih","tuh","gw","mas","c","dg","ayo","lo","d","gue","bro","hal","no","lu","dgn","deh","ah","mu","pd","yah","nga","eh","bs","loe","udh","yuk","loh","u","nah","hrs","sm","ku","bu","ama","ente","blm","dl","thn","ha","ni","gua","ia","kpd","i","doang","bgt","msh","the","y","an","in","se","kek","s","haha","amat","wong","dn","sok","ko","k","ntar","to","oh","mbah","klu","koq","kang","km","sya","al","ok","h","t","de","th","cm","wkwk","wkwkwk","ane","nt","sang","situ","mo","dri","tpi","he","hehehe","lha","yo","pula","elu","byk","he","gmn","mak","tg","gmn","o","oke","do","yak","kyk","tuk","aj","sj","you","kah","trs","aj","tsb","bnyk","donk","toh","ala","ndak","on","of","bg","hm","mg","ot","duh","wow","ngk","ka","for","ad","min","ye","krna","uda","bm","elo","ora","so","engak","gaes","abah","la","klw","lgi","pakdhe","pakde","cak","kn","gp","emg","smg","bp","aq","kak","ato","ahy","kaga","at","ber","dlu","adlh","brp","wae","yra","up","aje","guys","akn","jan","td","dhe","sing","bang","dll","klau","da","is","gt","kt","hi","new","b","aduh","bnyak","w","ae","ny","skrng","sprti","wes","wis","moga","it","r","ta","ajah","ampe","iki","dng","gtu","bhw","hihihi","love","woi","nek","doi","wib","mr","nan","ud","bapa","wkwkw","neng","ra","apan","per","luh","sono","nge","jga","hayo","mang","bla","bsa","na","mongo","wkwkwkw","hny","ja","enga","one","dur","neh","slu","by","mw","dek","hnya","hny","hai","atuh","as","bae","me","ape","den","hihi","ono","my","ih","mreka","spy","mbok","bah","wk","ea","lae","ky","yng","blom","sory","ojo","woy","jgn","dk","jng","ki","sdg","wkwkwkwkwk","wkwk","wkwkwk""bgtu","smpe","teu","sip","tar","gada","stlh","kmu","v","ap","napa","sprt","ne","spt","cuk","q","got","be","ir","doank","nyampe","cok","anjg","bacot","anjing","j","nak","noh","ve","euy","mi","hehehehe","https","twitter","com","detik","status","pny","pdhal","cmn","ng","gegara","laen","cuy","blum","jngan","mslh","or","pr","kpn","aya","itupun","ak","gak","ga","mksd","mksdnya"]
    stopwordsk.extend(newStopwords)
    # print(str(stopwordsk))
    listStopword = set(stopwordsk)
    cleanWords = ""
    for t in tokens:
        if t not in listStopword:
            cleanWords = cleanWords+" "+t
    return cleanWords

def cleanAllTweet(tweet):
    try:
        tweet = tweet.lower()
        doc = removeUrl(tweet)
        doc = remove_hashtag(doc)
        # print("Setelah remove hastag = "+doc)
        doc = clean_tweet(doc)
        # print("Setelah dibersihkan = " + doc)
        doc = removeStopWords(doc)
        # print("Setelah remove stopwords = " + doc)
        # print("Clean tweet = "+str(doc))
        return doc
    except Exception as e:
        print("Error = "+str(e))
        pass
