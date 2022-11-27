# Simple attributed of the page, these are kind of defaults
# they are overwritten when called from pynfeld.py
from flask import Flask, render_template
app = Flask(__name__)

# list of all the possible components of the pynfeld class. The order may change
# page
# title
# navbar 
# host
# port 
# debug
# app
# theme 
# --additional that is added by user ---
# ordered list (ord_lst) -> this should be a dictionary 
# section -> dictionary for a paragraph {heading : "string", paragraph : "string"}
# card -> dictionary {heading : "string", paragraph : "string", image : "filename"}

class Pynfeld:
	"""
	The class is base class that taken in every component that the webpage will take in
	like starting from title, heading, host, port, navbar, app, theme etc. A comprehensive list will 
	be added later. 
	Methods to the class are :
	add_table - a numbered list (this should be made a dictionary that contains link to each item)
	add_section - dictionary that is (heading and paragraph)
	add_card - a heading, an image and a paragraph
	"""

	def __init__(self,default_page, title,navbar, host,port, debug, app, theme):
		self.default_page = default_page
		self.title=title
		self.navbar = navbar
		self.host=host
		self.port=port
		self.debug=debug
		self.app = app
		self.theme = theme
		return None

	def __repr__(self):
		return f"Pynfeld Instance:\n\
Title : {self.title} @ host/port \
: {self.host}/{self.port} with debug : {self.debug}"

	def add_table(self, ord_lst):
		self.ord_lst = ord_lst
		self.len_lst= len(ord_lst)
		return self

	def add_section(self, section_dict):
		self.section_dict = section_dict
		return self
		
	def add_card(self, card_dict):
		self.card_dict = card_dict
		return self

	def run_page(self):
		@self.app.route("/")
		def index():
			return render_template("index.html", title=self.title, navbar = self.navbar, ord_lst = self.ord_lst, 
				len_lst=self.len_lst, section_dict = self.section_dict, theme=self.theme, card_dict = self.card_dict)
		#if __name__ == "__main__":
		self.app.run(self.host, self.port, self.debug)