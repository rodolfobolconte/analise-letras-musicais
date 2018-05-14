

def media_entropia_por_genero(genero):
    arquivo_music = open(genero  + '_entropia.txt' , 'r')
    media = 0
    for linha in arquivo_music:
        leitura  = linha.split("\n")
        x = float(leitura[0])
        media+=x
    
    return media/20
    
generos = ['forro', 'mpb','rock','sertanejo','funk']
medias = {}
for genero in generos:
	medias[genero.upper()] = media_entropia_por_genero(genero)


from pylab import *

fig, eixo = plt.subplots(nrows=1, ncols=1, figsize=(80, 7))
grafico = eixo.bar(medias.keys(),medias.values(), width=0.3, color=['yellow', 'blue', 'red', 'black', 'green'], zorder=3, tick_label=['FORRÓ', 'FUNK', 'MPB', 'ROCK', 'SERTANEJO'])

for i in grafico:
        height = i.get_height()
        eixo.text(i.get_x() + i.get_width() / 2, 1.01 * height, '%.1f' % height, fontsize=12, ha='center',
                      va='bottom')

grid(zorder=0)

yticks(range(0,400,20))

eixo.set_title('média de palavras por letra em cada gênero musical'.upper())
eixo.set_ylabel('quantidade média'.upper())
eixo.set_xlabel('gêneros musicais'.upper())

mng = get_current_fig_manager()
mng.window.showMaximized()

show()
