  #!/usr/bin/python
  # -*- coding: utf-8 -*-
import datetime
import json
#Para limpiar el json general obtenido del repositorio



fname = raw_input("Enter a file name: ")
if ( len(fname) < 1 ) : fname = '../data/bl.json'

fh = open(fname)
stringdata=fh.read()
#print stringdata
#news=dict(stringdata)

fh=open('blnodes.json', "w")

#path=nodes['rounds']
#print nodes
index=0

# for element in news:
news=stringdata.replace('team1', 'teamHome')
stringdata=news
news=stringdata.replace('score1', 'goalsHome')
stringdata=news
news=stringdata.replace('team2', 'teamAway')
stringdata=news
news=stringdata.replace('score2', 'goalsAway')


fh.write(news)
	
fh.close()
fh=open('nodes.json', "w")
fh.write('[\n{\n')
with open('blnodes.json') as datafile:
	data=json.load(datafile)
	index=0
	count=0	
	day=0
	for i in range(0, 34):
		
		rounds=data['rounds']
		matches=data['rounds'][i]
		day+=1
		for x in range(0,9):
			fecha=data['rounds'][i]['matches'][x]['date']
			newdate=datetime.datetime.strptime(fecha, '%Y-%m-%d').strftime('%d/%m/%y')
			fecha=newdate
			equipolocal=data['rounds'][i]['matches'][x]['teamHome']['name']
			equipovisitante=data['rounds'][i]['matches'][x]['teamAway']['name']
			goleslocal=data['rounds'][i]['matches'][x]['goalsHome']
			golesvisitante=data['rounds'][i]['matches'][x]['goalsAway']
			x+=1
			count+=1
			id=count
			print fecha, equipolocal, equipovisitante,goleslocal,golesvisitante, id
			fh.write('"id":'+str(count)+',\n"teamAway": "'+equipovisitante+'",\n"goalsAway": "'+str(golesvisitante)+'",\n"teamHome": "'
				+equipolocal+'",\n"day": '+str(day)+',\n"date": "'+fecha+'",\n"goalsHome": "'+str(goleslocal)+'"\n},\n{')
		#   

		
	
# 	for i in range(1, len(rounds)):

# 		partidos=data['rounds'][i]['matches'] 	
# 		fecha= 

# 		for partido in partidos:
			
# 		 	
# 			i+=1
	

# fh.write(nuevo)
fh.close()
	
