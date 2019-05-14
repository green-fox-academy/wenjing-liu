# Read all data from 'log.txt'.
# Each line represents a log message from a web server
# Write a function that returns an array with the unique IP adresses.
# Write a function that returns the GET / POST request ratio.

REQUEST_TYPE = {
  'GET': 'GET',
  'POST': 'POST'
}

def read_file(file_name):
  try:
    with open(file_name, 'r') as file:
      content = file.readlines()
    return content
  except Exception as e:
    print(f'Read file {file_name} error: {e}')

def get_ip_address(logs):
  ip_address = set()
  for log in logs:
    ip_address.add(list(filter(lambda x: x != '', log.split(' ')))[5])
  return ip_address

def get_post_ratio(logs):
  get_counter = 0
  post_counter = 0
  for log in logs:
    request_type = list(filter(lambda x: x != '', log.split(' ')))[6]
    if request_type == REQUEST_TYPE['GET']:
      get_counter += 1
    elif request_type == REQUEST_TYPE['POST']:
      post_counter += 1
  
  if post_counter != 0:
    return get_counter / post_counter
  else:
    return 'Cannot caculate get and post ratio becasue no post request'

logs = read_file('log.txt')
print('IP addresses:')
print(get_ip_address(logs))
print('GET vs PUT ratio')
print(get_post_ratio(logs))