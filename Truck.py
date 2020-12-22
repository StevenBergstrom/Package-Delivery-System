class Truck:
    def __init__(self):
        self.package_list = []
    #not sure why I wrote this yet?
    def add_packages(self, packages):
        for package in packages:
            self.package_list.append(packages)