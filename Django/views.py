from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("About Us Page")


def course(request):
    return HttpResponse("Contact Page")

def coursedetail(request, courseid):
    return HttpResponse(courseid)

def homePage(request):
    # data = {
    #     'title': 'Harsh Thapa',
    #     'content': 'Welcome to My Website',
    #     'clist': ['PHP', 'Java', 'Python'],
    #     'clist2': ['Python', 'Java', 'C++'],
    #     'clist3': ['Swift', 'Kotlin', 'React native'],
    #     'details': [{'name': 'harsh', 'phone': 9321971947},
    #                 {'name': 'rohit', 'phone': 8108889047}
    #                 ],
    # }
    return render(request, "index.html")
