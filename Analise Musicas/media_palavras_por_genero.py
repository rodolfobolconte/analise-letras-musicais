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

from pylab import *

fig, eixo = plt.subplots(nrows=1, ncols=1, figsize=(80, 7))
grafico = eixo.bar(medias.keys(), medias.values(), width=0.3, color=['yellow', 'blue', 'red', 'black', 'green'], zorder=3, tick_label=['FORRÓ', 'FUNK', 'MPB', 'ROCK', 'SERTANEJO'])

for i in grafico:
        height = i.get_height()
        eixo.text(i.get_x() + i.get_width() / 2, 1.01 * height, '%.1f' % height, fontsize=12, ha='center',
                      va='bottom')

grid(zorder=0)

yticks(range(0,400,20))

eixo.set_title('média de palavras por letra em cada gênero musical'.upper())
eixo.set_ylabel('quantidade média'.upper())
eixo.set_xlabel('gêneros musicais'.upper())

fig.canvas.set_window_title('média de palavras por letra em cada gênero musical'.upper())

mng = get_current_fig_manager()
mng.window.showMaximized()

show()