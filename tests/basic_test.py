# -*- coding:utf-8 -*-
import unittest
import requests 

class BasicTestCase(unittest.TestCase):
    
    def setUp(self):
        postman_official_json_collection = 'https://schema.getpostman.com/json/collection/v1/'
        r = requests.get(postman_official_json_collection)
        self.dump_file_path= './collection.json'
        if r.status_code == 200:
            self.collection_json = r.text 
            with open(self.dump_file_path, 'w') as f:
                f.write(r.text)
        else:
            self.assertFalse()


    def test_single(self):
        import postman2md
        postman2md.convert(postman_file=self.dump_file_path, multi_file=False)
        

    def test_multi(self):
        import postman2md
        postman2md.convert(postman_file=self.dump_file_path)


    def tearDown(self):
        import os 
        if os.path.exists(self.dump_file_path):
            os.remove(self.dump_file_path)

