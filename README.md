# WebP to PNG Converter


## 📜 Tanım

**WebP to PNG Converter** Python betiği, belirttiğiniz bir klasördeki `.webp` dosyalarını `.png` formatına dönüştürür ve dönüştürülen dosyaları belirttiğiniz hedef klasöre kaydeder. WebP dosyalarını yaygın olarak kullanılan PNG formatına dönüştürmek için ideal bir çözümdür.

## 🚀 Özellikler

- **Toplu Dönüştürme**: Bir klasördeki tüm `.webp` dosyalarını `.png` formatına dönüştürür.
- **Otomatik Klasör Yönetimi**: Hedef klasör mevcut değilse, otomatik olarak oluşturur.
- **Kolay Kullanım**: Sadece kaynak ve hedef klasörü belirtmeniz yeterli.

## 🛠️ Gereksinimler

- Python 3.x
- Pillow kütüphanesi

### Pillow Kurulumu

```sh
pip install pillow
```

## 💻 Kurulum ve Kullanım

1. **Projeyi Klonlayın**

    ```sh
    git clone https://github.com/kullaniciadi/webp-to-png-converter.git
    cd webp-to-png-converter
    ```

2. **Gerekli Kütüphaneleri Yükleyin**

    ```sh
    pip install pillow
    ```

3. **Klasörleri Hazırlayın**

    - `webpklasoru` adında bir klasör oluşturun ve `.webp` dosyalarınızı bu klasöre koyun.
    - `pngklasoru` adında bir klasör oluşturun veya betiğin otomatik olarak oluşturmasına izin verin.

4. **Betiği Çalıştırın**

    ```sh
    python convert_webp_to_png.py
    ```

5. **Sonuçları Kontrol Edin**

    - `webpklasoru` içindeki `.webp` dosyaları, `pngklasoru` içinde `.png` formatına dönüştürülmüş olarak bulunacaktır.

## 📂 Örnek

### Öncesi
- `webpklasoru`
  - `image1.webp`
  - `image2.webp`

### Sonrası
- `pngklasoru`
  - `image1.png`
  - `image2.png`
- GitHub: [kullaniciadi](https://github.com/kullaniciadi)

---

Bu README dosyası, projenizin GitHub sayfasında profesyonel ve çekici bir görünüm sunacak. README dosyasını `README.md` adıyla projenizin kök dizinine koyabilirsiniz.
