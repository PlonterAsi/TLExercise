import requests
from typing import Literal

class IpInfoAPI():
  def __init__(self, ip: str) -> None:
    self.ip = ip
    self.url = f"http://ipinfo.io/{ip}"

  def checkStatusCode(self, status_code: int, expected_status_code):
    if status_code != expected_status_code:
      raise Exception(f"error code is {status_code} expected {expected_status_code}")

  def getIpinfo(self, expected_status_code: int = 200):
    response = requests.get(self.url)
    self.checkStatusCode(response.status_code, expected_status_code)
    return response.json()

  def getSpecificInfo(self, key: Literal["hostname" ,"city" ,"region" ,"country" ,"postal" ,"timezone"], expected_sc: int = 200):
    response = requests.get(f"{self.url}/{key}")
    self.checkStatusCode(response.status_code, expected_sc)
    return response.text.strip()
