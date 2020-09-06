from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm


def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	form = CarForm()
	if request.method == 'POST':
		form = CarForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'You created a car successfully')
			return redirect ('car-list')
	context = {
		 "form" : form
	}
	return render(request, 'car_create.html', context)


def car_update(request, car_id):
	car_obj = Car.objects.get(id=car_id)
	form = CarForm(instance=car_obj)
	if request.method == 'POST':
		form = CarForm(request.POST, request.FILES, instance=car_obj)
		if form.is_valid():
			form.save()
			messages.info(request, 'You updated a car successfully')
			return redirect ('car-detail', car_id=car_obj.id)

	context = {
		"form" : form,
		"car_obj" : car_obj,
	}

	return render(request, 'car_update.html', context)


def car_delete(request, car_id):
	Car.objects.get(id=car_id).delete()
	messages.warning(request, 'You have deleted a car')
	return redirect ('car-list')
