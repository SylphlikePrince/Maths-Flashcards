from django.shortcuts import render

# Functions

def divisors(number):
	# ld = list[int]
	ld = [1]
	# i = int
	for i in range(2,number):
		if number%i==0:
			ld.append(i)
	return ld

# Create your views here.

def home(request):
	return render(request, 'home.html', {})


def addition(request):
	from random import randint

	num_1 = randint(0,9)
	num_2 = randint(0,9)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if form not filled out
		if not answer:
			my_answer = "Hey! You forgot to fill out the form!"
			colour = "warning"
			return render(request, 'division.html', {
			'my_answer':my_answer,
			'colour':colour,
			'answer':answer,
			'num_1':num_1,
			'num_2':num_2,
			})

		correct_answer = int(old_num_1) + int(old_num_2)
		
		if int(answer) == int(correct_answer):
			my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
			colour = "success"
		else:
			my_answer = "Incorrect! "+ old_num_1 + " + " + old_num_2 + " = " + str(correct_answer)
			colour = "danger"

		return render(request, 'addition.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'colour':colour,
			})
	
	return render(request, 'addition.html', {
		'num_1':num_1,
		'num_2':num_2,
		})


def subtraction(request):
	from random import randint

	num_1 = randint(0,9)
	num_2 = randint(0,9)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if form not filled out
		if not answer:
			my_answer = "Hey! You forgot to fill out the form!"
			colour = "warning"
			return render(request, 'division.html', {
			'my_answer':my_answer,
			'colour':colour,
			'answer':answer,
			'num_1':num_1,
			'num_2':num_2,
			})

		correct_answer = int(old_num_1) - int(old_num_2)
		
		if int(answer) == int(correct_answer):
			my_answer = "Correct! " + old_num_1 + " - " + old_num_2 + " = " + answer
			colour = "success"
		else:
			my_answer = "Incorrect! "+ old_num_1 + " - " + old_num_2 + " = " + str(correct_answer)
			colour = "danger"

		return render(request, 'subtraction.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'colour':colour,
			})
	
	return render(request, 'subtraction.html', {
		'num_1':num_1,
		'num_2':num_2,
		})


def multiplication(request):
	from random import randint

	num_1 = randint(0,9)
	num_2 = randint(0,9)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if form not filled out
		if not answer:
			my_answer = "Hey! You forgot to fill out the form!"
			colour = "warning"
			return render(request, 'division.html', {
			'my_answer':my_answer,
			'colour':colour,
			'answer':answer,
			'num_1':num_1,
			'num_2':num_2,
			})

		correct_answer = int(old_num_1) * int(old_num_2)
		
		if int(answer) == int(correct_answer):
			my_answer = "Correct! " + old_num_1 + " x " + old_num_2 + " = " + answer
			colour = "success"
		else:
			my_answer = "Incorrect! "+ old_num_1 + " x " + old_num_2 + " = " + str(correct_answer)
			colour = "danger"

		return render(request, 'multiplication.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'colour':colour,
			})
	
	return render(request, 'multiplication.html', {
		'num_1':num_1,
		'num_2':num_2,
		})


def division(request):
	from random import randint

	num_1 = randint(0,9)
	ld_1 = divisors(num_1)
	if len(ld_1) == 1:
		alea = 0
	else:
		alea = randint(0,len(ld_1)-1)
	num_2 = ld_1[alea]

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if form not filled out
		if not answer:
			my_answer = "Hey! You forgot to fill out the form!"
			colour = "warning"
			return render(request, 'division.html', {
			'my_answer':my_answer,
			'colour':colour,
			'answer':answer,
			'num_1':num_1,
			'num_2':num_2,
			})

		correct_answer = int(old_num_1) / int(old_num_2)
		
		if int(answer) == int(correct_answer):
			my_answer = "Correct! " + old_num_1 + " / " + old_num_2 + " = " + answer
			colour = "success"
		else:
			my_answer = "Incorrect! "+ old_num_1 + " / " + old_num_2 + " = " + str(correct_answer)
			colour = "danger"

		return render(request, 'division.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'colour':colour,
			})
	
	return render(request, 'division.html', {
		'num_1':num_1,
		'num_2':num_2,
		})