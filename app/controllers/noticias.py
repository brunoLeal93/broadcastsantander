from bs4 import BeautifulSoup
import requests
import datetime 
from pprint import pprint


class noticias:
    aux = datetime.date.today()
    hj = str(aux).replace("-","")
    url = "http://cp.ae.com.br/AEContent/output/NewsServlet?10039=9&10065=xml&10023=2&10095=9&10098="+hj
    vet_final = []
    old_vet = []
    html=""

    def ultimas10(self):
        i = 0
        #print(self.url)
        page = requests.get(self.url)
        #print(page)
        soup = BeautifulSoup(page.text, 'html.parser')
        #print(soup)
        vet_titulo = soup.find_all('titulo')
        vet_datahora = soup.find_all('data')
        #print(vet_titulo)
        #print(vet_datahora)
        #print(datetime.datetime.strptime(vet_datahora[0].get_text(), "%Y%m%d%H%M%S"))
        vet_0 = []
        while i < 10:
            post = {
                'titulo':vet_titulo[i].get_text(),
                'data': datetime.datetime.strptime(vet_datahora[i].get_text(), "%Y%m%d%H%M%S")
            }
            vet_0.append(post)
            i=i+1

        
        for x in vet_0:
            if x not in self.vet_final:
                if len(self.vet_final) > 10:
                    self.vet_final.insert(0, x)
                    self.vet_final.pop(-1)
                else:
                    self.vet_final.append(x)
        self.montaHtml() 

    def montaHtml(self):
        self.html=""
        i=0
        for x in self.vet_final:
            if i == 0:
                self.html = self.html + "<div class='carousel-item active text-left p-4'>"+\
                                "<p>"+str(x['data'].hour-3).zfill(2)+":"+str(x['data'].minute).zfill(2)+" - "+x['titulo']+"</p>"+\
                            "</div>"
                i=i+1
            else:
                self.html = self.html + "<div class='carousel-item text-left p-4'>"+\
                                "<p>"+str(x['data'].hour-3).zfill(2)+":"+str(x['data'].minute).zfill(2)+" - "+x['titulo']+"</p>"+\
                            "</div>"
        #print(html)

n= noticias()
n.ultimas10()

pprint(n.vet_final)