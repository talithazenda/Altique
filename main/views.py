from django.shortcuts import render

def home(request):
    context = {
        'app_name': 'Altique',
        'student_name': 'Talitha Zenda Shakira',
        'student_class': 'PBP A'
    }
    return render(request, 'home.html', context)
