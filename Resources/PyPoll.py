import csv 
import os 
file_to_load = os.path.join("election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)
file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")