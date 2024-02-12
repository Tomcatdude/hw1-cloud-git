# Dice Generator REST API

Using the /dice/command command, you can request any number of any sided dice 
To be randomly generated for you. An example would be if you wanted to 
roll five 6 sided dice and three 20 sided dice. Just enter
"/dice/5d6:3d20" and your dice will be generated and shown to you.

## Getting Started

These instructions will guide you through how use this REST API and utilize
its various dice generating tools

### Simple Example

Above we saw the dice command "/dice/5d6:3d20". This created five 6 sided dice
and three 20 sided dice. Notice that the individual dice command is split up by
a d. The way to call for a new dice type is by typing the number you want, typing
a "d", then typing the number of sides you want.

If we look at the example dice command once again, we can see that different dice 
requests are split by a ":". A colon symbolizes that we are maming a new dice request
and must always be followed by the (number)d(sides) dice command.

You can request an infinite amount of dice by stringing these along to help you create
DnD characters, play dice games, and more. Read the next section to find out how to 
use some of our helpful tools.


## Using More Advanced Tools

There are various tools that help users compute different type of dice rolling needs.

### Dice Sum

If we put a "+" in front of a dice request, then the sum of the dice rolls resulting from
that individual dice request will be returned instead of the individual rolls. For example,
using "/dice/+3d8" will roll three 8 sided dice and return the sum of them.

The usage of this sum character does not carry to other dice requests within the same 
dice command. This means that you can sum one dice request, but still have the others
display as their individual rolls. For example, "/dice/+3d8:2d10" would display the sum
of three 8 sided dice, but still display each of the two individual rolls from the 10
sided dice request. If we wanted both to show their respective sums, we could use 
"/dice/+3d8:+2d10".

### Dice Maximum

If we put the keyphrase "max" in front of a dice request, then the maximum roll of the dice
rolls resulting from that individual dice request will be returned instead of the individual 
rolls. For example using "/dice/max3d8" will roll three 8 sided dice and return the maximum
role.

The usage of this max keyphrase does not carry to other dice requests within the same 
dice command. This means that you can get the max of one dice request, but still have the others
display as their individual rolls. For example, "/dice/max3d8:2d10" would display the max
of three 8 sided dice, but still display each of the two individual rolls from the 10
sided dice request. If we wanted both to show their respective sums, we could use 
"/dice/max3d8:max2d10".

### Total Dice Sum

While the "+" character only acts on a single dice request within a dice command, the 
dice sum command will return the total sum of all dice requests within the dice command
and not the individual rolls.

To use this feature, use the command "/dice/sum/diceCommand". For example, 
using "/dice/sum/2d10:5d4" would roll two 10 sided dice and five 4 sided dice, then display
the sum of all seven dice.

The max feature is supported in sum commands, where only the maximum roll in a max dice request
will be added to the total sum. The "+" character is technically supported, but does not add utility
as the dice will be summed anyways.

### Dice Command Repeats

By adding "?repeat=someNumber" to the end of any dice command, we can roll the entire dice command 
multiple times. This is useful when you have to roll the same set of dice requests multiple times.
Rather than re-entering the requests, we can just use our repeat feature. A useful example
where one might use this feature is if they wanted to roll attacks in DnD for multiple attack turns.
Lets say we had to roll two 8 sided dice for one weapon and one 3 sided die for an additional modifier,
but we have two attack opportunites per turn, then we could just use the command "dice/2d8:1d3?repeat=2".

The repeat command also works with the total sum command, '+' sum character, and "max" keyphrase, meaning
that we can repeat any complicated dice commands that we can think of.


## Why Use Our REST API Over A Competitor's Version?

Add additional notes to deploy this on a live system

### More Features Than Competitors

Most competitors only show you the individually rolled dice and a total sum. They do not allow us to find 
sums for individual collections of dice, nor do they allow us to return the maximum of a given dice request.
Additionally, most competitors do not allow users to repeat a dice multiple times at once.

### No Account Needed!

The more advanced dice generating competitors often require an account of some sort to use their service. 
With our deice generator application, there is no need for us to store or use your personal information.
Simply type the command in and watch the magic happen!
