Phitron Python


Try by yourself. Do not google for help. It’s mandatory that you yourself solve the problems as much as you can.

1. We can read 'abba' if we reverse the letters, it’s still 'abba', so this string is called palindrome. Write a python program to check if a string is palindrome or not. 

2. Write a program center_align.py to centre align all lines in the given file.
Example output: 
I am sure that the shells are seashore shells. 
So if she sells seashells on the seashore, 
The shells that she sells are seashells, 
I am sure She sells seashells on the seashore;


3. Write a function nearly_equal to test whether two strings are nearly equal. Two strings a and b are nearly equal when a can be generated by a single mutation on b.
>>> nearly_equal('python', 'perl') 
False 
>>> nearly_equal('perl', 'pearl') 
True


4.  Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.
>>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']) 
[['eat', 'ate', 'tea], ['done', 'node'], ['soup']]


5. Which names are local, which are global and which are built-in in the following code fragment? 
space_invaders = [ . . . ] 
player_pos = ( 200 , 25 ) 
level = 1 max_level = 10 

def play ( ) : 
     . . . 
    while ( level < max_level +1 ) :
         if len ( space_invaders ) == 0 : 
            level += 1 
            continue 
. . .



6. Answer without running the code, run in your brain.
What is the result of executing the following code? 
def dp ( l1 , l2 ) : 
    def p ( ll1 , ll2 , n ) : 
        return ll1[n] * ll2[n] 
    r = 0 
    for i in range ( len ( l1 ) ) : 
      r += p ( l1 , l2 , i ) 
    return r 


print dp ( [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] )



7. Write a program to display a simple form of digital book. “Books” are text files in which each block (page) of text is followed by a double dash (--). When a book is displayed, the first block of text is shown and the program should wait for the user to press the enter key before displaying the next.

File.txt:
This is first page content--Now we are in the second page


Output:
This is first page content
[enter - read more, press q to quit]



8. Extend the previous challenge so that it is possible to skip forward by an arbitrary number of pages. This should be achieved by allowing the user to enter a number before pressing the enter key. If the number is positive, the given number of pages are skipped. If there is no number, the next page is displayed.

9. Further extend the book reader so that it can accept negative numbers for skipping pages. Entering -1 should go back to the previous page. There are many ways to achieve this.

10. If you search your computer’s hard disk, you may find that many files have the same name. Readme.txt, for example, appears many times on our hard disks. These files are distinct and normally have different contents. How is it that the operating system can maintain separate files of the same name?


