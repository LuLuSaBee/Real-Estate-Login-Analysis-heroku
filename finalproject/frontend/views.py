from django.shortcuts import render
from frontend import models
import datetime
import tejapi
import requests
import sys


def index(request):
    # addData()
    return render(request, 'frontend/index.html')


def addData():
    models.RealEstate.objects.all().delete()
    print('start get data')
    tejapi.ApiConfig.api_key = "wEjs7c3GMsT9xT7uIcsciNWIlgUjHQ"
    data = tejapi.get('TRAIL/TAAPRTRAN', paginate=True)
    print('end get data')
    data = data.dropna()

    print('start sql')
    for index, row in data.iterrows():
        # print('sql ' + str(index))

        # sys.stdout.write('\r')
        # step = index / len(data.index) * 100
        # sys.stdout.write("[%-20s] %.2f%%" % ('='*int(step / 5), step))
        # sys.stdout.flush()
        # tmp = {}
        # for column in data.columns:
        #     if row[column] != None:
        #         tmp[column] = row[column]

        tmp['caseID'] = tmp.pop('key3')
        tmp['cotID'] = tmp.pop('coid')
        tmp['districtID'] = tmp.pop('district_id')
        tmp['tranType'] = tmp.pop('tran_tp')
        sql = models.RealEstate(**tmp)
        sql.save()

    # url = "https://api.tej.com.tw/api/datatables/TRAIL/TAAPRTRAN.json?api_key=wEjs7c3GMsT9xT7uIcsciNWIlgUjHQ"
    # # models.ColumnDescription.objects.all().delete()

    # payload = {}
    # headers = {}

    # response = requests.request("GET", url, headers=headers, data=payload)

    # columns = response.json()['datatable']['columns']
    # for data in columns:
    #     sql = models.ColumnDescription(
    #         name=data['name'] if data['name'] != 'key3' else "caseID", columnName=data['cname'], description=data['description'], unit=data['unit'])
    #     sql.save()
