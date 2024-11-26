from django.http import JsonResponse
from .models import ChatParticipant
from account.models import Account
from rest_framework.authtoken.models import Token


# Create your views here.
def getChatParticipant(request):
    room = request.GET.get("room")

    chatCount = ChatParticipant.objects.filter(room=room).count()

    if chatCount == 0:
        participant = ChatParticipant()
        participant.user = Account.objects.all()[0]
        participant.room = room
        participant.save()
    else:
        if chatCount == Token.objects.all().count():
            all_participants = ChatParticipant.objects.filter(room=room)

            all_participants.delete()

            participant = ChatParticipant()

            participant.user = Account.objects.all()[0]

            participant.room = room

            participant.save()
        else:
            participant = ChatParticipant()
            participant.user = Account.objects.all()[chatCount]
            participant.room = room
            participant.save()

    return JsonResponse({
        "username": str(participant.user.username)
    }, safe=False)