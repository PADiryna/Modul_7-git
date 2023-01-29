class Movies:
    def __init__(self, title, year, genre, number_of_views):
        self.movie_title = title
        self.year = year
        self.genre = genre
        self.number_of_views = number_of_views

    def __str__(self):
        return f'"{self.title}" ({self.year}) Gerne:{self.genre} Views: {self.number_of_views}'

m_1 = Movies('The green mile', '1999', 'drama', '119735')
m_2 = Movies('Schindlers list', '1993', 'drama', '78003')
m_3 = Movies('TheShawshank Redemption', '1994', 'drama', '80321')
m_4 = Movies('Forrest Gump', '1994', 'drama', '111224')

movies_list = [m_1, m_2, m_3, m_4]

class Series(Movies):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'"{self.title}"({self.year}) Gerne:{self.genre} Vievs:{self.number_of_views} Episodes:{self.episode} Seasons:{self.season}'
      
    @property
    def play(self, view = 1):
      self.curent_number_of_views += 1
     
    def __lt__(self, other):
        return self.title < other.title
    

s_1 = Series('Breaking Bad', '2008-2013', 'kriminal', '90537', '62', '5')
s_2 = Series('Game of Thrones', '2011-2019', 'fantasy', '165864', '73', '8')

series_list = [s_1,s_2]

       
def get_video(video_type):

    video = []    
  
    for m in movies_list:
      if video_type == 1:
         video.append(movies_list)
    for s in series_list:    
      if video_type == 2:
        video.append(series_list)
              
    return video   
  
if __name__ == "__main__":
    
  video_type = int(input("Choose a type of video. Movie - 1, Series - 2: "))
  video = get_video(video_type)  
  for v in sorted(video):
    print(video)
  