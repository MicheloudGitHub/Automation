How to run this automated test framework

1. Open the python file test_arbusta.py and functions.py and maker sure you have installed the following packages:
    Pandas
    Pytest
    xmlrunner
    unittest

2. If you dont have some of these packages, please go to Terminal>New Terminal>"pip install {package that is missing}" then click enter and wait until installation finishes.

3. Go to test_arbusta.py and in line 149 fill the path with the one that you have on your machine: unittest.main(testRunner=xmlrunner.XMLTestRunner(output='your_path/results'))

4. Now you are ready to run our automated test framework that consists in a full regression test for our web page.

5. To run our test: Go to Terminal>New Terminal> "python -m pytest -v -s test_arbusta.py -m regression" then click enter and wait to see the results.

6. You are going to see how many test cases fail and how many test cases pass. And also the data printed in the terminal. 

7. You can also use te git bash terminal to run the automated test framework. You have to make sure that you are in the same folder as our test_arbusta.py and write
   $ python -m pytest -v -s test_arbusta.py -m regression

8. After the whole process finished you can run the xml report by typing "python -m pytest --junitxml report.xml" (Find the report.xml in the same folder "challenge_arbusta")

9. Please find more information about the marks in pytest.ini file.