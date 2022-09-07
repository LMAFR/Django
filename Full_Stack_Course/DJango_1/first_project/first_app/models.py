from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self) -> str:
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    # It is usual to add a string representation of our models:
    def __str__(self) -> str:
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        # It can only return strings, so we will convert the date into a string in the return line
        return str(self.date)

# Commands to save (migrate) models:
# python project_path/manage.py migrate
# python project_path/manage.py makemigrations app_w_models_name
# python project_path/manage.py migrate

# Some tests you can do directly in the python shell to check the migration was successful:
# python project_path/manage.py shell
# print("test_message")
# from app_name.models import a_model
# print(a_model.objects.all())
# t = a_model(column=new_data)
# t.save()
# print(a_model.objects.all())