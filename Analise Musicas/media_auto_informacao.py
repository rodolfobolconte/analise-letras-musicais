path_raiz = "MediaEntropia/"

def media_entropia_por_genero(genero):
    arquivo_music = open(path_raiz + genero  + '_entropia.txt' , 'r')
    media = 0
    for linha in arquivo_music:
        leitura  = linha.split("\n")
        x = float(leitura[0])
        media+=x
    
    return media/20
    
generos = ['forro', 'funk', 'mpb', 'rock', 'sertanejo']
medias = {}
for genero in generos:
    medias[genero.upper()] = media_entropia_por_genero(genero)

#print(medias)

from pylab import *

fig, eixo = plt.subplots(nrows=2, ncols=3)

def sub_grafico():

    grafico = eixo[0][0].bar(medias.keys(),medias.values(), width=0.3, color=['yellow', 'blue', 'red', 'black', 'green'], zorder=3, tick_label=['FORRÓ', 'FUNK', 'MPB', 'ROCK', 'SERTANEJO'])

    for i in grafico:
            height = i.get_height()
            eixo[0][0].text(i.get_x() + i.get_width() / 2, 1.01 * height, '%.1f' % height, fontsize=12, ha='center',
                          va='bottom')

    eixo[0][0].grid(zorder=0)

    eixo[0][0].set_yticks(range(0,10,1))

"""eixo[0][0].set_title('entropia média de músicas por gênero musical'.upper())
eixo[0][0].set_ylabel('entropia média'.upper())
eixo[0][0].set_xlabel('gêneros musicais'.upper())"""


mng = get_current_fig_manager()
mng.window.showMaximized()

show()
