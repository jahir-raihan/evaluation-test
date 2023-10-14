from django.db import models

# Book categories
category = (
    ('বিজ্ঞান', 'বিজ্ঞান'), ('সাহিত্য', 'সাহিত্য'), ('রোমান্টিক', 'রোমান্টিক'), ('সময়কালীন', 'সময়কালীন'),
    ("ক্রাইম থ্রিলার", "ক্রাইম থ্রিলার"), ("সত্য ঘটনা", "সত্য ঘটনা"), ("সাইন্স ফিকশন", "সাইন্স ফিকশন")
)


class Book(models.Model):

    """Book model to store book datas into database"""

    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    language = models.CharField(max_length=20, default='বাংলা')
    price = models.IntegerField(default=0)
    price_bangla = models.CharField(max_length=4)
    category = models.CharField(max_length=100, choices=category)
    cover_photo = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}, a book of {self.author}'

