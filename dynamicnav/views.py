from itertools import chain

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import AbstractPainting, WildlifePainting, PastelPainting, InkPainting


def dyna(request):
    painting = AbstractPainting.objects.all()
    return render(request, "basic.html", {"painting": painting})


def search(request):
    try:
        query = request.GET.get('search')
    except:
        query = None

    if query:
        painting = AbstractPainting.objects.filter(name__icontains=query) | AbstractPainting.objects.filter(
            artist__icontains=query, ) | AbstractPainting.objects.filter(
            description__icontains=query, ) | AbstractPainting.objects.filter(
            small_description__icontains=query, ) | AbstractPainting.objects.filter(specifications__icontains=query)

        wildlife = WildlifePainting.objects.filter(name__icontains=query) | WildlifePainting.objects.filter(
            artist__icontains=query, ) | WildlifePainting.objects.filter(
            description__icontains=query, ) | WildlifePainting.objects.filter(
            small_description__icontains=query, ) | WildlifePainting.objects.filter(specifications__icontains=query)

        pastelpainting = PastelPainting.objects.filter(name__icontains=query) | PastelPainting.objects.filter(
            artist__icontains=query, ) | PastelPainting.objects.filter(
            description__icontains=query, ) | PastelPainting.objects.filter(
            small_description__icontains=query, ) | PastelPainting.objects.filter(specifications__icontains=query)

        inkpainting = InkPainting.objects.filter(name__icontains=query) | InkPainting.objects.filter(
            artist__icontains=query, ) | InkPainting.objects.filter(
            description__icontains=query, ) | InkPainting.objects.filter(
            small_description__icontains=query, ) | InkPainting.objects.filter(specifications__icontains=query)

        context = {'query': query,
                   'painting': painting,
                   'wildlife': wildlife,
                   'pastelpainting': pastelpainting,
                   'inkpainting': inkpainting, }

        template = "search.html"
    else:
        template = "basic.html"
        context = {}

    return render(request, template, context)


# def searchMatch(query, item):
#     return True

# if query in item.description.lower() or query in item.name.lower() or query in item.artist.lower():
#     return True
# else:
#     return False
#
#
# def search(request):
#     query = request.GET.get('search')
#     allProds = []
#     catprods = AbstractPainting.objects.values()
#     cats = [item for item in catprods]
#
#     for cat in cats:
#         pain = AbstractPainting.objects.filter()
#
#         painting = [item for item in pain if searchMatch(query, item)]
#         allProds.append([painting])
#
#     return render(request, "basic.html", {"allProds": allProds})


def wildlifepaintings(request):
    wildlifepainting = WildlifePainting.objects.all()
    return render(request, "acrylic.html", {"wildlifepainting": wildlifepainting})


def pastelpaintings(request):
    pastelpainting = PastelPainting.objects.all()
    return render(request, "pastel.html", {"pastelpainting": pastelpainting})


def inkpaintings(request):
    inkpainting = InkPainting.objects.all()
    return render(request, "ink.html", {"inkpainting": inkpainting})


def abstract_description(request, id):
    painting = AbstractPainting.objects.filter(painting_id=id).first()
    return render(request, "main_description.html", {"painting": painting})


def wildlife_description(request, id):
    wildlifepainting = WildlifePainting.objects.filter(painting_id=id).first()
    return render(request, "wildlife_description.html", {"wildlifepainting": wildlifepainting})


def ink_description(request, id):
    inkpainting = InkPainting.objects.filter(painting_id=id).first()
    return render(request, "ink_description.html", {"inkpainting": inkpainting})


def pastel_description(request, id):
    pastelpainting = PastelPainting.objects.filter(painting_id=id).first()
    return render(request, "pastel_description.html", {"pastelpainting": pastelpainting})
