from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.address_dict = {}
        self.build_address_dictionary()

    def build_address_dictionary(self):
        for tree in self.__data:
            self._recursive_build_address_dictionary(tree, '')

    def _recursive_build_address_dictionary(self, area, current_address):
        current_address += area.name + ', '
        self.address_dict[area.id] = current_address[:-2]
        for child in area.areas:
            self._recursive_build_address_dictionary(child, current_address)

    """
        TODO:
        Сделать функцию перебора дерева:
        - Для каждого узла сохранять в словарь адресов
    """
    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Возвращать данные из словаря с адресами
        """
        return self.address_dict.get(area_id, "Адресс не найден")
