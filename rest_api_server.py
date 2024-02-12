#authored by Tom Odem on 12 Feb 2023
from bottle import route, run, request, response
import random
from datetime import datetime


break_text = '<br>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<br>' #reuse in multiple places


@route('/')
def welcome():
    if 'text/html' in request.headers.get('Accept', '*/*'): #if they accept html, return html
        response.content_type = 'text/html'
    
    #create the welcome cheat sheet
    text_to_display = ''

    #welcome
    text_to_display += '<br><br>Welcome to our dice generator website!<br>'
    text_to_display += '<br>Below are all of the commands you can use to generate some dice<br>'
    
    #basic roll command
    text_to_display += '<br><br>Roll | /dice/diceRequest:diceRequest:... -> generate dice according to the inputted dice command<br>'
    text_to_display += '/dice/1d8:4d7 would roll one 8 sided die and four 7 sided dice<br>'
    
    #sum command
    text_to_display += '<br><br>Sum | /dice/diceRequest:+diceRequest:... -> generate dice and return the sum of the dice with the "+" character before it<br>'
    text_to_display += '/dice/1d8:+4d7 would return one 8 sided die and the sum of four 7 sided dice<br>'

    #maximum command
    text_to_display += '<br><br>Maximum | /dice/diceRequest:maxdiceRequest:... -> generate dice and return the maximum of the dice with the "max" keyphrase before it<br>'
    text_to_display += '/dice/1d8:max4d7 would return one 8 sided die and the maximum roll of the four 7 sided dice<br>'

    #total sum command
    text_to_display += '<br><br>Total Sum | /dice/sum/diceRequest:diceRequest:... -> generate dice and return the total sum of all of the dice rolled in the command<br>'
    text_to_display += '/dice/sum/1d8:4d7 would return the sum of all 4 dice<br>'
    text_to_display += 'Total Sum supports Max within any dice command<br>'

    #repeat command
    text_to_display += '<br><br>Repeat | /dice/diceRequest:diceRequest:...?repeat=number -> repeat a dice command for the specified number of times<br>'
    text_to_display += '<br>/dice/1d8:+4d7?repeat=3 would return one 8 sided die and the sum of four 7 sided dice, then do that again 2 more times (3 total)<br>'
    text_to_display += 'Repeat supports Max, Sum, and Total Sum within any dice command<br>'

    return text_to_display

#just returns the dice, does not add them or do antyhing else
@route('/dice/<dicetext>')
def calculate_dice(dicetext, seed = 0):
    if 'text/html' in request.headers.get('Accept', '*/*'): #if they accept html, return html
        response.content_type = 'text/html'

    try :
        dice_rolls = get_dice_rolls(dicetext) #get the dice rolls

        #checks for "?repeat={number}" at end of uri
        repeat = int(request.query.get('repeat','0'))
        if(repeat != 0):
            print(f'repeat: {repeat}')
            text_to_display = ''
            for i in range(0, repeat): #since we have repeat, generate the dice command multiple times
                text_to_display += f'<br><br>repeat #{i+1} of {repeat}<br><br>'
                text_to_display += dice_compute(dice_rolls)
                text_to_display += '<br>====================================<br>'
            
            return text_to_display

        #no repeat, just do it once
        return dice_compute(dice_rolls, seed) #compute the dice, get the string, and return it


    except:
        return 'dice not formatted correctly. try "/dice/2d20:+5d7" as an example'


#sums all dice specified into one number
@route('/dice/sum/<dicetext>')
def calculate_sum_dice(dicetext, seed = 0):

    if 'text/html' in request.headers.get('Accept', '*/*'): #if they accept html, return html
        response.content_type = 'text/html'

    

    try :
        dice_rolls = get_dice_rolls(dicetext) #get the dice rolls

        
        #checks for "?repeat={number}" at end of uri
        repeat = int(request.query.get('repeat','0'))
        if repeat != 0:
            print(f'repeat: {repeat}')
            text_to_display = ''
            for i in range(0, repeat): #we have repeat, so generate the dice commands multiple times
                text_to_display += f'<br><br>repeat #{i+1} of {repeat}<br><br>'
                text_to_display += dice_sum(dice_rolls, seed)
                text_to_display += '<br>====================================<br>'
            
            return text_to_display

        #we don't have repeat, so just generate the command once
        return dice_sum(dice_rolls, seed)



    except:
        return 'dice not formatted correctly. try "/dice/sum/2d20:max5d7" as an example'


    
