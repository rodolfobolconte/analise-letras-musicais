def media_autoinformacao_por_genero(genero):
    arquivo_music = open('Auto_Informacao/' + genero  + '_auto_informacao.txt' , 'r')
    valores = []
    for linha in arquivo_music:
        leitura  = linha.split("\n")
        x = float(leitura[0])
        valores.append(x)
    
    valores = set(valores)
    valores_ordenados = sorted(valores)
    y = len(valores_ordenados)
    maiores_valores = []
    for i in range(1,6):
       
        maiores_valores.append(valores_ordenados[y-i])
    
    return maiores_valores
    
generos = ['FORRO', 'FUNK', 'MPB','ROCK','SERTANEJO']
medias = {}
for genero in generos:
    medias[genero] = media_autoinformacao_por_genero(genero)
#print(medias)



from pylab import *

fig, eixo = plt.subplots(nrows=2, ncols=3)

def sub_grafico(linha, coluna, y, cor, titulo):

    grafico = eixo[linha][coluna].bar([1,2,3,4,5], y, width=0.3, color=[cor], zorder=3)

    for i in grafico:
            height = i.get_height()
            eixo[linha][coluna].text(i.get_x() + i.get_width() / 2, 1.01 * height, '%.1f' % height, fontsize=10, ha='center',
                          va='bottom')

    eixo[linha][coluna].grid(zorder=0)

    eixo[linha][coluna].set_yticks(range(0,13,1))

    eixo[linha][coluna].set_title(titulo, fontsize=9)

sub_grafico(0, 0, medias[generos[0]], 'yellow', generos[0])
sub_grafico(0, 1, medias[generos[1]], 'blue', generos[1])
sub_grafico(0, 2, medias[generos[2]], 'red', generos[2])
sub_grafico(1, 0, medias[generos[3]], 'black', generos[3])
sub_grafico(1, 1, medias[generos[4]], 'green', generos[4])

fig.tight_layout()
fig.canvas.set_window_title('MAIORES PALAVRAS COM AUTO INFORMAÇÃO POR GÊNERO')

mng = get_current_fig_manager()
mng.window.showMaximized()

show()
