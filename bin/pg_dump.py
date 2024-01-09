#!/usr/bin/env python3
"""
Usage, in `crontab -e`:

    @daily /home/ubuntu/ai4media-bench-develop/bin/pg_dump.py

"""
import time

from subprocess import call

dump_name = time.strftime("%Y-%m-%d_%H-%M-%S.dump")

print(f"Making dump {dump_name}")

# Make dump
call([
    'docker',
    'exec',
    'ai4media-bench-prod-db-1',
    'bash',
    '-c',
    f'PGPASSWORD=$DB_PASSWORD pg_dump -Fc -U $DB_USERNAME $DB_NAME > /app/backups/{dump_name}'
])

# Push/destroy dump
call([
    'docker', 'exec', 'ai4media-bench-prod-django-1', 'python', 'manage.py', 'upload_backup', f'{dump_name}'
])
