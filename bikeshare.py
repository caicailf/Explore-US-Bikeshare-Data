import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Would you like to see data for Chicago, NewYork, or Washington?').lower()
            if city == 'chicago' or city == 'newyork' or city == 'washington':
                break
            else:
                print('Please input the right city name.')

        except:
            print('Please input the right city name.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Which month? January, February, March, April, May, or June?').lower()
            if month == 'all' or month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                break
            else:
                print('Please input the right month.')

        except:
            print('Please input the right month.')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
             day = input('Which day? monday, tuesday, wednesday, thursday, friday, saturday, sunday.').lower()
             if day == 'all' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday':
                 break
             else:
                 print('Please input the right day.')
        except:
             print('Please input the right day.')

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday_name
    common_day = df['weekday'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(("Most popular month : {}\nMost popular weekday :{}\nMost popupar hour :{}").format(common_month,common_day,popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print(("Most commondly start station is : {}\nMost commondly end station is : {}\nMost frequent trip is : {}").format(commonly_start_station,commonly_end_station,most_frequent_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(("Total duration : {}\nAvg duration : {}").format(total_travel_time,mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    common_birth_year = int(df['Birth Year'].mode()[0])

    sorted_column = df['Birth Year'].sort_values(ascending = False)
    recent_year = sorted_column.iloc[0]

    sorted_column = df['Birth Year'].sort_values(ascending = True)
    earliest_year = sorted_column.iloc[0]

    print(("User type : {}\nGender type : {}\nEarliest birth year : {}\nMost recent year : {}\nMost common year: {}").format(user_types,gender_types,earliest_year,recent_year,common_birth_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            break
        except:
            print('Washington is not have a column named gender or birthyear')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
