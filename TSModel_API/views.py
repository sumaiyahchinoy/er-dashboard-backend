import numpy as np
import pandas as pd
from .apps import TSModelApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from .ts_data_extract import get_time_series_data


class PatientIncomingPrediction(APIView):
    def get(self, request):
        # data = request.data
        # height = data['Height']
        # gender = data['Gender']
        # if gender == 'Male':
        #     gender = 0
        # elif gender == 'Female':
        #     gender = 1
        # else:
        #     return Response("Gender field is invalid", status=400)
        # lin_reg_model = TSModelApiConfig.model
        # weight_predicted = lin_reg_model.predict([[gender, height]])[0][0]
        # weight_predicted = np.round(weight_predicted, 1)
        # response_dict = {"Predicted Weight (kg)": weight_predicted}

        # ts_model = TSModelApiConfig.model
        # y_pred = ts_model.get_forecast(steps = 31)
        # y_pred_df = y_pred.conf_int(alpha = 0.05) 
        # y_pred_df["Predictions"] = ts_model.predict(start = y_pred_df.index[0], end = y_pred_df.index[-1])
        # y_pred_out = y_pred_df["Predictions"]
        # print(y_pred_out)
        # output_df = pd.DataFrame(y_pred_out)
        # output_df.reset_index(inplace=True)
        # print(output_df)
        return Response("Success", status=200) 
    
    def get_data_from_external_file(self, request):
        data = get_time_series_data()  # Call the function from your Python file
        # Process the data as needed
        # processed_data = process_data(data)
        print(data)

        return Response(data, status=200)