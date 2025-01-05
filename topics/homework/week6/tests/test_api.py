from unittest.mock import Mock, patch

import pytest
import requests
import requests.exceptions
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Define the schema for validating the post response
post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}


# Pytest fixture for base URL
@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"


# Pytest fixture for common headers
@pytest.fixture(scope="module")
def headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


# Pytest fixture for creating dummy data for new posts
@pytest.fixture(scope="function")
def new_post_payload():
    return {
        "userId": 1,
        "title": "New Post",
        "body": "This is a new post"
    }


# Test for fetching a post and validating its structure and data
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_fetch_post(base_url, headers, post_id):
    """
    Test to fetch a post by ID and validate its structure and data.
    """
    try:
        response = requests.get(f"{base_url}/posts/{post_id}", headers=headers)
        assert response.status_code == 200
        validate(instance=response.json(), schema=post_schema)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")


# Test for creating a new post
def test_create_post(base_url, headers, new_post_payload):
    """
    Test to create a new post and verify the response code and payload.
    """
    try:
        response = requests.post(f"{base_url}/posts", headers=headers, json=new_post_payload)
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["title"] == new_post_payload["title"]
        assert response_data["body"] == new_post_payload["body"]
        assert "id" in response_data  # New post should have an ID assigned
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


# Test for updating a post
@pytest.mark.parametrize("post_id", [1])
def test_update_post(base_url, headers, post_id, new_post_payload):
    """
    Test to update a post and check for proper updates.
    """
    updated_payload = new_post_payload.copy()
    updated_payload["title"] = "Updated Title"
    try:
        response = requests.put(f"{base_url}/posts/{post_id}", headers=headers, json=updated_payload)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["title"] == "Updated Title"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


# Test for deleting a post
@pytest.mark.parametrize("post_id", [1])
def test_delete_post(base_url, headers, post_id):
    """
    Test to delete a post and confirm its removal.
    Since JSONPlaceholder is a fake API, it will still return 200 even after deletion.
    """
    try:
        response = requests.delete(f"{base_url}/posts/{post_id}", headers=headers)
        assert response.status_code == 200
        # Further validation can be done by trying to fetch the deleted post
        fetch_response = requests.get(f"{base_url}/posts/{post_id}", headers=headers)
        assert fetch_response.status_code == 200  # Adjusting expectation due to API behavior
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


# Mock tests
@patch('requests.get')
def test_mock_fetch_post_failure(mock_get, base_url, headers):
    """
    Mock test simulating a failed GET request due to server error.
    """
    mock_get.return_value = Mock(status_code=500)
    response = requests.get(f"{base_url}/posts/1", headers=headers)
    assert response.status_code == 500


@patch('requests.post')
def test_mock_create_post_failure(mock_post, base_url, headers, new_post_payload):
    """
    Mock test simulating a failed POST request due to server error.
    """
    mock_post.return_value = Mock(status_code=500)
    response = requests.post(f"{base_url}/posts", headers=headers, json=new_post_payload)
    assert response.status_code == 500


@patch('requests.put')
def test_mock_update_post_failure(mock_put, base_url, headers, new_post_payload):
    """
    Mock test simulating a failed PUT request due to server error.
    """
    mock_put.return_value = Mock(status_code=500)
    response = requests.put(f"{base_url}/posts/1", headers=headers, json=new_post_payload)
    assert response.status_code == 500


@patch('requests.delete')
def test_mock_delete_post_failure(mock_delete, base_url, headers):
    """
    Mock test simulating a failed DELETE request due to server error.
    """
    mock_delete.return_value = Mock(status_code=500)
    response = requests.delete(f"{base_url}/posts/1", headers=headers)
    assert response.status_code == 500


# Tests for /comments endpoint
def test_fetch_comments(base_url, headers):
    """
    Test fetching comments and validating response.
    """
    try:
        response = requests.get(f"{base_url}/comments", headers=headers)
        assert response.status_code == 200
        comments = response.json()
        assert isinstance(comments, list)  # Expecting a list of comments
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


def test_filter_comments_by_post_id(base_url, headers):
    """
    Test filtering comments by post ID.
    """
    post_id = 1
    try:
        response = requests.get(f"{base_url}/comments?postId={post_id}", headers=headers)
        assert response.status_code == 200
        comments = response.json()
        assert all(
            comment['postId'] == post_id for comment in comments)  # All comments should belong to the specified post
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")
