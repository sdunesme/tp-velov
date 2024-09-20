import numpy as np
import rasterio as rio
import geopandas as gpd
from rasterio.features import geometry_mask
from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points


def velos_proches(input_gdf: gpd.GeoDataFrame, output_raster: str=None) -> np.array:
   '''
   Cartographier la distance au vélo disponible le plus proche en temps réel.
   Si le paramètre output_raster est renseigné, la fonction doit sauvegarder le raster en sortie.
   '''
   

   return


def nombre_velos_proches(input_gdf: gpd.GeoDataFrame, rayon_recherche: float=500.0, output_raster: str=None) -> np.array:
   '''
   Cartographier le nombre de vélos disponibles dans un rayon défini (valeur par défaut de 500m).
   Si le paramètre output_raster est renseigné, la fonction doit sauvegarder le raster en sortie.
   '''
   

   return 