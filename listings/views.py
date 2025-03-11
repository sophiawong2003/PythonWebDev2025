from django.shortcuts import render, get_object_or_404
from . models import Listing    # . means from same level
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from listings.choices import price_choices, bedroom_choices, district_choices

# Create your views here.
def listings(request):
    # listings = Listing.objects.filter(district= F('address'))
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)  #based on class Paginator, 3 in a group
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings' : paged_listings}    #variables wrapped under context
    return render(request, 'listings/listings.html', context) #pass address of context to template engine

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing' : listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description_icontains=keywords)
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title_icontains=title)
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district_iexact=district)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price_lte=price)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedroom_lte=bedrooms)

    context = {
        'price_choices' : price_choices,
        'district_choices' : district_choices,
        'bedroom_choices' : bedroom_choices,
        'listings' : queryset_list,
        'value' : request.GET
    }
    return render(request, 'listings/search.html')