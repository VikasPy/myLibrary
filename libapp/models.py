from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class contact(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=50)
    subject=models.CharField( max_length=50)
    misg=models.TextField(max_length=1000)
     
    
    
    def __str__(self):
        return self.name


class Category(models.Model):
    book_category=models.CharField(max_length=50)
    
    def __str__(self):
        return self.book_category
    
    
class book_table(models.Model):
    book_type=models.ForeignKey(Category, on_delete=models.CASCADE)
    book_name=models.CharField( max_length=550)
    book_image=CloudinaryField('book_pic')
    Author=models.CharField( max_length=150)
    Publish_date=models.DateField()
    book_content=RichTextField()
    
    def __str__(self):
      return self.book_name
    

class courses_data(models.Model):
    field_image=CloudinaryField('field_image')
    field_Type=models.CharField(max_length=50)
    price=models.CharField(max_length=30)
    field_name=models.CharField(max_length=50)
    about_field=models.TextField(max_length=5000)

    
    
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=266)
    Last_name = models.CharField(max_length=266)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=60)
    user_image = CloudinaryField('profile_pic')
    is_active=models.BooleanField(default=True)



    def __str__(self):
      return self.first_name    
  
  
class comment_user(models.Model):
      user=models.ForeignKey(profile, on_delete=models.CASCADE)
      post_id=models.ForeignKey(book_table,on_delete=models.CASCADE)
      com=models.TextField(max_length=2000)
      c_data=models.DateTimeField(auto_now_add=True)
      
class Like(models.Model):
      user=models.ForeignKey(profile, on_delete=models.CASCADE)
      post_id=models.ForeignKey(book_table,on_delete=models.CASCADE)
      like=models.BooleanField(default=False)
      
class fpd(models.Model):
    f=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.f  
      
      
class pb(models.Model):
    fd=models.ForeignKey(fpd, on_delete=models.CASCADE)
    pd=RichTextField()
    def __str__(self):
        return self.pd
    
    

  
    