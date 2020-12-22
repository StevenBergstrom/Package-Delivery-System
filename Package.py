class Package:
    def __init__(self, packageID, address, city, state, zip, deadline, mass, notes, status, deliveryTime):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status
        self.deliveryTime = deliveryTime