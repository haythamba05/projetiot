from .models import Dht
from .serializers import DhtSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import telebot


@api_view(['GET'])
def Dlist(request):
    all_data = Dht.objects.all()
    data = DhtSerializer(all_data, many=True).data
    return Response({'data': data})


class Dhtviews(generics.CreateAPIView):
    queryset = Dht.objects.all()
    serializer_class = DhtSerializer
    authentication_classes = []

    def perform_create(self, serializer):
        data = serializer.save()
        temperature = data.temperature
        if temperature > 25:
            message = f"Alerte ! Temperature = {temperature} °C"
            send_mail(
                subject="Alerte Temperature",
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["haythamba05@gmail.com"],
                fail_silently=False
            )
            bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
            bot.send_message(settings.TELEGRAM_CHAT_ID, message)