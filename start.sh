#________________
#
#  WEBHOST EGG
#  START SCRIPT
#
# samuel9221991
#________________



cd /mnt/server
apk --update add git
apk --update add certbot


#DESCARGA DE ARCHIVOS
git clone https://github.com/Samuel9221991/Web-Host-Pterodactyl-Egg ./temp
cp -r ./temp/nginx /mnt/server/
cp -r ./temp/php-fpm /mnt/server/
cp -r ./temp/webroot /mnt/server/
cp ./temp/start.sh /mnt/server/
chmod +x /mnt/server/start.sh
rm -rf ./temp


#CREACIÓN DE CARPETAS
mkdir /mnt/server/tmp
mkdir /mnt/server/logs


#________________________
#INSTALACIÓN DE WORDPRESS
#________________________

#SIN WORDPRESS
if [ "${WORDPRESS}" == "false" ] || [ "${WORDPRESS}" == "0" ]; then
echo -e "[-] Installing without WordPress"
fi

#CON WORDPRESS
if [ "${WORDPRESS}" == "true" ] || [ "${WORDPRESS}" == "1" ]; then
echo -e "[/] Installing WordPress"
cd /mnt/server/webroot
wget http://wordpress.org/latest.tar.gz
tar xzf latest.tar.gz
mv wordpress/* .
rm -rf wordpress latest.tar.gz
echo -e "[+] WordPress has been installed"
fi


#___________________________
#INSTALACIÓN CON CERTIFICADO
#___________________________

#SIN SSL
if [ "${SSL}" == "false" ] || [ "${SSL}" == "0" ]; then
echo -e "[-] Installing without SSL"
fi

#CON SSL
if [ "${SSL}" == "true" ] || [ "${SSL}" == "0" ]; then
echo -e "[/] Installing whit SSL"
#certbot certonly --standalone --preferred-challenges  -d ${DOMAIN}
fi


#TERMINAR INSTALACIÓN
echo "[+] WebHost server has been installed"
exit 0
