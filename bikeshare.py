import time

import numpy as np
import pandas as pd

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
    city = input('Please choose a city: chicago, new york city, washington:  ').lower().strip()
    while city.lower().strip() not in CITY_DATA.keys() :
        city = input('please enter correct city: ') 
        
        
          
          

    # get user input for month (all, january, february, ... , june)
    month = input('please choose a month: all, january, february, ..., june: ' )
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while month.strip().lower() not in months:
          month = input('please enter valid month: ')
          

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('please choose a day of week (all, monday, tuesday, ... sunday): ')).title()
    days = ['all','sunday', 'monday' , 'tuesday', 'wednsday', 'thursday', 'friday']
    while day.strip().lower() not in days: 
        day= input('please enter correct day: ')
        



    print('-'*40)
    return city.strip().lower(), month.strip().lower(), day.strip().lower()


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
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    print(df.head())
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    print(df.head())
    return df


    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mc_month = df['month'].value_counts().idxmax()     
    print('The most common month is: ', mc_month)

    # display the most common day of week
    print('The most common day of the week is: ', df['day_of_week'].value_counts().idxmax())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
 
    print('The most common start hour is: ', df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is: ', df['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print('The most common end station is: ', df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    df['start and end'] =  df['Start Station']+ ' '+ df['End Station']
    mc_combine = df['start and end'].mode()[0]
    print('The most frequent combination of start station and end station trip: ',mc_combine)
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_time)

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('The user types count is: ' , user_types_count)
    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('The gender count is: ', gender_count)
    except:
        print('There is no gender count in this city')
      

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        mc_year = df['Birth Year'].value_counts().idxmax()
        print(f'The earliest year of birth is {earliest_year}\n The most recent year of birth is {recent_year}\n The most common year of birth is {mc_year}')
    except:
        print('There is no birth year in this data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def display_data(df):
     # ''' display the 5 lines of raw data for city if answer is yes '''


   
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ").lower().strip()
    start_loc = 0
    while True:
       
       if view_data == 'yes':       
          print(df[start_loc:start_loc+5])
          start_loc += 5
          view_display = input("Do you wish to continue?: ").lower()
          if view_display == 'yes':
                continue
          elif view_display == 'no':
            break
          while view_display!= 'yes' and view_display!='no':
               view_display = input('please choose yes or no: ')
               if view_display =='no':
                  break 
               if view_display == 'yes':
                print(view_data)
    
              
               
       elif view_data == 'no':
           break
            
       else:
           print('please choose yes or no') 
            
            
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
