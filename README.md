![Header](/docs/header.png)

<div align="center">

[![GitHub license](https://img.shields.io/github/license/n-deleforge/binocle?style=for-the-badge)](https://github.com/n-deleforge/binocle/blob/main/LICENCE)
![GitHub last commit](https://img.shields.io/github/last-commit/n-deleforge/binocle?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/n-deleforge/binocle?style=for-the-badge)](https://github.com/n-deleforge/binocle/network)
[![GitHub stars](https://img.shields.io/github/stars/n-deleforge/binocle?style=for-the-badge)](https://github.com/n-deleforge/binocle/stargazers)
[![Paypal](https://img.shields.io/badge/DONATE-PAYPAL.ME-lightgrey?style=for-the-badge)](https://www.paypal.com/paypalme/nicolasdeleforge)

</div>

# Quick start
## Installation and usage

`python` and `pip` must be installed.

```
git clone https://github.com/n-deleforge/binocle.git
cd binocle
py -m pip install -r requirements.txt
binocle [keyword] [query]
```

### Usage

Binocle *always* need two arguments to work.
- `keyword` : keyword of the engine used - the list is available below.
- `query` : query sent to the engine

There are also some optionnals arguments :
- `-v` / `--version` : show Binocle version
- `-h` / `--help` : show Binocle help
- `-l` / `--list` : show every engines available

### Examples

- Search *My Super Research* on **Duckduckgo** : `binocle d "My Super Research"`.
- Search *SomeYoutuber* on **Youtube** : `binocle yt SomeYoutuber"`.
- Show engines available : `binocle -l`.

If your query is only one word, you do not need to add quote marks as you can notice with the second example.

## Launch from terminal (for Windows)

- Edit the PATH global variable and add the directory of binocle.
- Then you can type : `binocle [keyword] [query]` in your terminal.

# All search engines
## Search engines

| Keyword | Search on
| :----------: | -------------------
| b             | [Bing](https://www.bing.com)
| d             | [Duckduckgo](https://duckduckgo.com)
| e             | [Ecosia](https://www.ecosia.org)
| g             | [Google](https://google.com)
| q             | [Qwant](https://qwant.com)
| s             | [Startpage](https://startpage.com)

## Shopping

| Keyword | Search on
| :----------: | -------------------
| am          | [Amazon.com](https://www.amazon.com)
| am-uk     | [Amazon.uk](https://www.amazon.co.uk)
| am-fr       | [Amazon.fr](https://www.amazon.fr)
| am-de     | [Amazon.de](https://www.amazon.de)
| am-es     | [Amazon.es](https://www.amazon.es)
| am-it       | [Amazon.it](https://www.amazon.it)
| am-jp      | [Amazon.jp](https://www.amazon.jp)

## Utility

| Keyword | Search on
| :----------: | -------------------
| alt           | [Alternative To](https://alternativeto.net)
| hltb         | [HowLongTo Beat](https://howlongtobeat.com/)
| mal         | [MyAnimeList](https://myanimelist.net)
| wi           | [Wikipedia](https://wikipedia.org/wiki/)

## Entertainment

| Keyword | Search on
| :----------: | -------------------
| tw           | [Twitch](https://twitch.com)
| yt            | [Youtube](https://youtube.com)

## Development

| Keyword | Search on
| :----------: | -------------------
| ch           | [Chocolatey](https://chocolatey.org)
| gi            | [Github](https://github.com)
| so           | [StackOverflow](https://stackoverflow.com) 

## Social

| Keyword | Search on
| :----------: | -------------------
| li              | [LinkedIn](https://www.linkedin.com)
| re            | [Reddit](https://www.reddit.com)

## Translation

| Keyword | Search on
| :----------: | -------------------
| dl-en-fr    | [DeepL](https://www.deepl.com) (English > French)
| dl-fr-en    | [DeepL](https://www.deepl.com) (French > English)
| dl-en-es  | [DeepL](https://www.deepl.com) (Enligsh > Spanish)
| dl-es-en  | [DeepL](https://www.deepl.com) (Spanish > English)
| dl-es-fr    | [DeepL](https://www.deepl.com) (Spanish > French)
| dl-fr-es    | [DeepL](https://www.deepl.com) (French > Spanish)

# Changelog

- 0.5.2 : DeepL added
- 0.5 : Engines are now categorized in the list function
- 0.4 : List function added (show every search engines) + HowLongToBeat added
- 0.3 : Multiple new search engines
- 0.2 : Initial release
