postman2md
===========

[![Pyhton2.7](https://img.shields.io/badge/python-2.7-brightgreen.svg)](https://github.com/Plate-Project/postman2md)
[![Build Status](https://travis-ci.org/Plate-Project/postman2md.svg?branch=devleop)](https://travis-ci.org/Plate-Project/postman2md)

- postman collection json file to markdown(md) file.

##usage

Just Download and :

```python

import postman2md
# create multi markdown file in the directory.
postman2md.convert(postman_file='postman2md_example.json.postman_collection')

# create merged markdown file in the directory.
postman2md.convert(postman_file='postman2md_example.json.postman_collection', multi_file=False)

```

##dependency 
- [Documentation for the various versions of Postman Schemas](https://schema.getpostman.com/)

##support collection version 
- [v1](https://schema.getpostman.com/json/collection/v1.0.0/docs/index.html)
