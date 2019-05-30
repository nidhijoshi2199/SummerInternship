review= "Poornima got first rank in a tournament held last week. #poornima"
import re

import nltk
nltk.download('stopwards')
from nltk.corpus import stopwards

from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import wordnetelmmatizer

#perform rowise noise removal and stemming 

#do it on 1st row data
review=re.sub('[a-zA-z]',' ',review)
review=review.lower()
review=review.split()

review = [word for word in review if not word in set (stopwards.words('english'))]
ps = PorterStemmer()
rev=[ps,stem(word) for word in rev]
print(rev)

