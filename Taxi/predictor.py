from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas

with open('standard_scaler.kaviani', 'rb') as f:
    sc = pickle.load(f)

with open('random_forest_trained.kaviani', 'rb') as f:
    rf = pickle.load(f)

rate_code = input('Please Enter Rate Code:')
passenger_count = input('Please Enter Passanger Count:')
trip_time_in_secs = input('Please Enter Trip Time in Secs.:')
trip_distance = input('Please Enter Trip Distance:')
fare_amount = input('Please Enter Fare Amount:')
surcharge = input('Please Enter Surcharge:')
mta_tax = input('Please Enter MTA tax:')
tolls_amount = input('Please Enter Tolls Amount:')
total_amount = input('Please Enter Total Amount:')


x = [
    [rate_code, passenger_count, trip_time_in_secs, trip_distance, fare_amount, surcharge, mta_tax, tolls_amount, total_amount]
]

data_x_scaled = sc.transform(x)

result = rf.predict(data_x_scaled)[0]

if (result == 0):
    print('NO Tip')
else:
    print('Must Tip')