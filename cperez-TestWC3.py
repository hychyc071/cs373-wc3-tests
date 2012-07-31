import unittest
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed
from WC3 import *

class DSTestCase(unittest.TestCase):

	def setUp(self):
		"""
		# First, create an instance of the Testbed class.
		self.testbed = testbed.Testbed()
		# Then activate the testbed, which prepares the service stubs for use.
		self.testbed.activate()
		# Next, declare which service stubs you want to use.
		self.testbed.init_datastore_v3_stub()
		"""
		# For convenience, the subclass can implement 'set_up' rather than overriding setUp()
		# and calling this base method.
		if hasattr(self, 'set_up'):
			self.set_up()
		pass
	def tearDown(self):
		"""
		self.testbed.deactivate()
		"""
		if hasattr(self, 'tear_down'):
			self.set_up()
		pass
		pass
	
class MyTestCase1 (DSTestCase) :
	def set_up(self):
		model = Organization(
		identifier = "zzzzSalvationArmy", 
		name = "zzzzSalvation Army", 
		info_type = "zzzzEducational", 
		misc = "zzzzThe Outreach Programme on the Rwanda Genocide and the United Nations is an information and educational outreach programme run by the United Nations Department of Public Information.")
		
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).identifier == "zzzzSalvationArmy")
		self.assertTrue(db.get(self.key).name == "zzzzSalvation Army") 
		self.assertTrue(db.get(self.key).info_type == "zzzzEducational") 
		self.assertTrue(db.get(self.key).misc == "zzzzThe Outreach Programme on the Rwanda Genocide and the United Nations is an information and educational outreach programme run by the United Nations Department of Public Information.")
		

class MyTestCase2 (DSTestCase) :
	def set_up(self):
		model = Organization(
		location_city = "zzzzAlexandria", 
		location_region = "zzzzNorth America", 
		location_country = "zzzzUSA", 
		history = "zzzzThe Salvation Army was founded in London's East End in 1865 with a quasi-military structure by one-time Methodist minister William Booth and his wife Catherine.")
		
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).location_city == "zzzzAlexandria") 
		self.assertTrue(db.get(self.key).location_region == "zzzzNorth America") 
		self.assertTrue(db.get(self.key).location_country == "zzzzUSA") 
		self.assertTrue(db.get(self.key).history == "zzzzThe Salvation Army was founded in London's East End in 1865 with a quasi-military structure by one-time Methodist minister William Booth and his wife Catherine.")


class MyTestCase3 (DSTestCase) :
	def set_up(self):
		model = Organization(
		contact_phone = "zzzz232-323-2222",
		contact_email = "zzzzadmin@salv.com", 
		contact_mail_address = "zzzz316 Fall Creek Dr.", 
		contact_mail_city = "zzzzDallas", 
		contact_mail_state = "zzzzTexas", 
		contact_mail_country = "zzzzArgentina", 
		contact_mail_zip  = "zzzz75080")
		
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).contact_phone == "zzzz232-323-2222")
		self.assertTrue(db.get(self.key).contact_email == "zzzzadmin@salv.com") 
		self.assertTrue(db.get(self.key).contact_mail_address == "zzzz316 Fall Creek Dr.") 
		self.assertTrue(db.get(self.key).contact_mail_city == "zzzzDallas") 
		self.assertTrue(db.get(self.key).contact_mail_state == "zzzzTexas") 
		self.assertTrue(db.get(self.key).contact_mail_country == "zzzzArgentina") 
		self.assertTrue(db.get(self.key).contact_mail_zip  == "zzzz75080")


