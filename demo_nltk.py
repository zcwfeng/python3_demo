import nltk
import jieba
# nltk.download()

# raw=open('forgotten_times.txt').read()
# text=nltk.text.Text(jieba.lcut(raw))
# print(text.concordance(u'风花雪月'))
# print(text.common_contexts([u'一起',u'一同']))
# print(text.collocations())
# print(text.dispersion_plot([u'校园',u'大学']))


#
# fdist = nltk.FreqDist(nltk.word_tokenize(text))
# fdist.plot(30,cumulative=True)


# porter = nltk.PorterStemmer()
# porter.stem('lying') #'lie'
#
# lema=nltk.WordNetLemmatizer()
# lema.lemmatize('women')   #'woman'

# from nltk.tokenize import sent_tokenize, word_tokenize
#
# EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
#
# print(sent_tokenize(EXAMPLE_TEXT))

# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
#
# example_sent = "This is a sample sentence, showing off the stop words filtration."
#
# stop_words = set(stopwords.words('english'))
#
# word_tokens = word_tokenize(example_sent)
#
# filtered_sentence = [w for w in word_tokens if not w in stop_words]
#
# filtered_sentence = []
#
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#
# print(word_tokens)
# print(filtered_sentence)

# from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
#
# ps = PorterStemmer()
# example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
# for w in example_words:
#     print(ps.stem(w))
# new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
# words = word_tokenize(new_text)
#
# for w in words:
#     print(ps.stem(w))

import nltk
print(nltk.__file__)
