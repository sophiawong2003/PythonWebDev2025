from django.shortcuts import render
from . models import Listing    # . means from same level
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def listings(request):
    #listings = Listing.objects.all()     #take all variables from Listing class DB hold by listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)  #based on class Paginator, 3 in a group
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings' : paged_listings}    #variables wrapped under context
    return render(request, 'listings/listings.html', context) #pass address of context to template engine

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')