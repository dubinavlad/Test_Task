from rest_framework import serializers
from user_site.models import Team





class TeamSerializer(serializers.ModelSerializer):


    class Meta:
        model = Team
        fields = ['id', 'name', 'tag', 'rating', 'wins','losses','last_match_time','logo']

