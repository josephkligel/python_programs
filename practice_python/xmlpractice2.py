import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == 'PLANT':
            print(5*'-'+'Plant'+5*'-')
            id = attrs['id']
            print(f'ID: {id}')

    def endElement(self, item):
        if self.current == 'COMMON':
            print(f'Name: {self.common}')
        elif self.current == 'BOTANICAL':
            print(f'Botanical Name: {self.botanical}')
        elif self.current == 'PRICE':
            print(f'Price: {self.price}')
        else:
            self.current = ''

    def characters(self, content):
        if self.current == 'COMMON':
            self.common = content
        elif self.current == 'BOTANICAL':
            self.botanical = content
        elif self.current == 'PRICE':
            self.price = content

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('example.xml')
