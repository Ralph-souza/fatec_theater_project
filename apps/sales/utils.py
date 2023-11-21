from apps.movies.models import RoomsModel


def get_room_seats(room_id) -> int | None:
    room = RoomsModel.objects.get(id=room_id)
    if room:
        return room.seat
    else:
        return None

def seats_available(room_id):
    seats_available = get_room_seats(room_id=room_id)
    sold_seats = []

    while True:
        for seat in range(1, seats_available + 1):
            sold_seats.append(seat)
            if len(sold_seats) == seats_available:
                return f"All {seats_available} seats are sold"
            