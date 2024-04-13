from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "movies/index.html", {
        "movies": ["kung fu panda", "spiderman", "batman"]
    })

def about(request):
    return render(request, "movies/about.html", {})