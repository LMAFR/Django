from django.shortcuts import render
from first_app.models import Webpage, Topic, AccessRecord
# Create your views here.

def add_db_table(request):

    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_record":webpages_list}
    return render(request,"third_app/table_db.html",context=date_dict)