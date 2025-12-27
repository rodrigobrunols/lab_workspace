
class MeetingScheduler:

    def __init__(self, organizer, calendar):
        self.__organizer = organizer
        self.__calendar = calendar
        self.__rooms = []

    def schedule_meeting(self, users, interval):
        pass

    def cancel_meeting(self, users, interval):
        pass

    def book_room(self, room, number_of_persons, interval):
        pass

    def release_room(self, room, interval):
        pass

    def check_rooms_availability(self, number_of_persons, interval):
        pass


instance = MeetingScheduler(None, None)

