import pytest
from django.test import Client

@pytest.mark.django_db
def test_homepage_status_code():
    """
    測試首頁是否能正確回傳 HTTP 200
    """
    client = Client()
    response = client.get('/')
    assert response.status_code == 200