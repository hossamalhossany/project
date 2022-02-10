from django.shortcuts import render
from .models import Login
from django.db import connection


# Create your views here.

def index(request):
    html_file = 'eclinic/index.html'
    return render(request, html_file)
    return render(request, html_file)


def modules(request):
    # get data from table
    with connection.cursor() as cursor:
        sql = ''' select username, password from project_db.eclinic_login  '''
        cursor.execute(sql)
        rows = cursor.fetchall()

    # end of ==> get data from table

    # if request.method == 'POST':
    #     data = Login(request.POST)
    #
    #     if data.is_valid():
    #         pass

    data_from_table = dict(rows)

    username_from_temp = request.POST.get('username')
    password_from_temp = request.POST.get('password')

    if username_from_temp in data_from_table and password_from_temp in data_from_table.values():
        result = {'ok': 'ok'}
    else:
        result = {'user name or password NOT Correct': 'user name or password NOT Correct'}

    data_from_temp_2 = {username_from_temp: password_from_temp}

    html_file = 'eclinic/modules.html'
    return render(request, html_file,
                  {'data_from_table': data_from_table, 'data_from_temp_2': data_from_temp_2, 'result': result})
