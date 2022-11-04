import argparse as ap
import sys
import numpy as np
import webbrowser as wb

# Constants
NAME = "Binocle"
VERSION = "0.5.2"
CATEGORIES = np.array([
    # ID, Category name
    [1, "Search"],
    [2, "Shopping"],
    [3, "Utility"],
    [4, "Entertainment"],
    [5, "Development"],
    [6, "Social"],
    [7, "Translation"]
])
ENGINES = np.array([
    # Keyword, Engine name, URL engine, Category ID
    # Search
    ["b", "Bing", "https://www.bing.com/search?q=", 1],
    ["d", "Duckduckgo", "https://duckduckgo.com/?q=", 1],
    ["e", "Ecosia", "https://www.ecosia.org/search?method=index&q=", 1],
    ["g", "Google", "https://www.google.fr/search?q=", 1],
    ["q", "Qwant", "https://www.qwant.com/?q=", 1],
    ["s", "Startpage", "https://www.startpage.com/do/search?query=", 1],
    # Shopping
    ["am", "Amazon.com", "https://www.amazon.com/s?k=", 2],
    ["am-uk", "Amazon.uk", "https://www.amazon.co.uk/s?k=", 2],
    ["am-fr", "Amazon.fr", "https://www.amazon.fr/s?k=", 2],
    ["am-de", "Amazon.de", "https://www.amazon.de/s?k=", 2],
    ["am-es", "Amazon.es", "https://www.amazon.es/s?k=", 2],
    ["am-it", "Amazon.it", "https://www.amazon.it/s?k=", 2],
    ["am-jp", "Amazon.jp", "https://www.amazon.jp/s?k=", 2],
    # Utility
    ["alt", "AlternativeTo", "https://alternativeto.net/browse/search/?q=", 3],
    ["hltb", "HowLongToBeat", "https://howlongtobeat.com/?q=", 3],
    ["mal", "MyAnimeList", "https://myanimelist.net/search/all?q=", 3],
    ["wi", "Wikipedia", "https://wikipedia.org/wiki/", 3],
    # Entertainment
    ["tw", "Twitch", "https://www.twitch.tv/search?term=", 4],
    ["yt", "Youtube", "https://www.youtube.com/results?search_query=", 4],
    # Development
    ["ch", "Chocolatey", "https://community.chocolatey.org/packages?q=", 5],
    ["gi", "Github", "https://github.com/search?q=", 5],
    ["so", "StackOverflow", "https://stackoverflow.com/search?q=", 5],
    # Social
    ["li", "LinkedIn", "https://www.linkedin.com/search/results/all/?keywords=", 6],
    ["re", "Reddit", "https://www.reddit.com/search/?q=", 6],
    # Translation
    ["dl-en-fr", "DeepL (English > French)", "https://www.deepl.com/translator#en/fr/", 7],
    ["dl-fr-en", "DeepL (French > English)", "https://www.deepl.com/translator#fr/en/", 7],
    ["dl-en-es", "DeepL (English > Spanish)", "https://www.deepl.com/translator#en/es/", 7],
    ["dl-en-es", "DeepL (Spanish > English)", "https://www.deepl.com/translator#es/en/", 7],
    ["dl-es-fr", "DeepL (Spanish > French)", "https://www.deepl.com/translator#es/fr/", 7],
    ["dl-fr-es", "DeepL (French > Spanish)", "https://www.deepl.com/translator#fr/es/", 7],
])

# Define program and arguments
parser = ap.ArgumentParser(
    prog=NAME,
    description="Look for everything, everywhere",
    epilog="more details on https://github.com/n-deleforge/binocle")
parser.add_argument(
    "-v", "--version",
    action="version", 
    version=NAME + " " + VERSION)
parser.add_argument(
    "-l", "--list",
    action="version", 
    help="show engines list and exit")
parser.add_argument(
    "keyword",
    type=str,
    help="search engine keyword (ex : d for duckduckgo)")
parser.add_argument(
    "query",
    type=str,
    help="search query (ex : \"my super research\")")

# Binocle function
def startBinocle() :
    error = 0 #  count error to check if every engine has been check
    nbEngines = int(ENGINES.size / 4) # engine count (because there are 4 colums in the engine array)
    keyword = parser.parse_args().keyword
    query = parser.parse_args().query
    queryFormatted = parser.parse_args().query.replace(' ', '%20') # query sent to the engine

    # Check every engine
    for engine in ENGINES :
        # Engine found : open webbrowser
        if engine[0] == keyword :
            print(f"{NAME} {VERSION} \nEngine : {engine[1]} \nQuery : {query} \nFormatted query : {engine[2]}{queryFormatted}")
            wb.open(engine[2] + queryFormatted, new=2)

        # Enfine not found : increment error
        else :
            error = error + 1
            if error == nbEngines :
                print(f"{NAME}: error: '{keyword}' is not a correct keyword")

# Show every engines categorized
def showEngines() :
    # List categories
    for categorie in CATEGORIES :
        print(f"\n=== {categorie[1]} ===")
        # List engines only from the categorie
        for engine in ENGINES :
            if (categorie[0] == engine[3]) :
                print(f"- {engine[1]} : {engine[0]}")

# Workflow of Binocle
nbArgs = len(sys.argv) - 1 # number of arguments
if nbArgs > 0 :
    cmd = sys.argv[1] # the first argument (if it exists)

# 1st case : show engines
if nbArgs == 1 and (cmd == "-l" or cmd == "--list"):
    showEngines()
    sys.exit(1)

# 2nd case : display help
elif nbArgs == 0:
    parser.print_help(sys.stderr)
    sys.exit(1)

# 3rd case : call Binocle
else:
    startBinocle()