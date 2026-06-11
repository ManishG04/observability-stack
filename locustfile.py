from locust import HttpUser, task, constant_throughput

class FastApiUser(HttpUser):

    @task(1)
    def index_page(self):
        self.client.get("/")

    @task(1) 
    def heavy_process(self):
        # We use a with block to mark the 500 status code as "expected" 
        # so it doesn't fail the locust test purely because of our simulated failure.
        # If you prefer to see them as failures in Locust, you can just do: self.client.get("/heavy")
        with self.client.get("/heavy", catch_response=True) as response:
            if response.status_code == 500:
                response.success()
