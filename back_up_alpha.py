import os
import requests
import datetime

BACK_DIR = os.path.dirname(os.path.abspath(__file__))
ODOO_DATABASE = 'yourdbnamewhichyouwanttobackup'
ADMIN_PASSWORD = 'yourdbpassword'

date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
url = 'http://localhost:8069/web/database/backup'
data = {'master_pwd': ADMIN_PASSWORD, 'name': ODOO_DATABASE,'backup_format': 'zip'}

response = requests.post(url, data=data)

with open(os.path.join(BACK_DIR, date + '_' + ODOO_DATABASE + '.zip'), 'wb') as f:
    f.write(response.content)

print('Backup created successfully')
print(response.status_code)


