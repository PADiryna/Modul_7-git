class Movies:

  def __init__(self, title, year, genre, number_of_views):
    self.title = title
    self.year = year
    self.genre = genre
    self.number_of_views = number_of_views

  def __str__(self):
    return f'"{self.title}" ({self.year}) Gerne:{self.genre} Views: {self.number_of_views}'

  def __repr__(self):
    return str(self)

  def __lt__(self, other):
    return self.title < other.title

  def play(self):
    if action == 'yes':
      self.number_of_views = self.number_of_views + 1
    else:
      return None

class Series(Movies):

  def __init__(self, title, year, genre, number_of_views, episode, season):
    super().__init__(title, year, genre, number_of_views)
    self.episode = episode
    self.season = season

  def __str__(self):
    return f'"{self.title}" ({self.year}) Gerne:{self.genre} Views:{self.number_of_views} Episodes:{self.episode} Seasons:{self.season}'

  
def get_video(videos_list, v_title):

  for v in videos_list:
    if v.title == v_title:
      return v
  else:
    return None

def get_my_list(videos_list):
  
  for v in videos_list:
   if action == 'yes':
     my_list.append(v) 
  else:
   return None


if __name__ == "__main__":

  m_1 = Movies('The green mile', '1999', 'drama', 119735)
  m_2 = Movies('Schindlers list', '1993', 'drama', 78003)
  m_3 = Movies('TheShawshank Redemption', '1994', 'drama', 80321)
  m_4 = Movies('Forrest Gump', '1994', 'drama', 111224)

  movies_list = [m_1, m_2, m_3, m_4]

  s_1 = Series('Breaking Bad', '2008-2013', 'kriminal', 90537, 62, 5)
  s_2 = Series('Game of Thrones', '2011-2019', 'fantasy', 165864, 73, 8)
  s_3 = Series('True detective', '2014-2019', 'kriminal',88099, 25, 4)

  series_list = [s_1, s_2, s_3]

  video_type = int(input("Choose a type of video. Movie - 1, Series - 2: "))

  videos_list = []

  if video_type == 1:
    videos_list += movies_list
  else:
    videos_list += series_list

  for v in sorted(videos_list):
    print(v)

  v_title = str(input('Search by title: '))
  v = get_video(videos_list, v_title)
  print(v)
  
  action = str(input('Start to watch?(yes or no): '))
  v.play()
  print(v)

  my_list = []
  
  action = str(input('Do you want to add this video to MY LIST (yes or no): '))
  
  get_my_list(videos_list)
  print('Show MY LIST:')
  print(v)
