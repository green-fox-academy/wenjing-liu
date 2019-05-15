import json

def most_popular_comments(file_name):
  try:
    posts = read_json_file(file_name)
    comments = []
    for index in range(len(posts)):
      if posts[index]["comments"]:
        comments.extend(posts[index]["comments"])
    if comments:
      return sorted(comments, key = lambda item: item['like_count'], reverse = True)[0]
    else:
      return []
  except Exception as e:
    print(f'Error occurs when find most popular comments from file {file_name}: {e}')
    return False

def read_json_file(file_name):
  try:
    with open(file_name, 'r') as file:
      content = json.load(file)
      return content    
  except Exception as e:
    print(f'Error occurs read from file {file_name}: {e}')
    return False

print(most_popular_comments('posts.json'))