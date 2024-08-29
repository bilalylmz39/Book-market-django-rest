start: install release test run

install:
	pip install -U pip && pip install --no-cache-dir -r requirements-dev.txt

release:
	bash release.sh

test:
	python manage.py test --verbosity 2 --keepdb --failfast --settings=core.settings_test
	pytest --verbosity=2 -W ignore::DeprecationWarning -W ignore::PendingDeprecationWarning --exitfirst

lint:
	python -m flake8 . --extend-exclude=env,dist,build,migrations --show-source --statistics

check:
	python manage.py test --verbosity 2 --keepdb --failfast --settings=core.settings_test_pipeline
	pytest --no-migrations --verbosity=2 -c pytest.ini --exitfirst
	flake8 . --extend-exclude=core,env,errors,libs,migrations --show-source --statistics -v

# run:
# 	gunicorn core.wsgi -w 4 -b 0.0.0.0:8008 --max-requests 128 --forwarded-allow-ips='*' --access-logformat='%(t)s %(l)s %(l)s %({X-Forwarded-For}i)s %(l)s %(r)s %(s)s %(b)s %(f)s %(a)s' --access-logfile -