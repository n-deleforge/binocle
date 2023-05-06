import argparse as ap
import json
import os
import sys
import webbrowser as wb

# Constants
NAME = "Binocle"
VERSION = "0.6"
PATH = os.path.dirname(os.path.realpath(__file__))
CATEGORIES = json.load(open(PATH + '\data\categories.json', 'r'))
ENGINES = json.load(open(PATH + '\data\engines.json', 'r'))

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
    nbError = 0
    nbEngines = len(ENGINES)
    keyword = parser.parse_args().keyword
    query = parser.parse_args().query

    # Check every engine
    for engine in ENGINES :
        # Engine found : open webbrowser
        if engine["keyword"] == keyword :
            queryFormatted = engine['url'] + parser.parse_args().query.replace(' ', '%20')
            print(f"{NAME} {VERSION} \nEngine : {engine['name']} \nQuery : {query} \nFormatted query : {queryFormatted}")
            wb.open(queryFormatted, new=2)

        # Engine not found : increment error
        else :
            nbError = nbError + 1
            if nbError == nbEngines :
                print(f"{NAME}: error: '{keyword}' is not a correct keyword")

# Show every engines categorized
def showEngines() :
    # List categories
    for categorie in CATEGORIES :
        print (f"\n=== {categorie['id']}. {categorie['name']} ===")
        # List engines only from the categorie
        for engine in ENGINES :
            if (categorie["id"] == engine["category"]) :
                print(f"- {engine['keyword']} : {engine['name']}")

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