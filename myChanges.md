So overall I just made some code quality and readability changes to show you how you could simplify a few things, and
make it easier for someone to editing it to understand without having to comment each code block.

1. I modified your checkPercent function in a few ways:

    a. I added a try/except statement since that's generally the correct way of handling that. 
    
    b. I got rid of your prompt if the input wasn't exactly an integer. I wrote two methods that just basically do checks on
the two common ways of representing a percentage that aren't integers and called those.

    c. Then I return a tuple of whether it is valid or not and the int value of the percent (saves casting it later). This allows
us to check the value in our while looop further down. And that makes the code more clear to another person since you can 
use descriptive variables for the results.


2. I also wrote a function for your final calculation. This seems simple, but it puts an identical calculation in one place.
Later if you realize you made an error on that calculation you only have to change it in one spot. 

3. I combined your input and print statements in most places. This is a bit more readable.
4. I added input validation for your target commission input, this is probably overkill, but might save some headaches.
5. Finally if you're already doing string formatting you can go all the way and include the full print statement in that.
I used f strings to combine it all into one line. But these two lines would have worked identically well if you don't want
to use f strings (or are using a python version older than 3.6):


    print(f'Gross commission goal is: {:,}'.format(grossCommission))
    print(f'Total sales goal is: {:,}'.format(houseSales))

