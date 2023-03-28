import csv  
import requests  
import os    
 
def call_api_and_write_to_csv():  
    # Make API request  
    response = requests.get("http://localhost:8000/predict")  
    if response.status_code != 200:  
        raise Exception("Failed to call API")  
    data = response.json()  
  
    # Write data to CSV file  
    filename = "predictions.csv"  
    file_exists = os.path.isfile(filename)  
    with open(filename, mode="a", newline="") as file:  
        writer = csv.writer(file)  
        if not file_exists:  
            writer.writerow([  
                "Symbol",  
                "Interval",  
                "Actual Time",  
                "Actual Price",  
                "Next Hour",  
                "Predicted Close Price",  
                "Decision",  
            ])  
        writer.writerow([  
            data["symbol"],  
            data["interval"],  
            data["actual_time"],  
            data["actual_price"],  
            data["next_hour"],  
            data["predicted_close_price"],  
            data["decision"],  
        ])
  
    print('API call successful')  