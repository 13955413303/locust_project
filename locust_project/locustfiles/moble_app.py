from locust import HttpLocust, TaskSet, task, HttpUser, between, Locust
from api import Userbehavior


class MobleUser(HttpUser):
    weight = 2
    tasks = [Userbehavior]
    min_wait = 1000
    max_wait = 2000