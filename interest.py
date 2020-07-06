import numpy as np
import pandas as p
import matplotlib as mp

a = "I am Aninda. Aninda is a good boy. I am good"
b = a.split(" ")
sum = {}
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
for i in b:
    for j in punctuations:

        if j in i:
            i = i.replace(j, "")
            break
    if i not in uninteresting_words:
        if i not in sum:
            sum[i] = 1
        else:
            sum[i] += 1
print(sum)
