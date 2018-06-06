kill $(netstat -tlnp|grep 2222 |awk  '{print $7}'|awk -F '/' '{print $1}')
/home/coffee/tianyi/py35env/bin/gunicorn  --error-logfile /tmp/market_gunicorn.log  -w 4 --bind 0.0.0.0:2222 market.wsgi:application -D
