import argparse
import sys
import numpy
import webbrowser

# Constants
NAME = "Binocle"
VERSION = "0.3"
ALL_ENGINES = numpy.array([
    # Search engines
    ["b", "Bing", "https://www.bing.com/search?q="],
    ["d", "Duckduckgo", "https://duckduckgo.com/?q="],
    ["e", "Ecosia", "https://www.ecosia.org/search?method=index&q="],
    ["g", "Google", "https://www.google.fr/search?q="],
    ["q", "Qwant", "https://www.qwant.com/?q="],
    ["s", "Startpage", "https://www.startpage.com/do/search?query="],

    # Shopping
    ["am", "Amazon", "https://www.amazon.com/s?k="],
    ["am-fr", "Amazon.fr", "https://www.amazon.fr/s?k="],
    ["am-de", "Amazon.de", "https://www.amazon.de/s?k="],
    ["am-es", "Amazon.es", "https://www.amazon.es/s?k="],
    ["am-it", "Amazon.it", "https://www.amazon.it/s?k="],

    # Utility
    ["alt", "AlternativeTo", "https://alternativeto.net/browse/search/?q="],
    ["wi", "Wikipedia", "https://wikipedia.org/wiki/"],

    # Entertainment
    ["tw", "Twitch", "https://www.twitch.tv/search?term="],
    ["yt", "Youtube", "https://www.youtube.com/results?search_query="],

    # Programming
    ["ch", "Chocolatey", "https://community.chocolatey.org/packages?q="],
    ["gi", "Github", "https://github.com/search?q="],
    ["so", "StackOverflow", "https://stackoverflow.com/search?q="],

    # Social
    ["li", "LinkedIn", "https://www.linkedin.com/search/results/all/?keywords="],
    ["re", "Reddit", "https://www.reddit.com/search/?q="],
])

# Define program and arguments
parser = argparse.ArgumentParser(
    prog=NAME,
    description="Look for everything, everywhere.",
    usage=NAME + " " + VERSION + " [keyword] [query]")
parser.add_argument(
    "keyword",
    type=str,
    help="search engine keyword (ex : d for duckduckgo)")
parser.add_argument(
    "query",
    type=str,
    help="search query (ex : \"my super research\")")

# Prevent to display Python error
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Variables
errorLoop = 0
nbEngines = int(ALL_ENGINES.size / 3)
args = parser.parse_args()
keyword = args.keyword
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
