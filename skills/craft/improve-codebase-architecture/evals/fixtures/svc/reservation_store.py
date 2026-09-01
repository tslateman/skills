from .db import connect


class ReservationStore:
    def get(self, res_id):
        with connect() as c:
            return c.execute("select * from reservation where id = ?", (res_id,)).fetchone()

    def save(self, res):
        with connect() as c:
            c.execute("insert or replace into reservation values (?)", (res,))

    def delete(self, res_id):
        with connect() as c:
            c.execute("delete from reservation where id = ?", (res_id,))

    def list_for_hotel(self, hotel_id):
        with connect() as c:
            return c.execute(
                "select * from reservation where hotel_id = ?", (hotel_id,)
            ).fetchall()
