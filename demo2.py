"""

Events > Users > TaskSet > task


"""
import time
import random
import logging
from locust.exception import RescheduleTask
from locust.contrib.fasthttp import FastHttpUser

from locust import User, task, between, TaskSet, HttpUser, tag, events
from locust.runners import MasterRunner


@events.test_start.add_listener
def on_start(**kwargs):
    logging.info('this is start')


@events.test_stop.add_listener
def on_stop(**kwargs):
    logging.info('this is end')


@events.request_success.add_listener
def req_success(name, **kwargs):
    logging.info('req_success:%s' % name)


@events.init.add_listener
def on_locust_init(environment, **kwargs):
    if isinstance(environment.runner, MasterRunner):
        logging.info("I'm on master node")
    else:
        logging.info("I'm on a worker or standalone node")


@events.init.add_listener
def on_locust_init(web_ui, **kw):
    @web_ui.app.route("/add_page")
    def my_add_page():
        logging.info('my_add_page')
        return "another"


class Webbehavior(TaskSet):
    @tag('tag1')
    @task(1)
    def web_index(self):
        name = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 3))
        age = random.randint(1, 150)
        # response = self.client.post("/login", {"username": "testuser", "password": "secret"})
        with self.client.get(":5000/test_1.0", name='1.0', catch_response=True,
                             params={'name': name, 'age': age})as resp:
            # if resp.elapsed.total_seconds():
            # pass
            # print(resp.read())
            if resp.status_code == 200:
                # raise RescheduleTask()
                resp.success()
            else:
                resp.failure(
                    '/test_1.0 got wrong resp! code:' + str(resp.status_code) + ' ' + time.strftime(
                        "%Y-%m-%d %H:%M:%S",
                        time.localtime()))


class MyUser(HttpUser):
    # tasks = [Webbehavior,Gitbehavior]
    tasks = {Webbehavior: 1}
    # abstract = True
    wait_time = between(5, 10)

    # @task
    # def my_task(self):
    #     print("executing my_task")
    #     self.environment.runner.quit()

    # host = r'http://www.baidu.com'
    def on_start(self):
        print('start...')

    def on_stop(self):
        print('stop!!!')
