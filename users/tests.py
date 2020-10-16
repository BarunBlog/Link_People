from django.contrib.auth import get_user_model
from django.test import TestCase #an extension of Python’s TestCase



class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='partho',
            email='partho007@gmail.com',
            password='testpass123',
            first_name='Partho',
            last_name='Bhattacharjee',
            country='Bangladesh',
            city_or_district='Sylhet',
            account_role='Student',
        )

        self.assertEqual(user.username, 'partho')
        self.assertEqual(user.email, 'partho007@gmail.com')
        self.assertEqual(user.country, 'Bangladesh')
        self.assertEqual(user.account_role, 'Student')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )

        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)