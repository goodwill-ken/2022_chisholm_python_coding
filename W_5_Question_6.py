# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

# Using the sentence from Question 5 - “I am learning to code in
# Python” write a program that splits the string into its seven
# individual words.

q5_sentence = 'I am learning to code in Python'
print('The sentence from Question 5 is: ', q5_sentence)
word_1 = q5_sentence[0]
word_1ps = q5_sentence[0:2]
print('The first word in Question 5 is: ', word_1)
word_2 = q5_sentence[2:4]
word_2ps = q5_sentence[2:5]
print('The second word in Question 5 is: ', word_2)
word_3 = q5_sentence[5:13]
word_3ps = q5_sentence[5:14]
print('The third word in Question 5 is: ', word_3)
word_4 = q5_sentence[14:16]
word_4ps = q5_sentence[14:17]
print('The fourth word in Question 5 is: ', word_4)
word_5 = q5_sentence[17:21]
word_5ps = q5_sentence[17:22]
print('The fifth word in Question 5 is: ', word_5)
word_6 = q5_sentence[22:24]
word_6ps = q5_sentence[22:25]
print('The sixth word in Question 5 is: ', word_6)
word_7 = q5_sentence[25:32]
word_7ps = q5_sentence[25:33]
print('The seventh word in Question 5 is: ', word_7)
print('We can concatenate these words into the sentence: ')
print(word_1ps + '' + word_2ps + '' + word_3ps + '' + word_4ps + '' + word_5ps + '' + word_6ps + '' + word_7ps)
