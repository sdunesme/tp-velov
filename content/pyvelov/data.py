import requests
import pandas as pd
import geopandas as gpd

from sqlalchemy import create_engine

def get_station_information() -> gpd.GeoDataFrame:
    '''
    Wrapper de l'API JCDecaux pour récupérer les informations générales sur les stations Velo'v
    '''

    # On récupère les données sur l'API
    reponse = requests.get('https://download.data.grandlyon.com/files/rdata/jcd_jcdecaux.jcdvelov/station_information.json')
    infos_stations = pd.DataFrame(reponse.json()['data']['stations'])

    # On transforme le DataFrame en GeoDataFrame

    # On projette les coordonnées

    # On ne garde que les colonnes qui nous intéressent
    gdf_velov = gdf_velov[['station_id', 'name', 'capacity', 'geometry']]

    # On s'assure que les colonnes ont les bons types
    gdf_velov['station_id'] = gdf_velov['station_id'].astype(int)
    gdf_velov['name'] = gdf_velov['name'].astype(str)
    gdf_velov['capacity'] = gdf_velov['capacity'].astype(int)

    # On retourne les données
    return gdf_velov


def get_station_status() -> pd.DataFrame:
    '''
    Wrapper de l'API JCDecaux pour récupérer l'occupation des stations Velo'v en direct
    '''

    # On récupère les données sur l'API

    # On ne garde que les colonnes qui nous intéressent
    donnees_velov = donnees_velov[['station_id', 'num_bikes_available', 'num_docks_available', 'last_reported']]

    # On s'assure que les colonnes ont les bons types
    donnees_velov['station_id'] = 
    donnees_velov['num_bikes_available'] = 
    donnees_velov['num_docks_available'] = 
    donnees_velov['last_reported'] = pd.to_datetime(donnees_velov['last_reported'], unit='s')

    # On retourne les données
    return donnees_velov


### LES FONCTIONS SUIVANTES SONT OPTIONNELLES (ACTIONS SUR UNE BASE DE DONNEES POSTGRESQL)

def update_local_stations(station_information: gpd.GeoDataFrame):
    '''
    Met à jour la base de données locale avec les informations sur les stations fournies
    '''


    return


def update_local_status(station_status: pd.DataFrame):
    '''
    Met à jour la base de données locale avec les informations sur l'occupation des stations fournies
    '''


    return


def join_db_data(output_file: str=None) -> gpd.GeoDataFrame:
    '''
    Jointure des données des stations et de leur occupation depuis la base de données locale.
    Si output_file est renseigné, les données sont sauvegardées dans un fichier GeoPackage.
    '''
    

    return gdf_velov