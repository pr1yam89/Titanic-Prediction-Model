from django.shortcuts import render
from urllib import response
from .apps import PredictionConfig
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'base.html')

def about(request):
    return render(request,"about.html")

def predict(request):
        Pclass = request.POST.get('Pclass')
        Sex = request.POST.get('Sex')
        Age = request.POST.get('Age')
        Sibsp = request.POST.get('Sibsp')
        Parch = request.POST.get('Parch')
        Fare = request.POST.get('Fare')
        Embarked = request.POST.get('Embarked')
        Title = request.POST.get('Title')

        data = [Pclass,Sex,Age,Sibsp,Parch,Fare,Embarked, Title]
        
        prediction = PredictionConfig.model.predict([data])[0]
        #prediction = 0
        if prediction == 0:
            prediction = "The passenger will not survive."
        else:
            prediction = "The passenger will survive."
        
        response = {'Passenger_status':prediction}
        return JsonResponse(response)
        