
# Summary of repo # PlaywrightPytestTask:

Test core repo created to demonstrate the usage of Playwright+Pytest testing framework. Framework displays how to test different UI elements and scenarios utilising https://www.automationexercise.com/ as a testing sand box.
Framework utilises functionality of the Allure reporter.

# System requirements:

Python 3.8 or higher.  
Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL). 
MacOS 12 Monterey or MacOS 13 Ventura.
Debian 11, Debian 12, Ubuntu 20.04 or Ubuntu 22.04.
 
# Steps to install:

1. Open the repo: https://github.com/AndriiSavruk/PlaywrightPytestTask
2. Clone the repo
HTTP: https://github.com/AndriiSavruk/PlaywrightPytestTask.git   
Github: ```git clone https://github.com/AndriiSavruk/PlaywrightPytestTask```
3. Run a ``` pyton -m pip install --upgrade pip ``` in the project root
4. Run  ``` pip install pipenv ``` 
5. Run  ``` pipenv install --system ```
6. Run  ``` playwright install chromium ```

# Steps to launch:

for running the tests:  
```pytest```  
running in headed model:  
```pytest --headed```  
run one particular test:  
```pytest -k <name of the test>```  
 
# Steps to creating the report:

The report is generated automatically after each test run overriding the previous report. 
Use this command to see the report: ```allure serve reports``` 