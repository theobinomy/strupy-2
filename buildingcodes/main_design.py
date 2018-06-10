from geopy.geocoders import Nominatim

def geoaddr(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address, addressdetails = True)
    return location.raw
  
def appcode(state):
    if state == 'OR':
        print('OSSC -14')
        print('IBC -12')
        print('ACI 318 -11')
        print('NDS -12')
        print('AISC -10')
    elif state == 'WA':
        print('IBC -15')
        print('ASCE 7 -10')
        print('ACI 318 -14')
        print('NDS -15')
        print('AISC -10')
    elif state == 'CA': 
        print('CBC -16')
        print('ASCE 7 -10')
        print('ACI 318 -14')
        print('NDS -15')
        print('AISC -10')
         

if __name__ =='__main__':
    print('this will walk you through the design guideline process')
    print('the first step is to establish the governing codes')
    print('What is the address?')
    rawsite = geoaddr(input('enter state address: '))
    state = rawsite['address']['state']
    lat = rawsite['lat']
    lon = rawsite['lon']
    print(state, lat, lon)
    appcode(state)
    
    print('next is load generation')
    if state == 'Washington':
        print('wind load = 135 mph, Vult')
    elif state == 'Oregon':
        print('wind load = 120 mph, vult')
   

