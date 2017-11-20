'''
Created on Nov 20, 2017

@author: z002krv
'''
def generateSentences():
    subjects=["Americans ","Indians"]
    verbs=["play","watch"]
    objects=["Baseball","Cricket"]
    sentences = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = subject+" "+verb+" "+obj;
                sentences.append(sentence)
    return sentences


for sen in generateSentences():
    print(sen)

                