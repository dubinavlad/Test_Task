from user_site.models import Team
from rest_framework import viewsets
from api.serializers.team import TeamSerializer



class TeamView(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
