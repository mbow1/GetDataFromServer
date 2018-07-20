import requests
from lxml import html

payload = {
	"username": "alepage", 
	"password": "Tech%mmorpg02", 
	"csrfmiddlewaretoken": "acc66103-a55b-4d96-b5f6-64f7d4e9b6f4"
}

session_requests = requests.session()

login_url = "https://nrbdfpem.viacesi.fr/em/login"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]


