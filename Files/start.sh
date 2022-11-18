#________________
#
#  WEBHOST EGG
#  START SCRIPT
#
# samuel9221991
#________________



echo ""
echo "[/] Loading website"
echo ""
rm -rf /home/container/tmp/*


echo "[/] Starting PHP"
/usr/sbin/php-fpm8 --fpm-config /home/container/php-fpm/php-fpm.conf --daemonize


echo "[/] Starting Nginx"
echo "[+] Successfully started all packages"
/usr/sbin/nginx -c /home/container/nginx/nginx.conf -p /home/container/
