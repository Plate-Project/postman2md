# -*- coding:utf-8 -*-
import os 
import unittest
import requests 

class BasicTestCase(unittest.TestCase):
    
    def setUp(self):
        self.directory = 'postman2md_example'
        self.collection_file_path = 'postman2md_example.json.postman_collection'

    def test_single(self):
        import postman2md
        postman2md.convert(postman_file=self.collection_file_path, multi_file=False)

        file_count =  len([name for name in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, name))])
        self.assertEqual(file_count, 1)
            
    def test_multi(self):
       
        import postman2md
        postman2md.convert(postman_file=self.collection_file_path)
        file_count =  len([name for name in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, name))])
        self.assertGreater(file_count, 1)



 

    def tearDown(self):
        if os.path.exists(self.directory):
            import shutil
            shutil.rmtree(self.directory)
                             


