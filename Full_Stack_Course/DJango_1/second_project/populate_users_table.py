import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

from users_tag.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        fake_fname = fakegen.name()
        fake_lname = fakegen.name()
        fake_email = fakegen.email()

        users_row = Users.objects.get_or_create(fname = fake_fname, lname = fake_lname, email = fake_email)[0]

if __name__ == "__main__":
    print("populating the users table!")
    populate(30)
    print("users table has been populated!")