export SECRET_KEY=thisissecret
export UI_SECRET=thisissecret
export DEBUG=True
export DATABASE_URL=postgres://datahub:password@docker:5432/datahub
export ES_HOST=docker
export ES_PORT=9200
pushd ../leeloo-api
source env/bin/activate
python manage.py flush --noinput
python manage.py drop_index
