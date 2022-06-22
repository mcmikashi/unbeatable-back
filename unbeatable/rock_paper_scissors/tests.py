from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from django.urls import reverse

class TestRockPaperScissors(TestCase, APIClient):
    
    def test_rock_paper_scissors_good_slug(self):
        PLAY_DICTIONARY = {
            'rock':'paper',
            'paper':'scissors',
            'scissors':'rock'
        }
        for key,value in PLAY_DICTIONARY.items() :
            url = reverse("rock_paper_scissors:computer-play",args=[key])
            res = self.client.get(url)
            self.assertEqual(res.status_code,status.HTTP_200_OK)
            self.assertEqual(res.data,{'play':value})
    
    def test_rock_paper_scissors_bad_slug(self):
        url = reverse("rock_paper_scissors:computer-play",args=["bad_slug"])
        res = self.client.get(url)
        self.assertEqual(res.status_code,status.HTTP_404_NOT_FOUND)
