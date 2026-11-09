# Rastgele Şifre Üretici

Python ile geliştirilmiş basit bir rastgele şifre üreticisi. Uygulama, istenen uzunlukta; büyük ve küçük harf, rakam ve özel karakterlerden oluşan bir şifre üretir.

## Özellikler

- Varsayılan olarak 12 karakter uzunluğunda şifre üretir.
- İstenen uzunlukta şifre oluşturmayı destekler.
- Büyük/küçük harfleri, rakamları ve `string.punctuation` içindeki özel karakterleri kullanır.
- Şifre üretme işlevi `password.new_password.generate_password` adıyla tekrar kullanılabilir.
- Proje, `pytest` ile çalışan otomatik testler içerir.

> **Güvenlik notu:** Bu proje eğitim amaçlıdır. Üretim ortamında veya kritik hesaplarda kullanılacak şifreler için `secrets` modülü gibi kriptografik olarak güvenli araçlar tercih edilmelidir.

## Gereksinimler

- Python 3.6 veya üzeri
- Testleri çalıştırmak için `pytest`

Uygulamayı kullanmak için ek bir Python paketi gerekmez. Test bağımlılığını yüklemek için:

```bash
python -m pip install pytest
```

Windows'ta Python komutu `py` olarak tanımlıysa aynı işlemi şu şekilde de yapabilirsiniz:

```bash
py -m pip install pytest
```

## Proje yapısı

```text
Python-sifre-uretici-main/
├── password/
│   ├── __init__.py
│   └── new_password.py       # Şifre üretme işlevi
├── tests/
│   ├── __init__.py
│   └── test_new_password.py  # Otomatik testler
├── pytest.ini                # pytest ayarları
└── README.md
```

## Kullanım

Proje kök dizinindeyken uygulamayı çalıştırın:

```bash
python password/new_password.py
```

Windows'ta gerekirse:

```bash
py password/new_password.py
```

Komut, 12 karakterlik yeni bir şifre üretir ve ekrana yazdırır.

### Python kodundan kullanma

Belirli bir uzunlukta şifre üretmek için işlevi içe aktarabilirsiniz:

```python
from password.new_password import generate_password

password = generate_password(20)
print(password)
```

`generate_password()` uzunluk belirtilmezse 12 karakter üretir:

```python
from password.new_password import generate_password

password = generate_password()
```

## Testleri çalıştırma

Proje kök dizininde aşağıdaki komutu çalıştırın:

```bash
python -m pytest
```

Windows'ta alternatif olarak:

```bash
py -m pytest
```

Testler şunları kontrol eder:

- Üretilen şifrenin yalnızca izin verilen karakterleri içermesi
- Şifre uzunluğunun istenen değerle eşleşmesi
- Arka arkaya üretilen iki şifrenin farklı olması

## Sınırlamalar

- Komut satırı arayüzü kullanıcıdan uzunluk istemez; dosyadaki `password_length` değeri kullanılır.
- Uzunluk için ayrı bir doğrulama veya hata mesajı bulunmaz.
- `password.new_password` içe aktarıldığında dosyanın altındaki örnek kullanım da çalışır ve ekrana bir şifre yazdırır.
- Kullanılan `random` modülü güvenlik açısından kritik şifreler için uygun değildir.

## Lisans

Bu proje eğitim amaçlı hazırlanmıştır. Özel bir lisans belirtilmediği için kullanım ve dağıtım koşulları proje sahibinin tercihine bağlıdır.