class MyTestCase4 (DSTestCase) :
	def set_up(self):
		model = Organization(
		identifier = "zzzzSalvationArmy", 
		name = "zzzzSalvation Army", 
		info_type = "zzzzEducational", 
		misc = "zzzzThe Outreach Programme on the Rwanda Genocide and the United Nations is an information and educational outreach programme run by the United Nations Department of Public Information.",
		location_city = "zzzzAlexandria", 
		location_region = "zzzzNorth America", 
		location_country = "zzzzUSA", 
		history = "zzzzThe Salvation Army was founded in London's East End in 1865 with a quasi-military structure by one-time Methodist minister William Booth and his wife Catherine.",
		contact_phone = "zzzz232-323-2222",
		contact_email = "zzzzadmin@salv.com", 
		contact_mail_address = "zzzz316 Fall Creek Dr.", 
		contact_mail_city = "zzzzDallas", 
		contact_mail_state = "zzzzTexas", 
		contact_mail_country = "zzzzArgentina", 
		contact_mail_zip  = "zzzz75080")
		
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).identifier == "zzzzSalvationArmy")
		self.assertTrue(db.get(self.key).name == "zzzzSalvation Army") 
		self.assertTrue(db.get(self.key).info_type == "zzzzEducational") 
		self.assertTrue(db.get(self.key).misc == "zzzzThe Outreach Programme on the Rwanda Genocide and the United Nations is an information and educational outreach programme run by the United Nations Department of Public Information.")
		self.assertTrue(db.get(self.key).location_city == "zzzzAlexandria") 
		self.assertTrue(db.get(self.key).location_region == "zzzzNorth America") 
		self.assertTrue(db.get(self.key).location_country == "zzzzUSA") 
		self.assertTrue(db.get(self.key).history == "zzzzThe Salvation Army was founded in London's East End in 1865 with a quasi-military structure by one-time Methodist minister William Booth and his wife Catherine.")
		self.assertTrue(db.get(self.key).contact_phone == "zzzz232-323-2222")
		self.assertTrue(db.get(self.key).contact_email == "zzzzadmin@salv.com") 
		self.assertTrue(db.get(self.key).contact_mail_address == "zzzz316 Fall Creek Dr.") 
		self.assertTrue(db.get(self.key).contact_mail_city == "zzzzDallas") 
		self.assertTrue(db.get(self.key).contact_mail_state == "zzzzTexas") 
		self.assertTrue(db.get(self.key).contact_mail_country == "zzzzArgentina") 
		self.assertTrue(db.get(self.key).contact_mail_zip  == "zzzz75080")


class MyTestCase5 (DSTestCase) :
	def set_up(self):
		model = Crisis(identifier = "RwandaGen",
		name = "Rwanda Genocide",
		info_type = "Murder",
		misc = "Mass genocide of people.")
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).identifier == "RwandaGen")
		self.assertTrue(db.get(self.key).name == "Rwanda Genocide")
		self.assertTrue(db.get(self.key).info_type == "Murder")
		self.assertTrue(db.get(self.key).misc == "Mass genocide of people.")


class MyTestCase6 (DSTestCase) :
	def set_up(self):
		model = Crisis(
		location_city = "Santiago",
		location_region = "New York",
		location_country = "Rwanda",)
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).location_city == "Santiago")
		self.assertTrue(db.get(self.key).location_region == "New York")
		self.assertTrue(db.get(self.key).location_country == "Rwanda")

class MyTestCase7 (DSTestCase) :
	def set_up(self):
		model = Crisis(
		time = "15:20",
		day = 31,
		month = 03,
		year = 1948,
		time_misc = "20th century",)
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).time == "15:20")
		self.assertTrue(db.get(self.key).day == 31)
		self.assertTrue(db.get(self.key).month == 03)
		self.assertTrue(db.get(self.key).year == 1948)
		self.assertTrue(db.get(self.key).time_misc == "20th century")


class MyTestCase8 (DSTestCase) :
	def set_up(self):
		model = Crisis(
		history = "There had always been heavy ethnic tension between the majority Hutu people and the Tutsis in Rwanda since the country's establishment.",
		help = "Awareness",
		resources = "",
		human_impact_injured= 344,
		human_impact_deaths = 111,
		human_impact_missing = 19999,
		human_impact_displaced = 1222,
		economic_impact_amount = 10000000,
		economic_impact_currency = "US$",
		economic_impact_misc = "10000")
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).history == "There had always been heavy ethnic tension between the majority Hutu people and the Tutsis in Rwanda since the country's establishment.")
		self.assertTrue(db.get(self.key).help == "Awareness")
		self.assertTrue(db.get(self.key).resources == "")
		self.assertTrue(db.get(self.key).human_impact_injured == 344)
		self.assertTrue(db.get(self.key).human_impact_deaths == 111)
		self.assertTrue(db.get(self.key).human_impact_missing  == 19999)
		self.assertTrue(db.get(self.key).human_impact_displaced == 1222)
		self.assertTrue(db.get(self.key).economic_impact_amount == 10000000)
		self.assertTrue(db.get(self.key).economic_impact_currency == "US$")
		self.assertTrue(db.get(self.key).economic_impact_misc == "10000")

