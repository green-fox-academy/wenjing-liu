import csv
import json

def average_arriving_by_day(src, des):
  try:
    with open(src, 'r') as file:
      content_map = {}
      reader = csv.reader(file, delimiter=',')
      for row in reader:
        if not row or row[5] != 'A66 - 04 FÕBEJÁRAT (F-1) Door #1':
          continue
        date_time = row[1]
        day_time = date_time.split(' ')
        day = day_time[0]
        time = day_time[1]
        content_map[day] = content_map.get(day, {})
        user_id = row[-1]
        content_map[day][user_id] = content_map[day].get(user_id, time)
      average_arr_time = {}
      for key, item in content_map.items():
        total_arriving_time = 0
        for user_id, time in item.items():
          total_arriving_time += time_to_seconds(time)
        average_arr_time[key] = total_arriving_time / len(item)
      write_to_file(des, average_arr_time, 'average arriving time')
  except Exception as e:
    print(f'Error occurs when reading file {src}: {e}')
    return False


def time_to_seconds(time):
  time_array = time.split(':')
  return float(time_array[0]) * 3600 + float(time_array[1]) * 60 + float(time_array[2])

def seconds_to_time(time):
  hour = time // 3600
  minute = (time % 3600) // 60
  second = time % 3600 % 60
  return f'{int(hour)}:{int(minute)}:{int(second)}'

def write_to_file(des, data, key_value):
  with open(des, 'w') as outfile:
    outfile.write('export default')
    result = [{
      "values": []
    }]
    print(result)
    print(data)
    for key, item in data.items():
      result[0]["values"].append({"x": key, "y": item})
    json.dump(result, outfile)


def late_to_not_late_in_mounth(src, des):
  standard_time = 9 * 3600
  late_counter = 0
  not_late_counter = 0
  with open(src, 'r') as file:
    content_map = {}
    reader = csv.reader(file, delimiter=',')
    for row in reader:
      if not row:
        continue
      date_time = row[1]
      day_time = date_time.split(' ')
      day = day_time[0]
      time = day_time[1]
      content_map[day] = content_map.get(day, {})
      user_id = row[-1]
      content_map[day][user_id] = content_map[day].get(user_id, time)
    for key, day in content_map.items():
      for index, time in day.items():
        if time_to_seconds(time) > standard_time:
          late_counter += 1
        else:
          not_late_counter += 1
    result = [{ 
        "label": "Late",
        "value" : late_counter
      },
      {
        "label": "Not Late",
        "value" : not_late_counter
      }]
    with open(des, 'a') as outfile:
      outfile.write('export default')
      json.dump(result, outfile)


def person_in_day(src, des):
   with open(src, 'r') as file:
    content_map = {}
    reader = csv.reader(file, delimiter=',')
    for row in reader:
      if not row:
        continue
      date_time = row[1]
      day_time = date_time.split(' ')
      day = day_time[0]
      time = day_time[1]
      content_map[day] = content_map.get(day, {})
      user_id = row[-1]
      content_map[day][user_id] = content_map[day].get(user_id, time)
    for key, item in content_map.items():
      content_map[key]['counter'] = len(item)
    result = []
    for key, item in content_map.items():
      result.append({
        "label": key,
        "value": item['counter']
      })
    with open(des, 'a') as outfile:
      outfile.write('export default')
      json.dump(result, outfile)
  

average_arriving_by_day('logs.csv','average_arriving_by_day.js')
late_to_not_late_in_mounth('logs.csv', 'lateToNotLate.js')
person_in_day('logs.csv', 'person_in_day.js')