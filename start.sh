#________________
#
#  WEBHOST EGG
#  START SCRIPT
#
# samuel9221991
#________________



echo "[/] Loading website"


usando_dominio=none

if [ '${usando_dominio}' != none ]; then
echo "[/] Loading website with domain"
curl -I http://sd-1.supercores.xyz:4444/api/158.69.225.151/'${server.build.default.port}'/'${usando_dominio}'

else
echo "[-] Loading website without domain"
fi

rm -rf /home/container/tmp/*


echo "[/] Starting PHP"
/usr/sbin/php-fpm8 --fpm-config /home/container/php-fpm/php-fpm.conf --daemonize


echo "[/] Starting Nginx"
echo "[+] Successfully started all packages"
/usr/sbin/nginx -c /home/container/nginx/nginx.conf -p /home/container/
