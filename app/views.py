from django.http import HttpResponse
import datetime
from rest_framework import mixins, viewsets, views
from rest_framework.templatetags.rest_framework import data
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView  # for api
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.core.files import File
from .models import Voter
from rest_framework.views import APIView
from django.core import serializers

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)

class GetVoters(views.APIView):

    def get(self,request):

        state = request.query_params.get('state')
        state = state.lower() + '_db'
        limit = int(request.query_params.get('limit'))
        name = request.query_params.get('name')
        query=''
        if name !=None:
            query+='name__iexact=name'

        gender = request.query_params.get('gender')
        if gender !=None:
            query+=',gender__iexact=gender'
        print(query)

        # ac_no = int(request.query_params.get('ac_no'))

        # if query=='':
        #     data = serializers.serialize("json", Voter.objects.using(state).all()[:limit])
        # else:
        #     data = serializers.serialize("json", Voter.objects.using(state).filter(query)[:limit])

        data = serializers.serialize("json", Voter.objects.using(state).filter(name__iexact=name,gender__iexact=gender)[:limit])


        # print(data)

        return Response({'status': 'Success', 'data': data}, status=200)

