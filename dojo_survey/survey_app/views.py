from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def result(request):
    
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']
    dessert_from_form = request.POST['dessert']
    teacher_from_form = request.POST.getlist('teacher')
    teacher_from_form = ', '.join(teacher_from_form)

    context = {
        "name" : name_from_form,
        "location" : location_from_form,
        "language" : language_from_form,
        "comment" : comment_from_form,
        "dessert" : dessert_from_form,
        "teacher" : teacher_from_form
    }

    return render(request, "result.html", context)