run-dev:
	FLASK_APP=app.py \
	FLASK_ENV=development \
	flask run

run:
	FLASK_APP=app.py \
	flask run

test:
	pytest