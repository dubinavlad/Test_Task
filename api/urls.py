from rest_framework import routers
from api.views.team import TeamView

router = routers.SimpleRouter()
router.register(r"teams", TeamView)


urlpatterns = router.urls
