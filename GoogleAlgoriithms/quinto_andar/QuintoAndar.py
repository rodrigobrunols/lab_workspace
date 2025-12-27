# check time overlap
import collections
from datetime import datetime, timedelta
import heapq

today = datetime.now()
_day = datetime.strptime("2025-05-22", "%Y-%m-%d")
_hour = datetime.strptime("09:00", '%H:%M').time()
_new_day = _day.replace(hour=10, minute=10)

date_str = "2023-12-25 09:30"
dt_object = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

print(_day)
print(_new_day)
print(_hour)
print(dt_object)

# 1: Check Overlap in Intervals


def check_overlap(times_parameter):
    intervals = []

    for start, end in times_parameter:
        h_start, m_start = start.split(":")
        h_end, m_end = end.split(":")
        temp_start = h_start * 60 + m_start
        temp_end = h_end * 60 + m_end
        intervals.append((temp_start, temp_end))

    intervals.sort()

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return True

    return False


times = [("09:00", "10:00"), ("09:30", "10:30"), ("11:00", "12:00")]
print(check_overlap(times))


scheduled_visits1 = [
    {"casa_id": 1, "inicio": "14:00", "fim": "15:00"},
    {"casa_id": 2, "inicio": "16:00", "fim": "17:00"}
]

new_visit1 = {"casa_id": 3, "inicio": "14:30", "fim": "15:30"}

# 2: Schedule a new visit without conflict


def schedule_visits(scheduled_visits, new_visit):

    def time_to_minutes(time_str):
        hour, minute = time_str.split(":")
        return hour * 60 + minute

    new_start = time_to_minutes(new_visit["inicio"])
    new_end = time_to_minutes((new_visit["fim"]))

    for visit_ in scheduled_visits:
        e_start = time_to_minutes(visit_["inicio"])
        e_end = time_to_minutes((visit_["fim"]))

        if not (new_end < e_start or new_start > e_end):
            return False

    return True


print(schedule_visits(scheduled_visits1, new_visit1) )

# 3: Find Anagrams


def find_anagrams(words):
    anagrams = collections.defaultdict(list)

    for word in words:
        key = ''.join(sorted(word.lower()))
        if key not in anagrams:
            anagrams[key] = []
        anagrams.get(key).append(word)

    return list(anagrams.values())


word_list = ["amor", "roma", "casa", "saca", "ramo", "aroma"]
print("Anagrams-> ", find_anagrams(word_list))
# Output: [['amor', 'roma', 'ramo'], ['casa', 'saca'], ['aroma']]


current_dir = "/home/user/docs"
command = "../images"
# /home/user/docs -> /home/user/images


def exec_command_cd(current_path: str, cd_command: str):

    new_path = ''

    if cd_command.startswith('/'):
        new_path = cd_command.split('/')
    else:
        new_path = current_path.split('/') + cd_command.split('/')

    stack = []
    for directory in new_path:
        if not directory or directory == '.':
            continue
        elif directory == '..':
            stack.pop()
        else:
            stack.append(directory)

    return '/' + '/'.join(stack)


print(exec_command_cd(current_dir, command))

# 5: Optimize Visits


def optimize_routes(visits):
    if not visits:
        return []

    sorted_visits = sorted(visits, key=lambda v: v["hour"])
    return [v["id"] for v in sorted_visits]


visits1 = [
    {"id": 1, "hour": "09:00", "coords": (100, 200)},
    {"id": 2, "hour": "10:00", "coords": (150, 250)},
    {"id": 3, "hour": "11:00", "coords": (50, 300)}
]
print(optimize_routes(visits1))


