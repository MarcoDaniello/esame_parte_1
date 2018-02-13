carburanteg = raw_input ('Inserisci la quantita di carburante (in galloni) ')
carburante = float(carburanteg)
consumoorarioh = raw_input('Inserisci il consumo orario ')
consumoorario = float(consumoorarioh)

if carburante<0:
   
   print ('Senza carburante non vai da nessuna parte')

elif consumoorario <= 0:
   
   print ('Inserire un valore positivo')

else:
  
   tempovolo = carburante/consumoorario 
   ore = int (tempovolo)
   
   tempovolo = tempovolo - ore
   tempovolo = tempovolo * 60
   
   minuti = int (tempovolo)
   tempovolo = tempovolo - minuti
   tempovolo = tempovolo * 60

   secondi = int (tempovolo)
   
   print ('Durata massima del volo :'),('h'),ore,('min'),minuti,('sec'),secondi


