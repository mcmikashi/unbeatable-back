from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

class RockPaperScissorsComputerPlay(APIView):
    
    def get(self, request, **kwargs):
        """
        Return the computer play
        """
        
        COMPUTER_PLAY_DICTIONARY = {
            'rock':'paper',
            'paper':'scissors',
            'scissors':'rock'
        }
        the_slug = kwargs['slug']
        try:
            the_play = COMPUTER_PLAY_DICTIONARY[the_slug]
        except KeyError:
            raise  Http404()
        return Response({'play':the_play})
