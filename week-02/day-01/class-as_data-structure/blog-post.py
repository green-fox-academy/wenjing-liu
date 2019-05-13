from datetime import datetime

class BlogPost:
  def __init__(self, author_name, title, text, publication_date):
    self.author_name = author_name
    self.title = title
    self.text = text
    self.publication_date = datetime.strptime(publication_date, '%Y.%m.%d.')
  
  def __str__(self):
    return f'''"{self.title}" titled by {self.author_name} posted at {self.publication_date.year}-{self.publication_date.month}-{self.publication_date.day}.
    - {self.text}
    '''

post_1 = {
  'author_name': 'John Doe',
  'title': 'Lorem Ipsum',
  'text': 'Lorem ipsum dolor sit amet.',
  'publication_date': '2000.05.04.'
}

post_2 = {
  'author_name': 'Tim Urban',
  'title': 'Wait but why',
  'text': 'A popular long-form, stick-figure-illustrated blog about almost everything.',
  'publication_date': '2010.10.10.'
}

post_3 = {
  'author_name': 'William Turton',
  'title': 'One Engineer Is Trying to Get IBM to Reckon With Trump',
  'text': 'Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.',
  'publication_date': '2017.03.28.'
}

posts = [post_1, post_2, post_3]
blog_posts = []
for post in posts:
  blog_posts.append(BlogPost(post['author_name'], post['title'], post['text'], post['publication_date']))

for blog_post in blog_posts:
  print(blog_post)





"""
# BlogPost
- Create a `BlogPost` class that has
  - an `author_name`
  - a `title`
  - a `text`
  - a `publication_date`
- Create a few blog post objects:
  - "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
    - Lorem ipsum dolor sit amet.
  - "Wait but why" titled by Tim Urban posted at "2010.10.10."
    - A popular long-form, stick-figure-illustrated blog about almost everything.
  - "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
    - Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.
"""