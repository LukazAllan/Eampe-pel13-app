#Janeiro:   31 dias, do dia número   1 ao dia número  31.
#Fevereiro: 28 dias, do dia número  32 ao dia número  59.
#Março:     31 dias, do dia número  60 ao dia número  90. 
#Abril:     30 dias, do dia número  91 ao dia número 120.
#Maio:      31 dias, do dia número 121 ao dia número 151.
#Junho:     30 dias, do dia número 152 ao dia número 181.
#Julho:     31 dias, do dia número 182 ao dia número 212.
#Agosto:    31 dias, do dia número 213 ao dia número 243.
#Setembro:  30 dias, do dia número 244 ao dia número 273.
#Outubro:   31 dias, do dia número 274 ao dia número 304.
#Novembro:  30 dias, do dia número 305 ao dia número 334.
#Dezembro:  31 dias, do dia número 335 ao dia número 365.

def int_to_data(i:int):
	i %= 365
	# 1 == 01/01/XX
	# 2 == 02/01/XX
	
	normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
	month = 1
	for c in normal_year:
		if i > c:
			i -= c
			month += 1
			continue
		else:
			break
	if i < 10:
		if month < 10:
			return f'0{i}/0{month}'
		else:
			return f'0{i}/{month}'
	else:

		if month < 10:
			return f'{i}/0{month}'
		else:
			return f'{i}/{month}'

def datastr_to_int(d:str):
	# 1 == 01/01/XX
	# 2 == 02/01/XX
	#Janeiro:   31 dias, do dia número   1 ao dia número  31.
    #Fevereiro: 28 dias, do dia número  32 ao dia número  59.
    #Março:     31 dias, do dia número  60 ao dia número  90. 
    #Abril:     30 dias, do dia número  91 ao dia número 120.
    #Maio:      31 dias, do dia número 121 ao dia número 151.
    #Junho:     30 dias, do dia número 152 ao dia número 181.
    #Julho:     31 dias, do dia número 182 ao dia número 212.
    #Agosto:    31 dias, do dia número 213 ao dia número 243.
    #Setembro:  30 dias, do dia número 244 ao dia número 273.
    #Outubro:   31 dias, do dia número 274 ao dia número 304.
    #Novembro:  30 dias, do dia número 305 ao dia número 334.
    #Dezembro:  31 dias, do dia número 335 ao dia número 365.
	print(d[:2], d[3:5])
	dd, mm = int(d[:2]), int(d[3:5])
	normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
	i = dd
	for c in range(mm - 1):
		i += normal_year[c]
	
	return i

def data_to_int(d:int, m:int):
   normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
   i = d
   for c in range(m - 1):
      i += normal_year[c]
   
   return i


for c in range(5, 15):
	if (data_to_int(c, 9)%4) == 0:
		print(f"{c}/9 - Dia do 1° Qrt")
	elif (data_to_int(c, 9)%4) == 1:
		print(f"{c}/9 - Dia do 2° Qrt")
	elif (data_to_int(c, 9)%4) == 2:
		print(f"{c}/9 - Dia do 3° Qrt")
	else:
		print(f"{c}/9 - Dia do 4° Qrt")
