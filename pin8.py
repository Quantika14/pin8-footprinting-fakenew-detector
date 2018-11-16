import modules.text
import modules.web_func as web
import modules.dic as dic

#Constantes
#URL = "https://de-noticias.net/cachorro-se-reencuentra-con-su-madre-mucho-tiempo-despues-de-ser-separados/"

def pin8_banner():
	print ("""
                                                  
                `..` ::                           
              .:/::/:oh/                          
             ://+oooooss/-.                       
            /+so+/oyhdmmmdhy.            `+/.     
           `ysosdNMhdddhyoyMMo          :osss:    
          `//sNMMMd/..`....dMM.        `+/os:     
          /:yNmMMNs+///////:NN.         -:hNNs/.  
          :/msosy//+osos+oy++:        `-:so/syy:  
           .:sso+/+/+oo/+o+/-````         `sso+/  
              `-::/os+ooyyss+////+///////:://--.` 
              `...+sh+:////:  ...` :`             
  :.......`  -/.  `syyo+++/  -/.`   .-..          
  -.   ...::-.:.--:sssyysso`+//:`   ..--:         
    :     -+:++/..:sss+:sss+//-/:.`...-//-.       
   .``   .-/::/...-hsso./sh:.:/::    -yhhhhh+     
  ..-.. -` ---/...oMdyyssyys---`    -hhhhhhhh/    
  -: : -    `-.-syyyyhhhhyyy/:--    shhdhhhhh+    
   ..:-        +hyhhhhhhhhhhys+++:-.yhhdhhhhh:    
               +yhhhhhhhhhhdhos+-:::shhhhhhhs     
               +hhhhhhhhhhhhso/`.---/hhdhhhs`     
               :shhhhhhhhhh+        `./yyo:       
                 .hhhhhhhhh`                      
                  -hhhhhhh/                       
                    :osso-                        
                                                  
""")

def end_banner():
	print ("""

---------------------------------------------------------
PIN8 ES UNA APLICACIÓN QUE AYUDA AL USUARIO A IDENTIFICAR
    NOTICIAS FALSAS Y WEBS DE CONTENIDO SOSPECHOSOS. 
         MÁS INFORMACIÓN: BLOG.QUANTIKA14.COM
""")

def menu_banner():
	print("""
	██████╗ ██╗███╗   ██╗ █████╗ 
	██╔══██╗██║████╗  ██║██╔══██╗
	██████╔╝██║██╔██╗ ██║╚█████╔╝
	██╔═══╝ ██║██║╚██╗██║██╔══██╗
	██║     ██║██║ ╚████║╚█████╔╝
	╚═╝     ╚═╝╚═╝  ╚═══╝ ╚════╝ 
                             
---------------------------------------------------
_AUTHOR_ = Jorge Coronado | WEB: www.quantika14.com
Twitter = @JorgeWebsec    | EMAIL: jorge[.]coronado[@]quantika14.com
Licencia = GPL
--------------------------------------------
- Date: 16/11/2018
- Versión: 1.0

""")

def main():
	pin8_banner()
	menu_banner()

	URL = input("[TARGET][>] Inserte la web que quiere analizar: ")
	print ("[*][TARGET][>] " + URL)

	web.get_webData(URL)
	end_banner()
main()
