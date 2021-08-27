# ED5340 Files

## Lab1

1. WAP to print the operator precedence table (use the arithmetic and assignment operators)

2. WAP to generate 5 random numbers and use them in the arithmetic operators. Also, make use of 'seed' value.

3. WAP to demonstrate the various standard datatypes (not user-defined) available in Python and print the type of each of them?

4. WAP to demonstrate the various ways in which a string can be represented. Also show the different ways in which a string can be sliced.

5. String slicing can have more than two parameters (in the class, we used two parameters, start and end). (a) WAP a program to demonstrate the use of more than two. (b) Also, demonstrate how to reverse a given string in the same program.

## Lab 2

(1) Convert the string 'Light is faster than sound' to "LIGHT Is Faster Than SOUND."

(2) Check if a given string is a palindrome (the reverse of the string is the string itself, e.g., Never odd or even)

(3) For a string S and a pattern P, check whether P is present in S. If so, print the (first) index of occurrence, else print -1

(4) Check if a given number is a prime number.

(5) In the class, we saw different approaches to solve the largest (or smallest) of three numbers.

    (a) WAP them to demonstrate them.

    (b) The same can be solved using 'conditional expression'. Find out what is that and solve the same problem using (i) two different conditional expressions (ii) only one line conditional expression (i.e. nested)

(6) Find about continue, and pass statements and WAP to demonstrate them.

(7) Using loops, compute the series for

    (a) exp(x),
    (b) sin x and
    (c) cos x, taking input as x (and you can also take input for the number of terms to be computed in the series).

(8) WAP to print numbers 1 to 10 on the same line, breaking out of an infinite loop.

(9) WAP to print all unique combinations of 1, 2 and 3.

(10) Given an integer, find out the sum of its digits.

(11) Create a list of random integers in range(1,100) , find the median of the numbers in the list, later divide the list into two sublists with respect to the median.

(12) WAP to sort the list A=[5,3,1,2,4,0] in descending order i.e [5,4,3,2,1,0] ( dont use any inbuilt function for this)

(13) Given a list of numbers, remove the numbers that occur more than once. Return the remaining numbers in the order of occurrence [ONLY LIST DATA STRUCTURE IS ALLOWED]

(14) What is the difference between shallow and deep copying in list. WAP to demonstrate that.

(15) WAP to do the following:

    (a) Create a list of bank accounts with name alone

    (b)  then query for a new account and insert the details       wrt alphabetical order of the name

    (c) query for a name and delete from the list

    (d) take an input name and append at the beginning

    (e) identifying  duplicates and remove all but one

    (f) sort the bank accounts alphabetically.

## Lab 3

1.  Create 3 tuples one for name, age and salary and group them using zip function. Print them using unpacking operator as well as indexing approach.

2.  Using list comprehension and random number generation between 10 and 100,

        (a) Print the even numbers
        (b) Print the odd numbers
        (c) Print the numbers divisible by 3

3.  For two matrices of size 3X3 each, perform the following matrix operation:

         (a) addition,
         (b) subtraction
         (c) multiplication and
         (d) transpose
         (e) trace. For each of them, do in both ways i.e. (i)       Without using Zip() but use list comprehension (ii)     Using Zip()

4.  Given two matrices A and B (list of lists) perform the following operations using zip() and \*(unpacking) operator.

         (a) Interchange any two rows

         (b) Interchange any two columns

    You can take suitable inputs for rows / columns

(5) join tuples if similar initial elements - eg. -

       The original list is : [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

        The extracted elements : [(5, 6, 7), (6, 8, 10), (7, 13)]

(6) Sort the lists in tuple - eg.

        The original tuple is : ([7, 5, 4], [8, 2, 4], [0, 7, 5])

        The tuple after sorting lists : ([4, 5, 7], [2, 4, 8], [0, 5, 7])

(7) Given a list,

       (a) Find all possible subsets and Store them in a list of lists (of length = 2^n)

       (b)Demonstrate the following operations on a sublist ((i) Insert more elements into it (ii) Find and replace (iii) Delete individual elements till the sublist becomes empty (iv) Sorting

(8) Given two lists A and B of integers. Sort the lists A and B together, with respect to the list A. (Hint: use zip and "sorted" for sorting)

       Eg, A=[1,3,2], B=[6, -1, -2]

      Answer: A = [1,2,3], B=[6,-2,-1]
