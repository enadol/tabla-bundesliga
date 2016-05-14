import datetime
import json

#Para convertir el json original en otro con la estructura y los nombres de variables requeridos


#File a buscar
fname = raw_input("Enter a file name: ")
#el file del json original
if ( len(fname) < 1 ) : fname = '../data/bl.json'
#leer el file
fh = open(fname)
#los datos como string
stringdata=fh.read()

#abrir otro file en blanco para escribir
fh=open('blnodes.json', "w")
#para los id's
#reemplazar en modo string los nombres de variables
news=stringdata.replace('team1', 'teamHome')
#el nuevo contenido se actualiza y se guarda tres veces más
stringdata=news
news=stringdata.replace('score1', 'goalsHome')
stringdata=news
news=stringdata.replace('team2', 'teamAway')
stringdata=news
news=stringdata.replace('score2', 'goalsAway')
#se guarda todo el nuevo contenido
#falta cambiar la estructura

fh.write(news)
#cerrar el primer file
fh.close()

#hoja ne blanco para otro nuevo file con la estructura requerida
fh=open('nodes.json', "w")
#primeros brackets, etc
fh.write('[\n{\n')
#se abre en modo read el viejo file actualizado
with open('blnodes.json') as datafile:
	data=json.load(datafile)
	#count para los id
	count=0	
	#day paa las jornadas
	day=0
	#por cada jornada...
	for i in range(0, 34):
		#dónde están losdatos de jornada
		rounds=data['rounds']
		matches=data['rounds'][i]
		day+=1
		#por cada juego...
		for x in range(0,9):
			#dónde están los datos de partido
			fecha=data['rounds'][i]['matches'][x]['date']
			newdate=datetime.datetime.strptime(fecha, '%Y-%m-%d').strftime('%d/%m/%y')
			#se actualiza por juego para diferenciar fechas de viernes, sábado o domingo
			fecha=newdate
			equipolocal=data['rounds'][i]['matches'][x]['teamHome']['name']
			equipovisitante=data['rounds'][i]['matches'][x]['teamAway']['name']
			goleslocal=data['rounds'][i]['matches'][x]['goalsHome']
			golesvisitante=data['rounds'][i]['matches'][x]['goalsAway']
			#para cada partido
			x+=1
			#para los ids
			count+=1
			id=count
			#se escribe cada partido en la nueva estructura asumiendo los datos nuevos
			print fecha, equipolocal, equipovisitante,goleslocal,golesvisitante, id
			fh.write('"id":'+str(count)+',\n"teamAway": "'+equipovisitante+'",\n"goalsAway": "'+str(golesvisitante)+'",\n"teamHome": "'
				+equipolocal+'",\n"day": '+str(day)+',\n"date": "'+fecha+'",\n"goalsHome": "'+str(goleslocal)+'"\n},\n{')
#TODO- al final hay que ajustar el último bracket para que se valide el json
#se cierra el file
fh.close()
	