#return the dice command as a 1d array of pairs [number,type,number,type,...]
def get_dice_rolls(dicetext):
    dice = dicetext.split(':') #split up the text into the incidividual dice requests
    dice_rolls = [roll.split("d") for roll in dice] #get pairs of (how many dice, dice type)
    dice_rolls = [number for pair in dice_rolls for number in pair] #flatten array
    
    return dice_rolls

#computes the "total sum" command
def dice_sum(dice_rolls, seed = 0):
    total = 0 #holds total sum

    rolls_iter = iter(dice_rolls)
    for roll in rolls_iter: #for every dice request
        #lets find if there is a math type in front of this request
        math_type = ''
        for ch in roll: #find the word at the beginning
            if not ch.isdigit():
                math_type += ch
            else: #got to a number, remove the math_type and break
                roll = roll.replace(math_type,'')
                break
        
        how_many = int(roll) #the amount of dice to roll
        d_type = int(next(rolls_iter)) #the number of sides

        if math_type == "max": #only count the maximum roll
            rolls = max(return_dice_rolls(how_many, d_type, seed))
            total =+ rolls
        else: #normal dice roll, no math type
            rolls = return_dice_rolls(how_many, d_type, seed)
            total += sum(rolls)

    
    text_to_display = f'<br><br>sum of all dice<br>{total}{break_text}'
    return text_to_display

#just a normal computation, can use '+' and 'max' computation modifiers
def dice_compute(dice_rolls, seed = 0):

    text_to_display = ''
    rolls_iter = iter(dice_rolls)
    for roll in rolls_iter: #for every dice request
        #lets find if there is a math type in front of this request
        math_type = ''
        for ch in roll: #find the word at the beginning
            if not ch.isdigit():
                math_type += ch
            else: #got to a number, remove the math_type and break
                roll = roll.replace(math_type,'')
                break
        
        how_many = int(roll) #the amount of dice to roll
        d_type = int(next(rolls_iter)) #the number of sides

        if math_type == "+": #we want to find the sum of this particular dice request
            rolls = sum(return_dice_rolls(how_many, d_type, seed))
            text_to_display += f'<br><br> sum of {how_many} d{d_type}<br>{rolls}<br>'
            text_to_display += break_text
        elif math_type == "max": #only count the maximum roll
            rolls = max(return_dice_rolls(how_many, d_type, seed))
            text_to_display += f'<br><br> max roll of {how_many} d{d_type}<br>{rolls}<br>'
            text_to_display += break_text
        else: #normal dice roll, no math type
            rolls = return_dice_rolls(how_many, d_type, seed)
            text_to_display += f'<br><br>roll {how_many} d{d_type}<br>'
            for roll_value in rolls:
                text_to_display += f'{roll_value} '
            text_to_display += break_text

    return text_to_display

#computes and returns the actual random rolls. can be seeded to recreate exact rolls for testing purposes
def return_dice_rolls(how_many, d_type, s = 0):
    #create a list with all of the rolls for this d_type
    dice_rolls = []
    
    for i in range(0, how_many):
        if(s != 0): #make it a set seed
            random.seed(s)
            print('seeded')
        else: #get random seed based on time
            random.seed(datetime.now().timestamp())

        #compute this dice roll and add it to the list for this request
        rand_num = random.randint(1,d_type)
        print(rand_num)
        dice_rolls.append(rand_num)
    
    return dice_rolls



if __name__ == '__main__':
    run(host = '0.0.0.0', port = '8080')