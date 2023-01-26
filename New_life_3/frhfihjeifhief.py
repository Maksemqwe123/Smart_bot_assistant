# #Importing the requires modules
# import folium
# import pandas as pd
# from geopandas.tools import geocode
#
# #Creating a DataFrame
# wonders = ['Taj Mahal', 'Colosseum','Machu Picchu','Christ the Redeemer','Chichen Itza','petra']
#
# df = pd.DataFrame({'wonders' : wonders})
#
# #function to unzip latitude and longitude from GeoDataFrame
# def custom_geocoder(address):
#     dataframe = geocode(address , provider="nominatim" , user_agent = 'my_request')
#     point = dataframe.geometry.iloc[0]
#     return pd.Series({'Latitude': point.y, 'Longitude': point.x})
#
# #Applying function to the dataframe
# df[['latitude' , 'longitude']]= df.wonders.apply( lambda x: custom_geocoder(x))

# print(df)


