![Header](/docs/header.png)

<div align="center">

[![GitHub license](https://img.shields.io/github/license/n-deleforge/binocle?style=for-the-badge)](https://github.com/n-deleforge/binocle/blob/main/LICENCE)
![GitHub last commit](https://img.shields.io/github/last-commit/n-deleforge/binocle?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/n-deleforge/binocle?style=for-the-badge)](https://github.com/n-deleforge/binocle/network)
[![GitHub stars](https://img.shields.io/github/stars/n-deleforge/binocle?style=for-the-badge)](https://github.com/n-deleforge/binocle/stargazers)

</div>

# Quick start
## Installation

**Python must be installed on your computer**.

Instructions :
```
git clone https://github.com/n-deleforge/binocle.git
```

## Usage

Binocle *always* need two arguments to work.
- `engine` : engine to use - the list is available below.
- `query` : query to send

There are also some optionnals arguments :
- `-v` / `--version` : show Binocle version
- `-h` / `--help` : show Binocle help
- `-l` / `--list` : show every engines available

## Examples

- Search *My Super Research* on **Duckduckgo** : `binocle d "My Super Research"`.
- Search *SomeYoutuber* on **Youtube** : `binocle yt SomeYoutuber`.
- Show engines available : `binocle -l`.

If your query is only composed of one word, you don't need to add quote marks as you can notice with the second example.

## Launch from terminal (for Windows)

- Edit the PATH global variable and add the directory of binocle.
- Then you can type : `binocle [engine] [query]` directly in your terminal.

# Engine list

| Categorie     | Keyword | Search on
| :------------ | :------ | :-------------------
| Search Engine | b       | [Bing](https://www.bing.com)
| -             | d       | [Duckduckgo](https://duckduckgo.com)
| -             | e       | [Ecosia](https://www.ecosia.org)
| -             | g       | [Google](https://google.com)
| -             | q       | [Qwant](https://qwant.com)
| -             | s       | [Startpage](https://startpage.com)
| Utility       | alt     | [Alternative To](https://alternativeto.net)
| -             | hltb    | [HowLongTo Beat](https://howlongtobeat.com/)
| -             | mal     | [MyAnimeList](https://myanimelist.net)
| -             | wi      | [Wikipedia](https://wikipedia.org/wiki/)
| Entertainment | tw      | [Twitch](https://twitch.com)
| -             | yt      | [Youtube](https://youtube.com)
| Development   | ch      | [Chocolatey](https://chocolatey.org)
| -             | gi      | [Github](https://github.com)
| -             | so      | [StackOverflow](https://stackoverflow.com) 
| Social        | li      | [LinkedIn](https://www.linkedin.com)
| -             | re      | [Reddit](https://www.reddit.com)

# Editing engines list
## How to add a category
A **category** is composed of **2** mandatory values :
- *id* : must be an integer and unique
- *name* : must be a string

Edit the `categories.json` file in the data folder and follow this template : `{"id" : x, "name": x }`

## How to add an engine
An **engine** is composed of **4** mandatory values :
- *category* : must be an id of an existing category
- *name* : must be a string
- *keyword* : must be a string
- *url* : must be a string

Edit the `engines.json` file in the data folder and follow this template : `{"category" : x, "name": x, "keyword": x, "url": x}`

# Changelog

- 0.6 : Categories and engines are now managed throught JSON files.
- 0.5 : Engines are now categorized in the list function
- 0.4 : List function added (show every search engines) + HowLongToBeat added
- 0.3 : Multiple new search engines
- 0.2 : Initial release
