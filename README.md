# Problem Solve in TDD Approach

Here a program is built to retrieve day by day temperatures of a city in a predefined set in a given range of time.
The problem definition and solution approach can be found [here](./stories.txt) in details.

## Setup 
Create a virtual env and install the required dependencies
```
python -m venv tdd-weather-api-env
pip install -r requirements.txt
``` 
Folder Structure
```
/app
    - Class Defintion for Service
/tests
    - Test Cases for the app Services
requirements.txt
    - package dependencies
stories.txt
    - problem definition
config.ini
    - configurations
```

The Visual Crossing [Weather API](https://www.visualcrossing.com/weather-api) has been used for getting daily temperature data for specific cities[Dhaka, Paris, New York, Sydney, Singapore].

## 

### Run the Program

Run the program by using following command

```
python run.py
```

### Test the Program

To perform unittest, run the following command from the root folder

```
python -m unittest -v
```

## Reference

1. [Visual Crossing Weather API](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/)