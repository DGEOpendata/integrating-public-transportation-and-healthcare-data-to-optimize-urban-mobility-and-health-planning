python
import pandas as pd
import geopandas as gpd

# Load the public transportation dataset
transport_data = pd.read_csv('PublicTransportData_AbuDhabi.csv')

# Load the healthcare facilities dataset
healthcare_data = gpd.read_file('HealthcareFacilities_AbuDhabi.geojson')

# Function to find nearest healthcare facility for each public transport stop
def find_nearest_healthcare(transport_df, healthcare_gdf):
    healthcare_gdf = healthcare_gdf.to_crs(transport_df.crs)
    transport_df['geometry'] = gpd.points_from_xy(transport_df['longitude'], transport_df['latitude'])
    transport_gdf = gpd.GeoDataFrame(transport_df, geometry='geometry')
    transport_gdf = transport_gdf.set_crs(healthcare_gdf.crs)

    nearest_healthcare = []
    for index, row in transport_gdf.iterrows():
        distances = healthcare_gdf.geometry.distance(row.geometry)
        nearest = healthcare_gdf.iloc[distances.idxmin()]
        nearest_healthcare.append(nearest['facility_name'])
    transport_gdf['nearest_healthcare'] = nearest_healthcare
    return transport_gdf

# Find the nearest healthcare facility for each public transport stop
combined_data = find_nearest_healthcare(transport_data, healthcare_data)

# Save combined data to CSV
combined_data.to_csv('CombinedTransportHealthcareData.csv', index=False)
