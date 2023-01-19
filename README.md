# Explore US Bikeshare Data
In this project, a mini-python is used to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. 
The program aims to provide an interactive statistical summary based on the input value, i.e., selected city, month, and day.

## Files
### 1- The Datasets.
<ui>
<li>chicago.csv</li>
<li>new_york_city.csv</li>
<li>washington.csv</li>
</ui>
<br>The datasets are found in a zip file. The datasets contains randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
<ui>
<li>Start Time (e.g., 2017-01-01 00:07:57)</li>
<li>End Time (e.g., 2017-01-01 00:20:53)</li>
<li>Trip Duration (in seconds - e.g., 776)</li>
<li>Start Station (e.g., Broadway & Barry Ave)</li>
<li>End Station (e.g., Sedgwick St & North Ave)</li>
<li>User Type (Subscriber or Customer)</li>
</ui>
</br>
The Chicago and New York City files also have the following two columns:
<ui>
<li>Gender</li>
<li>Birth Year</li>
</ui>

### 2- The bikeshare.py file.
The file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change!
<br><br>There are four questions that will change the answers:</br>
<ui>
<li>Would you like to see data for Chicago, New York, or Washington?</li>
<li>Would you like to filter the data by month [january, february, march, etc..], or not at all?</li>
<li>Would you like to filter the data by day [monday, tuesday, wednesday, etc..], or not at all?</li>
<ui>
</br>
The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

## Descriptive Statisics
The output will provide the following informtion.
### 1 Popular times of travel (i.e., occurs most often in the start time)
<ui>
<li>most common month</li>
<li>most common day of week</li>
<li>most common hour of day</li>
</ui>

### 2 Popular stations and trip
<ui>
<li>most common start station</li>
<li>most common end station</li>
<li>most common trip from start to end (i.e., most frequent combination of start station and end station)</li>
</ui>

### 3 Trip duration
<ui>
<li>total travel time</li>
<li>average travel time</li>
</ui>

### 4 User info
<ui>
<li>counts of each user type</li>
<li>counts of each gender (only available for NYC and Chicago)</li>
<li>earliest, most recent, most common year of birth (only available for NYC and Chicago)</li>
</ui>
<br></br>
<i>This was assignment 01 required for the Data Analysis Professional nanodegree from Udacity.</i>
