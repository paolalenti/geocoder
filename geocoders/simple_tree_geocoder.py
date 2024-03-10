from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def find_branch(self, area_id, current_tree=None):
        if current_tree is None:
            for tree in self.__data:
                if tree.id == area_id:
                    return [tree]
                result = self.find_branch(area_id, tree)
                if result:
                    return [tree] + result
        else:
            if current_tree.id == area_id:
                return [current_tree]
            if current_tree.areas:
                for child in current_tree.areas:
                    result = self.find_branch(area_id, child)
                    if result:
                        return [current_tree] + result
        return []
    def _apply_geocoding(self, area_id: str) -> str:
        branch = self.find_branch(area_id)
        if not branch:
            return "Адрес не найден"

        address_parts = [node.name for node in branch]
        if len(address_parts) > 1:
            full_address = ', '.join(address_parts[1:])
        else:
            full_address = ', '.join(address_parts)
        return full_address

        """
            TODO:
            - Сделать перебор дерева для каждого area_id
            - В ходе перебора возвращать массив элементов, состоящих из TreeNode необходимой ветки
            - Из массива TreeNode составить полный адрес
        """
