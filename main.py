import sys
import argparse
import numpy
import webbrowser

# Define program and arguments
parser = argparse.ArgumentParser(prog="Binocle", description="Look for everything, everywhere.")
parser.add_argument("engine", type=str, help="search engine")
parser.add_argument("query", type=str, help="search query")

# Prevent to display Python error
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Variables and constants
NAME = "Binocle"
VERSION = "0.2"
ALL_ENGINES = numpy.array([
    ["b", "Bing", "https://www.bing.com/search?q"],
    ["c", "Chocolatey", "https://community.chocolatey.org/packages?q="],
    ["d", "Duckduckgo", "https://duckduckgo.com/?q="],
    ["e", "Ecosia", "https://www.ecosia.org/search?method=index&q="],
    ["g", "Google", "https://www.google.fr/search?q"],
    ["q", "Qwant", "https://www.qwant.com/?q"],
    ["s", "Startpage", "https://www.startpage.com/do/search?query"],
    ["y", "Youtube", "https://www.youtube.com/results?search_query="]])
errorLoop = 0
NB_ENGINES = int(ALL_ENGINES.size / 3)
ARGUMENTS = parser.parse_args()
ENGINE_KEYWORD = ARGUMENTS.engine
SEARCH_QUERY = ARGUMENTS.query.replace(' ', '%20')

# FUNCTION  : Display error
def displayError():
    if errorLoop == NB_ENGINES:
        print(NAME + " v" + VERSION)
        print("An error occured : " + ENGINE_KEYWORD + " is not a correct keyword.")

# FUNCTION : Open browser
def openingBrowser(engine):
    print(NAME + " v" + VERSION)
    print("Engine : " + engine[1])
    print("Webpage : " + engine[2] + SEARCH_QUERY)
    webbrowser.open(engine[2] + SEARCH_QUERY, new = 2)

# MAIN : Looking for one keyword
for engine in ALL_ENGINES:
    if engine[0] == ENGINE_KEYWORD:
        openingBrowser(engine)
    else:
        errorLoop = errorLoop + 1
        displayError()