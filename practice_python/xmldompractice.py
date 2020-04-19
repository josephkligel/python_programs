import xml.dom.minidom

domtree = xml.dom.minidom.parse('example.xml')
catalog = domtree.documentElement

plants = catalog.getElementsByTagName('PLANT')

for plant in plants:
    print(5*'-'+'Plants'+5*'-')
    if plant.hasAttribute('id'):
        print(f'ID: {plant.getAttribute("id")}')

    name = plant.getElementsByTagName('COMMON')[0]
    botanical = plant.getElementsByTagName('BOTANICAL')[0]
    price = plant.getElementsByTagName('PRICE')[0]
    print(f'Name: {name}', f'Botanical Name: {botanical}', f'Price: {price}', sep='\n')

plants[0].getElementsByTagName('COMMON')[0].childNodes[0].nodeValue = 'New Plant'

newPlant = domtree.createElement('PLANT')
newPlant.setAttribute('id', '4')
name = domtree.createElement('COMMON')
name.appendChild(domtree.createTextNode('Undiscovered Plant'))
newPlant.appendChild(name)
catalog.appendChild(newPlant)

domtree.writexml(open('example.xml', 'w'))
