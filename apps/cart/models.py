
#! Django function and methods
from django.db import models
from django.utils.translation import gettext_lazy as _


#! Third Party Packages
from django_extensions.db.models import TimeStampedModel


#!Models,forms and serializer classes


# Create your models here.


#*Cart
# class Cart(TimeStampedModel):
#     cart_id = models.CharField(_('Cart Id'),max_length=250,blank=True)

#     def __str__(self):
#         return f"{self.cart_id}"
        
#     class Meta:
#         ordering = ['-created']
#         verbose_name = 'Cart'
#         verbose_name_plural = 'Carts'



#*CartItem
# class CartItem(TimeStampedModel):
#     user = models.ForeignKey(Account, verbose_name=(_('Account')),on_delete=models.CASCADE,null=True)
#     book = models.ForeignKey("book.Book",verbose_name=_('Book'),related_name='product_cart_item',on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart,verbose_name=_('Cart'),related_name="cart_item",on_delete=models.CASCADE,null=True)
#     quantity = models.IntegerField(_('Quantity'),default=0)
#     is_active = models.BooleanField(default=True)
    
    
#     def __str__(self):
#         return f"{self.book.title} --- {self.cart}"
    
    
#     def sub_total(self):
#         return self.book.price*self.quantity
    
    
#     class Meta:
#         ordering=['-created']
#         verbose_name = 'CartItem'
#         verbose_name_plural = 'CartItems'



