from locust import HttpUser
from api import Userbehavior


class WebsiteUser(HttpUser):
    weight = 1
    tasks = [Userbehavior]
    min_wait = 1000
    max_wait = 2000
