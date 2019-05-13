class PostIt:
  def __init__(self, bg_color, text_color, text):
    self.background_color = bg_color
    self.text = text
    self.text_color = text_color
  
  def __str__(self):
    return f'This is an {self.background_color} with {self.text_color} text: {self.text}'

post_one = PostIt('orange', 'blue', 'Idea 1')
post_two = PostIt('pink', 'black', 'Awesome')
post_three = PostIt('yellow', 'green', 'Superb!')

post_list = [post_one, post_two, post_three]

for value in post_list:
  print(value)

"""
# Post-it
- Create a `PostIt` class that has
  - a `background_color`
  - a `text` on it
  - a `text_color`
- Create a few example post-it objects:
  - an orange with blue text: "Idea 1"
  - a pink with black text: "Awesome"
  - a yellow with green text: "Superb!"
"""