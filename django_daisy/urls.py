from django.conf.urls import include, patterns, url
from authentication.views import AccountViewSet
from rest_framework_nested import routers
from django_daisy.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts',AccountViewSet)
urlpatterns = patterns(
    '',
    # API endpoint for account creation
    url(r'^api/v1/', include(router.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
)