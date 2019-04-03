# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import datetime
import json
import csv
from pprint import pprint

# Import API key
from api_keys import api_key

file = open("weather_data.json")
json_data = json.load(file)
print(json.dumps(json_data, indent=4, sort_keys=True))