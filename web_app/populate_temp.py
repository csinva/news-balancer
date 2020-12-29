import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django
from myproject.myapp.models import Document

print("done populating...")
for name in ["test1", "test2", "test3"]:
    d = Document(title=name)
    d.save()
