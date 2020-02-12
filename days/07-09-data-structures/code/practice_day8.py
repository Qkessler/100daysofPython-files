

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeeps = cars['Jeep']
    str_jeeps = ""
    for jeep in jeeps:
        if jeep == jeeps[-1]:
            str_jeeps += jeep
        else:
            str_jeeps += jeep + ", "
    return str_jeeps


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_model = []
    for brand in cars.keys():
        first_model.append(cars[brand][0])
    return first_model


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    models_with_grep = []
    for brand in cars.keys():
        for car in cars[brand]:
            if grep.lower() in car.lower():
                models_with_grep.append(car)
    return sorted(models_with_grep)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    cars_copy = {}
    for brand, cars_array in cars.items():
        cars_copy[brand] = sorted(cars_array)
    return cars_copy


print(get_all_jeeps())
print(get_first_model_each_manufacturer())
print(get_all_matching_models())
print(sort_car_models())
