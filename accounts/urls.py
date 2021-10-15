from django.urls import path
from .views import home, UserDetailsView

urlpatterns = [
    path('', home, name='home'),
    path('accounts/my_details/', UserDetailsView.as_view()),
]
