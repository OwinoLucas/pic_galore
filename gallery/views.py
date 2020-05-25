from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Category, Image, location

# Create your views here.
def index(request):
    """
    view function returns the landing page
    """
    images = Image.objects.all()
    locations = location.get_locations()
    return render(request,'all-pics/index.html',{"images":images,"locations":locations})

def search_results(request):
    """
    view function returns the searched categories
    """
    if 'category' in request.GET and request.GET["category"]:
        category_search = request.GET.get("category")
        searched_categories = Image.search_image_by_category(category_search)
        message = f"{category_search}"

        return render(request, 'all-pics/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-pics/search.html',{"message":message})

def locate_image(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'location_images': images})