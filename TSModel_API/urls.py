from django.urls import path
from .views import PatientIncomingPrediction
from .views2 import PatientIncomingData

urlpatterns = [
    path('patientForecast/', PatientIncomingPrediction.as_view(), name = 'patient_prediction'),
    path('external-data/', PatientIncomingData.as_view(), name='external_data'),
]