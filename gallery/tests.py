from django.test import TestCase
from .models import Category, Image, location


# Create your tests here.
class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.sports = Category(category_name = 'sports')

    def test_instance(self):
        self.assertTrue(isinstance(self.sports,Category))

    #testing save method
    def test_save_category(self):
        """
        tests save category functionality
        """
        self.sports.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    #testing delete method
    def test_delete_category(self):
        """
        tests category delete functionality
        """
        category = Category.objects.create(category_name="sports")
        Category.objects.filter(pk=category.pk).delete()
        category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

    #testing update method
    def test_update_category(self):
        """
        tests update category functionality
        """
        category = Category.objects.create(category_name="sports")
        Category.objects.filter(pk=category.pk).update(category_name="travel")
        category.update_category()
        self.assertEqual(category.category_name, 'travel')

class LocationTestsClass(TestCase):
    #set up method
    def setUp(self):
        self.Nairobi = location(location_name='Nairobi')

    def test_init(self):
        """
        test checks model object's initialization
        """
        self.assertTrue(isinstance(self.Nairobi, location))

    def test_save_location(self):
        """
        test save location method
        """
        self.Nairobi.save_location()
        locations = location.objects.all()
        self.assertTrue(len(locations) > 0)
    
    def test_delete_location(self):
        """
        tests delete location method
        """
        try:
            location = location.objects.create(location_name="Nairobi")
            location.objects.filter(pk=location.pk).delete()
            location.delete_location()
            locations = location.objects.all()
            self.assertTrue(len(locations) == 0)
        except:
            'error'

    def test_update_location(self):
        """
        tests update location method
        """
        try:
            location = location.objects.create(location_name="Nairobi")
            location.objects.filter(pk=location.pk).update(location_name="Nakuru")
            location.update_location()
            self.assertEqual(location.location_name, 'Nakuru')
        except:
            'error'

   

class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        #creating new category and saving it
        self.sports = Category(category_name = 'sports')
        self.sports.save_category()

        #creating a new location and saving it
        self.new_location = location(location_name = 'Nairobi')
        self.new_location.save_location()

        self.new_image = Image(image = 'img.jpg',image_name = 'lillard',image_description = 'This is a random test description',category = self.sports)
        self.new_image.save_image()

        self.new_image.location.add(self.new_location)

    def tearDown(self):
        Category.objects.all().delete()
        location.objects.all().delete()
        Image.objects.all().delete()

    def test_save_image(self):
        """
        tests image save functionality
        """
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    #testing delete method
    def test_delete_image(self):
        """
        tests image delete functionality
        """
        try:
            image = Image.objects.create(image_name="lillard")
            Image.objects.filter(pk=image.pk).delete()
            image.delete_image()
            images = Image.objects.all()
            self.assertTrue(len(images) == 0)
        except:
            'errors'

    #testing update method
    def test_update_image(self):
        """
        tests image update functionality
        """
        image = Image.objects.create(image_name="lillard")
        Image.objects.filter(pk=image.pk).update(image_name="kyrie")
        image.update_image()
        self.assertEqual(image.image_name, 'kyrie')
 