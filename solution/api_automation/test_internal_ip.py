from fixtures import internalIp
import logging

def test_internal_ip_info_full_json(internalIp):
    assert internalIp.getIpinfo().__eq__(
        {"ip": "172.20.15.42", "bogon": True}
    )

def test_city_info(internalIp):
  assert internalIp.getSpecificInfo("city", 400).__contains__('"status": 400')

def test_region_info(internalIp):
    assert internalIp.getSpecificInfo("region", 400).__contains__('"status": 400')

def test_country_info(internalIp):
    assert internalIp.getSpecificInfo("country", 400).__contains__('"status": 400')

def test_postal_info(internalIp):
    assert internalIp.getSpecificInfo("postal", 400).__contains__('"status": 400')

def test_time_zone_info(internalIp):
    assert internalIp.getSpecificInfo("timezone", 400).__contains__('"status": 400')