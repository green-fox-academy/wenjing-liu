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