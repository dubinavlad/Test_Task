

from django.urls import path, include

from rest_framework import routers
from api.views.team import TeamView
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'team', TeamView,basename='Team')

#TeamView.reverse_action(TeamView.save.url_name, args=['1'])


urlpatterns = [
    path(r'save/',TeamView.as_view({'post': 'save'})),
    path(r'delete/',TeamView.as_view({'post': 'delete'})),
    path('', include(router.urls)),

]
