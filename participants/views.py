from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from participants.models import Participant
from participants.serializers import ParticipantSerializer


@api_view(['POST'])
def participant_add(request):
    if request.method == 'POST':
        participant_data = JSONParser().parse(request)
        participant_serializer = ParticipantSerializer(data=participant_data)
        if participant_serializer.is_valid():
            participant_serializer.save()
            return JsonResponse(participant_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(participant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def participants_list(request):
    if request.method == 'GET':
        participants = Participant.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            participants = participants.filter(name__icontains=name)
        participants_serializer = ParticipantSerializer(participants, many=True)
        return JsonResponse(participants_serializer.data, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def participant_detail(request, pk):
    # find tutorial by pk (id)
    try:
        participant = Participant.objects.get(pk=pk)
    except Participant.DoesNotExist:
        return JsonResponse({'message': 'The participant does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        participant_serializer = ParticipantSerializer(participant)
        return JsonResponse(participant_serializer.data)
    elif request.method == 'PUT':
        participant_data = JSONParser().parse(request)
        participant_serializer = ParticipantSerializer(participant, data=participant_data)
        if participant_serializer.is_valid():
            participant_serializer.save()
            return JsonResponse(participant_serializer.data)
        return JsonResponse(participant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        participant.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def participants_delete(request):
    if request.method == 'DELETE':
        count = Participant.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
