from django.shortcuts import render
from .models import Login
from django.db import connection


# Create your views here.

def index(request):
    html_file = 'eclinic/index.html'
    return render(request, html_file)
    return render(request, html_file)


def modules(request):
    if request.method == 'POST':

        username_from_temp = request.POST.get('username')
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
            html_file = 'eclinic/login_error.html'
            return render(request, html_file, )
