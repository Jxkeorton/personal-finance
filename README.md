# Personal Finance Tool

![Gif](./docs/personal-finance-gif.gif)


******

## Contents

1. [The User Experience](#the-user-experience)
    - [Site Goals](#site-goals)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
2. [Workflow Diagrams](#workflow-diagrams)
    - [Main Menu](#main-menu)
    - [Options](#options)
    - [Reports](#reports)
3. [Structure](#structure)
    - [Features](#features)
    - [Features left to implement](#features-left-to-implement)
4. [Technologies Used](#technologies-used)
5. [Deployment and Local Development](#deployment-and-local-development)
    - [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
        - [How to Fork](#how-to-fork)
        - [How to Clone](#how-to-clone)
6. [Testing](#testing)
    - [Pep8 Validation](#pep8-validation)
    - [Functional Testing](#functional-testing)
7. [Issues/Bugs](#issuesbugs)
    - [Fixed Issues](#fixed-issues)
    - [Known Bugs](#known-bugs)
8. [Credits](#credits)

******

## The User Experience

This project was created to help people manage finances better and more easily by categorizing different incomes and expenses. It also allows you to set a monthly budget and see reports within certain date ranges or for the previous month.

### Site Goals

* To provide data to allow for more calculated decisions on spending and budgeting.

### Target Audience

* For people who are looking to know exactly where their money is coming and going.

### User Stories

* As a User, I would like to be able to easily find the various menus so that I can view information or add information.
* As a User, I would like to be able to add a new income and expense
* As a User, I would like to be able to set a monthly budget
* As a User, I would like to be able to see my income and expenses over a specified range
* As a User, I would like to see a summary for the previous month
* As a User, I would like to see an analysis of a specified date range
* As a User, I would like to be able to return to the main menu without having to restart the application.

******

## Workflow Diagrams

#### Main menu
![Main Flow chart](./docs/main-flow-chart.png)

#### Options
![options Flow chart](./docs/options-flow-chart.png)

#### Reports
![reports Flow chart](./docs/reports-flow-chart.png)

<sup><sub>[*Back to top*](#contents)</sup></sub>

******

## Structure

### Features

USER STORY

`
As a User, I would like to be able to easily find the various menus so that I can view information or add information.
`

IMPLEMENTATION
* Main Menu
    * Here the user can select between the following options:
        * 1 - Options - This option will navigate the user to the options menu
        * 2 - Reports  - This option will navigate the user to the reports menu
        * 3 - Exit - This option will exit the application/program
    * The user must input a correct number corresponding to each menu or they will be alerted of an incorrect choice and the menu will be presented again. This is the same for all menus.

![Main menu](./docs/home-menu.png)

USER STORY

`
As a User, I would like to be able to add a new income and expense
`

IMPLEMENTATION
* New Transaction menu
    * Here the user can select between the following options:
        * 1 - Add Income - This option will ask for user input, once all the data is collected it will save to the google sheets worksheet.
        * 2 - Add Expense - This option will ask for user input, once all the data is collected it will save to the google sheets worksheet.
        * 3 - Go Back - This option will return the user to the Options menu.
        * 4 - Exit - This option will exit the application/program
    * The user can will be prompted to enter a number for the value of there income or expense depending on the option chosen and a category. They can then enter the value and press enter to upload there new data to the google worksheet.

![New transaction menu](./docs/new-transaction-menu.png)

![Add income or expense](./docs/add-income-expense.png)

USER STORY

`
As a User, I would like to be able to set a monthly budget
`

IMPLEMENTATION
* Options Menu
    * Here the user has the following options:
        * 1 - New Transaction - This option will send the user to the New Transaction menu
        * 2 - Edit monthly budget - This option will display the current monthly budget and ask for user input, once all the data is collected it will save to the google sheet worksheet under monthly budget.
        * 3 - Go Back - This option will return the user to the Main menu
        * 4 - Exit - This option will exit the application/program
    * When the user chooses the edit monthly budget option they will be able to see there current monthly budget and edit it.

![Edit monthly budget](./docs/edit-monthly-budget.png)

USER STORY

`
As a User, I would like to be able to see my income and expenses over a specified range
`

IMPLEMENTATION
* Reports menu
    * Here the user has the following options:
        * 1 - Income - The user will be prompted for multiple inputs , the appropriate data is then displayed 
        * 2 - Expenses - The user will be prompted for multiple inputs , the appropriate data is then displayed 
        * 3 - Summary - A monthly summary will be displayed for the previous month
        * 4 - Analytics - The user will be prompted for multiple inputs and will then be shown a display of there spending habits over a specified range
        * 5 - Go Back - This will take the user back to the previous menu
        * 6 - Exit - This option will exit the application/program
    * When the income or expenses option is selected the user will be prompted to input a date range, after a correct date range in inputted they will be displayed with the appropriate information

![Income or Expense report](./docs/income-expense-report.png)

USER STORY

`
As a User, I would like to see a summary for the previous month
`

IMPLEMENTATION
* Reports menu
    * Here the user has the following options:
        * 1 - Income - The user will be prompted for multiple inputs , the data is then saved to the google worksheet
        * 2 - Expenses - The user will be prompted for multiple inputs , the data is then saved to the google worksheet
        * 3 - Summary - A monthly summary will be displayed for the previous month
        * 4 - Analytics - The user will be prompted for multiple inputs and will then be shown a display of there spending habits over a specified range
        * 5 - Go Back - This will take the user back to the previous menu
        * 6 - Exit - This option will exit the application/program
    * When the summary option is selected the summary for the previous month will be displayed

![Summary report](./docs/summary-report.png)

USER STORY

`
As a User, I would like to see an analysis of a specified date range 
`

IMPLEMENTATION
* Reports menu
    * Here the user has the following options:
        * 1 - Income - The user will be prompted for multiple inputs , the data is then saved to the google worksheet
        * 2 - Expenses - The user will be prompted for multiple inputs , the data is then saved to the google worksheet
        * 3 - Summary - A monthly summary will be displayed for the previous month
        * 4 - Analytics - The user will be prompted for multiple inputs and will then be shown a display of there spending habits over a specified range
        * 5 - Go Back - This will take the user back to the previous menu
        * 6 - Exit - This option will exit the application/program
    * When the analytics option is selected the user would be prompted to input a date range, when a correct date range is entered a display of analytics for the users spending will be presented.

![Analytics report](./docs/analytics-report.png)

USER STORY

`
As a User, I would like to be able to return to the main menu without having to restart the application.
`

IMPLEMENTATION
Across all the menus there is an option to return to the previous menu which you can do until you get back to the main menu.
The user must input the correct corresponding number in order to return to the previous menu.

### Features left to implement

A future feature I would like to add, Improving the analytics report to show spending against the monthly budget and to be able to add recurring income/expenses that happen every month from specified dates. This would minimize the amount the user will have to interact with the app making it less of a task.

<sup><sub>[*Back to top*](#contents)</sup></sub>

******

## Technologies Used

* Python - Python was the main language used to build the application.
    * Python packages used:
        * DateTime - To validate dates
        * timedelta - To find a date range
        * Colorama - To color outputs
        * Tabulate - Used to create a table output
        * gspread - Used to read/write to google worksheets
* Google sheets - This was used as data storage in order to store transaction history and other information.
* Microsoft Snipping tool - This was used to screen record the Gif for the readme. It was originally an MP4 and ezgif.com was used to convert to GIF format.

<sup><sub>[*Back to top*](#contents)</sup></sub>

******

## Deployment and Local Development

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Blackjack Royale’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.


### Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

The steps for deployment are:

    1. Create a new Heroku app with a unique name and the region

    2. In the "settings" tab, set the build packs to 'Python' and 'NodeJS' (the order is important)

    3. Link the Heroku app to the GitHub repository

    4. In case it is wished, enable "automatic deploys" to automatically update the app in case of a new commit

    5. Click on Deploy in the "manual deploy" area

******

### Local Deployment

#### How to Fork

1. Log in to [GitHub](https://github.com/).

2. Find the repository for [this project](https://github.com/Jxkeorton/personal-finance).

3. Click the Fork button in the top right corner of the screen.

#### How to Clone

1. Log in to [GitHub](https://github.com/).

2. Find the repository for [this project](https://github.com/Jxkeorton/personal-finance).

3. Click the Code button and select whether you would like to clone with HTTPS, SSH or GitHub CLI. Copy the link displayed.

4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.

5. Type 'git clone' into the terminal and then paste the link you copied in step 3.

<sup><sub>[*Back to top*](#contents)</sup></sub>

******

## Testing

### Pep8 Validation

All python code was ran through https://pep8ci.herokuapp.com/ validator and any warnings or errors were fixed. Code then validated successfully.

menus.py

![Menus.py pep8](./docs/menus-pep8.png)

options.py

![options.py pep8](./docs/options-pep8.png)

reports.py

![reports.py](./docs/reports-pep8.png)

run.py

![run.py pep8](./docs/run-pep8.png)

sheet.py

![sheet.py pep8](./docs/sheet-pep8.png)

transactions.py

![transactions.py pep8](./docs/transactions-pep8.png)

utils.py

![utils.py pep8](./docs/utils-pep8.png)


******

### Functional Testing

| Test                                      | Steps                                                          | Expected                                                         | Actual                                                           |
| ----------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| running program                         | python [run.py](http://run.py/) in the terminal                | main menu appears in clear terminal                              | main menu appears in clear terminal                              |
| select all menu options                   | select each option available on every menu screen              | selected menu/option appears in clear terminal                   | selected menu/option appears in clear terminal                   |
| select go back option on all menu screens | select the go back option where available                      | go back to previous menu                                         | go back to previous menu                                         |
| add income                                | follow steps to add a new income                               | a new income is successfully added to google sheet               | a new income is successfully added to google sheet               |
| add expense                               | follow steps to add a new expense                              | a new expense is successfully added to google sheet              | a new expense is successfully added to google sheet              |
| select exit on all menu screens           | select exit option where available                             | the program exits                                              | the program exits                                              |
| edit monthly budget                       | visit the edit budget option and change the budget             | the monthly budget successfully updates in google sheet          | the monthly budget successfully updates in google sheet          |
| see income report                         | enter date range to see report                                 | report shows income within date range                            | report shows income within date range                            |
| see expense report                        | enter date range to see report                                 | report shows expenses within date range                          | report shows expenses within date range                          |
| see summary                               | select summary option                                          | monthly summary shown for previous month                         | monthly summary shown for previous month                         |
| see analytics                             | enter date range for analytics                                 | spending habits shown for each category within date range        | spending habits shown for each category within date range        |
| validation for date range inputs          | enter incorrect date format , a date that is before start date | error message is shown to user and user is prompted to try again | error message is shown to user and user is prompted to try again |
| validation for menu choices               | enter incorrect number , enter a letter                        | error message is shown to user and user is prompted to try again | error message is shown to user and user is prompted to try again |
| validation for monthly budget             | enter a letter                                                 | error message is shown to user and user is prompted to try again | error message is shown to user and user is prompted to try again |
| validation for new transactions           | enter letters                                                  | error message is shown to user and user is prompted to try again | error message is shown to user and user is prompted to try again |

<sup><sub>[*Back to top*](#contents)</sup></sub>

## Issues/Bugs

### Fixed Issues

The elif statements for the menus were not working correctly due to strings being passed in by the user for the input. 
So these were converted to integers before making the user input equal to the 'choice'.

### Known Bugs

No known bugs at this stage of development.

<sup><sub>[*Back to top*](#contents)</sup></sub>

******

## Credits

- **[Python Documentation on datetime](https://docs.python.org/3/library/datetime.html)**: Provided comprehensive details on using the `datetime` module in Python, including manipulating dates and times, using `timedelta` objects for date arithmetic, and formatting date strings. It also covered instance methods for `date` and `time` objects, crucial for handling various date-time operations in the project.

- **[Programiz on datetime strftime](https://www.programiz.com/python-programming/datetime/strftime)**: Helped understand how to format dates and times using the `strftime` method. Provided examples and explanations of different format codes, enabling the conversion of datetime objects into readable strings.

- **[Programiz on datetime strptime](https://www.programiz.com/python-programming/datetime/strptime)**: Essential for parsing strings into datetime objects using the `strptime` method. Explained how to specify the format of the input string, critical for converting user input or data from various sources into datetime objects.

- **[GeeksforGeeks on datetime.timedelta](https://www.geeksforgeeks.org/python-datetime-timedelta-function/)**: Detailed the `timedelta` class, explaining how to create and use `timedelta` objects for date and time arithmetic. Included practical examples of adding and subtracting time spans, useful for handling durations in the project.

- **[Tabulate on PyPI](https://pypi.org/project/tabulate/)**: Provided functionality to display tabular data in a readable format. Instrumental in presenting data in tables with various formatting options, enhancing the readability and presentation of data.

- **[Colorama on PyPI](https://pypi.org/project/colorama/)**: Used to add color to text in the project's console output. Simplified the process of making terminal output more user-friendly and visually appealing by providing cross-platform support for colored text.

- **[Ezgif](https://ezgif.com/)**: Used to create and edit GIFs, helping generate and manipulate animated images for the project. Provided a straightforward interface to perform tasks such as resizing, cropping, and optimizing GIFs.

- **[GeeksforGeeks on Python exit commands](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/)**: Explained various exit commands in Python (`quit()`, `exit()`, `sys.exit()`, and `os._exit()`), detailing their differences and appropriate usage scenarios. Crucial for implementing proper termination and cleanup routines in the project.


<sup><sub>[*Back to top*](#contents)</sup></sub>