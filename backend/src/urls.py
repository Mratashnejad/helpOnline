
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("dj_rest_auth.urls")), #provided by dj-rest-auth
    path("api/social/login" , include("users.urls")), #views in users app
]



