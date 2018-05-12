import os

path_raiz = "../Armazenamento Musicas/musicas/"

def media_palavras(genero):

	media_palavras = 0

	path_musicas = os.listdir(path_raiz + genero)

	for caminho_musica in path_musicas:


		arquivo_musica = open(path_raiz + genero + '/' + caminho_musica, 'r')

		musica = arquivo_musica.read().replace('\n', ' ').split(' ')
		media_palavras += len(musica)

	return media_palavras / 20


generos = ['funk', 'rock', 'sertanejo']

for genero in generos:
	print(genero, media_palavras(genero))