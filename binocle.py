import argparse
import json
import os
import sys
import webbrowser

#
# Constants
#

NAME = "Binocle"
VERSION = "0.6.1"
PATH = os.path.dirname(os.path.realpath(__file__))
CATEGORIES = json.load(open(PATH + '/data/categories.json', 'r'))
ENGINES = json.load(open(PATH + '/data/engines.json', 'r'))

#
# Arguments
#

parser = argparse.ArgumentParser(
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
    "engine",
    type=str,
    help="search engine (ex : d for duckduckgo)")
parser.add_argument(
    "query",
    type=str,
    help="search query (ex : \"my super research\")")

#
# Binocle function
#

def startBinocle() :
    nbError = 0
    nbEngines = len(ENGINES)
    engine = parser.parse_args().engine
    query = parser.parse_args().query

    # Check every engine
    for e in ENGINES :
        # Engine found : open webbrowser
        if e["keyword"] == engine :
            queryFormatted = e['url'] + parser.parse_args().query.replace(' ', '%20')
            print(f"{NAME} {VERSION} \nEngine : {e['name']} \nQuery : {query} \nFormatted query : {queryFormatted}")
            webbrowser.open(queryFormatted, new=2)

        # Engine not found : increment error
        else :
            nbError = nbError + 1
            if nbError == nbEngines :
                print(f"{NAME}: '{engine}' is not a configured engine. Please use the argument '-l' to look at all the available engines.")

def showEngines() :
    for i, c in enumerate(CATEGORIES, start=1):
        if i == 1:
            print (f"=== {c['id']}. {c['name']} ===")
        else:
            print (f"\n=== {c['id']}. {c['name']} ===")
        for e in ENGINES :
            if (c["id"] == e["category"]) :
                print(f"- {e['keyword']} : {e['name']}")

#
# Workflow of Binocle
#

nbArgs = len(sys.argv) - 1

# 1st case : display help
if nbArgs == 0:
    parser.print_help(sys.stderr)
    sys.exit(1)

# 2nd case : show engines
elif nbArgs == 1 and (sys.argv[1] == "-l" or sys.argv[1] == "--list"):
    showEngines()
    sys.exit(1)

# 3rd case : call Binocle
else:
    startBinocle()