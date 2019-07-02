from HTMLParser import HTMLParser


pstring = source_code = """<span class="UserName"><a href="#">Martin Elias</a></span>"""


class myhtmlparser(HTMLParser):
    def _init_(self):
        self.reset()
        self.NEWTAGS = []
        self.NEWATTRS = []
        self.HTMLDATA = []
    def handle_starttag(self, tag, attrs):
        self.NEWTAGS.append(tag)
        self.NEWATTRS.append(attrs)
    def handle_data(self, data):
        self.HTMLDATA.append(data)
    def clean(self):
        self.NEWTAGS = []
        self.NEWATTRS = []
        self.HTMLDATA = []

parser = myhtmlparser()
parser.feed(pstring)

# Extract data from parser
tags  = parser.NEWTAGS
attrs = parser.NEWATTRS
data  = parser.HTMLDATA

# Clean the parser
parser.clean()

# Print out our data
print(tags)
print(attrs)
print(data)