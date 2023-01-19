import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = str(input('Choose one of the following Cities [chicago, new york city, or washington] to explore: ').lower())
        except ValueError:
            print('Invalid entry .... Choose Again!')
            continue

        if city in CITY_DATA.keys():
            break 
        else: 
            print('Invalid entry .... Choose Again!')
            
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Select a month [january, february, march, etc...] or type all for data display:  ').lower())
        except ValueError:
            print('Invalid entry .... Choose Again!')
            continue
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december', 'all']
        if month in months:
            break
        else:
            print('Invalid entry .... Choose Again!')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Select a day [sunday, monday, tuesday, etc...] or type all for data display:  ').lower())
        except ValueError:
            print('Invalid entry .... Choose Again!')
            continue
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
        if day in days:
            break
        else:
            print('Invalid entry .... Choose Again!')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day of week 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most Common Month:')
    print(df['Start Time'].dt.month_name().mode(dropna=True).to_string())

    # display the most common day of week
    print('Most Common Day:')
    print(df['Start Time'].dt.day_name().mode(dropna=True).to_string())

    # display the most common start hour
    print('Most Common Hour-24h:')
    print(df['hour'].mode().to_string())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common Start Station is: ')
    print(df['Start Station'].mode(dropna=True).to_string())

    # display most commonly used end station
    print('While, the most common End Station is: ')
    print(df['End Station'].mode(dropna=True).to_string())

    # display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip: ')
    #df['Trip'] = df[['Start Station', 'End Station']].agg(' to '.join, axis=1)
    df['Trip'] = df['Start Station'] + df['End Station']
    print(df['Trip'].mode().to_string())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time:')
    df['Travel Time'] = (df['End Time'] - df['Start Time']).dt.total_seconds() / 60
    print(int(df['Travel Time'].sum()), 'mins i.e. ', int(df['Travel Time'].sum()/60), 'hours')


    # display mean travel time
    print('Average Travel Time:')
    print(float(df['Travel Time'].mean()), 'mins')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts(dropna=True).to_string())

    # Display counts of gender

    if 'Gender' in df.columns:
        print(df['Gender'].value_counts(dropna=True).to_string())
        print('Oldest User was born in:')
        print(int(df['Birth Year'].min()))

        print('Youngest User was born in:')
        print(int(df['Birth Year'].max()))

        print('While, Most Users were born in:')
        print(int(df['Birth Year'].mode(dropna=True)))
    else:
        print('Neither Gender nor Birth Year Data are Available for this City')


    # Display earliest, most recent, and most common year of birth
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
         while True:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            if view_data == 'yes':
                print(df.sample(5))
            else:
                break

        #  while True:
        #     view_data = input("Do you wish to continue?: ").lower()
        #     if view_data != 'yes':
        #         break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
