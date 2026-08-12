import urllib.request
import urllib

# Criamos uma requisição personalizada definindo um "User-Agent" de navegador comum
url = 'http://www.pudim.com.br'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)

try:
    site = urllib.request.urlopen(req)
except Exception as e:
    print(f'Deu erro: {e}')
else:
    print('Tudo ok')
    
