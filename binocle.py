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
    ["mal", "MyAnimeList", "https://myanimelist.net/search/all?q="],
    ["hltb", "HowLongToBeat", "https://howlongtobeat.com/?q="],

    # Entertainment
    ["tw", "Twitch", "https://www.twitch.tv/search?term="],
    ["yt", "Youtube", "https://www.youtube.com/results?search_query="],

    # Development
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
    epilog="more details on https://github.com/n-deleforge/binocle")
parser.add_argument(
    "-v", "--version",
    action="version", 
    version=NAME + " " + VERSION)
parser.add_argument(
    "-l", "--list",
    action="version", 
    help="show search engines list and exit")
parser.add_argument(
    "keyword",
    type=str,
    help="search engine keyword (ex : d for duckduckgo)")
parser.add_argument(
    "query",
    type=str,
    help="search query (ex : \"my super research\")")

# Binocle function
def startBinocle():
    # Variables
    errorLoop = 0
    nbEngines = int(ALL_ENGINES.size / 3)
    results = parser.parse_args()
    keyword = results.keyword
    query = results.query
    queryFormatted = results.query.replace(' ', '%20')

    # Looking for one keyword
    for engine in ALL_ENGINES:
        if engine[0] == keyword:
            print(f"{NAME} {VERSION} \nEngine : {engine[1]} \nSearch : {query} \nQuery : {engine[2]}{queryFormatted}")
            webbrowser.open(engine[2] + queryFormatted, new=2)

        else:
            errorLoop = errorLoop + 1
            if errorLoop == nbEngines:
                print(f"{NAME} {VERSION} \nError :  '{keyword}' is not a correct keyword.")

# Display every engines
def displayEngines():
    print(f"{NAME} {VERSION} \n\nSearch engine - Keyword\n=======================")
    sortedEngines = numpy.sort(ALL_ENGINES, axis = 0)
    for engine in sortedEngines:
        print(f"{engine[1]} - {engine[0]}")

# Workflow of Binocle
# 1st case : display search engines
if len(sys.argv) == 2 and (sys.argv[1] == "-l" or sys.argv[1] == "--list"):
    displayEngines()
    sys.exit(1)

# 2nd case : display help
elif len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# 3rd case : call Binocle
else:
    startBinocle()