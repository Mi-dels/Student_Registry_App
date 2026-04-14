from django.urls import path,include
from rest_framework import routers
from . import views
from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# urlpatterns = [
#     # path('', views.Home),
#     path('',views.LoginViewSet.as_view),
#     path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     # path('myprotectedroute', views.myprotectedroute),
# ]


# router = routers.DefaultRouter()
# router.register(r"students", views.SignupViewSet) 

# urlpatterns = [

#     path('api/auth/', include('dj_rest_auth.urls')), # Includes LoginView, LogoutView
#     path('api/auth/registration/', include('dj_rest_auth.registration.urls')), # Includes RegisterView

# path('', include(router.urls)),
# path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
# path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



# ]


urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    # THIS IS THE KEY ENDPOINT FOR YOUR FRONTEND DEVELOPER
    # They will POST the key from the email to this URL
    path('api/auth/registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    
    # This dummy URL is needed for the email generation logic to work
    re_path(r'^account-confirm-email/(?P<key>[-:\w%=]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
]
