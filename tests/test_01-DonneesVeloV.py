import geopandas as gpd
import pandas as pd
import os

from pyvelov import data
from sqlalchemy import create_engine


def test_get_stations_information():
    gdf_velov = data.get_station_information()

    assert type(gdf_velov) == gpd.GeoDataFrame
    assert set(['station_id', 'name', 'capacity']).issubset(gdf_velov.columns)
    assert gdf_velov.crs == "EPSG:3857"


def test_get_stations_status():
    status_velov = data.get_station_status()

    assert type(status_velov) == pd.DataFrame
    assert set(['station_id', 'num_bikes_available', 'last_reported']).issubset(status_velov.columns)
    assert len(status_velov) > 200


def test_update_local_stations():
    stations = data.get_station_information()
    data.update_local_stations(stations)

    engine = create_engine("postgresql://pyvelov:very_secure_password@localhost:5432/pyvelov")
    db_stations = gpd.read_postgis("SELECT * FROM stations", engine, geom_col='geometry')

    assert stations.equals(db_stations)


def test_update_local_status():
    status = data.get_station_status()
    data.update_local_status(status)

    engine = create_engine("postgresql://pyvelov:very_secure_password@localhost:5432/pyvelov")
    db_status = pd.read_sql_query('SELECT * FROM status', engine)

    assert len(status) == len(db_status)


def test_join_db_data():
    db_gdf = data.join_db_data(output_file='./datasets/output/stations.gpkg')

    assert type(db_gdf) == gpd.GeoDataFrame
    assert set(['station_id', 'name', 'capacity', 'num_bikes_available', 'last_reported']).issubset(db_gdf.columns)
    assert os.path.exists('./datasets/output/stations.gpkg')
    assert os.path.getsize('./datasets/output/stations.gpkg') > 0
