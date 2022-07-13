import time
import spacy
import spacy.cli
from collections import Counter 
import math
import json
import re
import http.client, urllib.parse


conn = http.client.HTTPConnection('api.positionstack.com')


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search




f = open('bangalore_news (1)', 'r')
content = f.readlines()
f.close()

lne = {'KP Agrahara', 'BVK Iyengar Road', 'Kothanur', 'Kalkere', 'Kumara Park West', 'DVG Road', 'Yelachenahalli', 'New Guddadahalli', '16th Cross', 'HMT', 'Church Road', 'ITI Layout', 'Nala Road', 'Electronic City', 'Chickpet', 'Tavarekere', 'Iblur', 'Kumaraswamy Layout', 'Kanakapura Main Road', 'Kempapura', 'Kumara Park', 'Hosahalli Main Road', 'Manjunatha Nagar', 'St. Marks Road', 'Brigade Road', 'Carmelaram', 'Richmond Town', 'Shantinagar', 'Vidyapeeta', 'Hoskote', 'Banashankari', 'Ejipura', 'Nandidurga Road', 'Wilson Garden', 'Suranjan Das Road', '8th Cross', 'Veeranapalya', 'MM Road', 'Kacharakanahalli', 'Hoysala Nagar', 'Thanisandra', 'Shivaji Nagar', 'Austin Town', 'South End Circle', 'Konanakunte', 'Sultanpet', 'Kaveripura', 'HSR Layout', 'Nayandahalli', 'Basavanapura', 'Bellandur', 'Ashwath Nagar', 'Vikram Hospital', 'Sunkadakatte', 'Richmond Circle', 'Sarjapur Road', 'Margosa Road', 'Thanisandra Main Road', 'Museum Road', 'Mahalakshmi Layout', 'Gandhi Bazaar', 'MICO Layout', 'Kaveri', 'Ashok Nagar', 'Devasandra', 'Begur Road', 'Seegehalli', 'Padarayanapura', 'Sarjapur', 'Banashankari 3rd Stage', 'Lakshmi Road', 'Davis Road', 'Magadi Road', 'Hesaraghatta Main Road', 'Hebbal Kempapura', 'RBI Layout', 'Narayanapura', 'Shastri Nagar', 'RK Puram', 'Gandhi Circle', 'Marathahalli', 'Seshadripuram', 'Bommasandra Industrial Area', 'Hosa Road', 'High Grounds', 'Kengeri Satellite Town', 'Crescent Road', 'Kasturba Road', 'Nagarathpet', 'Coles Park', 'Madiwala', 'Bharathi Nagar', 'Bommasandra', 'New BEL Road', 'Kumbalgodu', 'Main Road', 'OMBR Layout', 'Lavelle Road', 'Veerasandra', 'Laggere', 'Main', 'Block', 'Cooke Town', 'Koramangala 5th Block', 'Ring Road', 'Srinivasanagar', 'Bose Garden', 'Siddapur', 'Chord Road', '9th Block', 'Vidyaranyapura', 'Sampige Road', 'Basavanagudi', 'Residency Road', 'Sree Kanteerava Stadium', 'Kaval Byrasandra', 'Richmond Road', 'Hulimavu', 'Berlie Street', 'Yeshwanthpur', 'Electronics City', 'Seshadri Road', 'Ramamurthy Nagar', 'GKW Layout', 'Govindpura', 'Mathikere', 'Domlur', 'Hebbal', 'Kodihalli', 'Byadarahalli', 'Girinagar', 'HAL Airport Road', 'Isro', 'Thubarahalli', 'KHB Colony', 'Cubbon Road', 'Bagalagunte', 'Kumara Park East', 'Siddapura', 'Ibrahim Sahib Street', 'Church Street', 'Subedar Chatram Road', 'Jogupalya', 'Cox Town', 'Doddanekundi', 'Cunningham Road', 'Palace Road', 'Tilak Nagar', 'Yelahanka', 'Kalasipalyam', 'Jigani', '3rd Cross', 'Giri Nagar', 'Goodshed Road', 'Lakshminarayanapura', 'Begur', 'Anekal', 'Sanjay Nagar', 'Hennur', 'Puttenahalli', 'Bull Temple Road', 'Indira Nagar', 'Nagarabhavi', 'Jeevan Bheema Nagar', 'Avenue Road', 'Golf Course Road', 'Whitefield', 'Mysore Road', 'MLA Layout', 'Bhoopasandra', 'B. Narayanapura', 'Murphy Town', 'Peenya', 'Sampangirama Nagar', 'Hosur Road', 'Old Airport Road', 'Chandni Chowk Road', 'Commercial Street', 'St. Johns Road', 'GM Palya', 'Richards Town', 'Gandhi Nagar', 'Kengeri', 'Brookefield', 'Chamarajpet', 'Nagavara', 'Singasandra', 'Horamavu', 'Adugodi', 'Sankey Road', 'Kanakpura Road', 'Airport Road', '5th Cross', 'RT Nagar', 'Hongasandra', 'BEML Layout', 'Kundalahalli', 'Kanakapura Road', 'Dickenson Road', 'Varthur Main Road', 'Wheeler Road', 'Intermediate Ring Road', 'HRBR Layout', 'Srinagar', 'Peenya Industrial Area', 'Varthur', 'Banaswadi', 'Anand Rao Circle', 'Malleswaram', 'Basaveshwara Nagar', 'Hennur Road', 'Moti Nagar', 'Queens Road', 'New Thippasandra', 'HAL', 'Koramangala', 'Gandhi Bazaar Main Road', 'Nandini Layout', 'Infantry Road', 'Kaggadasapura', 'Outer Ring Road', 'Chandra Layout', 'BTM Layout', 'Old Madras Road', 'KK Halli', 'Neelasandra', 'Majestic', 'Race Course Road', 'Byatarayanapura', 'Mico Layout', 'Banaswadi Main Road', 'Service Road', 'Lingarajapuram', 'Langford Road', 'Defence Colony', 'Kalyan Nagar', 'Raj Bhavan Road', 'HBR Layout', 'Cubbon Park', 'Lakkasandra', 'Cottonpet', 'Tannery Road', 'Subramanyapura', 'Bannerghatta Road', 'Russell Market'}

files = open(r'outd.txt', 'a')

hey = []


count = 0

for head in content:
    count+=1
    for element in lne:
     try:
        
        line = json.loads(head)
        if findWholeWord(element)(line["locationNER"]) != None:

          try:
            params = urllib.parse.urlencode({
              'access_key': 'ed76926be967a852531025123aa4c29c',
              'query': element+" (Bangalore)",
                'limit': 1,
                'fields' : 'results.latitude, results.longitude',
               })

            conn.request('GET', '/v1/forward?{}'.format(params))

            res = conn.getresponse()
            data = res.read()
            hey.append(line)
            news_number = hey.append('"news_number": "'+str(count)+'"')
            matched_lne = hey.append('"matched_lne": "'+str(element)+'"')
            latitude = hey.append('"latitude": "'+str(((json.loads(data.decode('utf-8'))["data"])[0])["latitude"])+'"')
            longitude = hey.append('"longitude": "'+str(((json.loads(data.decode('utf-8'))["data"])[0])["longitude"])+'"')
            
            print(hey, file=files)
            hey = []
          except:
            print("error")
     except:
        pass

files.close()        

# print(findWholeWord("arun vihar")("hello there vihar kartarpura arun vihar"))