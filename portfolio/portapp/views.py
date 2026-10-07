from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
class Developerdetails(View):
    def get(self, request):
        data={'id':12,'full_name':'Anoop','title':'trainee','DOB':'12-09-2003',
          'email':"anoop@gmail.com",'contact':'23456788','location':'ekm',
          'github_url':'http://github.com/anoop',
          'linkedin-url':'https://www.linkedin.com/in/anoop'}
        return JsonResponse(data)

class Education(View):
    def get(self,request):
        data={'id':13,'Institution':'MCET','Course':'BTech','University':'KTU',
              'Location':'PTA','Start_year':2022,'End_year':2026,'Grade':'A',
              'Discription':'Bachelors Degree in Computer Science'}
        return JsonResponse(data)

class Project(View):
        def get(self,request):
            data=[


                {'id':1,'name': 'Portfolio Website',
                 'description': 'A personal portfolio website.',
                 'technologies': 'HTML, CSS, JavaScript','duration': '2 months',
                 'liveurl': 'https://example.com'},

               {'id': 2,
               'name':'E-Commerce Website',
                'description': 'An online shopping website.',
               'technologies': 'Python, Django, MySQL',
               'duration': '3 months',
               'liveurl': 'https://example.com'},


               {'id': 3,
                'name': 'Student Management System',
                'description': 'A system to manage student records.',
                'technologies': 'Python, Django',
                'duration': '2 months',
                'liveurl': 'https://example.com'}

            ]
            return JsonResponse(data,safe=False)