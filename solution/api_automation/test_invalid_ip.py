from fixtures import invalidIPHigh, invalidIPLong
import logging

invalid_ip_response = {
            "status": 404,
            "error": {
                "title": "Wrong ip",
                "message": "Please provide a valid IP address",
            },
        }

def test_invalid_ip_format_ip_info_full_json(invalidIPLong):
    assert invalidIPLong.getIpinfo(404).__eq__(invalid_ip_response)

def test_invalid_ip_octate_ip_info_full_json(invalidIPHigh):
    assert invalidIPHigh.getIpinfo(404).__eq__(invalid_ip_response)

def test_city_info(invalidIPLong):
    assert invalidIPLong.getSpecificInfo("city", 404).__contains__('"status": 404')

def test_region_info(invalidIPLong):
    assert invalidIPLong.getSpecificInfo("region", 404).__contains__('"status": 404')

def test_country_info(invalidIPLong):
    assert invalidIPLong.getSpecificInfo("country", 404).__contains__('"status": 404')

def test_postal_info(invalidIPLong):
    assert invalidIPLong.getSpecificInfo("postal", 404).__contains__('"status": 404')

def test_time_zone_info(invalidIPLong):
    assert invalidIPLong.getSpecificInfo("timezone", 404).__contains__('"status": 404')
