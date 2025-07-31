import datetime

def generate_daily_partitions(start_date, end_date, filename):
    current_date = start_date
    with open(filename, 'w') as f:
        while current_date <= end_date:
            # Format the date and write to file
            date_str = current_date.strftime("'%Y-%m-%d',")
            
            # Add newline every 10 dates for readability
            if current_date.day == 1 and current_date != start_date:
                f.write('\n')
            elif (current_date - start_date).days % 10 == 0:
                f.write('\n    ')
            
            f.write(f' {date_str}')
            current_date += datetime.timedelta(days=1)

# Define date range
start_date = datetime.date(2024, 11, 1)
end_date = datetime.date(2050, 12, 31)

# Generate and save the partitions
generate_daily_partitions(start_date, end_date, 'daily_partitions.txt')

print(f"Daily partitions from {start_date} to {end_date} have been saved to daily_partitions.txt")