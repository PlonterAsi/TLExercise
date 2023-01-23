from fixtures import externalIp

def test_exteral_ip_info_full_json(externalIp):
    assert externalIp.getIpinfo().__eq__(
        {
            "ip": "91.90.143.5",
            "city": "Tel Aviv",
            "region": "Tel Aviv",
            "country": "IL",
            "loc": "32.0809,34.7806",
            "org": "AS25046 Check Point Software Technologies LTD",
            "timezone": "Asia/Jerusalem",
            "readme": "https://ipinfo.io/missingauth",
        }
    )

def test_city_info(externalIp):
  assert externalIp.getSpecificInfo("city") == "Tel Aviv"

def test_region_info(externalIp):
  assert externalIp.getSpecificInfo("region") == "Tel Aviv"

def test_country_info(externalIp):
  assert externalIp.getSpecificInfo("country") == "IL"

def test_postal_info(externalIp):
  assert externalIp.getSpecificInfo("postal") == ""

def test_time_zone_info(externalIp):
  assert externalIp.getSpecificInfo("timezone") == "Asia/Jerusalem"