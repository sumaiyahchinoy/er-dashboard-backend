from django.urls import path
# from .views import PatientIncomingPrediction
from .views2 import PatientIncomingData

urlpatterns = [
    # path('patientForecast/', PatientIncomingPrediction.as_view(), name = 'weight_prediction'),
    #path('patientForecast/', PatientIncomingPrediction.as_view('get_model_predictions'), name='model_predictions'),
    path('external-data/', PatientIncomingData.as_view(), name='external_data'),
    # path('external-data/', PatientIncomingPrediction.as_view('get_data_from_external_file'), name='external_data'),
]