class MyTestCase9 (DSTestCase) :
	def set_up(self):
		model = Crisis(identifier = "RwandaGen",
		name = "Rwanda Genocide", info_type = "Murder",
		misc = "Mass genocide of people.",
		location_city = "Santiago",
		location_region = "New York",
		location_country = "Rwanda",
		time = "15:20",
		day = 31,
		month = 03,
		year = 1948,
		time_misc = "20th century",
		history = "There had always been heavy ethnic tension between the majority Hutu people and the Tutsis in Rwanda since the country's establishment.",
		help = "Awareness",
		resources = "",
		human_impact_injured= 344,
		human_impact_deaths = 111,
		human_impact_missing = 19999,
		human_impact_displaced = 1222,
		economic_impact_amount = 10000000,
		economic_impact_currency = "US$",
		economic_impact_misc = "10000")
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).identifier == "RwandaGen")
		self.assertTrue(db.get(self.key).name == "Rwanda Genocide")
		self.assertTrue(db.get(self.key).info_type == "Murder")
		self.assertTrue(db.get(self.key).misc == "Mass genocide of people.")
		self.assertTrue(db.get(self.key).location_city == "Santiago")
		self.assertTrue(db.get(self.key).location_region == "New York")
		self.assertTrue(db.get(self.key).location_country == "Rwanda")
		self.assertTrue(db.get(self.key).time == "15:20")
		self.assertTrue(db.get(self.key).day == 31)
		self.assertTrue(db.get(self.key).month == 03)
		self.assertTrue(db.get(self.key).year == 1948)
		self.assertTrue(db.get(self.key).time_misc == "20th century")
		self.assertTrue(db.get(self.key).history == "There had always been heavy ethnic tension between the majority Hutu people and the Tutsis in Rwanda since the country's establishment.")
		self.assertTrue(db.get(self.key).help == "Awareness")
		self.assertTrue(db.get(self.key).resources == "")
		self.assertTrue(db.get(self.key).human_impact_injured == 344)
		self.assertTrue(db.get(self.key).human_impact_deaths == 111)
		self.assertTrue(db.get(self.key).human_impact_missing  == 19999)
		self.assertTrue(db.get(self.key).human_impact_displaced == 1222)
		self.assertTrue(db.get(self.key).economic_impact_amount == 10000000)
		self.assertTrue(db.get(self.key).economic_impact_currency == "US$")
		self.assertTrue(db.get(self.key).economic_impact_misc == "10000")
		

class MyTestCase10 (DSTestCase) :
	def set_up(self):
		model = Person(identifier = "PaulRuse", 
		name = "Paul Ruse", 
		info_type = "Natural Disaster", 
		misc = "Paul Rusesabagina is a Rwandan humanitarian known for hiding and protecting 1,268 refugees during the Rwandan Genocide.")


		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).identifier == "PaulRuse")
		self.assertTrue(db.get(self.key).name == "Paul Ruse")
		self.assertTrue(db.get(self.key).info_type == "Natural Disaster")
		self.assertTrue(db.get(self.key).misc == "Paul Rusesabagina is a Rwandan humanitarian known for hiding and protecting 1,268 refugees during the Rwandan Genocide.")


class MyTestCase11 (DSTestCase) :
	def set_up(self):
		model = Person(
		birthdate_time = "9:15", 
		birthdate_day  = 25, 
		birthdate_month = 06, 
		birthdate_year = 1906, 
		birthdate_misc = "born in a leap year", 
		nationality = "American", 
		biography = "Michael Johanns is an American Republican politician.")


		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).birthdate_time == "9:15")
		self.assertTrue(db.get(self.key).birthdate_day  == 25)
		self.assertTrue(db.get(self.key).birthdate_month == 06)
		self.assertTrue(db.get(self.key).birthdate_year == 1906)
		self.assertTrue(db.get(self.key).birthdate_misc == "born in a leap year")
		self.assertTrue(db.get(self.key).nationality == "American")
		self.assertTrue(db.get(self.key).biography == "Michael Johanns is an American Republican politician.")

class MyTestCase12 (DSTestCase) :
	def set_up(self):
		model = Person(identifier = "PaulRuse", 
		name = "Paul Ruse", 
		info_type = "Natural Disaster", 
		misc = "Paul Rusesabagina is a Rwandan humanitarian known for hiding and protecting 1,268 refugees during the Rwandan Genocide.", 
		birthdate_time = "9:15", 
		birthdate_day  = 25, 
		birthdate_month = 06, 
		birthdate_year = 1906, 
		birthdate_misc = "born in a leap year", 
		nationality = "American", 
		biography = "Michael Johanns is an American Republican politician.")


		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).identifier == "PaulRuse")
		self.assertTrue(db.get(self.key).name == "Paul Ruse")
		self.assertTrue(db.get(self.key).info_type == "Natural Disaster")
		self.assertTrue(db.get(self.key).misc == "Paul Rusesabagina is a Rwandan humanitarian known for hiding and protecting 1,268 refugees during the Rwandan Genocide.")
		self.assertTrue(db.get(self.key).birthdate_time == "9:15")
		self.assertTrue(db.get(self.key).birthdate_day  == 25)
		self.assertTrue(db.get(self.key).birthdate_month == 06)
		self.assertTrue(db.get(self.key).birthdate_year == 1906)
		self.assertTrue(db.get(self.key).birthdate_misc == "born in a leap year")
		self.assertTrue(db.get(self.key).nationality == "American")
		self.assertTrue(db.get(self.key).biography == "Michael Johanns is an American Republican politician.")


