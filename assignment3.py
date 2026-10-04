# BLUEPRINT | DONT EDIT

import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE


for movie_id in movie_ids:
    website = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"

    response = requests.get(website)
    # print(response)

    data = response.json()
    print("Title:", data["title"])
    print("Overview:", data["overview"])
    print("Vote average:", data["vote_average"], "\n")



