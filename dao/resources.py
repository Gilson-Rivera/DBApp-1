# DAO Resources

from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:

    def getAllResources(self):
        result = "This is a list of resources"
        return result

    def getResourcesById(self, rid):
            result = "This is the resource with given id"
            return result

    def getResourcesByType(self, rtype):
        result = "List of resources of a specific type"
        return result

    def getResourcesByBrand(self, rbrand):
        result = "List of resources of a specific brand"
        return result

    def getResourcesByNumAvailable(self, rnumavailable):
        result = "Number of available resources"
        return result

    def getResourcesByPrice(self, rprice):
        result = "List of resources of specified price"
        return result

    def getResourcesBySupplier(self, rsupplier):
        result = "List of resources of a specific supplier"
        return result

    def getResourcesByLocation(self, rlocation):
        result = "List of locations for a specific resource"
        return result

    def insert(self, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation):
        result = "Supplier inserted"
        return result

