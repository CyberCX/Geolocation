from phonenumbers import geocoder, carrier, timezone
import  phonenumbers, time

print("NOTE : MASUKAN ANGKA/KODE TELEPON NEGARA, CONTOH (+62)")

def Exect():
  full_numb = raw_input("Masukan Nomor : ")
  time.sleep(2.5)

  code_country = phonenumbers.parse(full_numb, "None")
  ch_number = phonenumbers.parse(full_numb, "CH")
  provider_numb = phonenumbers.parse(full_numb, "RO")
  gb_numb = phonenumbers.parse(full_numb, "GB")

  country = geocoder.description_for_valid_number(ch_number, "en")
  provider = carrier.name_for_valid_number(provider_numb, "en")
  time_zone = timezone.time_zones_for_geographical_number(gb_numb)

  print "Kode Negara : ",code_country
  time.sleep(1)
  print "Negara : ",country
  time.sleep(1)
  print "Provider : ",provider
  time.sleep(1)
  print "Zona Waktu : ",time_zone

Exect()