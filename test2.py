import docker
import requests
import pytest

client = docker.from_env()
@pytest.fixture(scope="session")
def my_image():
    image, logs = client.images.build(path="path/to/dockerfile", tag="my-image")
    assert "Successfully built" in logs
    return image

@pytest.fixture(scope="session")
def nginx():
    image = client.images.pull("nginx:latest")
    return image



def test_nginx_availability(nginx):
    container = client.containers.run("nginx:latest", detach=True)
    response = requests.get("http://localhost/")
    assert response.status_code == 200
    container.stop()
    container.remove()




@pytest.fixture(scope="session")
def load_test_image():
    image = client.images.pull("weaveworksdemos/load-test:latest")
    return image


def test_load_test_image_availability(load_test_image):
    container = client.containers.run("weaveworksdemos/load-test:latest", detach=True)
    response = requests.get("http://localhost/")
    assert response.status_code == 200  
    container.stop()
    container.remove()


@pytest.fixture(scope="session")
def user_image():
    image = client.images.pull("weaveworksdemos/user:latest")
    return image

def test_user_image_availability(user_image):
    container = client.containers.run("weaveworksdemos/user:latest", detach=True)
    response = requests.get("http://localhost/")
    assert response.status_code == 200
    container.stop()
    container.remove()

@pytest.fixture(scope="session")
def payment_image():
    image = client.images.pull("weaveworksdemos/payment:latest")
    return image

def test_payment_image_availability(payment_image):
    container = client.containers.run("weaveworksdemos/payment:latest", detach=True)
    response = requests.get("http://localhost:8080")
    assert response.status_code == 200
    container.stop()
    container.remove()


@pytest.fixture(scope="session")
def front_end_image():
    image = client.images.pull("weaveworksdemos/front-end:latest")
    return image

def test_front_end_image_availability(front_end_image):
    container = client.containers.run("weaveworksdemos/front-end:latest", detach=True)
    response = requests.get("http://localhost:8080")
    assert response.status_code == 200
    container.stop()
    container.remove()

@pytest.fixture(scope="session")
def shipping_image():
    image = client.images.pull("weaveworksdemos/shipping:latest")
    return image

def test_shipping_image_availability(shipping_image):
    container = client.containers.run("weaveworksdemos/shipping:latest", detach=True)
    response = requests.get("http://localhost:8080")
    assert response.status_code == 200
    container.stop()
    container.remove()

@pytest.fixture(scope="session")
def carts_image():
    image = client.images.pull("weaveworksdemos/carts:latest")
    return image

def test_carts_image_availability(carts_image):
    container = client.containers.run("weaveworksdemos/carts:latest", detach=True)
    response = requests.get("http://localhost:8080")
    assert response.status_code == 200
    container.stop()
    container.remove()

@pytest.fixture(scope="session")
def orders_image():
    image = client.images.pull("weaveworksdemos/orders:latest")
    return image

def test_orders_image_availability(orders_image):
    container = client.containers.run("weaveworksdemos/orders:latest", detach=True)
    response = requests.get("http://localhost:8080")
    assert response.status_code == 200
    container.stop()
    container.remove()

@pytest.fixture(scope="session")
def queue_master_image():
    image = client.images.pull("weaveworksdemos/queue-master:latest")
    return image

def test_queue_master_image_availability(queue_master_image):
    container = client.containers.run("weaveworksdemos/queue-master:latest", detach=True)
    response = requests.get("http://localhost/")
    assert response.status_code == 200
    container.stop()
    container.remove()

@pytest.fixture(scope="session")
def edge_router_image():
    image = client.images.pull("weaveworksdemos/edge-router:latest")
    return image

def test_edge_router_image_availability(edge_router_image):
    container = client.containers.run("weaveworksdemos/edge-router:latest", detach=True)
    response = requests.get("http://localhost:80")
    assert response.status_code == 200
    container.stop()
    container.remove()


@pytest.fixture(scope="session")
def catalogue_db_image():
    image = client.images.pull("weaveworksdemos/catalogue-db:latest")
    return image


@pytest.fixture(scope="session")
def user_db_image():
    image = client.images.pull("weaveworksdemos/user-db:latest")
    return image
