import media
import fresh_tomatoes

# list of movies infor
movie_list = [["toy_story",
               "Toy Story",
               "A story of a boy and his toys that come to life",
               "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg",
               "https://www.youtube.com/watch?v=KYz2wyBy3kc"],
              ["life_of_pi",
               "Life of Pi",
               "Story of Pi and the tiger learn to trust each other if both are to survive.",
               "http://t2.gstatic.com/images?q=tbn:ANd9GcQLik2EaN6bm4GQBKTvI7uIlH4b5kQ29IhY1Tqh_nEoHkUsru82",
               "https://www.youtube.com/watch?v=j9Hjrs6WQ8M"],
              ["avatar",
               "Avatar",
               "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved.",
               "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY"]]

#empty list to hold movie objects
movies = []

# counter for index
i = 0

#run through the movie list, convert it to movie object and add it to movies
for movie in movie_list:
        # define instances of the class Movie defined in media.py
	movies.append(media.Movie(movie_list[i]))
	i = i + 1

#generate html through python
fresh_tomatoes.open_movies_page(movies)
