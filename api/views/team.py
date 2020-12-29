
from user_site.models import Team
from rest_framework import viewsets
import json
from rest_framework import status
from rest_framework.decorators import action
from api.serializers.team import TeamSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response



class TeamView(viewsets.ModelViewSet):



    queryset  = Team.objects.values().order_by('wins')
    serializer_class=TeamSerializer

    @csrf_exempt
    @action(detail=True, methods=['post'])
    def save(self,request, pk=None):


        id = (json.loads(request.data['body']))['id']
        serializer = TeamSerializer(data=json.loads(request.data['body']))

        if serializer.is_valid():

            team = Team.objects.get(id=id)

            team.name = serializer.data['name']
            team.tag = serializer.data['tag']
            team.rating =serializer.data['rating']
            team.wins =serializer.data['wins']
            team.losses = serializer.data['losses']
            team.last_match_time =serializer.data['last_match_time']
            team.logo =serializer.data['logo']
            team.save()
            return Response({'status': 'Team saved'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def delete(self, request, pk=None):
        id = json.loads(request.data['body'])
        team = Team.objects.get(id=id)

        if (team.delete()[0])==1:
            return Response({'status': 'Deleted!'})
        else:
            return Response('it is impossible to delete',status=status.HTTP_400_BAD_REQUEST)




