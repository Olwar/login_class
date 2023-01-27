# login_class
Designing and implementing a class which is responsible for identifying what kind of requests it receives

##### How I understood the problem:  
I had to write a class for the identity app to help other parts of the app to know what to do based on the parameters my class would return or do nothing if the uri given as in the wrong form.

##### What challenges I had with the implementation:  
How to parse the uri was the biggest challenge for me. I ended up using regular expressions (regex) to do this. I took a while to find the correct regex to divide the uri into scheme, path and parameters. After that it was pretty straightforward.  

##### How could I further improve my implementation:  
I could add more tests. I could make the class maybe a bit cleaner code-wise. Maybe someone would have some trouble understanding it even though I believe I added decent comments. The names of the variables could be slightly better.

##### Compromises I had to make:  
Maybe somebody could see using Python for this a compromise. Javascript may be a more suitable or natural choice. But Python is my strongest language so that's why I used that.

##### How to run tests:  
Only requirement is to have python installed and then run:
`python3 tests.py`
