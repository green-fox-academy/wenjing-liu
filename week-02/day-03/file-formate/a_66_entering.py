import csv
import json

def a_six_entering(src, des):
  try:
    with open(src, 'r') as file:
      with open(des, 'w') as outfile: 
        content_map = {}
        reader = csv.reader(file, delimiter=',')
        for row in reader:
          if not row:
            continue
          door_num = row[-1]
          content_map[door_num] = content_map.get(door_num, {})
          date_time = row[1]
          day = date_time.split(' ')[0]
          content_map[door_num][day] = content_map[door_num].get(day, 0) + 1
        json.dump(content_map, outfile)
  except Exception as e:
    print(f'Error occurs when reading file {src}: {e}')
    return False

a_six_entering('logs.csv',' a_six_entering.json')