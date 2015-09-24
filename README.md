#postman2md
- postman collection json file to markdown(md) file.

##usage

Just Download and :

'''python

import postman2md
postman2md.convert(postman_file="example.json.postman_collection")
// create multi markdown file in the directory.

postman2md.convert(postman_file="example.json.postman_collection", multi_file=False)
// create merged markdown file in the directory.
'''
