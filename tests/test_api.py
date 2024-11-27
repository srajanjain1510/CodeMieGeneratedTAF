def test_sample_endpoint(api_client, config):
    endpoint = config['endpoints']['sample_endpoint']
    response = api_client.get(endpoint)
    assert response.status_code == 200