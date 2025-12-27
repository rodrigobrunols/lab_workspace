from datetime import datetime, timedelta
import uuid
from enum import Enum
from typing import Dict, List


class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.meetings = set()

    def __repr__(self):
        return f"Participant(name={self.name}, email={self.email})"

    def __eq__(self, other):
        if not isinstance(other, Participant):
            return False
        return self.name == other.name and self.email == other.email

    def __hash__(self):
        return hash((self.name, self.email))



class MeetingRoom:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        # self.scheduled_meetings: Dict[datetime, List[Meeting]] = {}
        self.scheduled_meetings = {}

    def __repr__(self):
        return f"MeetingRoom({self.name}, {self.capacity})"
        # {date: [meetings]}


class MeetingStatus(Enum):
    Scheduled = 1
    In_Progress = 2
    Cancelled = 3


class Meeting:
    def __init__(self, title, organizer, start_time, duration_minutes, participants, room=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.organizer = organizer
        self.start_time = start_time
        self.duration = duration_minutes
        self.end_time = self.start_time + timedelta(minutes=duration_minutes)
        self.room = room
        self.participants = {organizer, participants}
        self.status = MeetingStatus.Scheduled

    def add_participant(self, participant):
        if participant not in self.participants:
            self.participants.add(participant)
            participant.meetings.add(self)
            return True
        return False

    def remove_participant(self, participant):
        if participant in self.participants and participant != self.organizer:
            self.participants.remove(participant)
            participant.meetings.remove(self)
            return True
        return False


    def reschedule(self, new_start_time, new_room=None):
        self.start_time = new_start_time
        self.end_time = new_start_time + timedelta(minutes=self.duration)
        if new_room:
            self.room = new_room
        return True

    def cancel(self):
        for participant in list(self.participants):
            participant.meetings.remove(self)
        self.participants.clear()
        self.status = MeetingStatus.Cancelled
        return True

    def __repr__(self):
        return f"Meeting({self.title}, {self.start_time}, {self.room})"


class MeetingScheduler:
    def __init__(self):
        self.participants = {}
        self.rooms = {}
        self.meetings = {}

    def add_participant(self, name, email):
        if email not in self.participants:
            self.participants[email] = Participant(name, email)
            return True
        return False

    def add_room(self, name, capacity, location):
        if name not in self.rooms:
            self.rooms[name] = MeetingRoom(name, capacity, location)
            return True
        return False

    def find_available_rooms(self, start_time, duration_minutes, min_capacity=1):
        end_time = start_time + timedelta(minutes=duration_minutes)
        available_rooms = []

        for room in self.rooms.values():
            if room.capacity < min_capacity:
                continue

            conflicting_meetings = False
            date_key = start_time.date()

            if date_key in room.scheduled_meetings:
                for meeting in room.scheduled_meetings[date_key]:
                    if not (end_time <= meeting.start_time or start_time >= meeting.end_time):
                        conflicting_meetings = True
                        break

            if not conflicting_meetings:
                available_rooms.append(room)

        return available_rooms


    def schedule_meeting(self, title, organizer_email, start_time, duration_minutes, participants):
        if organizer_email not in self.participants:
            raise ValueError("Organizer not found")

        organizer = self.participants[organizer_email]

        available_rooms = self.find_available_room(start_time, duration_minutes)
        if not available_rooms:
            raise ValueError("No Available Rooms")

        room = available_rooms[0]
        # Create meeting
        meeting = Meeting(title, organizer, start_time, duration_minutes, room)

        # Add to room's schedule
        date_key = start_time.date()
        if date_key not in room.scheduled_meetings:
            room.scheduled_meetings[date_key] = []
        room.scheduled_meetings[date_key].append(meeting)

        organizer.meetings.add(meeting)
        self.meetings[meeting.id] = meeting

        return meeting







