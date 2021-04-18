# Source for https://www.poliastro.space

This repository contains the source for https://www.poliastro.space/.

_Based on the wonderful job by Jake Vanderplas https://github.com/jakevdp/jakevdp.github.io-source (MIT License)_

[![poliastro website CI](https://github.com/poliastro/poliastro.github.io/actions/workflows/main.yml/badge.svg)](https://github.com/poliastro/poliastro.github.io/actions/workflows/main.yml)

## Building the website

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/poliastro/poliastro.github.io-source.git
$ git submodule update --init --recursive
```

_(Activate the python virtual environment before proceeding)_

Install the required packages using `pip install -r requirements.txt`

Build the html and serve locally:

```
$ make html
$ make serve
$ open http://localhost:8000
```

Deploy to github pages

```
$ make publish-to-github
```

## Development

To regenerate the main CSS:

```
$ lessc main.less > main.css
```