class MyTestCase13 (DSTestCase) :
	def set_up(self):
		model = Organization(
		identifier = "zzzzSalvationArmy", 
		name = "zzzzSalvation Army", 
)
		model.put()
		self.key = model.key()
		self.fromdb = db.get(model.key())
		
	def tear_down():
		db.delete(self.key())
	
	def test_org_1(self):
		self.assertTrue(db.get(self.key).identifier == "zzzzSalvationArmy")
		self.assertTrue(db.get(self.key).name == "zzzzSalvation Army") 

	def testMedia1(self) :
		media = Media()
		media.title = "Foo Title"
		self.assert_(media.title == "Foo Title")

	def testMedia2(self) :
		media = Media()
		media.site = "YouTube"
		self.assert_(media.site == "YouTube")

	def testMedia3(self) :
		media = Media()
		media.url = "http://hello.com"
		self.assert_(media.url == "http://hello.com")

	def testMedia4(self) :
		media = Media()
		media.description = "This is the video Description!"
		self.assert_(media.description == "This is the video Description!")

	def testCrisis1(self) :
		crisis = Crisis()
		crisis.identifier = "RwandaGen"
		crisis.name = "Rwanda Genocide"
		crisis.info_type = "Murder"
		self.assert_(crisis.identifier == "RwandaGen")
		self.assert_(crisis.name == "Rwanda Genocide")
		self.assert_(crisis.info_type == "Murder")
	
	def testCrisis2(self) :
		crisis = Crisis()
		crisis.location_city = "Austin"
		crisis.location_region = "Travis"
		crisis.location_country = "Merica"
		self.assert_(crisis.location_city == "Austin")
		self.assert_(crisis.location_region == "Travis")
		self.assert_(crisis.location_country == "Merica")

	def testCrisis3(self) :
		crisis = Crisis()
		crisis.help = None
		crisis.history = "brief or long history describing the topic."
		crisis.info_type = "Murder"
		crisis.misc = None
		self.assert_(crisis.help == None)
		self.assert_(crisis.history == "brief or long history describing the topic.")
		self.assert_(crisis.info_type == "Murder")
		self.assert_(crisis.misc == None)

	def testEconomicImpact1(self) :
		crisis = Crisis()
		crisis.economic_impact_ammount = 10000000000
		crisis.economic_impact_currency = "Euros"
		crisis.economic_impact_misc = None
		self.assert_(crisis.economic_impact_ammount == 10000000000)
		self.assert_(crisis.economic_impact_currency == "Euros")
		self.assert_(crisis.economic_impact_misc == None)

	def testHumanimpact1(self) :	
		crisis = Crisis()
		crisis.human_impact_deaths = 0
		crisis.human_impact_displaced = 1
		crisis.human_impact_injured = 2
		crisis.human_impact_missing = 3
		crisis.human_impact_misc = None
		self.assert_(crisis.human_impact_deaths == 0)
		self.assert_(crisis.human_impact_displaced == 1)
		self.assert_(crisis.human_impact_injured == 2)
		self.assert_(crisis.human_impact_missing == 3)
		self.assert_(crisis.human_impact_misc == None)


	def test_Media_site(self):
		model = Media(site = "YouTube")
		self.assert_(model.site == "YouTube")

	def test_Media_title(self):
		model = Media(title = "Avian Flu: The H5N1 virus")
		self.assert_(model.title == "Avian Flu: The H5N1 virus")

	def test_Media_url(self):
		model = Media(url = "http://www.youtube.com/embed/uHPBdjCFDkE")
		self.assert_(model.url == "http://www.youtube.com/embed/uHPBdjCFDkE")

	def test_Media_description(self):
		model = Media(description = "A veterinarian explains what exactly the H5N1 Avian Flu virus is about.")
		self.assert_(model.description == "A veterinarian explains what exactly the H5N1 Avian Flu virus is about.")

		
		
if __name__ == '__main__':
		unittest.main()
