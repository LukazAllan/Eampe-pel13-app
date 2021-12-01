from re import split
import pdfplumber
import pandas as pd
import json
pdf = pdfplumber.open("dsa.pdf")
first_page = pdf.pages[2]
table = first_page.extract_table()
table_df = pd.DataFrame(table[1:],columns=table[0])
table_df.to_json(orient="values")
tabela = json.loads(table_df.to_json(orient="values"))

#for c in range(len(tabela)):
	#print(c, tabela[c], end="\n\n")

aula_html = """<!DOCTYPE html>\n<html>
	<head>
		<meta charset="utf-8">
		<title>Aulas do Dia</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="_bootstrap.min.css" rel="stylesheet">
		<script src="_bootstrap.min.js"></script>
		<script src="_popper.min.js"></script>
		<script src="_bootstrap.bundle.min.js"></script>
		<style type="text/css">
		body {
			font-family: Montserrat;
		}
		h1 { font-size: 1rem; }
		h2 { font-size: 0.75rem; }
		p { font-size: 0.75rem; }
	</style>
    <script src="drag.js"></script>
	</head>
	<body>
		<nav class="navbar navbar-expand-lg fixed-bottom navbar-light bg-light">
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
                <a class="nav-link active" aria-current="page" href="index.html" style="color: black;">Presença</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#" style="color: black;">Aulas</a>
              </li>
            </ul>
          </div>
         </div>
		</nav>
		<div style="height: 50px"></div>
		<table class="table">
			<thead>
				<tr>
					<th scope="row">Hora</th>
					"""

jason = []
dias = tabela[3][2:]
for c in dias:
    aula_html += f"<th scope=\"row\">{c}</th>\n\t\t\t\t\t"


aula_html += """				</tr>
			</thead>
			<tbody>
				"""
hora = [
	[7,8],
	[9,10],
	0,
	[11,12],
	[13,14],
	0,
	[15,16],
	[17,18],
	1,
	[20,21],
	0,
	[22,23],
	[24,25],
	[26,27],
	[28,29]
]
mid = [ '08:40 ÀS 08:45', '10:15 ÀS 10:30', '12:00 ÀS 13:00', '14:50 ÀS 15:00']
cont_mid = 0
tag_counter = 0
for c in range(len(hora)):
	if type(hora[c]) == list:
		horario = tabela[hora[c][0]][1].replace("\n", " ")
		aula_html += f"""
				<tr>
					<th scope="row">
						<h5 class="card-title">{horario}</h5>
					</th>
					"""
		for b in range(len(tabela[hora[c][1]])):
			if b < 2:
				continue
			else:
				aula = tabela[hora[c][1]][b].split('\n')
				if len(aula) == 3:
					aula_html += f"""<th draggable=\"true\" ondrop=\"drop(event)\" ondragover=\"allowDrop(event)\" scope="row">
						<div id=\"tag{tag_counter}\" draggable="true" ondragstart="drag(event)" class="card text-white bg-primary mb-3">
							<div class="card-body">
								<h1>{aula[0].upper()}</h1>
								<h2>{aula[1].upper()}</h2>
								<p>{aula[2].upper()}<p>
							</div>
						</div>
					</th>\n\t\t\t\t\t"""
					tag_counter += 1
				
				elif len(aula) == 2:
					aula_html += f"""<th draggable=\"true\" ondrop=\"drop(event)\" ondragover=\"allowDrop(event)\" scope="row">
						<div id=\"tag{tag_counter}\" draggable="true" ondragstart="drag(event)" class="card text-white bg-primary mb-3">
							<div class="card-body">
								<h1>{aula[0].upper()}</h1>
								<h2>{aula[1].upper()}</h2>
								<p><p>
							</div>
						</div>
					</th>\n\t\t\t\t\t"""
					tag_counter += 1
				elif len(aula) == 1:
					aula_html += f"""<th draggable=\"true\" ondrop=\"drop(event)\" ondragover=\"allowDrop(event)\" scope="row">
						<div id=\"tag{tag_counter}\" draggable="true" ondragstart="drag(event)" class="card text-white bg-primary mb-3">
							<div class="card-body">
								<h1>{aula[0].upper()}</h1>
								<h2></h2>
								<p><p>
							</div>
						</div>
					</th>\n\t\t\t\t\t"""
					tag_counter += 1
				else:
					raise Exception("PDF Error data: a lot / no argument given")
	else:
		aula_html += f"""
				<tr>
					<th draggable=\"true\" ondrop=\"drop(event)\" ondragover=\"allowDrop(event)\" scope="row">
						<h5 class="card-title">{mid[cont_mid]}</h5>
					</th>
					"""
		if hora[c] == 0:
			aula_html +="""<td colspan="7">
						<div class="card bg-light mb-3">
							<div class="card-body">
								<h1>INTERVALO</h1>
							</div>
						</div>
					</td>\n\t\t\t\t\t"""
		else:
			aula_html +="""<td colspan="7">
						<div class="card bg-light mb-3">
							<div class="card-body">
								<h1>ALMOÇO</h1>
							</div>
						</div>
					</td>\n\t\t\t\t\t"""
		cont_mid += 1
	aula_html += """</tr>\n\t\t\t\t\t"""

	with open("aula_da_semana.html", 'w', encoding='utf-8') as f:
		f.write(aula_html)