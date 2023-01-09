from django.urls import path
from .views import test_view, test_view_with_exluding_keys, test_view_with_keys

urlpatterns = [
    path("test/<str:param>/", test_view, name="test_view"),
    path("test_excluding/<str:param>/", test_view_with_exluding_keys,
         name="test_view_with_exluding_keys"),
    path("test_keys/<str:param>/", test_view_with_keys,
         name="test_view_with_keys"),
]
