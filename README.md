# Source for https://poliastro.github.io

This repository contains the source for https://poliastro.github.io/.

_Based on the wonderful job by Jake Vanderplas https://github.com/jakevdp/jakevdp.github.io-source (MIT License)_

## Building the Blog

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/poliastro/poliastro.github.io-source.git
$ git submodule update --init --recursive
```

Install the required packages using `pip install -r requirements.txt`
(you will also need some node.js tools)

To generate the main CSS:

```
(poliastro36) $ lessc main.less > main.css
```

Build the html and serve locally:

```
(poliastro36) $ make html
(poliastro36) $ make serve
(poliastro36) $ open http://localhost:8000
```

Deploy to github pages

```
(poliastro36) $ make publish-to-github
```

