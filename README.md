# Python-Practice
Repository for learning and practicing python

Contains projects and modules that I did during my learning process

I enjoyed a lot creating my own modules

# Data Scraper
Navigate to data scraper folder to experience the below four projects:

   - **Fundoodata scraper** - *Program to scrape fundoodata websites for companies details. 1 program visits 100 pages and scraped away 1800 chennai companies data*
   
   - **Practice pyxl** - *Trying out openpyxl module to convert excel files into csv files and also the programs removes duplicates entries (companies in excel file). 22000 companies in excel file got converted into csv file containing 9600 companies after removing duplicates by the program. Used dictionary datastructure to remove duplicates*
   
   - **Scraping companies data from html files** - *Program to scrape companies data from local html files located in the folder 'companies data in html files/10'. Data scraper processed 8542 html files and extracted away 22000 companies data into a csv file*
   
   - **Tirupur database scraper** - *Program to convert an excel file (data.xlsx) containing companies data into an csv file of desired format. Datascraper2.py file will do the job better. The sample.csv file is the output and finished.xlsx is the result of manual processing of sample.csv file*


# Own Python Module
Navigate to Own Python Module folder to experience the module that I have created during my learning journey:

   - **Array** - *Array like module, you can do perform basic array operations using this module. This module also has the capacity to create 2d array*
   
   - **Bag** - *Bag module, this module basically act like a bag - you can pick things from the bag, put things into the bag and also it has iter dunder method to see what's inside the bag*
   
   - **Bagset** - *Set module, this Set module is created using the Bag module. This module basically act like a Set, only unique items will be added to the Set and you can perform certain operation on two Sets like comparing two Sets, performing Union, intersection, and Complement operations on Sets*
   
   - **Counter** - *Counter module to perform counting operation. Create instance and whenever you have a need to count something, call push method to increment the count and if you want to reset the count - call the reset method and if you want to know the current count - call the display method from Counter instances*
   
   - **Date** - *Date module perform basic operations on dates. Date module accepts month, day and year as arguments. Date instances has access to the methods like dayOfWeek(), monthName(), isLeapYear(), numDays(otherDate) - Number of dates between two dates, dayOfWeekName(), dayOfYear(), isWeekDay(), isEquinox(self), isSolstice() and you can compare two dates*
   
   - **Dict** - *An upgrade to Bag Module, basically the Bag can have non unique items and to keep track of non-unique items, this module was created. Eg.) If you have two apples in the bag, this module will tell you that you have two apples in your bag. Here we use Dictionary datastructure to achieve this feature, so I named the module as Dict*
   
   - **LinearSet** - *This module is same like Bagset module, but this module is created using python list datastructure and it perform all operations mentioned in Bagset module*
   
   - **LinearMap** - *Dictionary like module created using own Set and Array module, you can basic dictionary operations like assign values and access value using key and you can iterate through linearmap using keyArray() method*
   
   - **Linkedlist** - *Linked list datastructure - simple linked list datastructure*
   
   - **Point** - *Point module to represent a point(x,y), you can get coordinates of the point and distance between two points*
   
   - **Linesegment** - *Linesegment module can able to perform operations on line - you can determine the length, slope, midpoint of a line and can check whether a line is horizontal or vertical. This module can be used to check whether two lines intersect each other, parallel or perpendicular to each other, bisects each other or intersect at midpoint. This module created with the help of Point module*
   
   - **Multiarray** - *Module to create multi-dimensional array, array of any dimensions can be created using this module. Accessing and setting values can be done by passing tuple to getter and setter method like multiarray(2,2,2). This module was created with the help of Array1 module*
   
   - **Time** - *Module to handle operations on time*
   
   - **TimeDate** - *This module is like datetime module in python and it is a  combination of date and time module and can able to perform both operations that data and time module performs*
   
   - **Matrix** - *Module to perform matrix operations like transposing and scaling the matrix and adding, substracting, and multiplying two matrixes. This module created with the help of Array2D from Array1 module*
   
   - **range_iter** - *Like range function. Specify start and stop, it will iterate from start to stop, when used in for-in loop*
   
   - **Studentfile** - *This module was created to read a csv file, which has students records in it in csv format. This module has StudentFileReader and StudentFileWriter to read the file and write it to text file respectively. Supply the source file and you will get the result in desired format*
   
   - **Prime Number** - *This is helper function file for performing prime numbers operations and it is not a module. You can find list of prime numbers upto the given number, sum of prime numbers, largest prime factors etc... using this module*
   
   - **PrintCalendar** - *This is also a helper function, pass a date object and it will display the calendar of that month. This helper function created with the help of date1 module*
   
   - **Vector** - *This module is in progress, created to deal with vectors*
