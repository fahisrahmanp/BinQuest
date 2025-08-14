from django.shortcuts import render, redirect, get_object_or_404  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



def index(request):
    return render(request, 'index.html')



def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        superuser_code = request.POST.get('superuser_code')
        password = request.POST.get('password')
        

        # Check if the superuser code is correct
        if superuser_code == 'BINQUEST':  # Replace 'your_superuser_code' with your actual superuser code
            # Create the user
            myuser = User.objects.create_user(username, superuser_code, password)
            myuser.save()
            return redirect('loginn')  # Redirect to login page if signup is successful

    return render(request, 'signup.html')


def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('add_todo')
            

    return render(request, 'login.html')



@login_required
def add_todo(request):
    username = request.user.username
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form, 'username': username})

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if todo.user == request.user:
        todo.delete()
    return redirect('todo_list')


def user_logout(request):
    logout(request)
    return redirect('index')  # Redirect to the login page after logout













# views.py




def contact_form(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            subject = request.POST.get('subject')

            # Construct email message
            message = f"""
            New message from {first_name} {last_name} ({email}):
            Subject: {subject}
            """

            # Send email
            send_mail(
                'New message from website',
                message,
                settings.EMAIL_HOST_USER,  # Sender's email
                [settings.EMAIL_HOST_USER],  # Receiver's email (replace with your email)
                fail_silently=False,
            )
            messages.success(request, 'Your message was sent successfully!')
            return redirect('contact_form')  # Redirect to a success page
    else:

        return render(request, 'contact_form.html')






#web.views.py


# web.views.py

#web.views.py


#web.views.py
# views.py

# views.py


def todo_search(request):
    if request.method == 'GET':
        # Get the category from the request, defaulting to 'Biodegradable'
        category = request.GET.get('category', 'Biodegradable')
        
        # Get the place from the request
        place = request.GET.get('place')

        # Query all todos initially
        todos = Todo.objects.all()
        
        # If a place is provided, filter todos by place
        if place:
            todos = todos.filter(place__icontains=place)

        # Filter todos by category
        # Set 'Biodegradable' as the default category
        todos = todos.filter(category=category)
        
        context = {
            'todos': todos,
            'default_category': category
        }
        return render(request, 'bio_search.html', context)
    else:
        # If it's not a GET request, just render the search page without any context
        return render(request, 'bio_search.html', {})




def redirect_to_location(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    return redirect(f'https://maps.google.com/?q={todo.latitude},{todo.longitude}')






def nonbio_search(request):
    if request.method == 'GET':
        category = request.GET.get('category', 'Non Biodegrable')  # Default category (case-sensitive)
        place = request.GET.get('place')

        todos = Todo.objects.all()

        if place:
            todos = todos.filter(place__icontains=place)

        # Filter todos by category (case-sensitive)
        todos = todos.filter(category=category)

        context = {
            'todos': todos,
            'default_category': category
        }
        return render(request, 'nonbio_search.html', context)
    else:
        return render(request, 'nonbio_search.html', {})





def identify(request):
        return render(request, 'identify.html')



 # Redirect to the login page after logout









