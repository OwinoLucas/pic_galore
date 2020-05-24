from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Category, Image, location

# Create your views here.
def index(request):
    """
    view function returns the landing page
    """
    images = Image.objects.all()
    return render(request,'all-pics/index.html',{"images":images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        category_search = request.GET.get("category")
        searched_categories = Image.search_image_by_category(category_search)
        message = f"{category_search}"

        return render(request, 'all-pics/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-pics/search.html',{"message":message})
