from django.contrib import admin
from .models import Movie
from . import models


# Change the order in which attributes of a model are shown in the admin page (by default, they appear from top to bottom 
# in the order in which we created them)

class MovieAdmin(admin.ModelAdmin):
    fields = ["release_year", "title", "length"]
    # The line below adds a search bar where we can insert the data corresponding to any of the attributes of the model 
    # that we have defined in this line:
    search_fields = ["title", "length"]
    # We can also add filters for each field using the line below:
    list_filter = ('release_year', 'length')
    # We can modify the fields that are previsualized in the admin model´s page using the line below (this replaces 
    # the string representation we had previously assigned). This also allow us to order the model database by one 
    # of those fields, clicking in the column:
    list_display = ["title", "release_year", "length"]
    # We can also make attributes to be editable directly from the previsualized table using the line below:
    list_editable = ["length"]
# Register your models here. In this case we add the MovieAdmin model to indicate the order of the Movie model:
admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)