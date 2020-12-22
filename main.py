'''
Steven
Bergstrom
001231776
'''

import csv
import datetime
import Package
import HashMap
import Truck

#This section creates a blank list and takes the data from the csv file and creates instance of the packages which are put into the package list O(N)
packageList = []
with open('PackageSheet.csv', newline='') as csvfile:
    DataReader = csv.reader(csvfile)
    for row in DataReader:
        packageList.append(Package.Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 'At Hub', ''))



#This section creates a Hash table that is populated using the package ID as the key and the package itself as the value O(N)
hashTable = HashMap.HashMap()
for package in packageList:
    hashTable.add(int(package.packageID), package)

#This is a dictionary of locations for reference O(1)
locations = {
    '4001 South 700 East': 0,
    '1060 Dalton Ave S': 1,
    '1330 2100 S': 2,
    '1488 4800 S': 3,
    '177 W Price Ave': 4,
    '195 W Oakland Ave': 5,
    '2010 W 500 S': 6,
    '2300 Parkway Blvd': 7,
    '233 Canyon Rd': 8,
    '2530 S 500 E': 9,
    '2600 Taylorsville Blvd': 10,
    '2835 Main St': 11,
    '300 State St': 12,
    '3060 Lester St': 13,
    '3148 S 1100 W': 14,
    '3365 S 900 W': 15,
    '3575 W Valley Central Station bus Loop': 16,
    '3595 Main St': 17,
    '380 W 2880 S': 18,
    '410 S State St': 19,
    '4300 S 1300 E': 20,
    '4580 S 2300 E': 21,
    '5025 State St': 22,
    '5100 South 2700 West': 23,
    '5383 South 900 East #104': 24,
    '600 E 900 South': 25,
    '6351 South 900 East': 26
}

#Creates a 2D matrix of the values in the Distance csv for the edges between nodes O(N)
edges = []
with open('DistanceSheet.csv', newline='') as csvfile:
    DataReader = csv.reader(csvfile)
    for row in DataReader:
        edges.append(row)

#This is a function to search and return the distance between any 2 given nodes O(1)
def search_distance(u, v):
    return float(edges[u][v])

#This creates the trucks and then they are manually loaded from a list made from given constraints O(1)
truck1 = Truck.Truck()
truck2 = Truck.Truck()
truck3 = Truck.Truck()

#load truck 1 O(N)
truck1list = [14, 15, 16, 34, 13, 39, 19, 20, 21, 27, 35, 7, 29, 2, 33, 1]

for package in truck1list:
    truck1.package_list.append(hashTable.get(package))
    hashTable.get(package).status = 'On Truck 1'


#load truck 2 O(N)
truck2list = [31, 32, 25, 26, 28, 6, 18, 36, 3, 5, 4, 37, 38, 40, 30, 11]

for package in truck2list:
    truck2.package_list.append(hashTable.get(package))
    hashTable.get(package).status = 'On Truck 2'


#load truck 3 O(N)
truck3list = [9, 8, 17, 12, 24, 23, 10, 22]

for package in truck3list:
    truck3.package_list.append(hashTable.get(package))
    hashTable.get(package).status = 'On Truck 3'

#Sets start times for each truck
truck1starttime = datetime.datetime(2020, 1, 1, 8, 00, 00)
truck2starttime = datetime.datetime(2020, 1, 1, 9, 5, 00)
truck3starttime = datetime.datetime(2020, 1, 1, 10, 20, 00)

#Creates a distance variable and a current location variable
distance = 0.0
currentLocation = '4001 South 700 East'

#Sets time to be added to package for timestamp
time = 0

'''Main algorithm that iterates through truck list and then iterates through comparing current location to current index.
Then when closest node is found it travels to and delivers that package.
Also it increments delivery distance and updates the status of the package.
It does this for each truck.
The time complexity for the algorithm is O(N Squared)
The space complexity is also O(N Squared)
'''
while len(truck1.package_list) != 0:
    min = 20.0
    for index, item in enumerate(truck1.package_list):
        if search_distance(locations[currentLocation], locations[item.address]) <= min:
            min = search_distance(locations[currentLocation], locations[item.address])
            minIndex = index
    distance += min
    time += min/.3
    truck1.package_list[minIndex].deliveryTime = truck1starttime + datetime.timedelta(0, 0, 0, 0, time)
    currentLocation = truck1.package_list[minIndex].address
    truck1.package_list[minIndex].status = 'Delivered'
    print('Package', truck1.package_list[minIndex].packageID, truck1.package_list[minIndex].status, 'at', truck1.package_list[minIndex].deliveryTime.time())
    truck1.package_list.pop(minIndex)

#Resets time to be added to package for timestamp
time = 0

while len(truck2.package_list) != 0:
    min = 20.0
    for index, item in enumerate(truck2.package_list):
        if search_distance(locations[currentLocation], locations[item.address]) <= min:
            min = search_distance(locations[currentLocation], locations[item.address])
            minIndex = index
    distance += min
    time += min/ .3
    truck2.package_list[minIndex].deliveryTime = truck2starttime + datetime.timedelta(0, 0, 0, 0, time)
    currentLocation = truck2.package_list[minIndex].address
    truck2.package_list[minIndex].status = 'Delivered'
    print('Package', truck2.package_list[minIndex].packageID, truck2.package_list[minIndex].status, 'at', truck2.package_list[minIndex].deliveryTime.time())
    truck2.package_list.pop(minIndex)

#Resets time to be added to package for timestamp
time = 0

while len(truck3.package_list) != 0:
    min = 20.0
    for index, item in enumerate(truck3.package_list):
        if search_distance(locations[currentLocation], locations[item.address]) <= min:
            min = search_distance(locations[currentLocation], locations[item.address])
            minIndex = index
    distance += min
    time += min/ .3
    truck3.package_list[minIndex].deliveryTime = truck3starttime + datetime.timedelta(0, 0, 0, 0, time)
    currentLocation = truck3.package_list[minIndex].address
    truck3.package_list[minIndex].status = 'Delivered'
    print('Package', truck3.package_list[minIndex].packageID, truck3.package_list[minIndex].status, 'at', truck3.package_list[minIndex].deliveryTime.time())
    truck3.package_list.pop(minIndex)

print('Total distance is ', distance)

#This prompts the user to input a time to see the status of all packages based on user input O(N)
time_value = input('Please select a time to check status of package \n Enter as ex. 8:00AM \n')
datetime_object = datetime.datetime.strptime('Jan 1 2020 ' + time_value, '%b %d %Y %I:%M%p')
for package in packageList:
    if datetime_object > package.deliveryTime:
        print(package.packageID, '|', package.address, '|', package.deadline, '|', package.status, '|', package.deliveryTime)
    else:
        print(package.packageID, '|', package.address, '|', package.deadline, '|', 'Not Delivered', '|', 'N/A')

















