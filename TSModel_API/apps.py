import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class TSModelApiConfig(AppConfig):
    name = 'TSModel_API'
    MODEL_FILE = os.path.join(settings.MODELS, "PredictionTSModel.joblib")
    model = joblib.load(MODEL_FILE)