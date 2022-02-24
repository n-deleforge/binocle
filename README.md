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

`python3` and `pip` must be installed.

```
git clone https://github.com/n-deleforge/binocle.git
cd binocle
pip install r -requirements.txt
binocle [keyword] [query]
```

### Usage

Binocle *always* need two arguments to work.
- **keyword** : it is the first letter of the search engine (the available list is below)
- **query** : it is the query sent to the search engine

### Examples

- Search "My Super Research" on Duckduckgo : `binocle d "My Super Research"`
- Search "Github" on Youtube : `binocle y Github` 

If your query is only one word, you do not need to add quote marks as you can notice with the second example.

### Launch from terminal

- Edit the PATH global variable and add the directory of binocle
- Then you can type : `binocle [keyword] [query]` in your terminal

## Engines availables

| Keyword       | Search engine 
| :-----------: | -----------
| a             | [Alternative To](https://alternativeto.net)
| b             | [Bing](https://www.bing.com)
| c             | [Chocolatey](https://chocolatey.org)
| d             | [Duckduckgo](https://duckduckgo.com)
| e             | [Ecosia](https://www.ecosia.org)
| g             | [Google](https://google.com)
| gi            | [Github](https://github.com)
| q             | [Qwant](https://qwant.com)
| r             | [Reddit](https://www.reddit.com)
| s             | [Startpage](https://startpage.com)
| t             | [Twitch](https://twitch.com)
| y             | [Youtube](https://youtube.com)
| w             | [Wikipedia](https://wikipedia.org/wiki/)

# Changelog

- 0.2 : Initial release
