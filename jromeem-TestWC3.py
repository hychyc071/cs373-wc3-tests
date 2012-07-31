import unittest
from google.appengine.ext import testbed

from google.appengine.api.labs import taskqueue 

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump
from minixsv import pyxsval as xsv

import XMLHelpers
from MainHandler import link_values
from DataModels import Person, Organization, Crisis, Link

class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # First, create an instance of the Testbed class.
        cls.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        cls.testbed.activate()
        # Next, declare which service stubs you want to use.
        cls.testbed.init_datastore_v3_stub()

    @classmethod
    def tearDownClass(cls):
        #assert(False)
        cls.testbed.deactivate()

    def test_mergeLinks1(self):
        xml_file = open("test/test_mergelinks1.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : False})
        xml_file = open("test/test_mergelinks4.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : True})
        temp = db.GqlQuery("SELECT * FROM Link")
        
        #Stuff
        for i in temp:
            if i.link_type == "image":
                self.assert_(i.link_url == "http://images5.fanpop.com/image/photos/30600000/Mr-President-WTF-weegee-vs-tails-doll-30625832-435-360.jpg")
                break

        db.delete(db.Query())        

    def test_mergeLinks2(self):
        xml_file = open("test/test_mergelinks2.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : False})
        xml_file = open("test/test_mergelinks4.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : True})
        temp = db.GqlQuery("SELECT * FROM Link")
        
        #Stuff

        db.delete(db.Query())

    def test_mergeLinks3(self):
        xml_file = open("test/test_mergelinks1.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : False})
        xml_file = open("test/test_mergelinks1.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : True})
        temp = db.GqlQuery("SELECT * FROM Link")
        
        for i in temp:
            if i.link_type == "image":
                self.assert_(i.link_url == "")
                break

        db.delete(db.Query())

    def test_mergeModels1(self):
        xml_file = open("test/test_mergemodels1.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : False})
        temp = db.GqlQuery("SELECT * FROM Crisis")

        before_merge = ''
        for c in temp:
            before_merge = c.info_resources
        
        xml_file = open("test/test_mergelinks1.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : True})
        temp = db.GqlQuery("SELECT * FROM Crisis")

        after_merge = ''
        for c in temp:
            after_merge = c.info_resources

        self.assert_(before_merge == after_merge)

        db.delete(db.Query())

    def test_mergeModels2(self):
        xml_file = open("test/test_mergemodels1.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : False})
        temp = db.GqlQuery("SELECT * FROM Crisis")

        before_merge = ''
        for c in temp:
            before_merge = c.info_resources
            break
        
        xml_file = open("test/test_mergelinks2.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : False})
        temp = db.GqlQuery("SELECT * FROM Crisis")

        after_merge = ''
        for c in temp:
            after_merge = c.info_resources
            break

        self.assert_(before_merge != after_merge)

        db.delete(db.Query())

    def test_mergeModels3(self):
        xml_file = open("test/test_mergemodels3.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : False})
        temp = db.GqlQuery("SELECT * FROM Crisis")

        before_merge = ''
        for c in temp:
            before_merge = c.info_resources
        
        xml_file = open("test/test_mergelinks4.xml", 'rb')
        XMLHelpers.parseXML2(xml_file,{'check': False, 'merge' : False})
        temp = db.GqlQuery("SELECT * FROM Crisis")

        after_merge = ''
        for c in temp:
            after_merge = c.info_resources

        self.assert_(before_merge != after_merge)

        db.delete(db.Query())
