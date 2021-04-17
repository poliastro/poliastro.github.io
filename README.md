# Source for https://poliastro.space

This repository contains the source for https://poliastro.space/.

_Based on the wonderful job by Jake Vanderplas https://github.com/jakevdp/jakevdp.github.io-source (MIT License)_

[![Poliastro Website CI](https://github.com/poliastro/poliastro.github.io/actions/workflows/main.yml/badge.svg)](https://github.com/poliastro/poliastro.github.io/actions/workflows/main.yml)
## Building the Blog

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/poliastro/poliastro.github.io-source.git
$ git submodule update --init --recursive
```

Install the required packages using `pip install -r requirements.txt`
(you will also need some node.js tools)

_{ Activate the python virtual environment before proceeding forward }_

To generate the main CSS:

```
$ lessc main.less > main.css
```

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

