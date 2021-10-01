
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Vakation
from .form import findForm



def scraping_home(request):
    form = findForm()
    city = request.GET.get('city')
    language = request.GET.get('language')

    _context={}
    if city or language:
        _filter={}
        if city:
            _filter['city__slug']=city
        if language:
            _filter['language__slug'] = language

        v = Vakation.objects.filter(**_filter)
        vak = Paginator(v,7)
        page_number=request.GET.get('page')
        v_n=vak.get_page(page_number)
        _context={'vakantion':v_n,'form':form,'city':request.GET.get('city'),'language':request.GET.get('language')}
    else:
        _context = {'form': form,'city':request.GET.get('city'),'language':request.GET.get('language')}
    return render(request,'scraping/home.html',_context)
