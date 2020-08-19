from rest_framework import serializers
from participants.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = (
            'id', 'name', 'manager_email_address', 'type_of_participant',
            'foundation_date', 'registered_date', 'order'
        )
