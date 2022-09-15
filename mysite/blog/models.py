from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Method untuk custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

# Create your models here.
class Post(models.Model):

    # subclass dg type enum/members untuk mendefiniskan opsi yang tersedia. 
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft' # CHOICE = 'value','label'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    # ManyToMany: Sebuah Post ditulis oleh seorang User <-> Setiap User bisa menulis banyak Post
    author = models.ForeignKey(User,   # User = PK, author=FK
                                on_delete=models.CASCADE, # Ketika User dihapus, maka akan menghapus seluruh postnya (related_name)
                                related_name='blog_posts')  
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) # Date saat ini
    created = models.DateTimeField(auto_now_add=True) # Date akan tersimpan otomatis saat Object('created') DIBUAT 
    updated = models.DateTimeField(auto_now=True) # Date akan tersimpan/terupdate otomatis saat Object disimpan
    status = models.CharField(max_length=2,
                                choices=Status.choices,
                                default=Status.DRAFT)

    objects = models.Manager() # The default manager. --> memanggil semua object
    published = PublishedManager() # Our custom manager. --> memanggil object yang status=publish saja
    
    # Mendefinisikan metadata untuk model. 
    class Meta:
        ordering = ['-publish'] # Berfungsi untuk mengurutkan scr descending (-)
        indexes = [             
            models.Index(fields=['publish']), # Mendefinisikan database index dari sebuah model
        ]
    # method mengembalikan object dengan return string. memungkinkan menampilkan object sebagai string di semua tempat, misal admin panel
    def __str__(self):
        return self.title

    