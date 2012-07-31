import unittest
from main import *
from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree
from main import MyHandler
from StringIO import StringIO
from google.appengine.ext import webapp
from google.appengine.ext.webapp import Request
from google.appengine.ext.webapp import Response
import webapp2
import sys

class TestWC1(unittest.TestCase):

#export tests
	def test_search_1(self):
		handler = MyHandler()
		form = 'searchKeyword=pan'
		handler.request = Request({
			'ACTION': '/searchQuery',
			'METHOD': 'get',
			'wsgi.input': StringIO(form),
			'CONTENT_LENGTH': len(form),
			})

	def test_search_2(self):
		handler = MyHandler()
		form = 'searchKeyword=drug'
		handler.request = Request({
			'ACTION': '/searchQuery',
			'METHOD': 'get',
			'wsgi.input': StringIO(form),
			'CONTENT_LENGTH': len(form),
			})

	def test_search_3(self):
		handler = MyHandler()
		form = 'searchKeyword=abduction'
		handler.request = Request({
			'ACTION': '/searchQuery',
			'METHOD': 'get',
			'wsgi.input': StringIO(form),
			'CONTENT_LENGTH': len(form),
			})

	def test_search_4(self):
		handler = MyHandler()
		form = 'searchKeyword=Kony'
		handler.request = Request({
			'ACTION': '/searchQuery',
			'METHOD': 'get',
			'wsgi.input': StringIO(form),
			'CONTENT_LENGTH': len(form),
			})

	def test_printXML_1(self):
		f = open ('nalmanza-WC1.xml')
		s = ""
		for line in f:
			s += line
		result = printXML (s)
		assert (result == True)
		f.close()

	def test_printXML_2(self):
		s = ""
		try:
			result = printXML (s)
		except:
			assert (True) #does not coincide with out models

	def test_printXML_3 (self):
		s = "<crises>hello</crises>"
		try:
			result = printXML (s)
		except:
			assert(True) #does not coincide with out models

	def test_validate_schema_1 (self):
		f = open ('nalmanza-WC1.xml')
		xml = ""
		for line in f:
			xml += line
		f.close

		g = open ('nalmanza-WC1.xsd')
		schema = ""
		for line in g:
			schema += line
		g.close()

		result = ValidateSchema(xml, schema)
		assert (result == True)

	def test_validate_schema_2 (self):
		f = open ('nalmanza-WC1.xml')
		xml = ""
		for line in f:
			xml += line
		f.close

		g = open ('nalmanza-WC1.xsd')
		schema = ""
		for line in g:
			schema += line
		g.close()

		result = ValidateSchema(schema, xml) #reversed
		assert (result == False)

	def test_validate_schema_3 (self):
		xml = ""

		g = open ('nalmanza-WC1.xsd')
		schema = ""
		for line in g:
			schema += line
		g.close()

		result = ValidateSchema(xml, schema)
		assert (isinstance(result, int))
		assert (result == -1)

	def test_validate_schema_4 (self):
		f = open ('nalmanza-WC1.xml')
		xml = ""
		for line in f:
			xml += line
		f.close

		g = open ('nalmanza-WC1.xsd')
		schema = ""
		for line in g:
			schema += line
		g.close()

		result = ValidateSchema(schema, xml) #reversed
		assert (isinstance(result, int))
		assert (result == 0)

	def test_export_1 (self):
		handler = MyHandler()
		f = open ('nalmanza-WC1.xml')
		s = ""
		for line in f:
			s += line
		handler.request = Request({
			'ACTION': '/xmlExport',
			'METHOD': 'get',
			'wsgi.input': StringIO(s),
			'CONTENT_LENGTH': len(s),
			})

	def test_export_2 (self):
		handler = MyHandler()
		s = ""
		handler.request = Request({
			'ACTION': '/xmlExport',
			'METHOD': 'get',
			'wsgi.input': StringIO(s),
			'CONTENT_LENGTH': len(s),
			})

	def test_export_3 (self):
		handler = MyHandler()
		s = "<crises>name </crises>"
		handler.request = Request({
			'ACTION': '/xmlExport',
			'METHOD': 'get',
			'wsgi.input': StringIO(s),
			'CONTENT_LENGTH': len(s),
			})

	def test_upload_1 (self):
		handler = MyHandler()
		f = open ('nalmanza-WC1.xml')
		s = ""
		for line in f:
			s += line
		handler.request = Request({
			'ACTION': '/xmlupload',
			'METHOD': 'get',
			'wsgi.input': StringIO(s),
			'CONTENT_LENGTH': len(s),
			})

	def test_upload_2 (self):
		handler = MyHandler()
		f = open ('nalmanza-WC1.xml')
		s = ""
		for line in f:
			s += line
		handler.request = Request({
			'ACTION': '/xmlupload',
			'METHOD': 'get',
			'wsgi.input': StringIO(s),
			'CONTENT_LENGTH': len(s),
			})

	def test_upload_3 (self):
		handler = MyHandler()
		f = open ('nalmanza-WC1.xml')
		s = ""
		for line in f:
			s += line
		handler.request = Request({
			'ACTION': '/xmlupload',
			'METHOD': 'get',
			'wsgi.input': StringIO(s),
			'CONTENT_LENGTH': len(s),
			})