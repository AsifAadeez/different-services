from django.shortcuts import render 
from demo.models import Category,Category_details,Service


def home(request):
	obj = Category_details.objects.all()
	return render(request,'home.html', {'obj':obj})
	
def service(request,id):
	s = Category.objects.get(category_id = id)
	o = Category_details.objects.get(cat = s)
	details = Service.objects.filter(cat_id = o)
	return render(request,'detail.html',{"details":details})