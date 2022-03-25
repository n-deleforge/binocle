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
pip install r -requirements.txt
binocle [keyword] [query]
```

### Usage

Binocle *always* need two arguments to work.
- **keyword** : it is the first letter of the search engine (the available list is below).
- **query** : it is the query sent to the search engine.

### Examples

- Search "My Super Research" on Duckduckgo : `binocle d "My Super Research"`.
- Search "Github" on Youtube : `binocle yt Github`.

If your query is only one word, you do not need to add quote marks as you can notice with the second example.

## Launch from terminal

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
| am          | [Amazon](https://www.amazon.com)
| am-fr       | [Amazon.fr](https://www.amazon.fr)
| am-de     | [Amazon.de](https://www.amazon.de)
| am-es     | [Amazon.es](https://www.amazon.es)
| am-it       | [Amazon.it](https://www.amazon.it)

## Utily

| Keyword | Search on
| :----------: | -------------------
| alt           | [Alternative To](https://alternativeto.net)
| wi           | [Wikipedia](https://wikipedia.org/wiki/)

## Entertainment

| Keyword | Search on
| :----------: | -------------------
| tw           | [Twitch](https://twitch.com)
| yt            | [Youtube](https://youtube.com)

## Programming

| Keyword | Search on
| :----------: | -------------------
| ch           | [Chocolatey](https://chocolatey.org)
| gi            | [Github](https://github.com)
| so           | [StackOverflow](https://stackoverflow.com) 

## Social

| Keyword | Search on
| :----------: | -------------------
| re            | [Reddit](https://www.reddit.com)

# Changelog

- 0.3 : Multiple new search engines
- 0.2 : Initial release
