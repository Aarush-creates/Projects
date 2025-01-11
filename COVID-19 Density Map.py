import geopandas as gpd
import pandas as pd
import folium
import webbrowser

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
covid_data = pd.read_csv(url)

mlt = covid_data.melt(id_vars = ["Province/State", "Country/Region", "Lat", "Long"], var_name = "Date", value_name = "Cases")
latest_date = mlt['Date'].max()

newdata = mlt[mlt['Date'] == latest_date]
newdata = newdata.groupby("Country/Region").agg({'Cases': 'sum', 'Lat': 'mean', 'Long': 'mean'}).reset_index()

path = "C:/Users/ashis/Downloads/ne_110m_admin_0_countries"
world = gpd.read_file(path)

world = world.merge(newdata, how = 'left', left_on = "NAME", right_on = "Country/Region")

map = folium.Map(location = [20, 0], zoom_start = 2)

folium.Choropleth(
    geo_data = world.__geo_interface__,
    name='Choropleth',
    data = world,
    columns = ['Country/Region', 'Cases'],
    key_on = 'feature.properties.NAME',
    fill_color = 'YlOrRd',
    fill_opacity = 0.8,
    line_opacity = 0.5,
    legend_name = 'COVID-19 Cases'
).add_to(map)

folium.LayerControl().add_to(map)
map.save('covid_density_map.html')
webbrowser.open('covid_density_map.html')

