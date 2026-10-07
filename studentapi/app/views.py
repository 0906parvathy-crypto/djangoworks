from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse

class Studentdetails(View):
    def get(self,request):
        data={'name':'Amal','age':23,'course':'Python'}
        return JsonResponse(data)    #sends response as json data

class StudentList(View):
    def get(self,request):

        data=[
            {'name':'Amal','age':23,'course':'python','mark':76},
            {'name':'Anu','age':24,'course':'python','mark':78},
            {'name':'Arun','age':22,'course':'Java','mark':80}
            ]
        return JsonResponse(data,safe=False)




