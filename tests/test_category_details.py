from clients import CategoryClient
from assertions import CategoryAssertions


def test_category_details() -> None:
    """
    Validates category details for 'Carbon credits' (ID: 6327).
    
    Acceptance Criteria:
    - Name is 'Carbon credits'
    - CanRelist is true
    - 'Gallery' promotion description contains 'Good position in category'
    """
    # Initialize client
    client = CategoryClient()

    # Retrieve category details
    # Note: Default ID is 6327, so we can call without parameters
    response = client.get_category_details()

    # Perform validations
    CategoryAssertions.assert_category_name(response, "Carbon credits")
    CategoryAssertions.assert_can_relist(response, True)
    CategoryAssertions.assert_gallery_promotion_description_contains(response, "Good position in category")
