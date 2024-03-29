from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from frontend import models
import datetime
import tejapi
import requests
import sys


def index(request, path='/'):
    # addData()
    return render(request, 'frontend/index.html')


def getRealEstate(request, times):
    indexStart = 25
    data = models.RealEstate.objects.all(
    )[indexStart * times: indexStart * (1 + times)]
    qs_json = serializers.serialize('json', data)
    return HttpResponse(qs_json, content_type='application/json')


def getColumnDescription(request):
    data = models.ColumnDescription.objects.all()
    qs_json = serializers.serialize('json', data)
    return HttpResponse(qs_json, content_type='application/json')


def getTotalValue(request):
    data = models.TotalValue.objects.all()
    qs_json = serializers.serialize('json', data)
    return HttpResponse(qs_json, content_type='application/json')


def addData():
    models.RealEstate.objects.all().delete()
    models.TotalValue.objects.all().delete()
    print('start get data')
    tejapi.ApiConfig.api_key = "wEjs7c3GMsT9xT7uIcsciNWIlgUjHQ"
    data = tejapi.get('TRAIL/TAAPRTRAN', paginate=True)
    print('end get data')
    data = data.dropna()
    # data.reset_index(inplace=True)

    print('start sql')
    for index, row in data.iterrows():
        # # print('sql ' + str(index))
        sys.stdout.write('\r')
        step = index / len(data.index) * 100
        sys.stdout.write("[%-50s] %.2f%%" % ('.'*int(step / 2), step))
        sys.stdout.flush()
        tmp = {}
        for column in data.columns:
            tmp[column] = row[column]

        tmp['caseID'] = tmp.pop('key3')
        tmp['cotID'] = tmp.pop('coid')
        tmp['districtID'] = tmp.pop('district_id')
        tmp['tranType'] = tmp.pop('tran_tp')
        sql = models.RealEstate(**tmp)
        sql.save()

    d = []
    for t in list(set(list(data['mdate']))):
        d.append(str(t).split('-')[0] + "-" + str(t).split('-')[1])
    d = list(sorted(list(set(d))))
    data['mdate'].apply(lambda t: str(t).split(
        '-')[0] + "-" + str(t).split('-')[1])
    for date in d:
        df = data[data['mdate'] == date]
        sql = models.TotalValue(
            date=date, price=df['tot_prc'].sum(), total=len(df.index))
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
