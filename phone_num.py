import phonenumbers
from phonenumbers import timezone,geocoder,carrier

num = input("Enter The Number +91__: ")

phone = phonenumbers.parse(num)
time = timezone.time_zones_for_number(phone)
carr = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(reg)
print(carr)