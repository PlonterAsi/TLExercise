import logging
from fixtures import googleDnsIp

def test_ip_info_full_json(googleDnsIp):
    assert googleDnsIp.getIpinfo().__eq__(
        {
            "ip": "8.8.8.8",
            "hostname": "dns.google",
            "anycast": True,
            "city": "Mountain View",
            "region": "California",
            "country": "US",
            "loc": "37.4056,-122.0775",
            "org": "AS15169 Google LLC",
            "postal": "94043",
            "timezone": "America/Los_Angeles",
            "readme": "https://ipinfo.io/missingauth",
        }
    )

def test_city_info(googleDnsIp):
    assert googleDnsIp.getSpecificInfo("city") == "Mountain View"

def test_region_info(googleDnsIp):
    assert googleDnsIp.getSpecificInfo("region") == "California"

def test_country_info(googleDnsIp):
    assert googleDnsIp.getSpecificInfo("country") == "US"

def test_postal_info(googleDnsIp):
    assert googleDnsIp.getSpecificInfo("postal") == "94043"

def test_time_zone_info(googleDnsIp):
    assert googleDnsIp.getSpecificInfo("timezone") == "America/Los_Angeles"