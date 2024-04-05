
'''
# Do not repeat yourself (DRY)

#Kendinizi tekrar etmeyin" (DRY), bir yazılım sistemi içindeki kod tekrarını azaltmayı amaçlayan 
#bir yazılım geliştirme ilkesidir. İlke, bir sistem içindeki her bilgi veya mantık parçasının 
#tek ve net bir temsile sahip olması gerektiğini belirtir. 
#Başka bir deyişle çoğaltma mümkün olduğunca kodlardan kaçınılmalıdır.


def dikdörtgen_alan_ve_cevre_hesapla(uzunluk, genislik):
    alan = uzunluk * genislik
    cevre = 2 * (uzunluk + genislik)
    print(f"dikdörtgen alanı : {alan}  dikdörtgen çevresi : {cevre}" )

uzunluk_degeri = int(input("bir uzunluk değeri giriniz : "))
genislik_degeri = int(input("bir genislik degeri giriniz : "))

dikdörtgen_alan_ve_cevre_hesapla(uzunluk_degeri, genislik_degeri)

# düzenlenen bu kodda, girdi olarak bir dikdörtgenin uzunluğunu ve genişliğini alan 
# ve hesaplanan alanı ve çevreyi döndüren bir dikdörtgen_alan_ve_cevre_hesapla fonksiyonunu tanımlıyoruz. 
# Bunu yaparak, DRY ilkesine bağlı kalarak alan ve çevre hesaplamasında kod tekrarını ortadan kaldırıyoruz.
'''









'''
# Write everything twice (WET)

# "Her Şeyi İki Kez Yaz" (WET) ifadesi, yazılım geliştirmede "Kendini Tekrarlama" (DRY) ilkesiyle 
# çelişmek için sıklıkla kullanılır. DRY, kodun yeniden kullanımının ve fazlalıktan 
# kaçınmanın önemini vurgularken, WET tam tersini, yani kodun kasıtlı olarak çoğaltılmasını önerir.


# 1. dikdörtgenin alanını ve çevresini hesaplama

uzunluk1 = int(input("bir uzunluk değeri giriniz : "))
genislik1 = int(input("bir genişlik değeri giriniz : "))

alan1 = uzunluk1 * genislik1
cevre1 = 2 * (uzunluk1 + genislik1)

print(f"dikdörtgen1 alanı : {alan1}  dikdörtgen1 cevresi : {cevre1}")


# 2. dikdörtgenin alanını ve çevresini hesaplama

uzunluk2 = int(input("bir uzunluk değeri giriniz : "))
genislik2 = int(input("bir genişlik değeri giriniz : "))

alan2 = uzunluk2 * genislik2
cevre2 = 2 * (uzunluk2 + genislik2)

print(f"dikdörtgen2 alanı : {alan2}  dikdörtgen2 cevresi : {cevre2}")


# 3. dikdörtgenin alanını ve çevresini hesaplama

uzunluk3 = int(input("bir uzunluk değeri giriniz : "))
genislik3 = int(input("bir genişlik değeri giriniz : "))

alan3 = uzunluk3 * genislik3
cevre3 = 2 * (uzunluk3 + genislik3)

print(f"dikdörtgen3 alanı : {alan3}  dikdörtgen3 cevresi : {cevre3}")

# Bu örnekte, her dikdörtgenin alanını ve çevresini hesaplamak için kullanılan kodu kasıtlı olarak tekrarladık. 
# Bu, DRY ilkesini ihlal eder ancak artıklığı benimseyerek ve aynı kodu birden çok kez tekrarlayarak WET ilkesini gösterir.

# WET ilkesi bu bağlamda mantığa aykırı görünse de, açıklık, performans optimizasyonu veya başka nedenlerle 
# artıklığın kasıtlı olarak getirildiği durumlar olabilir. Ancak çoğu durumda DRY prensibine bağlı kalmak 
# daha sürdürülebilir ve verimli kodlara yol açar.
'''









