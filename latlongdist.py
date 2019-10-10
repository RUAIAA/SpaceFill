import math
def convertdist(lat1,long1,lat2,long2):
    long1 = math.radians(long1)
    lat1 = math.radians(lat1)
    long2 = math.radians(long2)
    lat2 = math.radians(lat2)

    a = (math.sin((lat2-lat1)/2)**2)+ math.cos(lat1)*math.cos(lat2)*(math.sin((long2-long1)/2)**2)
    d = 2*6371100*math.asin(math.sqrt(a))
    return d

def latLongToCart(latPoint, longPoint, latOrigin, longOrigin):
    x = convertdist(latOrigin, longPoint, latOrigin, longOrigin)
    y = convertdist(latPoint, longOrigin, latOrigin, longOrigin)
    return (x, y)
