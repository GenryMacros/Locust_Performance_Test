from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(10, 600)
    host = 'http://192.168.0.113:5000'

    @task(60)
    def post_user(self):
        self.client.post("/users", json={
            "login": "firstUser",
            "pass": "firstPassword"
        })

    @task(30)
    def post_channel(self):
        self.client.post("/users/1/channels", json={
            "name": "firstChannel"
        })

    @task(100)
    def get_channel(self):
        self.client.get("/users/1/channels")

    @task(30)
    def post_task(self):
        self.client.post("/users/1/channels/1/tasks", json={
            "name": "firstTask",
        })

    @task(100)
    def get_task(self):
        self.client.get("/users/1/channels/1/tasks")


