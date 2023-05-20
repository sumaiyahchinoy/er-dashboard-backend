def get_time_series_data():
    import pandas as pd
    from .access_onedrive import create_onedrive_directdownload

    onedrive_link = 'https://1drv.ms/x/s!AsCp_kE1E5Md6harC_UNDuwrjUbd?e=x0RSN0' #time series data
    link = create_onedrive_directdownload(onedrive_link)
    data = pd.read_excel(link)

    data['Triage_Datetime'] = pd.to_datetime(data['Triage_Datetime'])
    data['Triage_Datetime'] = data['Triage_Datetime'].dt.date
    new_data = data.groupby(['Triage_Datetime'])['Triage_Datetime'].count().reset_index(name='Recorded')
    new_data['Triage_Datetime'] = pd.to_datetime(new_data['Triage_Datetime'])
    new_data.index = new_data['Triage_Datetime']
    #del new_data['Triage_Datetime']
    #print(new_data.head(5))
    return new_data
   

get_time_series_data()