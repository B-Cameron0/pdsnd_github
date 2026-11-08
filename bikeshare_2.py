# the following function utilizes pandas and numpy to help guide users in identifyin bike share statistics for three cities, Chicao, New York, and Washington:

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Global mappings to replace manual index tracking
MONTH_MAP = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
VALID_DAYS = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}

def get_user_choice(prompt, valid_options):
    """Generic helper to handle validated user input without duplicating while-loops."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options: 
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

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
    city = get_user_choice(
         "Please enter your desired city (options currently include chicago, new york city, and washington): ",
         CITY_DATA.keys()  
    )

    # get user input for month (all, january, february, ... , june)
    month = get_user_choice(
         "Please enter month (all, january, february, ... , june): ",
         ['all'] + list(MONTH_MAP.keys())
    )

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_user_choice(
        "Please enter your desired day of the week, or 'all': ",
        ['all'] + list(VALID_DAYS)
    )

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

# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the start time column to datetime 
    start_time = pd.to_datetime(df['Start Time'])
    
    # Extract month and day of week from start time to create new columns
    df['month'] = start_time.dt.month
    df['day_of_week'] = start_time.dt.day_name().str.lower() # Standardize to lowercase matching our filters
    
    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == MONTH_MAP[month]]
     
     # Filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe 
        df = df[df['day_of_week'] == day]

    return df

#     return df


# #def time_stats(df):
#     """Displays statistics on the most frequent times of travel."""

#     print('\nCalculating The Most Frequent Times of Travel...\n')
#     start_time = time.time()

#     # display the most common month


#     # display the most common day of week


#     # display the most common start hour


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# def station_stats(df):
#     """Displays statistics on the most popular stations and trip."""

#     print('\nCalculating The Most Popular Stations and Trip...\n')
#     start_time = time.time()

#     # display most commonly used start station


#     # display most commonly used end station


#     # display most frequent combination of start station and end station trip


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# #def trip_duration_stats(df):
#     """Displays statistics on the total and average trip duration."""

#     print('\nCalculating Trip Duration...\n')
#     start_time = time.time()

#     # display total travel time


#     # display mean travel time


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# #def user_stats(df):
#     """Displays statistics on bikeshare users."""

#     print('\nCalculating User Stats...\n')
#     start_time = time.time()

#     # Display counts of user types


#     # Display counts of gender


#     # Display earliest, most recent, and most common year of birth


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# #def main():
#     while True:
#         city, month, day = get_filters()
#         df = load_data(city, month, day)

#         time_stats(df)
#         station_stats(df)
#         trip_duration_stats(df)
#         user_stats(df)

#         restart = input('\nWould you like to restart? Enter yes or no.\n')
#         if restart.lower() != 'yes':
#             break


# if __name__ == "__main__":
# 	main()
