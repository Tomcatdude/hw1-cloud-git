import rest_api_server



def sum_case(request):
    return rest_api_server.calculate_sum_dice(request, seed = 10)

def test_sum_normal_case():
    assert sum_case('5d20:6d7') == '<br><br>sum of all dice<br>125<br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br>'

def test_sum_max_case():
    assert sum_case('5d20:max6d7') == '<br><br>sum of all dice<br>5<br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br>'

