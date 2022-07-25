The 2 main sequences in Mathematics are Arithmetic Progression and Geometric Progression. Those are the sequences you will be working with in this kata.

# Introduction
A sequence of numbers is called an Arithmetic Progression if the difference between any two consecutive terms is always same. In simple terms, it means that next number in the series is calculated by adding a fixed number to the previous number in the series. This fixed number is called the common difference.

A sequence of numbers is called a Geometric Progression if the ratio of any two consecutive terms is always same. In simple terms, it means that next number in the series is calculated by multiplying a fixed number to the previous number in the series. This fixed number is called the common ratio.

# Rules
Given an array of integers that follow either series, you have to determine the series and return accordingly :

    "0" if it is an AP
    "1" if it is a GP
    "-1" if it doesn't follow any of the above sequences
    "2" if it is both an AP and GP



For Example,

      series_array = [2, 5, 8, 11, 14]   #should return 0
      series_array = [1, 2, 4, 8, 16]    #should return 1
      series_array = [1, 2, 1, 3, 4, 5]  #should return -1
      series_array = [1, 1, 1, 1, 1]     #should return 2
      series_array = [0, 0, 0, 0, 0]     #should return 0

  
The main challenge is identifying the differences between the 2 sequences and to find a way of determining each sequence

If the series has all 0's, then 0 should be returned as it is not accepted as a 
term GP

NOTE : Only APs and GPs are considered in this question. Other series like Harmonic Progression are not considered and assume that the array will have atleast one element