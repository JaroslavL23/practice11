import nltk
import string
import re
import matplotlib.pyplot as plt

#Завантаження корпусів та ресурсів бібліотеки NLTK
nltk.download('gutenberg') #тексти для аналізу
nltk.download('stopwords') #список стоп-слів

from nltk.corpus import*
from nltk import FreqDist

#Завантаження слів із тексту burgess-busterbrown.txt із корпусу gutenberg
text = nltk.corpus.gutenberg.words('burgess-busterbrown.txt')
print("\nКількість слів у тексті =", len(text))

#Отримання 10 найбільш вживаних слів
top_words = nltk.FreqDist(text).most_common(10)
words = [word for word, freq in top_words] #найбільш вживані слова
freq = [freq for word, freq in top_words] #їх частота
print("10 найбільш вживаних слів:\n")
for word, fq in top_words:
    print(word, " з частотою -", fq)

#Побудова стовпчастої діаграми
plt.figure(figsize=(10, 5))
plt.bar(words, freq)
plt.xlabel("Слова")
plt.ylabel("Частоти")
plt.title("Найбільш вживані слова тексту")
plt.show()

#Видалення стоп-слів та пунктуації з тексту
stop_words = set(stopwords.words("english"))
text_without = [word for word in text if not word.lower() in stop_words]
text_result = [word for word in text_without if not re.fullmatch('[' + string.punctuation + ']+', word)]

#Отримання 10 найбільш вживаних слів без стоп-слів та пунктуації
top_words_without = nltk.FreqDist(text_result).most_common(10)
words_without = [word for word, freq in top_words_without]
freq_without = [freq for word, freq in top_words_without]
print("\n10 найбільш вживаних слів без стоп-слів та пунктуації:\n")
for word, fq in top_words_without:
    print(word, " з частотою -", fq)
    
#Побудова стовпчастої діаграми
plt.figure(figsize=(10, 5))
plt.bar(words_without, freq_without)
plt.xlabel("Слова")
plt.ylabel("Частоти")
plt.title("Найбільш вживані слова тексту без стоп-слів та пунктуації")
plt.show()

