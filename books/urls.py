from django.urls import path, include
from books import views as api_views
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('book/', api_views.BookViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/createadmin/',api_views.CreateAdminAPIView.as_view()),
    path('api/createstudent/',api_views.StudentAPIView.as_view()),
    path('api/studentlogin/',api_views.StudentLoginAPIView.as_view()),
    path('api/adminlogin/',api_views.AdministratorLoginAPIView.as_view()),

    path('api/crudbook/',api_views.CreateBooksAPIView.as_view()),
    path('api/bookdelnup/<int:b_id>/',api_views.BookDelandUpAPIView.as_view())
]
