# Django Project Template

Readymade Django project, complete with:
* Poetry ✅
* Gitignore ✅
* Github Actions ✅
* Custom User model ✅
* Folder restructure ✅
* Static setup ✅
* Environs[django] ✅
* Model-Bakery ✅
* Psycopg2 ✅
* Gunicorn ✅
* Dockerfile ✅
* docker-compose ✅
* Nginx ✅
* django-debug-toolbar 🔜
* django-browser-reload 🔜
* widget-tweaks 🔜
* neapolitan 🔜

## Creating a project

```bash
// clone repo
mkdir your_projet_name
cd your_projet_name
git clone https://github.com/charliewhu/Dj_Project_Template.git .

// install dependencies and activate virtual environment
poetry install
source .venv/bin/activate

// run server (using local sqlite3 db)
./manage.py runserver

// run tests 
./manage.py test

// run type checks
mypy .

// run server (docker)
docker-compose up
```

