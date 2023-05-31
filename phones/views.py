from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort')
    if sort_by == 'min_price' or sort_by == 'max_price':
        phones = Phone.objects.all().order_by('price') if sort_by == 'min_price' \
            else Phone.objects.all().order_by('-price')
    elif sort_by == 'name':
        phones = Phone.objects.all().order_by('name')
    else:
        phones = Phone.objects.all()


    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(name=slug.replace('-', ' '))}
    return render(request, template, context)
