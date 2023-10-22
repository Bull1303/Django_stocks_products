#!bin/bash
cd home/denis/Django_stocks_products
git pull origin main
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
sudo systemctl restart gunicorn
