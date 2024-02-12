#tests all cases for the total sum command

import rest_api_server



def sum_case(request):
    return rest_api_server.calculate_sum_dice(request, seed = 10)

#test the normal case where we just take the total sum
def test_sum_normal_case():
    assert sum_case('5d20:6d7') == '<br><br>sum of all dice<br>125<br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br>'

#test the case where we take the total sum, where at least one dice request uses a max command
def test_sum_max_case():
    assert sum_case('5d20:max6d7') == '<br><br>sum of all dice<br>5<br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br>'

