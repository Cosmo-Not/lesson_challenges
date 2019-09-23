# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[len(word)-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print (word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
sogl = "бвгджзклмнпрстфхцчшщ"
gl = "аеёиоуыэюя"
sum_gl = sum (1 for letter in word.lower() if letter in gl)
print (sum_gl)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print (len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
slova = sentence.split()
for each_word in slova:
    print (each_word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
slova = sentence.split()
sum_slova = len(slova)
bukv = 0
for word1 in slova:
    bukv += len(word1)
avg_bukv = bukv / sum_slova
print(avg_bukv)