import telnetlib

print('Leyendo archivo...')
archivo = open('ips.txt', "r")
lineas = []
for linea in archivo:
    lineas.append(linea)
archivo.close()

concentradoList = [s.rstrip('\n') for s in lineas]

ipList = []
portList = []
for ip in concentradoList:
     ipList.append(ip.split(" ")[0])
     portList.append(ip.split(" ")[1])

conexiones = {}

print('Haciendo conexiones...')
for i in range(len(ipList)):
     try:
          conexiones[ipList[i], portList[i]] = isinstance(telnetlib.Telnet(ipList[i], portList[i], .01), telnetlib.Telnet)
     except:
          conexiones[ipList[i], portList[i]] = False

print('Generando archivo...')
fic = open("ips_conexion.txt", "w")
for key in conexiones:
     linea = ' : '.join(key) + ' -> ' + str(conexiones[key])
     fic.write(linea)
     fic.write("\n")
    
fic.close()

print('Script terminado!')