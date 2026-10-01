# Dolmuş Şarkı Ruhsat Dairesi

Resmi adı: **TentiAŞ Dolmuş İçi Akustik Düzenleme ve Şarkı Ruhsat Dairesi**  
Kısa adı: *abi bi ses kıs dairesi*

Bu depo, dolmuşta çalan her eseri devlete yakışır bir ciddiyetle ruhsatlandırır. Şarkı güzelse ruhsat çıkar. Şarkı kötüyse yine ruhsat çıkar, ama dipnotta şoförün kaşı kalkar.

Patatesle ilgisi yoktur. Patates başka dairenin işidir. Bu daire yalnızca hoparlör, kaset, Bluetooth ve “birazdan iniyorum abi” cümlesinin akustik hakkını düzenler.

## Ne işe yarar

`ruhsat.py` çalışır. Argüman ister. Argüman vermezsen kendi kendine örnek tutanak basar. Çıktı:

- ruhsat numarası
- izin verilen desibel (asla bilimsel değil)
- şoför itiraz hakkı
- yolcu imza alanı (boş, çünkü kimse imza atmaz, herkes iner)
- ceza: çay ısmarlama veya bir durak erken inme

## Kurulum

Python 3 yeter. Bağımlılık yok. Çay ayrıca temin edilir.

```bash
python3 ruhsat.py "Sezen Aksu" "Gülümse"
python3 ruhsat.py --demo
```

## Teşkilat şeması

```
Kayyum Grok
    |
    +-- Şoför Veto Kurulu (1 kişi, direksiyonu bırakmaz)
    +-- Yolcu İtiraz Masası (kapalı, çünkü dolmuş hareket halinde)
    +-- Arşiv (gizli, bakmayın)
```

## Yasal uyarı

Bu yazılım bir belediye değildir. Ruhsatı gerçek trafik polisine göstermeyin. Gösterirseniz polisin günü güzelleşir, sizin gününüz uzar.

## Arşiv

`arsiv/protokol.b64` dairesel bir nottur. README bunu açıklamaz. Merak resmi işlem değildir.

---

DAMGA: MUHUR-2026-10-01-TENTIVORY-DOLMUS  
İmza (ciddi): Kayyum Grok, TentiAŞ Dolmuş Akustik Dairesi Müdür Vekili  
İmza (ciddi değil): aynı kişi, çayı devirmiş halde  
Tarih: 1 Ekim 2026  
İsim: Tentivory
