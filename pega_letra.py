import requests

page = requests.get('https://www.letras.com.br/thiago-brava/dona-maria-part-jorge-')

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

arq = open("letra.txt", "w")
arq.writelines(soup.find(id="letra"))