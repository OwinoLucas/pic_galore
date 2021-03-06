from django.db import models



# Create your models here.
class Category(models.Model):
    """
    class containing category objects
    """
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.category_name

    def save_category(self):
        """
        save category method
        """
        self.save()

    def update_category(self, using=None, fields=None, **kwargs):
        """
        update category method
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_category(self):
        """
        delete category method
        """
        self.delete()

class location(models.Model):

    """
    class containing location objects
    """
    location_name = models.CharField(max_length=40)

    def __str__(self):
        return self.location_name

    def save_location(self):
        """
        save location method
        """
        self.save()

    def update_location(self, using=None, fields=None, **kwargs):
        """
        update location method
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_location(self):
        """
        delete location method
        """
        self.delete()

    @classmethod
    def get_locations(cls):
        locations = location.objects.all()
        return locations

    

class Image(models.Model):
    """
    class containing image objects
    """
    image = models.ImageField(upload_to = 'images/',default='DEFAULT VALUE')
    image_name = models.CharField(max_length =60)
    image_description = models.TextField()
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    location = models.ForeignKey(location,null=True,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.image_name

    def save_image(self):
        """
        save image method
        """
        self.save()

    def update_image(self, using=None, fields=None, **kwargs):
        """
        update image method
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_image(self):
        """
        delete image method
        """
        self.delete()

    @classmethod
    def display_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_image_by_category(cls,category_search):
        images = cls.objects.filter(category__category_name__icontains=category_search)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        locate_image = Image.objects.filter(location__location_name=location).all()
        return locate_image
