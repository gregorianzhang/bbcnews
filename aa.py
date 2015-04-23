from __future__ import division
import os
import exifread

data=[]

def findfile(filetype):
    """
    get  current working directory filename
    """
    allfile = os.listdir(os.getcwd())
    for x in allfile:
        extensionfile = x.split(".")[-1]
        if extensionfile.lower() == filetype.lower():
            yield x

def getphotoinfo(filename):
    """
    get photo infomation
    """
    date1 = ""
    glon = ""
    glonref = ""
    glat = ""
    glatref = ""
    mode = ""
    dd={}
    with open(filename,'rb') as f:
        dd['filename'] = filename
        dd['data1'] = ""
        dd['mode'] =""
        tags = exifread.process_file(f)
        for tag in tags.keys():
            if tag == "Image DateTime":
                dd['data1'] = tags[tag].values
            if tag == "GPS GPSLongitude":
                glon = tags[tag].values
            if tag == "GPS GPSLatitudeRef":
                glatref = tags[tag]
            if tag == "GPS GPSLatitude":
                glat = tags[tag].values
            if tag == "GPS GPSLongitudeRef":
                glonref = tags[tag]
            if tag == "Image Model":
                dd['mode'] = tags[tag].values

        #calc lon lat
        if glon == "":
            lon = ""
        else:
            lon = float(glon[0].num)/1 + float(glon[1].num)/60 + float(glon[2].num)/float(glon[2].den)/3600
            if glonref == 'W':
                lon = 0 - lon

        dd['lon'] = lon

        if glat == "":
            lat = ""
        else:
            lat = float(glat[0].num)/1 + float(glat[1].num)/60 + float(glat[2].num)/float(glat[2].den)/3600
            if glonref == 'N':
                lat = 0 - lat

        dd['lat'] = lat

        data.append(dd)
    #print data




def writehtml(template,outfile,data):
    lihtml=""
    itemhtml=""
    for x in xrange(len(data)):
        if x == 0:
            lihtml += '<li data-target="#carousel-example-generic" data-slide-to="'+ str(x) +'" class="active"></li>'
            itemhtml += '<div class="item active"><img src="'+data[x]['filename']+'" alt="" height="100%" width="100%" lat="'+str(data[x]['lat'])+'" lon="'+str(data[x]['lon'])+'"><div class="carousel-caption">'+ data[x]['data1'] + " " + data[x]['mode']  +'</div></div>'
        else:
            lihtml += '<li data-target="#carousel-example-generic" data-slide-to="'+ str(x) +'"></li>'
            itemhtml += '<div class="item"><img src="'+data[x]['filename']+'" alt="" height="100%" width="100%" lat="'+str(data[x]['lat'])+'" lon="'+str(data[x]['lon'])+'"><div class="carousel-caption">'+ data[x]['data1'] + " " + data[x]['mode']  +'</div></div>'

    with open(template,'rb') as f1, open(outfile,'wb') as f2:
        for line in f1:
            line = line.replace("abab",lihtml)

            line = line.replace("acac",itemhtml)

            f2.write(line)


        

#    print lihtml +"\n"+ itemhtml


if __name__ == '__main__':
    for x in findfile('jpg'):
    #    print x
        getphotoinfo(x)
    
    print data          
    writehtml('maps_templates.html','maps11.html',data)
