from django.test import TestCase
from wedding.models import Gallery, PictureEntry
# Create your tests here.

class TestGalleryModel(TestCase):

    def setUp(self):
        gallery_name = 'Vacation'
        Gallery.objects.create(gallery_name = gallery_name)

    def test_gallery_creation(self):
        self.assertEqual(Gallery.objects.all()[0].gallery_name, 'Vacation', 'The gallery name should be Vacation' \
                         + ' but it is ' + Gallery.objects.all()[0].gallery_name)

    def test_adding_pictures(self):
        pics =['hagiasofia.jpg', 'basilicacistern.jpg', 'mynewrug.jpg']
        caps = ['The Hagia Sofia (Aya Sofya)', 'Sewers, eww', 'Good deal...not']
        x = zip(pics, caps)
        g = Gallery.objects.all()[0]
        for p in x:
            PictureEntry.objects.create(gallery = g, pic_name = p[0], caption = p[1])

        self.assertEqual(len(PictureEntry.objects.all()), 3, 'The length of picture entries should be 3')
