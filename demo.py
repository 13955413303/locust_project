import random

from locust import HttpLocust, TaskSet, task, HttpUser, between, Locust
import time

'''
1. HttpUser 类，非HttpLocust,Locust
2. tasks = [], 非 task_set
3. weight:行为权重
4. task(1),task(3) 任务权重
5. catch_response 参数与 with 语句一起使用，手动把 HTTP 的错误请求在统计信息中用正确作为测试报告：


'''


class Gitbehavior(TaskSet):
    @task(1)
    def github_index(self):
        with self.client.get("/", catch_response=True) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(
                    '/ got wrong resp! code:' + str(resp.status_code) + ' ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                            time.localtime()))

    @task(0)
    def github_microsoft(self):
        with self.client.get("/microsoft/", catch_response=True)as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure('/microsoft/ got wrong resp! code:' + str(resp.status_code) + ' ' + time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime()))

    @task(0)
    def github_login(self):
        with self.client.get("/login/", catch_response=True)as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(
                     '/login/ got wrong resp! code:' + str(resp.status_code) + ' ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                                  time.localtime()))


class Webbehavior(TaskSet):
    @task(1)
    def web_index(self):
        with self.client.get("/", catch_response=True) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(
                    '/ got wrong resp! code:' + str(resp.status_code) + ' ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                            time.localtime()))

    @task(2)
    def web_111(self):
        with self.client.get("/111.html", catch_response=True)as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure('/111.templates got wrong resp! code:' + str(resp.status_code) + ' ' + time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime()))

    @task(3)
    def web_test(self):
        name = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 3))
        age = random.randint(1, 150)
        with self.client.get(":5000/test_1.0", catch_response=True, params={'name': name, 'age': age})as resp:
            print(resp.text)
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(
                    '/test_1.0 got wrong resp! code:' + str(resp.status_code) + ' ' + time.strftime(
                        "%Y-%m-%d %H:%M:%S",
                        time.localtime()))


class WebsiteUser(HttpUser):
    weight = 0
    tasks = [Gitbehavior]
    min_wait = 1000
    max_wait = 2000


class MobleUser(HttpUser):
    weight = 1
    tasks = [Webbehavior]
    min_wait = 1000
    max_wait = 2000
