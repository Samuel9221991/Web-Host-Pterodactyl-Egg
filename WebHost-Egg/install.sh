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
git clone https://github.com/finnie2006/ptero-nginx ./temp
cp -r ./temp/nginx /mnt/server/
cp -r ./temp/php-fpm /mnt/server/
cp -r ./temp/webroot /mnt/server/
cp ./temp/start.sh /mnt/server/
chmod +x /mnt/server/start.sh
rm -rf ./temp
mkdir /mnt/server/tmp
if [ "${WORDPRESS}" == "false" ] || [ "${WORDPRESS}" == "0" ]; then
echo -e "Install complete go to http://ip:port/"
fi
#wordpress
if [ "${WORDPRESS}" == "true" ] || [ "${WORDPRESS}" == "1" ]; then
echo -e "Installing wordpress"
cd /mnt/server/webroot
wget http://wordpress.org/latest.tar.gz
tar xzf latest.tar.gz
mv wordpress/* .
rm -rf wordpress latest.tar.gz
echo -e "Install complete go to http://ip:port/wp-admin "
exit 0
fi