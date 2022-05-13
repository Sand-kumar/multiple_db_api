from django.http import HttpResponse,JsonResponse
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
from .serializer import VoterSerializer
import json

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)

# class GetVoters(views.APIView):
#
#     def get(self,request):
#
#         state = request.query_params.get('state')
#         state = state.lower() + '_db'
#         limit = int(request.query_params.get('limit'))
#
#         name = request.query_params.get('name')
#         ac_no=request.query_params.get('ac_no')
#         gender=request.query_params.get('gender')
#
#         # voters = Voter.object.using(state)
#         #
#         # if name
#         #     voters = voters.filter(name__iexact=name)
#
#         if name==None and ac_no==None and gender==None:
#             data = Voter.objects.using(state).all()[:limit]
#
#         elif name!=None and ac_no!=None and gender!=None:
#             data = Voter.objects.using(state).filter(name__iexact=name, gender__iexact=gender,ac_no=ac_no)[:limit]
#
#         elif name == None and ac_no != None and gender != None:
#             data = Voter.objects.using(state).filter(gender__iexact=gender,ac_no=ac_no)[:limit]
#
#         elif name != None and ac_no == None and gender == None:
#             data = Voter.objects.using(state).filter(name__iexact=name)[:limit]
#
#         elif name == None and ac_no != None and gender == None:
#             data = Voter.objects.using(state).filter(ac_no=ac_no)[:limit]
#
#         elif name == None and ac_no == None and gender != None:
#             data = Voter.objects.using(state).filter(gender__iexact=gender)[:limit]
#
#         elif name != None and ac_no == None and gender != None:
#             data = Voter.objects.using(state).filter(name__iexact=name, gender__iexact=gender)[:limit]
#
#         elif name != None and ac_no != None and gender == None:
#             data = Voter.objects.using(state).filter(name__iexact=name,ac_no=ac_no)[:limit]
#
#         # serializer = VoterSerializer(data)
#         # print(serializer)
#         voters = serializers.serialize("json", data[:limit])
#         # return Response({'status': 'Success', 'data': voters}, status=200)
#         return HttpResponse(voters, content_type='application/json')
#


class GetVoters(views.APIView):

    def get(self,request):

        state = request.query_params.get('state')
        state = state.lower() + '_db'
        limit = int(request.query_params.get('limit'))
        offset=int(request.query_params.get('offset'))

        name = request.query_params.get('name')
        ac_no=request.query_params.get('ac_no')
        gender=request.query_params.get('gender')

        voters =Voter.objects.using(state).all()
        # print(voters)

        if name:
            voters = voters.filter(name__contains=name)

            print('NAME VOTERS')
        if ac_no:
            voters = voters.filter(ac_no=ac_no)
            print('AC_NO VOTERS')

        if gender:
            voters = voters.filter(gender__iexact=gender)
            print('GENDER VOTERS')
            print(voters)

        # voters = serializers.serialize("json", voters[offset:limit+offset])
        # try:
        #     voters = serializers.serialize("json", voters[offset:limit+offset]).values()
        # except:
        #     voters = voters[offset:limit + offset].values()
        #     # voters=serializers.serialize("json", voters)
        #     print('error caught')
        #     print(type(voters))
        #     # voters=json.dumps(voters)
        voters = voters.order_by('s_no')
        print(type(voters))
        voters = voters[offset:limit + offset].values()


        return Response({'message': 'Voter List', 'data': voters}, status=200)

        # return HttpResponse(voters, content_type='application/json')


