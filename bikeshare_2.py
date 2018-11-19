import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    city = input(
        'Please type in one of these cities you\'d like to investigate: chicago, new york city or washington : ').lower()
    cities = ['chicago', 'new york city', 'washington']
    while city not in cities:
        print('Ups. There must be something wrong. \n You can only choose between the given three cities.')
        city = input('Please type in one of these cities: chicago, new york city or washington : ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(
        'Please type in a month you\'d like to investigate. If you\'d like to choose all, type in all : ').lower()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        print('Ups. There must be something wrong.')
        month = input(
            'Please type in a month you\'d like to investigate. If you\'d like to choose all, type in all : ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        'Please type in a day of week you\'d like to explore. If you\'d like to choose all, type in all : ').lower()
    days = ['all', 'monday', 'tuesday', 'wendsday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
        print('Ups. There must be something wrong.')
        day = input(
            'Please type in a day of week you\'d like to explore. If you\'d like to choose all, type in all : ').lower()
    print('-' * 40)

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
    df = pd.read_csv(CITY_DATA[city]).dropna()
    df = df.sort_values(['Start Time'])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def test_empty_df(df):
    """Tests if data exists for the combination of city, month and day."""
    if df.empty:
        print('Your selected combination of city, month and day dos not contain information. Try another combination.')
        main()
        sys.exit()

def raw_data_display(df):
    """Displays raw data on users request."""
    print('\nDisplaying raw data on request...\n')
    start_time = time.time()

    user_request = input('Do you like to see raw data? Enter yes or no: ').lower()
    count = 5
    while user_request == 'yes':
        try:
            print(df.head(count))
            user_request = input('Do you like to see 5 more rows? Enter yes or no: ').lower()
            count += 5
        except:
            print('You can not see 5 more rows.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = np.bincount(df['month']).argmax()
    month_num_to_name = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'Mai', 6: 'June'}
    print('Most Frequent Month:', month_num_to_name[popular_month])
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].value_counts().index[0]
    print('Most Frequent Day of Week:', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = np.bincount(df['hour']).argmax()
    print('Most Frequent Start Hour:', popular_hour, 'o\'clock')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used Start Station was:', df['Start Station'].value_counts().index[0])

    # TO DO: display most commonly used end station
    print('The most commonly used End Station was:', df['End Station'].value_counts().index[0])

    # TO DO: display most frequent combination of start station and end station trip
    # source https: // knowledge.udacity.com / questions / 2042
    df['Start End Combi'] = df['Start Station'].map(str) + '&' + df['End Station']
    most_frequent_start_end_combi = df['Start End Combi'].value_counts().idxmax()
    print('The most frequent combination of start and end station was: ', most_frequent_start_end_combi)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays s    print("\nThis took %s seconds." % (time.time() - start_time))
tatistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration'] = df['Trip Duration']
    print('The total travel time was:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The mean trip duration was:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # to_frame inspiration https://stackoverflow.com/questions/35523635/extract-values-in-pandas-value-counts
    print(df['User Type'].value_counts().to_frame(), '\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = pd.Series(df['Gender'].value_counts())
        print('{} of the participants were male and {} were female.'.format(gender[0], gender[1]), '\n')
    else:
        print('No statistics about the gender are available for the chosen city.')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        # Idea to solve different year format: https://stackoverflow.com/questions/45531489/converting-different-date-time-formats-to-mm-dd-yyyy-format-in-pandas-dataframe
        # df['Birth Year'] = df['Birth Year'].dropna()
        df['Birth Year'] = df['Birth Year'].apply(lambda x: str(int(x)))
        df['Birth Year'] = df['Birth Year'].apply(lambda x: pd.to_datetime(x).year)
        print('The most common year of birth was:', df['Birth Year'].value_counts().index[0],"\n",
        'The most recent year of birth was:',
        df['Birth Year'].sort_values().iloc[0],"\n",
        'The earliest year of birth was:',
        df['Birth Year'].sort_values().iloc[-1])

    else:
        print('No statistics about the birth year are available for the chosen city.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        test_empty_df(df)
        raw_data_display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
