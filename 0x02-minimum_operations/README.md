# 0x02. Minimum Operations
#### `Algorithm` `Python`

For this project, you will need to understand several key algorithmic and mathematical concepts to devise a solution that efficiently calculates the minimum number of operations to achieve a given number of characters using only “Copy All” and “Paste” operations. Here is a list of concepts and resources that will be helpful:

## Concepts Needed:
1. Dynamic Programming:
* Familiarity with dynamic programming can help in breaking down the problem into simpler subproblems and building up the solution.
* [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)
2. Prime Factorization:
* Understanding how to perform prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number n.
* [Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-factorization-prealg/v/prime-factorization)
3. Code Optimization:
* Knowing how to approach problems from an optimization perspective can be useful in finding the most efficient solution.
* [How to optimize Python code](https://stackify.com/how-to-optimize-python-code/)
4. Greedy Algorithms:
* The problem can also be approached with greedy algorithms, choosing the best option at each step.
* [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)
5. Basic Python Programming:
* Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
* [Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
By studying these concepts and utilizing the resources provided, you will be equipped to tackle the “Minimum Operations” problem effectively, applying both mathematical reasoning and programming skills to find the most efficient solution.

## Additional Resources
Mock Technical Interview


## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu `20.04` LTS using python3 (version `3.4.3`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be documented
* Your code should use the `PEP 8` style (version `1.7.x`)
* All your files must be executable

## Tasks

[0. Minimum Operations](./0-minoperations.py)

In a text file, there is a single character `H`. Your text editor can execute only **two** operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

* Prototype: `def minOperations(n)`
* Returns an integer
* If `n` is impossible to achieve, return `0`

**Example**:

`n = 9`

`H` => `Copy All` => `Paste` => `HH` => `Paste` => `HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

**Number of operations: `6`**

```
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```

# Overview

Let's dive into the details of each step in the `minOperations` function:

1. **Initialization**:
```
operations_needed = 0
divisor = 2
```
* `operations_needed` is a variable that will keep track of the total operations needed.

* `divisor` is initialized to `2` because we start the factorization process from the smallest prime number.

2. **Outer Loop - Prime Factorization**:
```
while n > 1:
```
* This outer loop continues until `n` becomes `1`. It ensures that the process of factorization continues until `n` is completely factored into prime numbers.

3. **Inner Loop - Divisibility Check**:
```
while n % divisor == 0:
```
* This inner loop executes as long as the current divisor evenly divides `n`. It checks for divisibility by the current divisor and proceeds only if `n` is divisible.

4. **Update Operations and `n`**:
```
operations_needed += divisor
n /= divisor
```
* Inside the inner loop, if `n` is divisible by the current divisor, the divisor is added to `operations_needed`. This step indicates that an operation is performed to get the factorized prime number.
* `n` is then updated by dividing it by the divisor, effectively reducing `n` to its next factor.

5. **Increment Divisor**:
```
divisor += 1
```
* After completing the inner loop, the outer loop increments the divisor. This step moves to the next potential prime factor for further factorization.

6. **Return Total Operations**:
```
return operations_needed
```
* Once the outer loop completes (i.e., `n` becomes `1`), the function returns the total `operations_needed`. This value represents the sum of prime factors of the original `n`, which corresponds to the minimum number of operations needed to obtain the desired number of 'H' characters.


In summary, the algorithm leverages prime factorization to represent the given number `n` as the product of its prime factors.
The sum of these prime factors is then returned as the minimum number of operations needed to achieve the desired outcome.
This approach is based on the fundamental theorem of arithmetic, which states that every integer greater than `1` is either a prime number itself or can be factorized uniquely into a product of prime numbers.
