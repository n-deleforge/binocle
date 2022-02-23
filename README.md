![Header](/docs/header.png)

<div align="center">

[![GitHub license](https://img.shields.io/github/license/n-deleforge/binocle?style=for-the-badge)](https://github.com/n-deleforge/binocle/blob/main/LICENCE)
![GitHub last commit](https://img.shields.io/github/last-commit/n-deleforge/binocle?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/n-deleforge/binocle?style=for-the-badge)](https://github.com/n-deleforge/binocle/network)
[![GitHub stars](https://img.shields.io/github/stars/n-deleforge/binocle?style=for-the-badge)](https://github.com/n-deleforge/binocle/stargazers)
[![Paypal](https://img.shields.io/badge/DONATE-PAYPAL.ME-lightgrey?style=for-the-badge)](https://www.paypal.com/paypalme/nicolasdeleforge)

</div>

# Quick start
## Requirements

Python must be installed on your device.

## Installation and usage

```
git clone https://github.com/n-deleforge/binocle.git
cd binocle
python main.py [engine] [query]
```

### Usage

Binocle *always* need two arguments to work.
- **engine** : it is the first letter of the search engine (the available list is below)
- **query** : it is the query sent to the search engine

### Examples

- Search "My Super Research" on Duckduckgo : `binocle d "My Super Research"`
- Search "Github" on Youtube : `binocle y Github` 

If your query is only one word, you do not need to add quote marks as you can notice with the second example.

### Launch from terminal (Windows only)

- Edit the PATH global variable and add the directory of binocle
- Then you can type : `binocle` in your terminal

## Engines availables

| Keyword | Search engine 
| :----------: | -----------
| b             | Bing
| c             | Chocolatey
| d             | Duckduckgo
| e             | Ecosia
| g             | Google
| gi            | Github
| q             | Qwant
| s             | Startpage
| t             | Twitch
| y             | Youtube

- 0.2 : Initial release
