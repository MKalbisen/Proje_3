# 🎬 Film Analiz Projesi

Bu proje, [**movies_initial.csv**](https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis) film veri seti üzerinde detaylı analizler yaparak IMDb puanları, türler, diller, yönetmenler, oyuncular ve film öneri sistemi gibi çeşitli konularda bilgi çıkarımı sağlar.

---

## İçerik ve Dosya Yapısı

* `proje_3.py ve proje_3.ipynb` — Analiz kodları 
* `movies_inital.csv` — Film bilgileri 
* `README.md` — Projeyi, kullanım talimatlarını ve analiz adımlarını açıklar.


## Proje İçeriği

### **1. Veri Yükleme**

* CSV dosyası pandas ile okunur.
* Filmlere ait tüm bilgiler DataFrame'e aktarılır.

---

### **2. IMDb Puanı En Yüksek Filmler**

* IMDb puanına göre sıralama yapılır.
* En yüksek puanlı 10 film seçilir.
* Film adı, yönetmen, dil, ödüller, ülke, yıl ve süre bilgileri gösterilir.

---

### **3. En Popüler Dil, Ülke ve Türler**

* En çok geçen ilk 7 dil hesaplanır.
* En çok film üretilen ilk 7 ülke listelenir.
* En popüler 7 tür (tema) bulunur.

---

### **4. En Yüksek Ortalama IMDb Puanına Sahip Yönetmenler**

* En az 5 filmi olan yönetmenler filtrelenir.
* Bu yönetmenlerin ortalama IMDb puanları hesaplanır.
* En yüksek ortalamaya sahip 10 yönetmen listelenir.

---

### **5. IMDb Ortalaması En Yüksek Diller**

* En az 200 filme sahip diller seçilir.
* Ortalama IMDb puanı en yüksek 10 dil listelenir.

---

### **6. Türlere Göre Ortalama IMDb Analizi**

* Türler "genre" sütunundan ayrıştırılır.
* Her türün ortalama IMDb puanı ve toplam film sayısı hesaplanır.
* En az 50 filmi olan türler arasından en yüksek ortalamaya sahip 10 tür seçilir.

---

### **7. En Uzun Filmler**

* "runtime" sütunundaki dakika değerleri sayısal hale getirilir.
* En uzun 10 film listelenir.

---

### **8. Film Süresi ile IMDb Puanı İlişkisi**

* Süresi 30–200 dakika olan filmler filtrelenir.
* Scatter plot (serpilme grafiği) çizilerek ilişki incelenir.

---

### **9. En Çok Oy Alan Filmler**

* IMDb oy sayısına göre en çok oy almış 10 film listelenir.

---

### **10. IMDb Puanlarının Yıllara Göre Değişimi**

* Filmleri yıl bazında gruplayarak IMDb ortalaması hesaplanır.
* Zaman grafiği çizilir.

---

### **11. Oyuncuların Ortalama IMDb Puanları**

* Oyuncu listeleri ayrıştırılır.
* En az 10 filmde yer alan oyuncuların IMDb ortalaması hesaplanır.
* En yüksek 10 oyuncu listelenir.

---

### **12. Basit Film Öneri Sistemi**

* Tür, yönetmen, oyuncu ve açıklama birleşimi ile "features" isimli bir metin alanı oluşturulur.
* TF-IDF yöntemi ile metinler vektörleştirilir.
* Cosine similarity ile filmler arası benzerlik hesaplanır.
* `get_recommendations(title, n)` fonksiyonu ile seçilen filme benzeyen filmler listelenir.

**Örnek kullanım:**

```
get_recommendations("The Hacker Wars", 20)
```

---

## Kullanılan Kütüphaneler

* **pandas** – veri işleme
* **numpy** – sayısal işlemler
* **matplotlib & seaborn** – veri görselleştirme
* **sklearn** – TF-IDF ve cosine similarity işlemleri

---

## Çıktılar

Bu proje aşağıdaki çıktıları üretir:

* IMDb puanına göre sıralamalar
* En popüler ülkeler, türler ve diller
* Yönetmen ve oyuncu başarı analizleri
* Tür bazlı IMDb istatistikleri
* Film süresi–IMDb ilişkisi grafiği
* İçerik tabanlı film öneri sistemi

