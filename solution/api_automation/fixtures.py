import pytest
from ipInfoApi import IpInfoAPI

@pytest.fixture(scope="module")
def networkIp():
  return IpInfoAPI("172.20.15.0")

@pytest.fixture(scope="module")
def zeroIp():
  return IpInfoAPI("0.0.0.0")

@pytest.fixture(scope="module")
def externalIp():
  return IpInfoAPI("91.90.143.5")

@pytest.fixture(scope="module")
def internalIp():
  return IpInfoAPI("172.20.15.42")

@pytest.fixture(scope="module")
def googleDnsIp():
  return IpInfoAPI("8.8.8.8")