# python-hw-checker
Automatically check your Technion python course homework

# How to use

```python autocompare.py```

enter the path to the tests zip file downloaded from the technion website
then enter the paths for each question (number of questions required is loaded automatically from the zip)

# how to interpret results

If all the tests pass, the script will print "All tests pass!".
If some tests fail, it will print which ones failes, as well as the input for that test and what *your code* returned.
If a test takes more than 5 seconds to run, it will time out and an error will print.
