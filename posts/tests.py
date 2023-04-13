from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username="adam",
            password="pass"
        )

    def test_can_list_post(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_logged_in_user_can_not_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(
            username="adam",
            password="pass"
        )
        brian = User.objects.create_user(
            username="brian",
            password="pass2"
        )
        Post.objects.create(owner=adam, title='adams post')
        Post.objects.create(owner=brian, title='brians post')

    def test_any_user_can_retrieve_valid_post(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'adams post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_any_user_cant_retrieve_invalid_post(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_their_own_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/1/', {'title': 'updated title'})
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title, 'updated title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_others_post(self):
        self.client.login(username='brian', password='pass2')
        response = self.client.put('/posts/1/', {'title': 'updated title'})
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title, 'adams post')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
