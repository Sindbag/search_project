#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from search.indexer import split_query
from search.indexer import InvIndex
from search.indexer import build_index
from search.query import Query
from search.indexer import split_query
from search.indexer import index


class TestInvIndexGetMethods(unittest.TestCase):
    def test_inv_index_get_empty_request(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["qwerty"] = set([3])     
        inverted_index.dictionary["admin"] = set([3])  
        inverted_index.dictionary["father"] = set([2])  
        inverted_index.dictionary["fatnet"] = set([1])  
        inverted_index.dictionary["codeforces"] = set([1])
        inverted_index.dictionary["sister"] = set([2])    
        inverted_index.dictionary["qw"] = set([0])  
        inverted_index.dictionary["rn"] = set([0])  
        inverted_index.dictionary["we"] = set([0])
        inverted_index.dictionary["et"] = set([0])        
        q = Query("")
        self.assertEqual(inverted_index.get_all(q), [])  
        
    def test_inv_index_get_max_len_2(self):
        inverted_index = InvIndex()  
        inverted_index.dictionary["qw"] = set([0])  
        inverted_index.dictionary["rn"] = set([0])  
        inverted_index.dictionary["we"] = set([0])
        inverted_index.dictionary["et"] = set([0])        
        q = Query("we ty  gh kj bn ар лд нп ша")
        self.assertEqual(inverted_index.get_all(q), [])
        
    def test_inv_index_get_words_in_one_document(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["qwerty"] = set([3])     
        inverted_index.dictionary["admin"] = set([3])  
        inverted_index.dictionary["father"] = set([2])  
        inverted_index.dictionary["fatnet"] = set([1])  
        inverted_index.dictionary["codeforces"] = set([1])
        inverted_index.dictionary["sister"] = set([2])    
        inverted_index.dictionary["qw"] = set([0])  
        inverted_index.dictionary["rn"] = set([0])  
        inverted_index.dictionary["we"] = set([0])
        inverted_index.dictionary["et"] = set([0])        
        q = Query("codeforces fatnet  father qwerty")
        self.assertEqual(inverted_index.get_all(q), [1,2,3]) 
        
    def test_inv_index_get_words_in_many_documents(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["qwerty"] = set([3])     
        inverted_index.dictionary["admin"] = set([3, 4, 5, 6, 7, 8])  
        inverted_index.dictionary["father"] = set([2, 8, 10])  
        inverted_index.dictionary["fatnet"] = set([1, 8, 9])  
        inverted_index.dictionary["codeforces"] = set([1, 8])
        inverted_index.dictionary["sister"] = set([2, 9, 10])    
        inverted_index.dictionary["qw"] = set([0])  
        inverted_index.dictionary["rn"] = set([0])  
        inverted_index.dictionary["we"] = set([0])
        inverted_index.dictionary["et"] = set([0])        
        q = Query("codeforces fatnet  father qwerty admin qw we")
        self.assertEqual(inverted_index.get_all(q), [8, 1, 3, 2, 4, 5, 6, 7, 9, 10])     
        
    def test_inv_index_get_no_words_in_the_documents(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["qwerty"] = set([3])     
        inverted_index.dictionary["admin"] = set([3, 4, 5, 6, 7, 8])  
        inverted_index.dictionary["father"] = set([2, 8, 10])  
        inverted_index.dictionary["fatnet"] = set([1, 8, 9])  
        inverted_index.dictionary["codeforces"] = set([1, 8])
        inverted_index.dictionary["sister"] = set([2, 9, 10])    
        inverted_index.dictionary["qw"] = set([0])  
        inverted_index.dictionary["rn"] = set([0])  
        inverted_index.dictionary["we"] = set([0])
        inverted_index.dictionary["et"] = set([0])        
        q = Query("пароль тема признак призрак")
        self.assertEqual(inverted_index.get_all(q), []) 
    
    def test_inv_index_get_all(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["qwerty"] = set([3])     
        inverted_index.dictionary["admin"] = set([3, 4, 5, 6, 7, 8])  
        inverted_index.dictionary["father"] = set([2, 8, 10])  
        inverted_index.dictionary["fatnet"] = set([1, 8, 9])  
        inverted_index.dictionary["codeforces"] = set([1, 8])
        inverted_index.dictionary["sister"] = set([2, 9, 10])    
        inverted_index.dictionary["qw"] = set([0])  
        inverted_index.dictionary["rn"] = set([0])  
        inverted_index.dictionary["we"] = set([0])
        inverted_index.dictionary["et"] = set([0])        
        q = Query("пароль тема признак призрак, er rt oi ug dj vh xb nt ck пр по ро ар ва ка на не ни рп ра сп, qwerty admin father")
        self.assertEqual(inverted_index.get_all(q), [3, 8, 2, 4, 5, 6, 7, 10])  
        
        
    def test_split_query_0(self):       
        q = split_query(Query("codeforces fatnet father qwerty").get_text())
        self.assertEqual(q, ["codeforces", "fatnet",  "father", "qwerty"])    
        
    def test_split_query_space(self):      
        q = split_query(Query("         codeforces      fatnet                      father            qwerty      ").get_text())
        self.assertEqual(q, ["codeforces", "fatnet",  "father", "qwerty"])  
        
    def test_split_query_exclamation_mark(self):       
        q = split_query(Query("!!!!!!!! staf02 !!!!!!!! eagIe !!!!!!!!!!").get_text())
        self.assertEqual(q, ["staf02", "eagIe"])
        
    def test_split_query_question_mark(self):       
        q = split_query(Query("qwerty ?????????? staf02 ??????????????? eagIe ???????????").get_text())
        self.assertEqual(q, ["qwerty", "staf02", "eagIe"])    
        
    def test_split_query_minus(self):      
        q = split_query(Query("---- cf ------ codeforces ------------------- fatnet --------- go ---------").get_text())
        self.assertEqual(q, ["codeforces", "fatnet"])    
        
    def test_split_query_plus(self):      
        q = split_query(Query("+++ cf ++++ codeforces +++++++++ fatnet +++++++ go ++++++").get_text())
        self.assertEqual(q, ["codeforces", "fatnet"])
        
    def test_split_query_point(self):      
        q = split_query(Query("red.... blue..... black").get_text())
        self.assertEqual(q, ["red", "blue", "black"])
        
    def test_split_query_comma(self):      
        q = split_query(Query("red,,,,,,, ,blue,,,,,,, ,black,").get_text())
        self.assertEqual(q, ["red", "blue", "black"])
        
    def test_split_query_bigrams(self):      
        q = split_query(Query("qw er ty no ng hf k jf  j j j dl l j  ао ое оа он но ка те").get_text())
        self.assertEqual(q, [])  
        
    def test_split_query_all(self):      
        q = split_query(Query("!!! пароль      == password,,,,,father   != fatnet.... пa - но,@#   name((username)) goodbay").get_text())
        self.assertEqual(q, ["пароль", "password", "father", "fatnet", "name", "username", "goodbay"])  

    def test_build(self):
        build_index("../test")
        arr = ["hello", "honey", "pie", "good", "very", "bad", "window", "apple", "name", "grigorij", "like", "apples", "bye"]
        arr.sort()
        arr1 = index.dictionary.keys()
        arr1.sort()
        self.assertEqual(arr1, arr)

if __name__ == '__main__':
    unittest.main()