from django.test import Client
import pytest


@pytest.mark.django_db
class TestCreateBlogPost:
    def test_create_post_returns_200(self, api_client):
        data = {'title': 'bhvb', 'body': 'thbhb hfbvb'}
        response = api_client.post('/blog/posts/', data=data)
        assert response.status_code == 201

    def test_create_empty_post_title_returns_400(self, api_client):
        data = {'title': '', 'body': 'thbhb hfbvb'}
        response = api_client.post('/blog/posts/', data=data)
        assert response.status_code == 400