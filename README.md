#postman2md
- postman collection json file to markdown(md) file.

##usage

Just Download and :

```python

import postman2md
# create multi markdown file in the directory.
postman2md.convert(postman_file="example.json.postman_collection")

# create merged markdown file in the directory.
postman2md.convert(postman_file="example.json.postman_collection", multi_file=False)

```

##dependancy 
- [Documentation for the various versions of Postman Schemas](https://schema.getpostman.com/)

