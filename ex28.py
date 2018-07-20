$ python
Python 2.7.15 (default, Jun 11 2018, 14:53:41) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> True and True
True
>>> False and True
False
>>> 1==1 and 2==1
False
>>> "test"=="test"
True
>>> 1==1 or 2!=1
True
>>> True and 1==1
True
>>> False and 0!=0
False
>>> True or 1==1
True
>>> "test" == "testing"
False
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not (True and False)
True
>>> not (1==1 and 0!=1)
False
>>> not (1!=10 or 3==4)
False
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1==1 and not ("testing" == 1 or 1==0)
True
>>> "chunky" == "bacon" and not (3==4 or 3==3)
False
>>> 3==3 and not ("testing" == "testing" or "Python" == "Fun")
False
