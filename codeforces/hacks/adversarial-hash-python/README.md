# Making a set/dict/Counter O(n^2)
### This directory demonstrates how you can take advantage of hashing collision in python to TLE code in an adversarial manner.
Please see the mk function to see how we solve this problem.
This problem comes from Codeforces Contest round 950 (Div 3)
To demonstrate the difference between a hacked solution and unhacked solution we've provided the two files C.py and Cmodified.py
To run the code use the command
```python3 Bad.py | python3 C.py```
And then run
```python3 Bad.py | python3 Cmodified.py```
You will notice a HUGE speed increase in the modified example that uses the mk function to alter the input keys before being hashed in a dict/set/Counter.
A special thanks to Neal Wu and his Codforces blog [post][1].

[1]:<https://codeforces.com/blog/entry/62393>