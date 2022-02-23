import argparse
import sys
import numpy
import webbrowser

# Constants
NAME = "Binocle"
VERSION = "0.2"
ALL_ENGINES = numpy.array([
    ["b", "Bing", "https://www.bing.com/search?q="],
    ["c", "Chocolatey", "https://community.chocolatey.org/packages?q="],
    ["d", "Duckduckgo", "https://duckduckgo.com/?q="],
    ["e", "Ecosia", "https://www.ecosia.org/search?method=index&q="],
    ["g", "Google", "https://www.google.fr/search?q="],
    ["gi", "Github", "https://github.com/search?q="],
    ["q", "Qwant", "https://www.qwant.com/?q="],
    ["s", "Startpage", "https://www.startpage.com/do/search?query="],
    ["t", "Twitch", "https://www.twitch.tv/search?term="],
    ["y", "Youtube", "https://www.youtube.com/results?search_query="]
])

# Define program and arguments
parser = argparse.ArgumentParser(prog=NAME, description="Look for everything, everywhere.",usage=NAME + " " + VERSION + " [-help] [-list] engine query")
parser.add_argument("engine", type=str, help="search engine (ex : d for duckduckgo, y for youtube etc.)")
parser.add_argument("query", type=str, help="search query (ex : \"my super research\")")

# Prevent to display Python error
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Variables
errorLoop = 0
nbEngines = int(ALL_ENGINES.size / 3)
args = parser.parse_args()
keyword = args.engine
query = args.query.replace(' ', '%20')

# MAIN : Looking for one keyword
for engine in ALL_ENGINES:
    if engine[0] == keyword:
        print(NAME + " " + VERSION + "\nEngine : " + engine[1] + "\nQuery : " + engine[2] + query)
        webbrowser.open(engine[2] + query, new=2)

    else:
        errorLoop = errorLoop + 1
        if errorLoop == nbEngines:
            print(NAME + " " + VERSION + "\nAn error occured : " + keyword + " is not a correct keyword.")
