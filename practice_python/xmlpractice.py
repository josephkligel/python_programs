import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attr):
        print(name)

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('example.xml')

# handler = xml.sax.ContentHandler()
# parser = xml.sax.make_parser()
# parser.setContentHandler(handler)
# parser.parse('example.xml')
