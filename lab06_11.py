#-*- coding:utf-8 -*-
#!/usr/bin/python


dict1 = {
        "London": ["British Museum", "TATE Britain", "TATE Modern", "National Gallery","Natural History Museum", "Victoria and Albert Museum"],
        "Lisbon" : ["Ancient Art Museum", "Design Museum", "Tile Museum", "Berado Museum","Belem Cultural Centre"],
        "Madrid" : ["Prado", "Reina Sofia", "Thyssen", "CaixaForum"],
        "Paris" : ["Musée Rodin", "Louvre", "Musée d'Orsay", "Centre Georges-Pompidou" ],
        "Rome" : ["Galleria Borghese", "Palazzo Barberini", "Vatican Museum", "Galleriad'arte contemporanea"],
        "Berlin" : ["Deutsches Historisches Musem", "DDR Museum", "Altes Museum", "AlteNationalgalerie"],
        "Vienna": ["Albertina", "Leopold Museum", "Kunst historisches museum", "SigmundFreud Museum"],
        }

with open('the european tour.html','w') as html:
    html.write('<html>' + '\n')
    html.write('<head><title>European Grand Tour</title></head>' + '\n')
    html.write('<body>' + '\n')
    html.write('<h1>European Grand Tour</h1>' + '\n')

    for k,v in dict1.iteritems():
        html.write('<h2>' + k + '</h2>' + '\n')
        html.write('<ul>' + '\n')
        for a in v:
            html.write('<li>' + a + '</li>' + '\n')
        
        html.write('</ul>' + '\n')
    html.write('</body>'+ '\n')
    html.write('</html>'+ '\n')

        
#print dict1
