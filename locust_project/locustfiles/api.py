from locust import HttpLocust, TaskSet, task, HttpUser, between, Locust
import time

class Userbehavior(TaskSet):
    @task(1)
    def github_index(self):
        with self.client.get("/", catch_response=True) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure('/ got wrong resp! code:'+str(resp.status_code)+' '+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    @task(2)
    def github_microsoft(self):
        with self.client.get("/microsoft/", catch_response=True)as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure('/microsoft/ got wrong resp! code:'+str(resp.status_code)+' '+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    @task(3)
    def github_login(self):
        with self.client.get("/login/", catch_response=True)as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure('/login/ got wrong resp! code:'+str(resp.status_code)+' '+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
