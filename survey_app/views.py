from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def result(request):
    candy = ''
    
    candy1 = request.form.get('candy1')
    if candy1:
        candy += candy1

    candy2 = request.form.get('candy2')
    if candy2:
        candy += candy2

    candy3 = request.form.get('candy3')
    if candy3:
        candy += candy3

    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']
    dessert_from_form = request.POST['dessert']
    candy_from_form = request.POST['candy']

    context = {
        "name" : name_from_form,
        "location" : location_from_form,
        "language" : language_from_form,
        "comment" : comment_from_form,
        "dessert" : dessert_from_form,
        "candy" : candy_from_form,
    }

    return render(request, "result.html", context)