# 🔐 SecurePass Generator

> **Python ile saniyeler içinde güçlü, rastgele ve özelleştirilebilir şifreler üret.**

SecurePass Generator, Python'un `random` ve `string` modüllerini kullanarak belirlediğin uzunlukta rastgele şifreler oluşturan küçük ama kullanışlı bir araçtır.

Karmaşık şifrelerle uğraşmak yerine tek bir fonksiyon çağrısıyla yeni bir şifre üret. 🎲🔑

## ✨ Özellikler

* 🔢 İstediğin uzunlukta şifre oluşturma
* 🔤 Büyük ve küçük harf desteği
* 🔢 Rakamlar
* 🔣 Özel karakterler
* ⚡ Basit ve hızlı kullanım
* 🐍 Harici kütüphane gerektirmez

## 🚀 Kurulum

Python 3 veya üzeri bir sürümün kurulu olması yeterlidir.

Projeyi bilgisayarına aldıktan sonra doğrudan çalıştırabilirsin:

```bash
python password_generator.py
```

## 🧠 Nasıl Çalışıyor?

Şifre üreticisi şu karakter kümelerini bir araya getirir:

```python
string.ascii_letters
string.digits
string.punctuation
```

Daha sonra `random.choice()` ile bu karakterler arasından rastgele seçimler yapılır.

Örneğin:

```text
Yeni şifreniz: fG7@kP2!xR9#
```

Her çalıştırmada farklı bir şifre üretilebilir. 🎰

## 🛠️ Kullanım

Şifre uzunluğunu değiştirmek için:

```python
password_length = 20
print("Yeni şifreniz:", generate_password(password_length))
```

Örneğin `20` girersen 20 karakterlik bir şifre üretilebilir.

## 📂 Proje Yapısı

```text
SecurePass/
│
├── password_generator.py
└── README.md
```

## ⚠️ Güvenlik Notu

Bu proje öğrenme ve temel şifre üretimi amacıyla hazırlanmıştır.

Gerçek dünyada yüksek güvenlik gerektiren uygulamalarda Python'un `random` modülü yerine kriptografik olarak güvenli rastgelelik sağlayan `secrets` modülünün kullanılması daha doğru bir tercihtir.

Örneğin:

```python
import secrets
```

## 🎯 Gelecek Fikirleri

Proje ileride şunları destekleyebilir:

* 📊 Şifre güç göstergesi
* 🎚️ Minimum / maksimum uzunluk
* 🔠 Karakter türlerini ayrı ayrı seçme
* 📋 Şifreyi panoya kopyalama
* 🖥️ Grafik arayüz
* 🌐 Web tabanlı sürüm
* 🔐 `secrets` tabanlı güvenli üretim
* 📜 Şifre geçmişi
* ⚙️ Komut satırı seçenekleri

## 👨‍💻 Teknolojiler

**Python** • `random` • `string`

---

### 🔑 Birkaç satır kod, sonsuz kombinasyon.

**SecurePass Generator** küçük bir Python projesi olabilir. Ama iyi bir şifre üreticisinin görevi basit: tahmin edilmesi zor, oluşturulması kolay. 
