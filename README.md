Project on django

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver 
   ```
   
4. Run [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```bash
   redis-server
   ```
   
5. Run Celery:
   ```bash
   celery -A store worker --loglevel=INFO
   ```

## Functional:️
- SSO authorization (GitHub).
- Personal cabinet. 
- Shopping cart. With connected payment system Stripe. History of orders.
- Caching in Redis.
- Pending tasks in Celery (sending email upon registration).
- PostgreSQL.
