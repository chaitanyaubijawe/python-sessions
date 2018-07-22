Maharashtra_State_Name = "MAH"
Up_State_Name = "UP"
California_State_Name = "CAL"
Nevada_State_Name = "NEV"

Mah_list=["Bombay","Pune","Nagpur","Nashik"]
Up_list=["Lucknow","Noida"]
California_list=["San Francisco","Los Angeles"]
Nevada_list=["Las Vegas","Desert"]

def get_cities_by_states(state = None):
	if state is not None:
		if state == Maharashtra_State_Name:
			return Mah_list
		elif state == Up_State_Name:
		    return Up_list
		elif state == California_State_Name:
		    return California_list
		elif state == Nevada_State_Name:
			return Nevada_list
	else:
		return Mah_list

def get_map_for_countries(country = None):
    if country is not None:
        if country == "Ind":
            return {Maharashtra_State_Name:get_cities_by_states(Maharashtra_State_Name),Up_State_Name:get_cities_by_states(Up_State_Name)}
        elif country == "USA":
            return {California_State_Name:get_cities_by_states(California_State_Name),Nevada_State_Name:get_cities_by_states(Nevada_State_Name)}
    else:
        return "Not Valid Country"

def world_map():
	world_map = {}
	map_ind = get_map_for_countries("Ind")
	map_USA = get_map_for_countries("USA")
	world_map["INDIA"] = map_ind
	world_map["USA"] = map_USA
	return world_map


def print_world_map():
	for country,state in world_map().items():
		print("Country is ",country)
		for state,city in state.items():
			print("\t State is", state)
			for index,cities in enumerate(city):
				if index <2:
						print("\t\t",cities)
	return
print(print_world_map())

print("hello")