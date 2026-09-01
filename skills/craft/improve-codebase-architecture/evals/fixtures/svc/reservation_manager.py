from .reservation_store import ReservationStore


class ReservationManager:
    def __init__(self):
        self.store = ReservationStore()

    def get(self, res_id):
        return self.store.get(res_id)

    def save(self, res):
        return self.store.save(res)

    def delete(self, res_id):
        return self.store.delete(res_id)

    def list_for_hotel(self, hotel_id):
        return self.store.list_for_hotel(hotel_id)
