import numpy as np
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from .ts_data_extract import get_time_series_data


class PatientIncomingData(APIView):
    def get(self, request):
        data = get_time_series_data()  # Call the function from your Python file
        # Process the data as needed
        # processed_data = process_data(data)
        print(data)

        return Response(data, status=200)