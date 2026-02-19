import string
from password.new_password import generate_password

def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)
    for char in password:
        assert char in valid_characters, f"Geçersiz karakter bulundu: {char}"

def test_password_length():
    """1. Test: Şifrenin belirtilen uzunlukta oluşturulduğunu doğrular"""
    lengths = [8, 16, 32, 64]
    for length in lengths:
        password = generate_password(length)
        assert len(password) == length, f"Beklenen uzunluk {length}, ancak {len(password)} geldi."

def test_passwords_are_unique():
    """2. Test: Arka arkaya üretilen iki şifrenin farklı olduğunu doğrular (Rastgelelik)"""
    pass1 = generate_password(20)
    pass2 = generate_password(20)
    assert pass1 != pass2, "Hata: Üretilen iki şifre birbiriyle aynı!"

def test_password_complexity():
    """Ek Test: Şifrenin sadece tek bir türden (örn. sadece rakam) oluşmadığını, 
    karışık karakterler içerdiğini kabaca kontrol eder."""
    password = generate_password(100)
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    assert has_upper and has_lower and has_digit, "Şifre yeterince karmaşık değil (büyük harf, küçük harf veya rakam eksik)."
