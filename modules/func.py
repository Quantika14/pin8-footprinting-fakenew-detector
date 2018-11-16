import re, requests
from bs4 import BeautifulSoup
import modules.dic as dic

TAG_RE = re.compile(r'<[^>]*?>')
def remove_tags(text):
	return TAG_RE.sub('', text)

def check_http(url):
	if "//" in url:
		url = url.replace("//", "")

	if not "http://" in url:
		return "http://" + url
	else:
		return url

#Funcion para devolver las palabras cercas de las palabras claves
def obtenNGramas(listaPalabras, n):
	return [listaPalabras[i:i+n] for i in range(len(listaPalabras)-(n-1))]

#Funcion para obtener el dominio
def get_domain_and_subdomain(url):
	return url.split("://")[1].split("/")[0].replace("www.", "")

def analyze_text(text):
	print ("|----[!][INFO][TEXTO][>] Buscando palabras claves...")
	clean_t = remove_tags(str(text))
	t_split = clean_t.split(" ")
	
	count_pc = 0
	for pc in dic.palabras_claves:
		try:
			i= t_split.index(pc)
			x = i - 15
			z = i + 15
			texto = ' '.join(t_split[x:z])
			print ("|--------[!][P.CLAVES][>]" + texto)
			count_pc += 1
		except:
			pass
	if count_pc == 0:
		print ("|--------[!][INFO][P.CLAVES][>] No se han encontrado referencias hacia ninguna investigación, informe, estudio o fuente en la página web.")


def extractAnalyze_links(enlaces):
	print ("|----[!][INFO][LINKS][>] Analizando si algún enlace de la web redirije a una universidad, instituto, empresa, etc.")
	count_e = 0
	for e in enlaces:
		try:
			e = check_http(e)
			html = requests.get(e).text
			soup = BeautifulSoup(html, "html.parser")
		
			#Analizamos el dominio
			domain = get_domain_and_subdomain(e)
			if ".edu" in e and not domain in e:
				print ("|--------[!][INFO][" + soup.title + "][LINK][" + domain + "[>] Parece una web educativa.")
			#Analizamos el título con el listado de palabras de fuentes
			for fu in dic.t_fuentes:
				if fu in soup.title:
					print ("|--------[!][INFO][" + soup.title + "[LINK][" + domain + "[>] Parece una web de una universidad, instituto, centro de investigación o empresa.")
			count_e += 1
		except:
			pass
	if count_e == 0:
		print ("|----[!][INFO][>] No se ha encontrado ninguna fuente.")
