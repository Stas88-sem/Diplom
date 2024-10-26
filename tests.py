# Шубин Стас, 22-я когорта — Финальный проект. Инженер по тестированию плюс
import request
import data

def test_order_info():
    track_numer = request.create_order(data.body).json()["track"]
    response = request.order_info(track_numer)
    assert response.status_code == 200
