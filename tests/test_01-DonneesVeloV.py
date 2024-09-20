import geopandas as gpd
import pandas as pd
import os

from pyvelov import data
from sqlalchemy import create_engine


def test_get_stations_information():
    # On charge les données des stations depuis l'API
    gdf_velov = data.get_station_information()

    # On vérifie que l'objet retourné est bien un GeoDataFrame
    assert isinstance(gdf_velov, gpd.GeoDataFrame)

    # On vérifie que le GeoDataFrame contient bien les colonnes attendues
    assert set(['station_id', 'name', 'capacity']).issubset(gdf_velov.columns)

    # On vérifie que le GeoDataFrame est projeté correctement en WebMercator
    assert gdf_velov.crs == "EPSG:3857"


def test_get_stations_status():
    # On charge les données des stations depuis l'API
    status_velov = data.get_station_status()

    # On vérifie que l'objet retourné est bien un DataFrame
    assert isinstance(status_velov, pd.DataFrame)

    # On vérifie que le DataFrame contient bien les colonnes attendues
    assert set(['station_id', 'num_bikes_available', 'last_reported']).issubset(status_velov.columns)

    # On vérifie que le DataFrame contient bien des données
    assert len(status_velov) > 200


def test_update_local_stations():
    # On charge les données des stations depuis l'API
    stations = data.get_station_information()

    # On met à jour la base de données locale
    data.update_local_stations(stations)

    # On recharge les données depuis la base de données
    engine = create_engine("postgresql://pyvelov:very_secure_password@localhost:5432/pyvelov")
    db_stations = gpd.read_postgis("SELECT * FROM stations", engine, geom_col='geometry')

    # On vérifie que les données sont identiques
    assert stations.equals(db_stations)


def test_update_local_status():
    # On charge les données des stations depuis l'API
    status = data.get_station_status()

    # On met à jour la base de données locale
    data.update_local_status(status)

    # On recharge les données depuis la base de données
    engine = create_engine("postgresql://pyvelov:very_secure_password@localhost:5432/pyvelov")
    db_status = pd.read_sql_query('SELECT * FROM status', engine)

    # On vérifie que les données sont identiques
    assert len(status) == len(db_status)


def test_join_db_data():
    # On lance la fonction de jointure des tables de la base de données
    db_gdf = data.join_db_data(output_file='./datasets/tests/stations.gpkg')

    # On vérifie que l'objet retourné est bien un GeoDataFrame
    assert isinstance(db_gdf, gpd.GeoDataFrame)

    # On vérifie que le GeoDataFrame contient bien les colonnes attendues
    assert set(['station_id', 'name', 'capacity', 'num_bikes_available', 'last_reported']).issubset(db_gdf.columns)

    # On vérifie que le GeoPackage est bien créé
    assert os.path.exists('./datasets/output/stations.gpkg')

    # On vérifie que le GeoPackage n'est pas vide
    assert os.path.getsize('./datasets/output/stations.gpkg') > 0
