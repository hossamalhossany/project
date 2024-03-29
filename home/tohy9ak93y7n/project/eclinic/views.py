from django.shortcuts import render, HttpResponse
from .models import Login
from django.db import connection


# Create your views here.

def index(request):
    html_file = 'eclinic/index.html'
    return render(request, html_file)



def modules(request):
    if request.method == 'POST':

        username_from_temp = str(request.POST.get('username')).strip().lower()
        password_from_temp = request.POST.get('password')

        # get data from table
        with connection.cursor() as cursor:
            sql = ''' select username, password from project_db.eclinic_login  '''
            cursor.execute(sql)
            rows = cursor.fetchall()
        # end of ==> get data from table

        # convert rows from tuple to dictionary
        data_from_table = dict(rows)

        if username_from_temp in data_from_table and password_from_temp in data_from_table.values():
            html_file = 'eclinic/modules.html'
            return render(request, html_file, )
        else:
            data = {'error': 'error'}
            html_file = 'eclinic/index.html'
            return render(request, html_file, data)


def search_patient_data(request):
    if request.method == 'POST':
        data_from_search_box = str(request.POST.get('search_patient')).strip().lower()

        # get data from table
        with connection.cursor() as cursor:
            sql = ''' select patient_name from project_db.eclinic_patient_data '''
            cursor.execute(sql)
            rows =cursor.fetchall()
        # end of === > get data from table

        data_from_table = dict(rows)
        data = {'error_key': 'error_value'}

        if data_from_search_box in data_from_table.values():
            html_file = 'eclinic/search_patient.html'
            return render(request, html_file,data)
        else:
            data = {'error_key': 'error_value'}
            html_file = 'eclinic/search_patient.html'
            return render(request, html_file, data)






def search_patient(request):
    html_file = 'eclinic/search_patient.html'
    return render(request, html_file,)




def clinic(request):
    html_file = 'eclinic/clinic.html'
    return render(request, html_file, )

