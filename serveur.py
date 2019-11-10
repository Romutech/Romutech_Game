import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    msg_recu = msg_recu.decode()
    print(msg_recu)
    text = "Le serveur a recu le message : " + msg_recu 
    text = text.encode()
    connexion_avec_client.send(text)

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
