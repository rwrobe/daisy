from django.conf.urls import include, patterns, url
from authentication.views import AccountViewSet, LoginView, LogoutView
from rest_framework_nested import routers
from django_daisy.views import IndexView

from risks.views import RiskViewSet, UserRisksViewSet

router = routers.SimpleRouter()
router.register(r'users',AccountViewSet)
router.register(r'risks', RiskViewSet)

# Nested Router
users_router = routers.NestedSimpleRouter(
    router, r'users', lookup='user' # Add a user endpoint like this /api/v1/users/
)
users_router.register(r'risks', UserRisksViewSet) # Adds a risks endpoint for URLs like /api/v1/users/risks/

urlpatterns = patterns(
    '',
    # API endpoint for account creation
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(users_router.urls)),

    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url('^.*$', IndexView.as_view(), name='index'),
)