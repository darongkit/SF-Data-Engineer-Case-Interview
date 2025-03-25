import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_covid_data(start_date, end_date):
    covid_data = []

    # Lop over range of date 
    current_date = start_date

    while (current_date <= end_date):
        formatted_date = current_date.strftime('%Y-%m-%d')

        # API URL
        url = "https://covid-api.com/api/reports/total"
        
        # Parameters for the API request
        params = {
            "date": formatted_date,
            "iso": "SGP"
        }
        
        # Make the request to the API
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json().get("data", {})
            confirmed = data.get("confirmed", "0")
            covid_data.append({"date": formatted_date, "confirmed": confirmed})
            print(formatted_date, confirmed)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

        current_date += relativedelta(months=1)

    return covid_data


start_date = datetime(2020, 2, 1)
end_date = datetime(2023, 3, 1)

data = get_covid_data(start_date, end_date)

# for entry in data:
#     print(entry)


# import plot lib
import matplotlib.pyplot as plt

# extract X and Y
dates = [entry["date"] for entry in data]
values = [entry["confirmed"] for entry in data]

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(dates, values, marker='o', color='r', linestyle='-', label="Confirmed Cases")

# Customizing the plot
plt.title('Confirmed Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45, ha='right')  # Rotate the date labels for better readability
plt.ylim(0, 3000000)
plt.ticklabel_format(style="plain", axis="y")
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.legend()
plt.show()