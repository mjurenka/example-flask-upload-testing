import io

def test_upload_textfile(test_client):
    file = "random-file.txt"
    data = {
        'image': (open(file, 'rb'), file)
    }
    response = test_client.post('/upload', data=data)
    assert response.status_code == 400

def test_upload_image_file(test_client):
    image = "pizza-cat.jpg"
    data = {
        'image': (open(image, 'rb'), image)
    }
    response = test_client.post('/upload', data=data)
    assert response.status_code == 201
    assert response.json['file'] == image

def test_upload_image_stream(test_client):
    image_name = "fake-image-stream.jpg"
    data = {
        'image': (io.BytesIO(b"some random data"), image_name)
    }
    response = test_client.post('/upload', data=data)
    assert response.status_code == 201
    assert response.json['file'] == image_name