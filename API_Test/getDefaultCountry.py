import pytest
import requests
import json

def test_default_country():
    url = "https://demo.spreecommerce.org/api/v2/storefront/countries/default"
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(j)
    assert resp.status_code == 200, resp.text
    assert j['data']['attributes']['iso3'] == "USA", resp.text
