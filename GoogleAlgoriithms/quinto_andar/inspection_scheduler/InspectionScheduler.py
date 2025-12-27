
from datetime import datetime, timedelta
from collections import defaultdict

"""
     Requirements:
     Same inspector cant repeat a house
     Do not overlap inspectors at same time
"""


class Inspection:
    def __init__(self, house_id, inspector_id, scheduled_time, duration=timedelta(hours=1)):
        self.house_id = house_id
        self.inspector_id = inspector_id
        self.scheduled_time = scheduled_time
        self.duration = duration

    def check_overlap(self, new_inspection):
        existing_start = self.scheduled_time
        existing_end = existing_start + self.duration

        new_start = new_inspection.scheduled_time
        new_end = new_start + new_inspection.duration

        return existing_start <= new_start < existing_end or existing_start < new_end <= existing_end

    def __eq__(self, other):
        if not isinstance(other, Inspection):
            return False
        return (self.house_id == other.house_id and
                self.inspector_id == other.inspector_id and
                self.duration == other.duration and
                self.scheduled_time == other.scheduled_time)

    def __hash__(self):
        return hash((self.house_id, self.inspector_id,
                     self.scheduled_time, self.duration))

    def __repr__(self):
        return f"Inspection(house_id = {self.house_id}, inspector_id={self.inspector_id}, scheduled_time={self.scheduled_time})"


class InspectionScheduler:
    def __init__(self):
        self.inspection_by_house = defaultdict(list)
        self.inspection_by_inspector = defaultdict(list)

    def schedule_inspection(self, house_id, inspector_id, schedule_time):
        new_inspection = Inspection(house_id, inspector_id, schedule_time)

        # validate inspector overlap
        if inspector_id in self.inspection_by_inspector:
            for inspection in self.inspection_by_inspector[inspector_id]:
                if inspection.house_id == house_id:
                    print(f"House already visited by inspector: {inspector_id}")
                    return False
                if inspection.check_overlap(new_inspection):
                    print(f"Inspector inspection time overlap for inspector: {inspector_id}")
                    return False

        # validate house overlap
        if house_id in self.inspection_by_house:
            for inspection in self.inspection_by_house[house_id]:
                if inspection.check_overlap(new_inspection):
                    print(f"House inspection time overlap for house: {house_id}")
                    return False

        if house_id not in self.inspection_by_house:
            self.inspection_by_house[house_id] = []
        self.inspection_by_house.get(house_id, []).append(new_inspection)

        if inspector_id not in self.inspection_by_inspector:
            self.inspection_by_inspector[inspector_id] = []
        self.inspection_by_inspector.get(inspector_id).append(new_inspection)

        # print(f"Inspections for house {house_id}:", self.get_inspections_by_house(house_id))
        # print(f"Inspections for inspector {inspector_id}:", self.get_inspections_by_inspector(inspector_id))
        print(f"Inspection scheduled successfully: {new_inspection}")
        return True

    def get_inspections_by_house(self, property_id):
        return self.inspection_by_house[property_id]

    def get_inspections_by_inspector(self, inspector_id):
        return self.inspection_by_inspector[inspector_id]

    # def check_overlap(self, existing_inspection: Inspection, new_inspection: Inspection):
    #     existing_start = existing_inspection.scheduled_time
    #     existing_end = existing_start + existing_inspection.duration
    #
    #     new_start = new_inspection.scheduled_time
    #     new_end = new_start + new_inspection.duration
    #
    #     return existing_start < new_start < existing_end or existing_start < new_end < existing_end



if __name__ == "__main__":

    scheduler = InspectionScheduler()

    today = datetime.now()
    tomorrow = today + timedelta(days=1)

    scheduler.schedule_inspection("house1", "inspector1", today.replace(hour=10, minute=0))
    scheduler.schedule_inspection("house2", "inspector1", today.replace(hour=11, minute=0))
    scheduler.schedule_inspection("house3", "inspector2", today.replace(hour=10, minute=0))

    scheduler.schedule_inspection("house1", "inspector3", today.replace(hour=10, minute=30))  # Time conflict for house1
    scheduler.schedule_inspection("house4", "inspector1", today.replace(hour=10, minute=2))   # Time conflict for inspector1
    scheduler.schedule_inspection("house1", "inspector1", tomorrow.replace(hour=10, minute=0)) # Same inspector for same house


