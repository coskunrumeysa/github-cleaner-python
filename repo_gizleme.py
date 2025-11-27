# Pythonda Github ile konusabilmek icin , PyGithub kütüphanesinden Github aracını getir.
from github import Github
#Birden fazla repomuz olduğu icin sürekli istek atacak buda Github bizi robot sanmasın diye kullaniyoruz.
import time

#Github üzerinden aldığımız Token 'ın degiskene atanması
GITHUB_TOKEN = "gTOKEN_BURAYA_GELECEK" 

#Ana Fonksiyonumuz
def repolari_gizle():
    print("GitHub'a bağlanılıyor...")

#Program çökmesin diye onlem aliyoruz.
    try:
        # Github'a giris ve g isimli bir nesne olusturma
        g = Github(GITHUB_TOKEN)
        #Token sahibi user'in alinmasi 
        user = g.get_user()
        print(f"Giriş Başarılı: {user.login}")
        print("Public (Herkese Açık) repolar taranıyor...\n")

        # Sadece kendi sahip oldugumuz repolarımızı alıyoruz , bunu yapmazsak uyesi oldugumuz repolarida private edebilir
        repolar = user.get_repos(affiliation="owner")
        
        sayac = 0

        for repo in repolar:
            # Eger repo gizliyse , sıradaki repoya gecer zaman kaybetmez
            if repo.private:
                continue

            # Eğer repo public ise işlem yap
            print(f"İşleniyor: {repo.name}")
            try:
                repo.edit(private=True) #repo'yu private çekiyoruz. 
                print(f"--> [BAŞARILI] {repo.name} gizlendi.")
                sayac += 1
                time.sleep(1) # GitHub' ın bizim saldırı yaptığımızı sanmasın diye 1sn bekle
            except Exception as hata: # Hata alırsak hatayı yakalayacağımız yer
                print(f"--> [HATA] {repo.name} gizlenemedi: {hata}")

        print(f"\n--- İŞLEM TAMAMLANDI ---")
        print(f"Toplam {sayac} adet repo gizlendi.")

    except Exception as e:
        print(f"HATA: Token hatalı olabilir. Detay: {e}")

if __name__ == "__main__":
    repolari_gizle()