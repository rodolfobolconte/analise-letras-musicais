import requests
import lyrics

path = "musicas/"


genero = "rock/"

links = ['https://www.vagalume.com.br/charlie-brown-jr/ceu-azul.html', 'https://www.vagalume.com.br/legiao-urbana/tempo-perdido.html', 'https://www.vagalume.com.br/legiao-urbana/pais-e-filhos.html', 'https://www.vagalume.com.br/legiao-urbana/eduardo-e-monica.html', 'https://www.vagalume.com.br/nando-reis/pra-voce-guardei-o-amor.html', 'https://www.vagalume.com.br/jota-quest/so-hoje.html', 'https://www.vagalume.com.br/legiao-urbana/faroeste-cabloco.html', 'https://www.vagalume.com.br/legiao-urbana/indios.html', 'https://www.vagalume.com.br/capital-inicial/primeiros-erros.html', 'https://www.vagalume.com.br/legiao-urbana/quase-sem-querer.html', 'https://www.vagalume.com.br/charlie-brown-jr/senhor-do-tempo.html', 'https://www.vagalume.com.br/charlie-brown-jr/so-os-loucos-sabem.html', 'https://www.vagalume.com.br/los-hermanos/ultimo-romance.html', 'https://www.vagalume.com.br/legiao-urbana/vento-no-litoral.html', 'https://www.vagalume.com.br/supercombo/piloto-automatico.html', 'https://www.vagalume.com.br/charlie-brown-jr/lugar-ao-sol.html', 'https://www.vagalume.com.br/supercombo/amianto.html', 'https://www.vagalume.com.br/charlie-brown-jr/dias-de-luta-dias-de-gloria.html', 'https://www.vagalume.com.br/legiao-urbana/monte-castelo.html', 'https://www.vagalume.com.br/cazuza/o-tempo-nao-para.html']


for link in links:

	link = link.split('/')

	artist_name = link[3]
	song_name = link[4][:-5]

	musica = lyrics.find(artist_name, song_name)

	nome_arquivo = path + genero + genero[:-1] + '+' + artist_name + "+" + song_name + ".txt"

	arquivo = open(nome_arquivo, "w")
	arquivo.writelines(str(musica.song.lyric.encode("utf-8")))


"""
sertanejo = ['https://www.vagalume.com.br/jorge-e-mateus/propaganda.html', 'https://www.vagalume.com.br/ze-neto-e-cristiano/largado-as-tracas.html', 'https://www.vagalume.com.br/marilia-mendonca/ausencia.html', 'https://www.vagalume.com.br/thiago-matheus/safadometro.html', 'https://www.vagalume.com.br/gustavo-mioto/anti-amor.html', 'https://www.vagalume.com.br/gusttavo-lima/apelido-carinhoso.html', 'https://www.vagalume.com.br/marilia-mendonca/parece-namoro.html', 'https://www.vagalume.com.br/thiago-brava/dona-maria-part-jorge.html', 'https://www.vagalume.com.br/jorge-e-mateus/trincadinho.html', 'https://www.vagalume.com.br/leo-magalhaes/oi.html', 'https://www.vagalume.com.br/felipe-araujo/amor-da-sua-cama.html', 'https://www.vagalume.com.br/thiago-matheus/seu-ze.html', 'https://www.vagalume.com.br/marilia-mendonca/estranho.html', 'https://www.vagalume.com.br/naiara-azevedo/obrigado-mae.html', 'https://www.vagalume.com.br/jorge-e-mateus/inesperado.html', 'https://www.vagalume.com.br/almir-sater/tocando-em-frente.html', 'https://www.vagalume.com.br/jorge-e-mateus/contrato.html', 'https://www.vagalume.com.br/marilia-mendonca/a-culpa-e-dele-part-maiara-e-maraisa.html', 'https://www.vagalume.com.br/ze-neto-e-cristiano/status-que-eu-nao-queria.html', 'https://www.vagalume.com.br/matheus-e-kauan/nessas-horas.html']

funk = ['https://www.vagalume.com.br/mc-rita/amor-de-verdade-part-mc-kekel.html', 'https://www.vagalume.com.br/aldair-playboy/amor-falso.html', 'https://www.vagalume.com.br/mc-mm/so-quer-vrau.html', 'https://www.vagalume.com.br/gaab/cuidado.html', 'https://www.vagalume.com.br/dani-russo/jeito-malicioso.html', 'https://www.vagalume.com.br/gaab/tem-cafe-com-mc-hariel.html', 'https://www.vagalume.com.br/mc-wm/fuleragem.html', 'https://www.vagalume.com.br/mc-loma-e-as-gemeas-lacracao/envolvimento.html', 'https://www.vagalume.com.br/mc-careca/os-opostos-se-atraem.html', 'https://www.vagalume.com.br/mc-kevinho/papum.html', 'https://www.vagalume.com.br/gaab/to-brisando-em-voce.html', 'https://www.vagalume.com.br/mc-kevinho/pega-a-receita-com-mc-dede.html', 'https://www.vagalume.com.br/pikeno-e-menor/valeu-amigo.html', 'https://www.vagalume.com.br/mc-loma-e-as-gemeas-lacracao/treme-treme.html', 'https://www.vagalume.com.br/gaab/positividade.html', 'https://www.vagalume.com.br/jojo-maronttinni/que-tiro-foi-esse.html', 'https://www.vagalume.com.br/mc-don-juan/amar-amei-gostar-gostei.html', 'https://www.vagalume.com.br/mc-loma-e-as-gemeas-lacracao/paralisa-part-mc-wm.html', 'https://www.vagalume.com.br/mc-kevinho/rabiola.html', 'https://www.vagalume.com.br/mc-kevinho/ta-tum-tum-com-simone-e-simaria.html']

"""