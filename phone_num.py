import phonenumbers
from phonenumbers import geocoder,carrier


number='+9779867922731'

ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en")) #displays the country name

service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))#displays the service provider.