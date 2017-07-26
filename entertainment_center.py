#Saranya Ruiz-Esparza_Movie website project

import fresh_tomatoes
import media

"""Contain details of movies and display movies on the website."""

trolls = media.Movie("Trolls",
                     "Small happy creatures who love to sing, dance and hug all day long.",
                     "https://s-media-cache-ak0.pinimg.com/originals/a9/20/21/a9202115927e1e6849b31151be0f7d50.jpg",
                     "https://www.youtube.com/watch?v=xyjm5VQ11TQ")
print(trolls.title)+":"
print(trolls.storyline)
print"----------------"

beauty_and_the_beast = media.Movie("Beauty and the Beast",
                                   "Belle, a young woman who is taken prisoner by a beast in its castle.",
                                   "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                                   "https://www.youtube.com/watch?v=e3Nl_TCQXuw")
print(beauty_and_the_beast.title)+":"
print(beauty_and_the_beast.storyline)
print "----------------"

trainwreck = media.Movie("Trainwreck",
                         "Amy is a party girl.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c5/Trainwreck_poster.jpg",
                         "https://www.youtube.com/watch?v=jGtqeO5oFCc")
print(trainwreck.title)+":"
print (trainwreck.storyline)
print "----------------"

the_imitation_game = media.Movie("The Imitation Game",
                                 "Alan Turing who crack Nazi codes.",
                                 "https://fanart.tv/fanart/movies/205596/movieposter/the-imitation-game-550e90ac7bab9.jpg",
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM")
print(the_imitation_game.title)+":"
print (the_imitation_game.storyline)
print "----------------"

captain_america_civil_war = media.Movie("Captain America Civil War",
                                        "Fighting among superheroes because of disagreement.",
                                        "https://images.moviepilot.com/image/upload/c_fill,h_470,q_auto:good,w_620/tk136qn8oryxeebmdz5e.jpg",
                                        "https://www.youtube.com/watch?v=uVdV-lxRPFo")
print(captain_america_civil_war.title)+":"
print (captain_america_civil_war.storyline)
print "----------------"

doctor_strange = media.Movie("Doctor strange",
                             "Dr. Stephen Strange's life changes after a car accident.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=Lt-U_t2pUHI")
print(doctor_strange.title)+":"
print (doctor_strange.storyline)
print "----------------"

wonder_woman = media.Movie("Wonder woman",
                           "Diana leaves her home to fight alongside men in a war to end all wars.",
                           "https://d1nao0k9edgivc.cloudfront.net/wp-content/uploads/2017/05/wwpost345.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")
print(wonder_woman.title)+":"
print (wonder_woman.storyline)
print "----------------"

movies = [trolls, beauty_and_the_beast, trainwreck, the_imitation_game, captain_america_civil_war, wonder_woman]
"""List of movies"""
fresh_tomatoes.open_movies_page(movies)
"""Recieving list of movies and open them in browser"""

