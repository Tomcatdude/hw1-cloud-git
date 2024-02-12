import rest_api_server

def typical_case(request):
    return rest_api_server.calculate_dice(request, seed = 10)

def test_normal_case():
    assert typical_case('5d20:6d7') == '<br><br>roll 5 d20<br>19 19 19 19 19 <br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br><br><br>roll 6 d7<br>5 5 5 5 5 5 <br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br>'

def test_max_case():
    assert typical_case('5d20:max6d7') == '<br><br>roll 5 d20<br>19 19 19 19 19 <br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br><br><br> max roll of 6 d7<br>5<br><br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br>'

def test_plus_case():
    assert typical_case('5d20:+6d7') == '<br><br>roll 5 d20<br>19 19 19 19 19 <br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br><br><br> sum of 6 d7<br>30<br><br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br>'