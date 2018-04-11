
# coding: utf-8

# # Using Folium to Visualize Beijing Station Data

# Reference: https://projects.raspberrypi.org/en/projects/mapping-the-weather/9
# 
# Using data from [KDD CUP of Fresh Air](https://biendata.com/competition/kdd_2018/data/).

# In[1]:


import numpy as np 
import pandas as pd
import folium


# In[2]:


bj_aq = pd.read_csv("../data/bj_201803_renamed_aq.csv")


# In[3]:


stations = pd.read_csv("../data/Beijing_AirQuality_Stations.csv")
stations.head()


# ## Basic Map of Beijing

# In[4]:


map_hooray = folium.Map(
    location=[39.929, 116.417],
    tiles = "Stamen Terrain",
    zoom_start = 10) # Uses lat then lon. The bigger the zoom number, the closer in you get
map_hooray # Calls the map to display 


# ## Mark Stations using folium.Marker

# In[5]:


data = pd.merge(bj_aq[bj_aq["time"]=="2017-01-01 14:00:00"], stations, on="station_id")
data.head()


# In[6]:


map_hooray = folium.Map(
    location=[39.929, 116.8],
    tiles = "Stamen Terrain",
    zoom_start = 9) 

for _, row in data.iterrows():
    folium.Marker([
        row["Latitude"],row["Longitude"]],
        popup=row["station_id"]).add_to(map_hooray)

map_hooray


# ## Using Colors to Reprecent PM2.5 Concentration with folium.CircleMarker

# In[7]:


def colourgrad(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = (value-minimum) / (maximum - minimum)
    g = int(max(0, 128*(1 - ratio)))
    r = int(max(0, 128*(1 - ratio) + 127))
    b = 0
    hexcolour = '#%02x%02x%02x' % (r,g,b)
    return hexcolour


# In[8]:


data = pd.merge(bj_aq[bj_aq["time"]=="2017-01-01 15:00:00"], stations, on="station_id")
map_hooray = folium.Map(
    location=[39.929, 116.8],
    tiles = "Stamen Terrain",
    zoom_start = 9) 

for _, row in data.iterrows():
    color = colourgrad(0, 500, min(row["PM25_Concentration"], 500))
    folium.CircleMarker([
        row["Latitude"],row["Longitude"]],
        color=color, radius=9, fill_opacity=1, fill=True, fill_color=color,
        popup=row["station_id"] + ":" + str(row["PM25_Concentration"])).add_to(map_hooray)

# CWD = os.getcwd()
# map_ws.save('osm.html')
# webbrowser.open_new('file://'+CWD+'/'+'osm.html')
map_hooray


# ### A Few Hours later...

# In[9]:


data = pd.merge(bj_aq[bj_aq["time"]=="2017-01-01 18:00:00"], stations, on="station_id")
map_hooray = folium.Map(
    location=[39.929, 116.8],
    tiles = "Stamen Terrain",
    zoom_start = 9) 

for _, row in data.iterrows():
    color = colourgrad(0, 500, min(row["PM25_Concentration"], 500))
    folium.CircleMarker([
        row["Latitude"],row["Longitude"]],
        color=color, radius=9, fill_opacity=1, fill=True, fill_color=color,
        popup=row["station_id"] + ":" + str(row["PM25_Concentration"])).add_to(map_hooray)

map_hooray


# In[10]:


data = pd.merge(bj_aq[bj_aq["time"]=="2017-01-01 20:00:00"], stations, on="station_id")
map_hooray = folium.Map(
    location=[39.929, 116.8],
    tiles = "Stamen Terrain",
    zoom_start = 9) 

for _, row in data.iterrows():
    color = colourgrad(0, 500, min(row["PM25_Concentration"], 500))
    folium.CircleMarker([
        row["Latitude"],row["Longitude"]],
        color=color, radius=9, fill_opacity=1, fill=True, fill_color=color,
        popup=row["station_id"] + ":" + str(row["PM25_Concentration"])).add_to(map_hooray)

map_hooray

