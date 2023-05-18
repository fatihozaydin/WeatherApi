import requests

def hava_durumu_al(sehir):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid=YOUR_API_KEY"

    try:
        response = requests.get(url)
        veri = response.json()

        if veri["cod"] != "404":
            hava_durumu = veri["weather"][0]["description"]
            sicaklik = veri["main"]["temp"]
            nem_orani = veri["main"]["humidity"]

            print(f"{sehir} hava durumu: {hava_durumu}")
            print(f"Sıcaklık: {sicaklik} Kelvin")
            print(f"Nem Oranı: {nem_orani}%")
        else:
            print("Belirtilen şehir bulunamadı.")
    except requests.ConnectionError:
        print("İnternet bağlantısı hatası.")

sehir = input("Hava durumunu öğrenmek istediğiniz şehri girin: ")
hava_durumu_al(sehir)


'''
Yukarıdaki kod parçasında, YOUR_API_KEY yazan yere kendi OpenWeatherMap API anahtarınızı 
eklemelisiniz. Bu anahtarı, OpenWeatherMap'e kaydolarak ücretsiz olarak alabilirsiniz. 
API anahtarınızı aldıktan sonra, kodun url değişkenindeki YOUR_API_KEY kısmını API anahtarınızla 
değiştirin.

Kod, kullanıcıdan bir şehir girmesini isteyecek ve girdiği şehrin hava durumu verilerini 
OpenWeatherMap API'sini kullanarak alacak. Alınan verileri kullanarak hava durumunu, 
sıcaklığı ve nem oranını ekrana yazdıracaktır.

Not: Bu kod OpenWeatherMap API'sini kullanmaktadır. Bu nedenle, API'nin kullanım koşullarına 
uymanız gerekmektedir. Ayrıca, internet bağlantınızın aktif olması gerekmektedir.
'''