import string
from password.new_password import generate_password

def test_password_characters():
    """Şifre üretilirken yalnızca geçerli karakterlerin kullanıldığını test etme"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenilir test için uzun bir şifre üret
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Şifrenin uzunluğunun belirtilen uzunlukla eşleştiğini test etme"""
    for length in range(1, 21): 
        assert len(generate_password(length)) == length

def test_password_randomness():
    """Arka arkaya oluşturulan iki şifrenin farklı olduğunu test etme"""
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2, "Arka arkaya oluşturulan iki şifre aynı olmamalıdır."

def test_password_complexity():
    """Şifrenin en az bir büyük harf, küçük harf, rakam ve özel karakter içerdiğini test etme"""
    # Karakter çeşitliliğinden emin olmak için makul uzunlukta bir şifre üretiyoruz
    password = generate_password(25)
    
    has_upper = any(char in string.ascii_uppercase for char in password)
    has_lower = any(char in string.ascii_lowercase for char in password)
    has_digits = any(char in string.digits for char in password)
    has_punctuation = any(char in string.punctuation for char in password)
    
    assert has_upper, "Şifre en az bir büyük harf içermelidir."
    assert has_lower, "Şifre en az bir küçük harf içermelidir."
    assert has_digits, "Şifre en az bir rakam içermelidir."
    assert has_punctuation, "Şifre en az bir özel karakter (sembol) içermelidir."

