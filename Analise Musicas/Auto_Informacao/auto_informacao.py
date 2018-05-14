# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:15:28 2018

@author: mique
"""

def media_autoinformacao_por_genero(genero):
    arquivo_music = open(genero  + '_auto_informacao.txt' , 'r')
    valores = []
    for linha in arquivo_music:
        leitura  = linha.split("\n")
        x = float(leitura[0])
        valores.append(x)
    
    valores = set(valores)
    valores_ordenados = sorted(valores)
    y = len(valores_ordenados)
    print(y)
    maiores_valores = []
    for i in range(1,6):
       
        maiores_valores.append(valores_ordenados[y-i])
    print(maiores_valores)
    return maiores_valores
    
generos = ['forro', 'mpb','rock','sertanejo','funk']
medias = {}
for genero in generos:
	medias[genero.upper()] = media_autoinformacao_por_genero(genero)
print(medias.values())