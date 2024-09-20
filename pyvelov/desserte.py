import geopandas as gpd
from shapely.ops import unary_union

def zone_desservie(input_data: gpd.GeoDataFrame, output_file: str=None) -> gpd.GeoDataFrame:
    '''
    Créer une zone tampon desservie par les stations Velo'v.
    Si le paramètre output_file est renseigné, la fonction doit sauvegarder les données en sortie dans un fichier GeoPackage.
    '''


    return output_gdf