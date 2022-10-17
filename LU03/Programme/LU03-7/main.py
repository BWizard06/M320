from reservation import Reservation
from customer import Customer



if __name__ == "__main__":
    reservation = Reservation("456-332", "Queen das Musical")
    julian = Customer("Julian", reservation)
    julian.print()
    reservation.customer = julian
    reservation.print()
