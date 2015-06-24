import endpoints
from api.controllers.helloworld_api import HelloWorldApi
from api.controllers.tictactoe_api import TicTacToeApi

application = endpoints.api_server([HelloWorldApi, TicTacToeApi])