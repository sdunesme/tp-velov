import geopandas as gpd
import os

from shapely.geometry import Polygon

from pyvelov import desserte

def test_zone_desservie():
    # On charge le GeoDataFrame de test
    test_data = gpd.read_file('datasets/tests/stations.gpkg')
    
    # On appelle la fonction zoneDesservie
    
    # On vérifie que le fichier a bien été créé
    
    # On vérifie que le GeoDataFrame retourné est bien un GeoDataFrame
    
    # On vérifie que le GeoDataFrame retourné contient bien des Polygons
    
    # On vérifie que le nombre de Polygons retournés est correct
