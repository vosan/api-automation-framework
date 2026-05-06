from models import CategoryResponse
from .base_client import BaseClient

class CategoryClient(BaseClient):
    def get_category_details(self, category_id: int = 6327, catalogue: bool = False) -> CategoryResponse:
        """
        Fetches category details and returns a validated CategoryResponse model.
        
        :param category_id: The ID of the category (defaults to 6327).
        :param catalogue: Whether to include catalogue info (defaults to False).
        :return: CategoryResponse model instance.
        """
        endpoint = f"v1/Categories/{category_id}/Details.json"
        params = {"catalogue": str(catalogue).lower()}
        
        response = self.get(endpoint, params=params)
        return CategoryResponse.model_validate(response.json())
