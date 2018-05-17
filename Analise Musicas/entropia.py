# -*- coding: utf-8 -*-

import io
import string
import urllib2

# 3rd Party
from PIL import Image
import numpy as np
#from matplotlib import pyplot as plt
from scipy import ndimage
import os

path_raiz = "musicas/"

def media_palavras_por_genero(genero):
    path_musicas = os.listdir(path_raiz + genero)
    for caminho_musica in path_musicas:
        arquivo_musica = open(path_raiz + genero + '/' + caminho_musica, 'r')
        print(arquivo_musica)
        text = ""
        for linha in arquivo_musica:
            text += linha

        text = text.translate(string.maketrans("",""), string.punctuation)
        words = text.split()
        
        wordset = set(words)
        freq={word: words.count(word) for word in wordset}


        print "Word \t\t Count \t Self Information"
        word_count_information = []
        entropy = 0
        for word in wordset:
            probability = freq[word] / float(1.0 * len(words)) 
            self_information = np.log2(1.0/probability) 
            entropy += (probability * self_information)
            word_count_information.append([word, freq[word], self_information])

        sorted_word_count_information = list(sorted(word_count_information, key=lambda k:k[2], reverse=True))

        for ii in sorted_word_count_information:
    # Very inelegant way of formatting
            separation = '\t\t' if len(ii[0]) < 7 else '\t'
            if len(ii[0]) >= 15: separation = '' 
        
            arquivo_music = open(genero  + '_auto_informacao.txt' , 'a')
            arquivo_music.writelines(ii[0])
            arquivo_music.writelines('\t')
            arquivo_music.writelines(str(ii[2]))
            arquivo_music.writelines('\n')
        

generos = ['forro', 'mpb','rock','sertanejo','funk']

medias = {}
for genero in generos:
	medias[genero.upper()] = media_palavras_por_genero(genero)
