from blog_post import BlogPost

class Blog:
  def __init__(self):
    self.blog_list = []
  def add(self, blog_post):
    self.blog_list.append(blog_post)
  def delete(self, index):
    if self.blog_list[index]:
      self.blog_list.pop(index)
  def update(self, index, blog_post):
    if self.blog_list[index]:
      self.blog_list[index] = blog_post
  def __str__(self):
    result = ''
    for index in range(len(self.blog_list)):
      result += str(index + 1) + ' blog post: ' + self.blog_list[index].__str__() + '\n'
    return result


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

blog = Blog()
blog.add(blog_posts[0])
blog.add(blog_posts[1])
print('After add:')
print(blog)
blog.update(1, blog_posts[2])
print('After update')
print(blog)
blog.delete(1)
print('After detele')
print(blog)




"""
# Blog

 -  Reuse your `BlogPost` class
 -  Create a `Blog` class which can
     -  store a list of BlogPosts
     -  add BlogPosts to the list
     -  delete(int) one item at given index
     -  update(int, BlogPost) one item at the given index and update it with another BlogPost
"""