# CronParser
A python script to expand values of cron time string. The script will output different values allowed for each time component in the console.

## Command to Execute
`python3 <file_name> <cron_string>`
1. The file name to execute in this project is `main.py`
2. cron string should be a valid string enclosed by inverted commas. The validity of a cron string is described in details below.
3. Test Cases can be run using this command: `python3 -m unittest test.py`

Example of a valid command string: `python3 main.py '*/15 0 1,15 * 1-5 /usr/bin/find'`

## Supported Time Components
The cron string takes input of six values separate by space. 

eg: `*/15 0 1,15 * 1-5 /usr/bin/find`

Below are the details of each part in cron string in sequence:
1. ***Minutes***: Values supported are from 0 to 59 integer values
2. ***Hours***: Values supported are from 0 to 23 integer values
3. ***Day of Month***: Values supported are from 1 to 31 integer values
4. ***Month***: Values supported are from 1 to 12 integrer values representing month in a calender year. January and December are represented by 1 & 12 respectively. Also, string values for month are also supported. Valid string values are `JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC`
5. ***Day of week***: Values supported are from 1 to 7 integer value representing different day in a week. Sunday and Saturday are represented by 1 and 7 respectively. All other week days are represented by integer in the same order eg: Monday by 2, Tuesday by 3, Wednesday by 4 etc. Also, string values for week day are also supported. Valid string values are `SUN MON TUE WED THU FRI SAT`
6. ***Command***: It represents a string value of path of command to be executed by cron.


## Supported Special Characters and Usages
1. `*` : Astrisk represent all values for a time component. “*” in the minute field means every minute.
2. `/` : Slash represents increments. “0/15” in the seconds field means the seconds 0, 15, 30 and 45. Only numerical values are allowed before and after slash. eg: "1/20", "10/45" etc.
3. `-` : A hyphen indicates a range. “15-18” in the hour field means the hours 15, 16, 17 and 18. Only numerical values are allowed before and after hyphen. eg: "1-20", "10-45" etc.
4. `,` : A comma is used to separate multiple allowed values. “MON,WED,FRI” in the day_of_week field means the days Monday, Wednesday, and Friday.

## Project Design Considerations:
1. The `main.py` file is the main executor of the project.
2. `ExpressionParser` class is the driver class
3. `TimeComponent` class is parent class which is inherited by other specific time bound class. This class has methods to parse an expression in a particular time format.
4. `MinuteComponent`, `HourComponent`, `DayOfMonthComponent`, `MonthComponent` and `DayOfComponent` inherits `TimeComponent` class. All details and static values are contained in respective child class.
5. `CommandComponent` class is an independent class.
6. Baisc validation for cron expression are also implemented in `TimeComponent` class.
   
## Example Command:
`python3 main.py '*/15 0 1,15 * 1-5 /usr/bin/find'`

Output:
<code>
Expression: */15 0 1,15 * 1-5 /usr/bin/find
Minute         0, 15, 30, 45
Hour           0
DayOfMonth     1, 15
Month          1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
DayOfWeek      1, 2, 3, 4, 5
Command        /usr/bin/find
</code>
