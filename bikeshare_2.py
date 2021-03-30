import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february','march','april','may','june']

days = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']


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
        city = str(input('Enter in a city - chicago, new york city, or washington: ')).lower()
        if city in ['chicago','new york city','washington']:
            break
        else:
            print('Please enter either chicago, new york city, or washington as your city. ')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Enter in the full name of the month - all, january to june. ')).lower()
        if month == 'all' or month in months:
            break
        else:
            print('Please enter a valid month or all. ')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Enter the full name of a day in the week: ')).lower()
        if day == 'all' or day in days:
            break
        else:
            print('Please enter a valid day.')
        
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
       
    df = df.replace('', np.nan)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
   
    return df

def display_data(df):
    """ Asks the user for input on viewing the raw data.
    Returns:
        (DataFrame) df - Shows first 5 or more rows of data frame loaded in.
    """
    i = 0
    raw = str(input('Would you like to view the raw data? Y/N: ')).upper() 
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'N':
            break
        elif raw == 'Y':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = str(input('Would you like to view more raw data? Y/N: ')).upper()  # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'Y' or 'N'\n").upper()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day of the Week: ', popular_day)

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: ', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End'] = df['Start Station'] + ' to ' + df['End Station']
    popular_combo = df['Start and End'].mode()[0]
    print('The Most Common Combo of Stations is: ', popular_combo)
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('The Total Travel Duration is: ', total_trip_duration)

    # TO DO: display mean travel time
    mean_travel_duration = df['Trip Duration'].mean()
    print('The Average Travel Duration is: ', mean_travel_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print(genders)
    except KeyError:
        print('There is no gender associated data.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try: 
        earliest_birth = df['Birth Year'].min()
        print('The Earliest Birthday Year is: ', earliest_birth)
    
        most_recent_birth = df['Birth Year'].max()
        print('The Most Recent Birthday Year is: ', most_recent_birth)
    
        most_common_birth = df['Birth Year'].mode()[0]
        print('The Most Common Birth Year is: ', most_common_birth)
    
    except KeyError:
        print('There is no birth year associated with this data.')
        
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
       
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'yes':
                print("We'll explore the data once again.")
                break
            elif restart.lower() == 'no':
                break
            else:
                print('Your input is invalid. Please enter in yes or no.')
        
        if restart.lower() == 'no':
            break

if __name__ == "__main__":
	main()