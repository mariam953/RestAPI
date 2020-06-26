import nltk
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import csv,re

nltk.download('stopwords')
stop= stopwords.words("english")

def tweet_preprocessing(tweets):

    tweets.drop_duplicates(subset ="tweet_id",keep = False, inplace = True)

    tweets['text'] = tweets.text.apply(lambda text:  re.sub(r"http\S+", "", text))

    tweets['text'] = tweets.text.apply(lambda text:  translator.translate(text).text)
        

    #First step : ----------------------Remove Stop Words---------------------------------

    tweets['text'] = tweets['text'].apply(lambda x: '  '.join( [word for word in x.split() if word not in (stop)] ) )

    print("First step : ----------------------Remove Stop Words---------------------------------")
    print(tweets)

    #Second step : ----------------------Replace abbreviations and some spell correction---------------------------------

    def translator(user_string):
        user_string = user_string.split(" ")
        j = 0
        for _str in user_string:
            # File path which consists of Abbreviations.
            fileName =  "D:\Desktop\mariam mongodb+python tanger\REST API\mymodules\slang.csv"
            # File Access mode [Read Mode]
            accessMode = "r"
            with open(fileName, accessMode) as myCSVfile:
                # Reading file as CSV with delimiter as "=", so that abbreviation are stored in row[0] and phrases in row[1]
                dataFromFile = csv.reader(myCSVfile, delimiter="=")
                # Removing Special Characters.
                _str = re.sub('[^a-zA-Z0-9-_.]', '', _str)
                for row in dataFromFile:
                    # Check if selected word matches short forms[LHS] in text file.
                    if _str.upper() == row[0]:
                        # If match found replace it with its appropriate phrase in text file.
                        user_string[j] = row[1]
                myCSVfile.close()
            j = j + 1
        # Replacing commas with spaces for final output.
        clean=' '.join(user_string)
        print(clean)    
        return clean
    
    tweets['text'] = tweets['text'].apply(lambda x: translator(x) )

    print("Second step : ----------------------Replace abbreviations and some spell correction---------------------------------")
    print(tweets)

    #Third Step : --------------------- Stemming [New Feature] --------------------- remove ing from verbs

    ps=PorterStemmer()
    tweets['text'] = tweets['text'].apply(lambda x: '  '.join( [ ps.stem(word) for word in x.split() ] ) )

    print("Third Step : --------------------- Stemming [New Feature] ---------------------")
    print(tweets)

    #Forth Step : --------------------- Lemmatization [New Feature] --------------------- 
    lmtz= WordNetLemmatizer()
    tweets['text'] = tweets['text'].apply(lambda x: ' '.join([lmtz.lemmatize(word,'v') for word in x.split() ])  )

    print("Forth Step : --------------------- Lemmatization [New Feature] --------------------- )")
    print(tweets)


    #Fifth Step 5: --------------------- Parts of Speech Tagging (POS) [New Feature] ---------------------
    #tweets['text'] = tweets['text'].apply(lambda x: nltk.pos_tag(nltk.word_tokenize(x) ))

    #print("Fifth Step 5: --------------------- Parts of Speech Tagging (POS) [New Feature] ---------------------")
    #print(tweets)

    #Sixth Step : --------------------- Capitalization ---------------------

    tweets['text'] = tweets['text'].apply(lambda x: '  '.join( [word.upper() for word in x.split()] ) )

    print("Sixth Step : --------------------- Capitalization ---------------------")
    print(tweets)

    return tweets