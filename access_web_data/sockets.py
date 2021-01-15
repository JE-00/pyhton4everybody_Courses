import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Prepara la conexión por internet y transferencia de info
mysock.connect(("data.pr4e.org", 80))  # (Host, Port) Conecta al servidor, falla si no existe server

cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()  # Prepara la info a enviar, da dos enter
# .encode() convierte de Unicode (que usa python) a bytes de UTF-8
mysock.send(cmd)  # Envia la info

while True:
    data = mysock.recv(512)  # Recibe 512 caracteres
    if len(data) < 1:  # Si no hay datos significa eof
        break
    print(data.decode())  # Decodifica lo recibido en strings (de bytes de UTF-8 a Unicode) y lo imprime
mysock.close()  # Termina la conexion

# Recibe el metadata de la página con información de lso datos y luego recibe el contenido de la pagina en hypertext
# Lo que recibe se llaman Headers y Response
