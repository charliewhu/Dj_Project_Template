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
* Ruff (formatter) ✅
* Pyright (types) ✅
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

// OPTIONAL: install dependencies locally
// this is only required for module intellisense to work
poetry install

// run type check
docker-compose run type_check

// run unit tests
docker-compose run unit_test

// run e2e tests
docker-compose run e2e_test

// run server
docker-compose up

// run nginx server
docker-compose -f docker-compose.prod.yaml up
```