'''
# Single Responsibility Principle (SRP)

# Tek Sorumluluk İlkesi (SRP), bir sınıfın değişmek için tek bir nedeni olması gerektiğini, 
# yani yazılım sistemi içinde yalnızca tek bir sorumluluğa veya işe sahip olması 
# gerektiğini belirtir. Bu ilke anlaşılması, bakımı ve genişletilmesi daha kolay olan kodu destekler.

class İsci:
    
    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas

class VergiHesapla:
    
    @staticmethod
    def vergi_hesaplama(maas):
        return maas * 0.2

class MaasBordrosuOlustur:
    
    @staticmethod
    def maas_bordrosu_olusturma(isci):
        vergi = VergiHesapla.vergi_hesaplama(25000)
        return f"işçi {isci.isim} için maaş bordrosu: Maas = {isci.maas}, Vergi = {vergi}"

class VeriTabani:
    
    @staticmethod
    def isci_kaydet(isci):
        pass

calisan = İsci("selim", 25000)
print(f"çalışanın adı = {calisan.isim}")
print(f"çalışanın maaşı = {calisan.maas}")

ver = VergiHesapla()
print(f"çalışanın vergisi = {ver.vergi_hesaplama(25000)}")

bordro = MaasBordrosuOlustur()
print(bordro.maas_bordrosu_olusturma(calisan))


# İşçi sınıfı yalnızca çalışan bilgilerinin saklanmasından sorumludur.
# Vergi Hesapla sınıfı verginin hesaplanmasından sorumludur.
# Maaş Bordrosu Oluştur sınıfı maaş bordrolarının oluşturulmasından sorumludur.
# Veritabanı sınıfı, çalışan bilgilerinin veritabanında kalıcı olmasından sorumludur.
# Artık Tek Sorumluluk İlkesine bağlı kalarak her sınıfın tek bir sorumluluğu vardır. 
# Bu, kodun anlaşılmasını, test edilmesini ve bakımını kolaylaştırır. 
# Ayrıca sistemin bir yönünün değişmesi gerekiyorsa bunun kod tabanının diğer bölümlerini etkileme 
# olasılığı daha azdır.
'''








'''
# Separation of Concerns (SOC)

# Endişelerin Ayrılması (SOC), yazılım mühendisliğinde, bir bilgisayar programının her biri ayrı bir 
# endişe veya sorumluluğu ele alan farklı bölümlere ayrılmasını savunan temel bir prensiptir. 
# SOC'nin amacı, sistemin bir kısmında yapılan değişikliklerin diğer kısımları olumsuz etkilememesi için 
# yazılımın farklı yönlerini veya işlevlerini izole etmektir.

# SOC'nin arkasındaki temel fikir, yazılım tasarımında modülerliği, sürdürülebilirliği ve ölçeklenebilirliği
# teşvik etmektir. Geliştiriciler endişeleri ayırarak karmaşıklığı daha etkili bir şekilde yönetebilir, 
# kodun okunabilirliğini geliştirebilir ve daha kolay test ve hata ayıklamayı kolaylaştırabilir.


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_to_database(self):
        pass


class UserView:
    def render(self, user):
        pass


class UserController:
    def __init__(self, user_view):
        self.user_view = user_view

    def register_user(self, username, email):
        new_user = User(username, email)
        new_user.save_to_database()
        self.user_view.render(new_user)


user_view = UserView()
user_controller = UserController(user_view)

user_controller.register_user("monster", "bernard@gmail.com")

'''








'''
# KISS (Keep It Simple Stupid)

# "Basit Tut, Aptal" (KISS) ilkesi, yazılım geliştirme ve diğer alanlarda tasarım ve uygulamada basitliği savunan 
# temel bir tasarım ilkesidir. Bu ilke, çoğu sistemin gereksiz derecede karmaşık hale getirilmek yerine basit tutulması 
# durumunda en iyi şekilde çalışacağını öne sürmektedir. KISS, geliştiricileri yazılım geliştirmenin her alanında 
# basitliğe, açıklığa ve anlaşılırlığa öncelik vermeye teşvik eder.

# KISS ilkesinin ardındaki temel fikir, karmaşıklığı en aza indirmek ve aşırı mühendislikten kaçınmaktır. 
# Geliştiriciler işleri basit tutarak hata riskini azaltabilir, okunabilirliği artırabilir ve başkalarının kodu anlamasını 
# ve üzerinde çalışmasını kolaylaştırabilir.



#KISS'in ihlali:

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(19))

# Bu örnekte işlev, herhangi birinin sayıyı bölüp bölmediğini kontrol etmek için 2'den sayı - 1'e kadar tüm sayıları yineler. 
# Bu yaklaşım işe yarasa da en basit ve en etkili çözüm değildir.

# KISS'e bağlılık:

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(37))

# Bu geliştirilmiş versiyonda, bölenleri kontrol etmek için yalnızca sayının kareköküne kadar yinelememiz gerekiyor. 
# Bu daha verimli bir yaklaşımdır ve uygulamayı daha basit ve anlaşılır hale getirir.

# Açıklama:
# İşlevin ilk sürümü çalışır ancak - 1'e kadar tüm sayıları yineleyerek gereksiz karmaşıklık içerir. 
# Geliştirilmiş sürüm, algoritmayı yalnızca sayının kareköküne kadar yineleyecek şekilde basitleştirerek 
# KISS ilkesine uyar ve böylece işlev sayısını azaltır. 
# Yinelemelerin gerekli olması ve kodun daha basit ve verimli hale getirilmesi.

# Bu örnek, KISS ilkesinin uygulanmasının nasıl daha basit, daha verimli ve anlaşılması daha kolay çözümlere 
# yol açtığını göstermektedir.
'''

























