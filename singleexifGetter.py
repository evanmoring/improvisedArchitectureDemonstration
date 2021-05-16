from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import json

def get_exif(image_file_path):
    exif_table = {}
    image = Image.open(image_file_path)
    info = image._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value
    gps_info = {}
    for key in exif_table['GPSInfo'].keys():
        decode = GPSTAGS.get(key,key)
        gps_info[decode] = exif_table['GPSInfo'][key]
    return gps_info

def get_GPS_from_image (fn):
    filename = fn
    exif = get_exif(filename)
    print(exif)
    #print(exif)
    cLat = exif['GPSLatitude']
    cLon = exif['GPSLongitude']
##    print(exif['GPSLatitude'])
##    print(exif['GPSLongitude'])
##    print(exif['GPSLongitudeRef'])
##    print(exif['GPSLatitudeRef'])
    
    dLat = cLat[0][0] + (cLat[1][0]/60) + ((cLat[2][0]/3600/10000))
    dLon = cLon[0][0] + (cLon[1][0]/60) + ((cLon[2][0]/3600/10000))
    if (exif['GPSLatitudeRef']=='S'):
        dLat *= -1
    if (exif['GPSLongitudeRef']=='W'):
        dLon *= -1
    return [fn,dLat, dLon]

def compressImage (filename):
    	toCompressImage = Image.open("images/"+filename)
    	toCompressImage.save("compressed/"+filename, optimize=True, quality=10)

    
#print(get_GPS_from_image('testImage.jpg'))

imageDataList = []
##for image in os.listdir('images'):
##    imageDataList.append(get_GPS_from_image (image))
##    compressImage(image)
print(get_GPS_from_image ('test.jpg'))

