# -*- coding: utf-8 -*-
from json import load
import datetime as dt
from time import sleep as slp
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from re import split
#import pdfplumber
#import pandas as pd
import json

cor = [
'text-white bg-primary',
'text-white bg-secondary',
'text-white bg-info',
'text-white bg-success',
'bg-warning',
'text-white bg-danger',
'text-white bg-black',
'bg-light',
]

## Data ##
agora = dt.datetime.today()
aa = agora.year
mm = agora.month
dd = agora.day

def data_to_int(d:int, m:int):
   normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
   i = d
   for c in range(m - 1):
      i += normal_year[c]
   
   return i

with open("code/alunos.json", encoding="UTF-8") as f:
	datum = load(f)
data = datum["alunos"]
#datum["conf"]["Xerife"] = (dt.date(aa,mm,dd).isocalendar()[1]-18)%30

## Quarto de Serviço ##
q1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,14,15,16,22]
q2 = [13,17,18,19,20,21,23,24,25,26,27,28,29,30]

tagcounter = 0
while True:
   ## Lista de Presença
   html=f"""<!DOCTYPE html>
<html lang="pt-br"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="_bootstrap.min.css" rel="stylesheet">
      <script src="_bootstrap.min.js"></script>
      <script src="_popper.min.js"></script>
      <script src="_bootstrap.bundle.min.js"></script>
      <script src="_main.js"></script>
      <title>Verificação de Presença</title>
      <link href="_style.css" rel="stylesheet">
      <script src="drag.js"></script>
      
   </head>
   <body>
      <nav class="navbar navbar-expand-lg navbar-light bg-success">
         <div class="container-fluid">
           <a class="navbar-brand" href="#">
              <img src="brasao_min.png" height="24">
           </a>
           <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
             <span class="navbar-toggler-icon"></span>
           </button>
           <div class="collapse navbar-collapse" id="navbarNav">
             <ul class="navbar-nav">
               <li class="nav-item">
                 <a class="nav-link active" aria-current="page" href="#" style="color: black;">Presença</a>
               </li>
               <li class="nav-item">
                 <a class="nav-link active" aria-current="page" href="aula_da_semana.html" style="color: black;">Aulas</a>
               </li>
             </ul>
           </div>
          </div>
       </nav>
      <p id="wtever"></p>
      <div id="top">
         <div style="font-size: 3.5rem;">{datum['conf']['Pelotao'][0]}°&nbsp;CIA&nbsp;/&nbsp;{datum['conf']['Pelotao'][1]}°&nbsp;PEL</div>

         <div><p style="font-size: 1.25rem;">COMCIA: {datum['conf']['comcia']}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  
                  COMPEL: {datum['conf']['compel']}&nbsp;</p></div>
      </div>
      <div id="counter">
         <span id="contador" style="font-size: 2rem;">0</span>
         <p>/30</p>
      </div>
      <div style="align-content: center;">
         <div>
            <div class="card" style="width: 33.33%;">
               <ul class="list-group list-group-flush">"""
   css = """body {
   background-color: #198754;
   font-size: 15px;
   font-family: Montserrat;
}
.card {
   float: left;
}
span {
   font-size: 2rem;
   padding-left: 4px;
}
#counter {
   width: 100%;
   display: flex;
   justify-content: center;
}
#top {
   width: 100%;
   text-align: center;
}
.form-check-input:checked {
   background-color: #0d6e0d;
   border-color: #0d6e0d;
}\n"""
   aluno = 0
   aluno_por_coluna = 10
   alunos = list(data.keys())
   funcois = list(data.values())
   if len(alunos) != len(funcois):
      raise Exception("a quantidade de alunos é diferente da quantidade de funcois")
   ids = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac','ad']
   while aluno < len(alunos):
      #print("aluno:{} aluno_por_coluna:{} ..... {}".format(aluno+1,aluno_por_coluna,aluno % aluno_por_coluna))
      if aluno +1 in q1:
         html += "<li class=\"list-group-item pq\"><div class=\"form-check\" draggable=\"true\" ondrop=\"drop(event)\" ondragover=\"allowDrop(event)\"><input class=\"form-check-input\" type=\"checkbox\" value=\"0\" id=\"{}\" onclick=\"toggle_count()\"><label class=\"form-check-label\" for=\"flexCheckDefault\">{}".format(ids[aluno],alunos[aluno])
      else:
         html += "<li class=\"list-group-item sq\"><div class=\"form-check\" draggable=\"true\" ondrop=\"drop(event)\" ondragover=\"allowDrop(event)\"><input class=\"form-check-input\" type=\"checkbox\" value=\"0\" id=\"{}\" onclick=\"toggle_count()\"><label class=\"form-check-label\" for=\"flexCheckDefault\">{}".format(ids[aluno],alunos[aluno])
      
      if aluno == datum["conf"]["Xerife"] -1:
         html += "<span id=\"tag{}\" style=\"margin-left: 3px;\" class=\"badge rounded-pill bg-primary\" draggable=\"true\" ondragstart=\"drag(event)\">Xerife</span>".format(tagcounter)
         tagcounter += 1
      for c in funcois[aluno]:
         html += "<span id=\"tag{}\" style=\"margin-left: 3px;\" class=\"badge rounded-pill bg-secondary\" draggable=\"true\" ondragstart=\"drag(event)\">{}</span>".format(tagcounter, c)
         tagcounter += 1
      
      html += """</label>
                     </div>
                  </li>"""
      aluno += 1
      if 0 != aluno and aluno % aluno_por_coluna == 0:
            #print('proxima coluna')
            html += """</ul>
               </div>
               <div class="card" style="width: 33.33%;">
                  <ul class="list-group list-group-flush">"""

   html += """         </div>
      </div>
      </div>
      <button type="button" class="btn btn-danger" onclick="disable_all()">Zerar</button><button type="button" class="btn btn-primary" onclick="enable_all()">Completo</button><button type="button" class="btn btn-warning" onclick="switch_all()">Trocar</button>
      <script>
         toggle_count();
      </script>
   </body>
</html>"""
   
   if (data_to_int(dd, mm)%4) == 0:
      #Dia do 1° Qrt
      css += """.pq{
      color: green;
      background-color: #fff;
   }
   .sq{
      background-color: #fff;
   }"""
   elif (data_to_int(dd, mm)%4) == 1:
      #Dia do 2° Qrt"
      css += """.pq{
      background-color: #fff;
   }
   .sq{
      color: green;
      background-color: #fff;
   }"""
   

   ## DSA
   #import aula



   with open("code/alunos.json", encoding="UTF-8") as f:
      datum = load(f)
   data = datum["alunos"]
   ## Data ##
   agora = dt.datetime.today()
   aa = agora.year
   mm = agora.month
   dd = agora.day

   #slp(10)
   with open("index.html", "w", encoding="UTF-8") as f:
      f.write(html)
   with open("_style.css", "w", encoding="UTF-8") as f:
      f.write(css)

   break

## service

hostName = "localhost"
serverPort = 8080
def get_page(page):
   with open(f'{page}.html', encoding="UTF-8") as f:
      return f.read()

class MyServer(http.server.SimpleHTTPRequestHandler):
   def do_GET(self):
      print(self.path)
      if self.path == "/":
         self.send_response(200)
         self.send_header("Content-type", "text/html")
         self.end_headers()
         self.wfile.write(bytes(html, "utf-8"))
      else:
         return http.server.SimpleHTTPRequestHandler.do_GET(self)



if __name__ == "__main__":        
   webServer = HTTPServer((hostName, serverPort), MyServer)
   print("Server started http://%s:%s" % (hostName, serverPort))

   try:
      webServer.serve_forever()
   except KeyboardInterrupt:
      pass

   webServer.server_close()
