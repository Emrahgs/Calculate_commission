# ** Django Imports **
from django.urls import path

# ** App Imports **
from core.views import index, reservation, commissions, download_csv_data

# App name
app_name = 'core'

# URL patterns
urlpatterns = [
    path('', index, name='index'),
    path('reservations/', reservation, name='reservations'),
    path('commissions/', commissions, name='commissions'),
    path('download/', download_csv_data, name='download'),
]
