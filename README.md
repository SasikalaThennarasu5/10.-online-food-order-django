# Foodie - Online Food Ordering System (Django)

This is a ready-to-use Django project scaffold for an Online Food Ordering System.
Stack: Python, Django, SQLite, Bootstrap (via CDN).

Project name: **foodie**
App name: **orders**

What is included:
- Django project files (manage.py, settings, urls)
- `orders` app with models, views, templates, static CSS
- Sample templates: home, menu, cart, checkout, restaurant dashboard
- `requirements.txt`
- `fixtures/sample_menu.json` to load sample menu items

Notes:
- To run locally:
  1. Create a virtualenv and `pip install -r requirements.txt`
  2. `python manage.py migrate`
  3. `python manage.py loaddata fixtures/sample_menu.json`
  4. `python manage.py runserver`
- This scaffold uses Bootstrap via CDN and simple SQLite DB.

