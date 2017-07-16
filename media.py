class Movie():
    # This class provides a way to store movie related information


    def __init__(self, movie_info):
    	'''
    		Contructor to create an instance of Movie. 
			Usage: Movie(listOfMovies)
			listOfMovies should have list of [Movie_ID, Movie_title, Movie_Desc, Movie Poster, Movie_Trailer_URL]
		'''
		self.movie_id = movie_info[0]
		self.title = movie_info[1]
		self.movie_desc = movie_info[2]
		self.poster_image_url = movie_info[3]
		self.trailer_youtube_url = movie_info[4]

        
