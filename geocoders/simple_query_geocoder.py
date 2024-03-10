from geocoders.geocoder import Geocoder
from api import TreeNode, API

# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        tree = API.get_area(area_id)
        decoder = tree.name
        while tree.parent_id is not None:
            tree = API.get_area(tree.parent_id)
            decoder = tree.name + ', ' + decoder
        """
            TODO:
            - Делать запросы к API для каждой area
            - Для каждого ответа формировать полный адрес
        """
        return decoder

