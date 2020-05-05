from nltk.corpus import stopwords
import pandas as pd

stop= stopwords.words("english")

print(stopwords)
#First step : ----------------------Remove Stop Words---------------------------------

data= [[1,'is so sad for my alp'],[2,'i think mi bf cheating me'],[3,'omg its already 7:30']]

tweets = pd.DataFrame(data,columns=['Id','Text'])

print(tweets.head())

short_data = tweets['Text'].apply(lambda x: '  '.join( [word for word in x.split() if word not in (stop)] ) )

#Second step : ----------------------Replace abbreviations and some spell correction---------------------------------

clean_data2 = short_data['Text'].apply(lambda x: '  '.join( [word for word in x.split() if word not in (stop)] ) )





