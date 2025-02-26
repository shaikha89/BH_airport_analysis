import requests 

response = requests.get("https://v2.jokeapi.dev/joke/Any")
response.json()

def collect_flight_data(day, flight_direction):
    '''
    This function scrapes the data fom BH airportand return it as a table
    Args:
        day (str): it will be today(TD) or tomorrow (TM).
        flight_direction (str): It will be 'arrivals' or 'departures'.
    Returns:
        Pandas DataFrame that have 7 columns
    '''
    url = f"https://www.bahrainairport.bh/flight-{flight_direction}?date={day}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    time_lst = []
    destination_lst = []
    airways_lst = []
    gate_lst = []
    status_lst = []
    flight_lst = []
    flights = soup.find_all('div', {'class': f'flight-table-list row dv{flight_direction[:-1].title()}List'})
    for flight in flights:
        time = flight.find('div', class_ = 'col col-flight-time').text.strip() # it does the samething but this is better
        time_lst.append(time)
        destination = flight.find('div', class_ = 'col col-flight-origin').text.strip()
        destination_lst.append(destination)
        flight_no = flight.find('div', class_ = 'col col-flight-no').text.strip()
        flight_lst.append(flight_no)
        gate = flight.find('div', class_ = 'col col-gate').text.strip()
        gate_lst.append(gate)
        status = flight.find('div', class_ = 'col col-flight-status').text.strip()
        status_lst.append(status)
        try:
            airways = flight.find('img')['alt'] # We have only one image per div so we don't need to specify the name.
            airways_lst.append(airways)
        except:
            airways_lst.append(pd.NA)
        flights_data = {
        'destination':destination_lst,
        'flight_number':flight_lst,
        'airline':airways_lst,
        'gate':gate_lst,
        'status':status_lst,
        'time':time_lst}
        df = pd.DataFrame(flights_data)
        if day == 'TD':
            date=Today_date
        elif day == 'TM':
            date=Tomorrow_date + datetime.timedelta(days=1)
        df['date'] = date
        df['direction'] = flight_direction
        return df
        df_arr=collect_flight_data('TM', 'arrivals')
df_arr


import time
def collect_arr_dep():
    tables=[]
    directions= ['arrivals','departures']
    day=['TD','TM']
    for direction in directions:
        for day in day:
            #df= collect_flight_date(day,direction)
            tables.append(ollect_flight_date(day,direction))
            time.sleep(10) # to slow down
    df=pd.concat(tables)
    return df
df = collect_arr_dep
df




