1.
Explain what is happening in the following program -

class Foo ( Bar ) : 
     def __init__ ( self ) : 
         Bar.__init__ ( self ) 
         return

What do the terms ’subclass’ and ’superclass’ mean in object-oriented programming?
What is duck typing?
What does the name self mean? Is self a Python keyword?
What does the special method __repr__ do and why is it different to the __str__ method?


2. Problem -1
Given: A string of length at most 200 letters and four integers a, b, c and d. 
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. 
Sample Dataset
 HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandallt heKingsmenCouldntputHumptyDumptyinhisplaceagain. 
22 27 97 102 
Sample Output 
Humpty Dumpty

3.Problem -2 

Given: A string of length at most 10000 letters. 
Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order. 
Sample Dataset 
We tried list and we tried dicts also we tried Zen

Output
and 1 
We 1 
tried 3 
…. 

4.Problem -3
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'. Given a DNA string corresponding to a coding strand, its transcribed RNA string is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string having length at most 1000 nt.
Return: The transcribed RNA string of t.
Sample Dataset 
GATGGAACTTGACTACGTAAATT

Output
GAUGGAACUUGACUACGUAAAUU

5.Problem -4


Write a program to store a list of contact names and telephone numbers, similar to the contact lists you might find on a mobile phone. The data needs to be stored in a file so that it is persistent – that is, the data available at the beginning of a new execution of the program is the same as at the end of the previous execution.


6.Problem -5
Extend the program (problem 4) written for the previous exercise so that as new contacts are added, the program checks for duplicate names and numbers. If the new contact’s name is already in the database, the message “This person is already entered.” should appear. If the telephone number is already in the database, the program should display “This person’s telephone number is already in the database. This could be an error, or a second contact at the same company. Add anyway?” If the user enters “Y”, the contact is added.

7.Problem -6
