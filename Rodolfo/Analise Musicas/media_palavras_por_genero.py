import os

path_raiz = "../Armazenamento Musicas/musicas/"

def media_palavras_por_genero(genero):

	media_palavras = 0

	path_musicas = os.listdir(path_raiz + genero)

	for caminho_musica in path_musicas:

		arquivo_musica = open(path_raiz + genero + '/' + caminho_musica, 'r')

		musica = arquivo_musica.read().replace('\n', ' ').split(' ')
		media_palavras += len(musica)

	return media_palavras / len(path_musicas)


generos = ['forro', 'funk', 'mpb', 'rock', 'sertanejo']

medias = {}
for genero in generos:
	medias[genero.upper()] = media_palavras_por_genero(genero)

print(medias)

from pylab import *

grid(zorder=0)
yticks(range(0,400,20))
title('média de palavras por letra em cada gênero musical'.upper())

grafico = bar(medias.keys(), medias.values(), width=0.3, color=['yellow', 'blue', 'red', 'black', 'green'], zorder=3)

mng = get_current_fig_manager()
mng.window.showMaximized()

show()