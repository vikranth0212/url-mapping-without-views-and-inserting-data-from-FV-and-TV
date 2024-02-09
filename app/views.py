from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse


# Create your views here.
class Templateview(TemplateView):
    template_name='cbt.html'

    #it is an object method since it doesnt have any decorator
    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Vikranth'
        ECDO['age']='10000'
        return ECDO

class InsertSchoolByTV(TemplateView):
    template_name='InsertSchoolByTV.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['SFO']=SchoolForm
        return ECDO
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByTV is done')

class InsertSchoolByFV(FormView):
    template_name='InsertSchoolByFV.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('InsertSchoolByFV is done')
