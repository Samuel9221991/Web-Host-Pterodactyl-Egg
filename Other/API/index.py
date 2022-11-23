import sys
import os
import sqlite3


#_____________________
# CREAR CONFIG
#_____________________



#DB
conn = sqlite3.connect('datos.db')
curs = conn.cursor()

#DESCOMENTAR AL EJECUTAR EL CODIGO POR PRIMERA VEZ
curs.execute('''CREATE TABLE config (id, ip, puerto, dominio)''')
curs.execute(f"INSERT INTO config (id) VALUES ({int(0)})")



#VARIABLES
ip_b = sys.argv[1]
puerto = sys.argv[2]
dominio_b = sys.argv[3]

ip = f"{ip_b}"
dominio = f"{dominio_b}"


#CHEQUEO
curs.execute(f"SELECT * FROM config WHERE dominio = '{dominio}'")
resultadoOne = len(curs.fetchall())
conn.commit()

#MISMA IP MISMO PUERTO MISMO DOMINIO (CAMBIO)
if resultadoOne > 0:

    curs.execute(f"SELECT id FROM config WHERE dominio = '{dominio}' AND ip = '{ip}' AND puerto = {puerto}")
    resultadoTwo = len(curs.fetchall())
    idOne = curs.fetchone()[0]
    conn.commit()

    if resultadoTwo > 0:
        
        #COMANDOS Y CONFIG
        os.system("systemctl stop nginx")
        os.system("systemctl stop iptables")
        os.system(f"certbot certonly --standalone --preferred-challenges http -d {dominio}")

        os.system(f"rm /etc/nginx/sites-available/{idOne}.conf")
        config = open(f"/etc/nginx/sites-available/{idOne}.conf", "w+")


        config.write("server {\n")
        config.write("  listen 80;\n")
        config.write(f" server_name {dominio};\n")
        config.write("  return 301 https://$server_name$request_uri;\n")
        config.write("}\n\n")

        config.write("server {\n")
        config.write("  listen 443 ssl http2;\n\n")
        
        config.write(f" server_name {dominio};\n")
        config.write(f" ssl_certificate /etc/letsencrypt/live/{dominio}/fullchain.pem;\n")
        config.write(f" ssl_certificate_key /etc/letsencrypt/live/{dominio}/privkey.pem;\n")
        config.write("  ssl_session_cache shared:SSL:10m;\n")
        config.write("  ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;\n")
        config.write("  ssl_ciphers  HIGH:!aNULL:!MD5;\n")
        config.write("  ssl_prefer_server_ciphers on;\n\n")

        config.write("  location / {\n")
        config.write(f"     proxy_pass http://{ip}:{puerto}/;\n")
        config.write("      proxy_http_version 1.1;\n")
        config.write("      proxy_set_header Upgrade $http_upgrade;\n")
        config.write("      proxy_set_header Connection 'Upgrade';\n")
        config.write("      proxy_set_header Host $host;\n")
        config.write("      proxy_buffering off;\n")
        config.write("      proxy_set_header X-Real-IP $remote_addr;\n")
        config.write("  }\n")
        config.write("}\n")

        config.close()

        os.system(f"ln -s /etc/nginx/sites-available/{idOne}.conf /etc/nginx/sites-enabled/{idOne}.conf")
        os.system("systemctl start nginx")
        #os.system("systemctl start iptables")

#DOMINIO LIBRE
else:

    curs.execute(f"SELECT * FROM config")
    resultadoTree = len(curs.fetchall())
    conn.commit()

    idTwo = resultadoTree + 1
    curs.execute(f"INSERT INTO config (id, ip, puerto, dominio) VALUES (?,?,?,?)", (int(idTwo), str(ip), int(puerto), str(dominio)))
    conn.commit()


    #COMANDOS Y CONFIG
    os.system("systemctl stop nginx")
    os.system("systemctl stop iptables")
    os.system(f"certbot certonly --standalone --preferred-challenges http -d {dominio}")
    
    config = open(f"/etc/nginx/sites-available/{idTwo}.conf", "w+")


    config.write("server {\n")
    config.write("  listen 80;\n")
    config.write(f" server_name {dominio};\n")
    config.write("  return 301 https://$server_name$request_uri;\n")
    config.write("}\n\n")

    config.write("server {\n")
    config.write("  listen 443 ssl http2;\n\n")
        
    config.write(f" server_name {dominio};\n")
    config.write(f" ssl_certificate /etc/letsencrypt/live/{dominio}/fullchain.pem;\n")
    config.write(f" ssl_certificate_key /etc/letsencrypt/live/{dominio}/privkey.pem;\n")
    config.write("  ssl_session_cache shared:SSL:10m;\n")
    config.write("  ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;\n")
    config.write("  ssl_ciphers  HIGH:!aNULL:!MD5;\n")
    config.write("  ssl_prefer_server_ciphers on;\n\n")

    config.write("  location / {\n")
    config.write(f"     proxy_pass http://{ip}:{puerto}/;\n")
    config.write("      proxy_http_version 1.1;\n")
    config.write("      proxy_set_header Upgrade $http_upgrade;\n")
    config.write("      proxy_set_header Connection 'Upgrade';\n")
    config.write("      proxy_set_header Host $host;\n")
    config.write("      proxy_buffering off;\n")
    config.write("      proxy_set_header X-Real-IP $remote_addr;\n")
    config.write("  }\n")
    config.write("}\n")

    config.close()

    os.system(f"ln -s /etc/nginx/sites-available/{idTwo}.conf /etc/nginx/sites-enabled/{idTwo}.conf")
    os.system("systemctl start nginx")
    #os.system("systemctl start iptables")


