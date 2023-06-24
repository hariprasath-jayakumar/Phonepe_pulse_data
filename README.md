# phonepe_pulse_data_visualization
Interactive Dashboard of Phonepe Pulse data using StreamLit 

In this project, we are going to Clone Phonepe pulse data to the local directory, Then we are going to transfer the data to SQL. Finally, Using SQL & Streamlit we are going to create an interactive dashboard with basic insights about the data & basic information about the Phonepe organization.


## prerequisites

First, We need the below prerequisites to process further

1) Python
2) Git
3) Sql


## Cloning from Git Hub Repository 

#Specify the GitHub repository URL
response = requests.get('https://api.github.com/repos/PhonePe/pulse')

repo = response.json()

clone_url = repo['clone_url']

#Specify the local directory path
clone_dir = "E:/phonepe_pulse"

#Clone the repository to the specified local directory
subprocess.run(["git", "clone", clone_url,clone_dir], check=True)

## Usage

1. Run the Data_Data_Cloning_From_Git_toSQl.py script to retrieve, transform and store the data 

Data Cloning From Git to SQl.py

2. After Cloning & Storing the data to Sql, run the Phonepe_data_Visualization.py script to Visualize the data using STREAMLIT

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.
