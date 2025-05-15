def add_time(start, duration, starting_day=None):
    # Days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse start time into time part and meridiem (AM/PM)
    time_part, meridiem = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert start hour to 24-hour format for easier calculations
    if meridiem == "PM" and start_hour != 12:
        start_hour += 12  # Convert PM hours to 24-hour format
    if meridiem == "AM" and start_hour == 12:
        start_hour = 0  # Handle midnight (12 AM) as 0 in 24-hour format

    # Parse duration into hours and minutes
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Add duration minutes to start minutes
    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60  # Calculate extra hours from minutes overflow
    final_minutes = total_minutes % 60  # Remaining minutes after overflow

    # Add duration hours and extra hours to start hours
    total_hours = start_hour + dur_hour + extra_hour
    days_later = total_hours // 24  # Calculate how many days later
    final_hour_24 = total_hours % 24  # Remaining hours in 24-hour format

    # Convert final hour back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12  # Handle midnight as 12 AM
        final_meridiem = "AM"
    elif final_hour_24 < 12:
        final_hour = final_hour_24  # Morning hours remain the same
        final_meridiem = "AM"
    elif final_hour_24 == 12:
        final_hour = 12  # Handle noon as 12 PM
        final_meridiem = "PM"
    else:
        final_hour = final_hour_24 - 12  # Convert afternoon hours to 12-hour format
        final_meridiem = "PM"

    # Format the new time as a string
    new_time = f"{final_hour}:{final_minutes:02d} {final_meridiem}"

    # Add the day of the week if starting_day is provided
    if starting_day:
        index = days_of_week.index(starting_day.capitalize())  # Find the index of the starting day
        new_day_index = (index + days_later) % 7  # Calculate the new day index
        new_day = days_of_week[new_day_index]  # Get the new day name
        new_time += f", {new_day}"

    # Add information about the number of days later
    if days_later == 1:
        new_time += " (next day)"  # Add "next day" if it's one day later
    elif days_later > 1:
        new_time += f" ({days_later} days later)"  # Add "(n days later)" for multiple days

    return new_time  # Return the formatted new time



add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
