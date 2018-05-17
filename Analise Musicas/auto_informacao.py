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
    
generos = ['forro', 'mpb','rock','sertanejo','funk']
medias = {}
for genero in generos:
	medias[genero.upper()] = media_autoinformacao_por_genero(genero)
print(medias)