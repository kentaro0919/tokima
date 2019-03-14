import logging

"""Akamai EdgeGrid Settings."""

from masonite import env
from masonite.environment import LoadEnvironment
import requests
from akamai.edgegrid import EdgeGridAuth
from urllib.parse import urljoin
from types import SimpleNamespace
from urllib import parse

"""Load Environment Variables
Loads in the environment variables when this page is imported.

Add the following lines to .env file
EG_SECTION =
"""

LoadEnvironment()

"""EdgeGrid Settings
"""
EDGEGRID = {
    "section": env("EG_SECTION", "billingcenter"),
    "client_secret": env("AKAMAI_CLIENT_SECRET"),
    "host": env("AKAMAI_HOST"),
    "access_token": env("AKAMAI_ACCESS_TOKEN"),
    "client_token": env("AKAMAI_CLIENT_TOKEN"),
}

EG = SimpleNamespace(**EDGEGRID)

s = requests.Session()
BASEURL = "%s://%s/" % ("https", EG.host)
s.auth = EdgeGridAuth(
    client_token=EG.client_token, client_secret=EG.client_secret, access_token=EG.access_token
)


def edgegrid_caller(path, data_string):
    return s.get(parse.urljoin(BASEURL, path), params=data_string)
