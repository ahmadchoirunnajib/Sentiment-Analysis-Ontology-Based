# SentimentAnalysisOntologyBased
Ontology-based Sentiment Analysis on the Twitter - Indonesian President Election Campaign 2019 Study Case
We developed an ontology based on the dataset -> "Ekonomi" with three attributes i.e., "Finansial", "Lapangan Kerja", "Kesejahteraan". 

Then we calculate the sentimen of the tweets and summarize the sentiment results based on the ontology attributes.


## Raw Dataset
* Extract file on the data/allchunk_dataset_raw.zip
* We already processed the raw dataset to the labelled tweets on the Sampel600.xlsx

## Methodology
1. Data Acquisition
 * Tweet selection -> tweetmanipulation.py
2. Development of Ontology
 * Make initial ontology -> ontology.py
 * Preprocessing -> utils.py & ontology.py
 * Update the ontology to Final Ontology using WordCloud -> tweetmanipulation.py
 * Classify the tweets based on the Final Ontology -> ontology.py
3. Sentiment Analysis
 * Sentiment analysis by Lexicon-based -> sentimenlexicon.py
 * Sentiment analysis by SVM -> sentimenklasifikasisvm.py
 * Measuring performance -> performance.py
 * Mapping the sentimen based on the ontology -> tweetontology.py
