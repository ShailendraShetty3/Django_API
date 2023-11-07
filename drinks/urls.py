"""
URL configuration for drinks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drinks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', views.drink_list),
    path('drinks/<int:id>', views.drink_detail),
    path('employee/', views.employee_list),
    path('employee/<int:id>', views.employee_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)





# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# from django.contrib import admin
# from django.urls import path
# from drinks import views
# from rest_framework.urlpatterns import format_suffix_patterns

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API",
#         default_version="v1",
#         description="Your API description",
#         terms_of_service="https://www.yourapi.com/terms/",
#         contact=openapi.Contact(email="contact@yourapi.com"),
#         license=openapi.License(name="Your License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

# urlpatterns = [
#     # ...
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

#     path('swagger/admin/', admin.site.urls),
#     path('swagger/drinks/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


# #     path('drinks/', views.drink_list),
# #     path('drinks/<int:id>', views.drink_detail),
# #     path('user/', views.user_data),
# #     path('user/<int:id>', views.user_detail),
# ]
