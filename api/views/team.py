from user_site.models import Team
from rest_framework import viewsets
import json
from rest_framework import status
from rest_framework.decorators import action, api_view
from api.serializers.team import TeamSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response


class TeamView(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
