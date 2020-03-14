from locust import HttpLocust, TaskSet, between, task
from random import randrange

urlPets = "https://petstore.swagger.io/v2/pet/"
urlStore = "https://petstore.swagger.io/v2/store/order"

class FullCycle(TaskSet):

    @task(5)
    def createStore(self):
        storeId = randrange(10000)
        petId = randrange(10000)
        data = {
            "id": str(storeId),
            "petId": str(petId),
            "quantity": "1000",
            "shipDate": "2020-03-14T09:24:15.509Z",
            "status": "placed",
            "complete": "true"
        }
        self.client.post(urlStore, json=data)

    @task(5)
    def getPets(self):
        num = randrange(10)
        self.client.get(urlPets + str(num))

class StartCycle(HttpLocust):
    task_set = FullCycle
    wait_time = between(5.0, 9.0)