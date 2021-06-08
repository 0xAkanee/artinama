import requests

print(" [+]  Author    : Rianda Fuad Shafly")
print(" [+]  Info      : Arti Nama Generator")
print(" [+]  Website   : www.riandafuadshafly.my.id")
print(" [+]  Contact   : bangrianda456@gmail.com")
print(" ---------------------------------------------")
arti = input(" [?]  Masukkan Namamu : ")
def main(nama):
      url = "https://jar-api.xyz/api/primbon/artinama?q={}&apikey=aichan".format(arti)
      data = requests.get(url).json()
      makna = data['result']
      print(" Arti Namamu  : " + makna)
      
main(arti)