# **REQUIRED DEPENDENCIES**

Flask == 0.12.2

Python == 2.7.6

Python == 3.4.3 

SQLite == 3.8.2 

beautifulsoup4

# **DIRECTORY STRUCTURE**



## bmtc->FlaskApp->templates
                             ->index.html

                             ->app.py
                             
                             ->bmtc.db
                             
      ->route.py
      
      ->fare.py
      
      ->route_db.py
      
      ->fare_db.py
      
      ->route.pdf
      
      ->fare.pdf
      
      ->bmtc.db
      
      ->bmtc_fare_scrap_Nov_09_2017.json
      
      ->bmtc_route_scrap_Nov_09_2017.json
   
# **BUILD INSTRUCTIONS**

1. To fetch, parse the bus stops and timings, and store them in json file and database, run route.py using **python3 route.py** [input example: bus_id could be: 312, 314, etc, and route_id could be 3E, 3F,3B, etc]
2. To fetch, parse the fares list, and store them in json file and database, run fare.py using **python3 fare.py**
[valid input types are: A/C and General]
3. To fetch the data from database, run route_db.py and fare_db.py, using **python3 route_db.py** and **python3 fare_db.py**, respectively.
4. To represent the data on the webpage, run app.py after setting up the dependencies.


    
    
