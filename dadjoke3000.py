import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKE 3000!")
header = colored(header, color="magenta", on_color="on_cyan")
space = "\n" * 2
print(space + header)

topic = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"
jokes = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
).json()

num_jokes = jokes["total_jokes"]
joke_results = jokes["results"]
if num_jokes > 1:
    print(f"There are {num_jokes} jokes about {topic}. Here's one:")
    print(choice(joke_results)["joke"])
    print(space)
elif num_jokes == 1:
    print(f"There is one joke about {topic}. Here it is:")
    print(joke_results[0]["joke"])
    print(space)
else:
    print(f"Sorry, couldn't find a joke for your term {topic}")
    print(space)
