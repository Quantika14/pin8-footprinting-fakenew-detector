import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import modules.dic as dic
import modules.func as f


def get_description(html):
	soup = BeautifulSoup(html, "html.parser")
	metas = soup.find_all('meta')
	desc = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]
	desc = ' '.join(desc)
	print ("|----[!][INFO][>] Descripción de la web: " + desc)


def get_webData(url):
	enlaces = []
	data = []
	html = requests.get(url).text
	
	#Extraemos la descripción
	get_description(html)

	soup = BeautifulSoup(html, "html.parser")
	
	#-------------------------------------------
	#Verificamos el dominio con la blacklist
	title = soup.find('title')
	domain = f.get_domain_and_subdomain(url)
	print (domain)
	
	#buscamos en webs de humor
	for web in dic.webs_humor:
		if web == domain:
			print ("|----[!][BLACKLIST][HUMOR][>] Esta web aparece en nuestra blacklist de webs de humor y satíricas.")
			print ("|--------[+][INFO][>] Es posible que el contenido de esta web sea ficción y tenga un objetivo de humor.")

	for web in dic.webs_virales:
		if web == domain:
			print ("|----[!][BLACKLIST][VIRAL][>] Esta web aparece en nuestra blacklist de webs virales.")
			print ("|--------[+][INFO][>] Es posible que esta web cree contenido falso y de ficción para beneficiarse económicamente. Recomendamos encarecidamente que no se le de fiabilidad al contenido subido en esta página web.")
	
	#------------------------------------------
	#Analizamos el título
	title = f.remove_tags(str(title))
	for word in dic.titulos:
		if word in title:
			print ("|---[!][TITLE][>] En el título de esta página aparecen palabras que indican que puede ser de humor, satírica o una noticia falsa.")

	#------------------------------------------
	#Buscamos enlace aviso legal
	count_al = 0
	for a in soup.find_all('a', href=True):
		if "avisolegal" in a['href'] or "aviso-legal" in a['href'] or "legal" in a['href']:
			print ("|----[!][AVISO LEGAL][>] Se ha encontraro la URL del aviso legal:", a['href'])
			e = f.check_http(a['href'])
			#Analizamos el aviso legal
			analyze_avisoLegal(e)
			count_al += 1
		else:
			if not domain in a['href'] and len(a['href'])> 4:
				enlaces.append(a['href'])
	if count_al == 0:
		print ("|----[!][INFO][>] No se ha encontrado la página de aviso legal.")
		print ("|--------[+][AVISO LEGAL][>] Esta web es sospechosa de generar contenido falso o poco fiable.")

	#------------------------------------------
	#Analizamos el texto
	f.analyze_text(soup.body)
	f.extractAnalyze_links(enlaces)


def analyze_avisoLegal(url):
	try:
		html = requests.get(url).text
		soup = BeautifulSoup(html, "html.parser")
		body = soup.find('body')
		for word in dic.aviso_legal:
			if word in f.remove_tags(str(body)):
				print ("|--------[!][INFO][>] Esta web según su aviso legal es de humor y satírica. La información que exponen no debe ser considerada fiable o real.")
				break
			else:
				pass
	except:
		pass
