from datetime import datetime, timedelta
from collections import defaultdict


class Inspection:

    def __init__(self, property_id, inspector_id,scheduled_time, duration=timedelta(hours=1) ):
        self.property_id = property_id
        self.inspector_id = inspector_id
        self.scheduled_time = scheduled_time
        self.duration = duration


    def __str__(self):
        return f"Inspection(property_id = {self.property_id}, inspector_id={self.inspector_id}, scheduled_time={self.scheduled_time}, duration={self.duration})"

    def check_overlap(self, new_inspection):
        new_start = new_inspection.scheduled_time
        new_end = new_start + new_inspection.duration

        current_start = self.scheduled_time
        current_end = current_start + self.duration

        return not (new_end < current_start or new_start > current_end)


class InspectionScheduler:

    def __init__(self):
        self.inspection_by_property = defaultdict(list)
        self.inspection_by_inspector = defaultdict(list)


    def add_inspection(self, property_id, inspector_id, scheduled_time):

        new_inspection = Inspection(property_id, inspector_id, scheduled_time)

        if not self.validate_inspector_schedule(new_inspection):
            return False

        if not self.validate_property_schedule(new_inspection):
            return False

        if not self.inspection_by_property:
            self.inspection_by_property[property_id] = []
        self.inspection_by_property[property_id].append(new_inspection)

        if not self.inspection_by_inspector:
            self.inspection_by_inspector[inspector_id] = []
        self.inspection_by_property[inspector_id].append(new_inspection)

        print(f"Inspection scheduled successfully: {new_inspection}")
        return True


    def validate_inspector_schedule(self, inspection: Inspection):
        #     	validate property already visited
        for old_inspection in self.inspection_by_inspector[inspection.inspector_id]:
            if old_inspection.property_id == inspection.property_id:
                print(f"Property already visited by inspector {inspection.inspector_id}!")
                return False
                #       validate inspector schedule overlap
            if old_inspection.check_overlap(inspection):
                print(f"Schedule overlap for inspector {inspection.inspector_id}!")
            return False


    def validate_property_schedule(self, inspection: Inspection):
        # 		validate property schedule overlap
        for old_inspection in self.inspection_by_property[inspection.property_id]:
            if old_inspection.check_overlap(inspection):
                print(f"Schedule overlap for property {inspection.property_id}!")
                return False


