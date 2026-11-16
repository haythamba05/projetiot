from django.shortcuts import render
from .models import Dht


def dashboard(request):
    derniere_mesure = Dht.objects.last()
    dernieres_mesures = Dht.objects.all().order_by('-dt')[:5]

    contexte = {
        'mesure': derniere_mesure,
        'dernieres_mesures': dernieres_mesures,
    }

    return render(request, "DHT/dashboard.html", contexte)