import app

import unittest

di, do = app.update_date()

class Accounting_test(unittest.TestCase):
    def setUp(self):
        app.directories, app.documents = app.update_date()
        
    def test_check_document_existance(self):
        self.assertTrue(app.check_document_existance('2207 876234'))
        self.assertFalse(app.check_document_existance('88005553535'))
        
    def test_get_all_doc_owners_names(self):
        self.assertSetEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'})
        
    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf('256'), ('256', True))
        self.assertNotEqual(add_new_shelf('257'), ('255', True))
        
    
        
if __name__ == '__main__':       
    unittest.main()