pushd ../data-hub-backend
docker-compose run leeloo python manage.py flush --noinput
docker-compose run leeloo python manage.py loaddata metadata.yaml
docker-compose exec korben korben sync django
