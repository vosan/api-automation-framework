"""
Domain-specific assertions for Category API.
"""
from models import CategoryResponse


class CategoryAssertions:
    """
    Reusable assertions for Category API responses.
    """

    @staticmethod
    def assert_category_name(response: CategoryResponse, expected_name: str) -> None:
        """
        Asserts that the category name matches the expected name.
        """
        assert response.Name == expected_name, \
            f"Expected category name '{expected_name}', but got '{response.Name}'"

    @staticmethod
    def assert_can_relist(response: CategoryResponse, expected_can_relist: bool) -> None:
        """
        Asserts that the CanRelist flag matches the expected value.
        """
        assert response.CanRelist == expected_can_relist, \
            f"Expected CanRelist to be {expected_can_relist}, but got {response.CanRelist}"

    @staticmethod
    def assert_gallery_promotion_description_contains(response: CategoryResponse, expected_substring: str) -> None:
        """
        Locates the 'Gallery' promotion and asserts its description contains the expected substring.
        """
        gallery_promo = next((p for p in response.Promotions if p.Name == "Gallery"), None)

        assert gallery_promo is not None, "Promotion with Name='Gallery' was not found in the response"
        assert expected_substring in gallery_promo.Description, \
            f"Expected Gallery promotion description to contain '{expected_substring}', but got '{gallery_promo.Description}'"
