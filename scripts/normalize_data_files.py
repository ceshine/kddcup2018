import pandas as pd

bj = pd.concat([
    pd.read_csv("data/beijing_17_18_aq.csv"),
    pd.read_csv("data/beijing_201802_201803_aq.csv")
])
bj = bj.rename(columns={
    "stationId": "station_id",
    "utc_time": "time",
    "PM2.5": "PM25_Concentration",
    "PM10":  "PM10_Concentration",
    "NO2":   "NO2_Concentration",
    "CO":    "CO_Concentration",
    "O3":    "O3_Concentration",
    "SO2":   "SO2_Concentration"
})
bj.to_csv("data/bj_201803_renamed_aq.csv", index=False)

ld = pd.read_csv("data/London_historical_aqi_forecast_stations_20180331.csv")
del ld["Unnamed: 0"]
ld = ld.rename(columns={
    "MeasurementDateGMT": "time",
    "PM2.5 (ug/m3)": "PM25_Concentration",
    "PM10 (ug/m3)":  "PM10_Concentration",
    "NO2 (ug/m3)":   "NO2_Concentration"
})
ld.to_csv("data/ld_201803_renamed_aq.csv", index=False)
