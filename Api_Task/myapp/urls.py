from django.urls import path,include
from myapp import drfviews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("per_data/<pk>",drfviews.PersonAPI.as_view()),
    path("per_data/",drfviews.PersonAPI.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',drfviews.RegisterUser.as_view())

    
]
