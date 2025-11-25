# server/djangoapp/urls.py

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for login page (React frontend)
    path('djangoapp/login/', TemplateView.as_view(template_name="index.html"), name='login_page'),

    # Path for login API
    path('api/login/', views.login_user, name='login_api'),

    # Path for logout API
    path('api/logout/', views.logout_user, name='logout_api'),

    # Path for registration API
    path('api/registration/', views.registration, name='registration_api'),

    # Path to get all dealerships
    path('api/dealerships/', views.get_dealerships, name='get_dealerships'),

    # Path to get dealer reviews
    path('api/dealerships/<int:dealer_id>/reviews/', views.get_dealer_reviews, name='get_dealer_reviews'),

    # Path to get dealer details
    path('api/dealerships/<int:dealer_id>/', views.get_dealer_details, name='get_dealer_details'),

    # Path to add a review
    path('api/dealerships/<int:dealer_id>/add_review/', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
