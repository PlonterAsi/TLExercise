from fixtures import zeroIp

def test_exteral_ip_info_full_json(zeroIp):
  import logging
  logging.info(zeroIp.getIpinfo())
  assert zeroIp.getIpinfo().__eq__(
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

def test_city_info(zeroIp):
  assert zeroIp.getSpecificInfo("city") == "Tel Aviv"

def test_region_info(zeroIp):
  assert zeroIp.getSpecificInfo("region") == "Tel Aviv"

def test_country_info(zeroIp):
  assert zeroIp.getSpecificInfo("country") == "IL"

def test_postal_info(zeroIp):
  assert zeroIp.getSpecificInfo("postal") == ""

def test_time_zone_info(zeroIp):
  assert zeroIp.getSpecificInfo("timezone") == "Asia/Jerusalem"