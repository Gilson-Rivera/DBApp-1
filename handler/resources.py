# resources handler

from flask import jsonify
from dao.resources import ResourcesDAO


class ResourcesHandler:
    def build_resources_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
	result['rprice'] = row[4]
	result['rsupplier'] = row[5]
	result['rlocation'] = row[6]
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()
        return jsonify(Resources=resources_list)

    def getResourcesById(self, rid):
        dao = ResourcesDAO()
        result = dao.getResourcesById(rid)
        return jsonify(Resources=result)

    def getResourcesByType(self, rtype):
	dao = ResourcesDAO()
	resources_list = dao.getResourcesByType(rtype)
	return jsonify(Resources=resources_list)

    def getResourcesByBrand(self, rbrand):
	dao = ResourcesDAO()
	resources_list = dao.getResourcesByBrand(rbrand)
	return jsonify(Resources=resources_list)

    def getResourcesByNumAvailable(self, rnumavailable):
	dao = ResourcesDAO()
	resources_list = dao.getResourcesByNumAvailable(rnumavailable)
	return jsonify(Resources=resources_list)

    def getResourcesByPrice(self, rprice):
	dao = ResourcesDAO()
	resources_list = dao.getResourcesByPrice(rprice)
	return jsonify(Resources=resources_list)

    def getResourcesBySupplier(self, rsupplier):
	dao = ResourcesDAO()
	resources_list = dao.getResourcesBySupplier(rsupplier)
	return jsoninfy(Resources=resources_list)

    def getResourcesByLocation(self, rlocation):
	dao = ResourcesDAO()
	resources_list = dao.getResourcesByLocation(rlocation)
	return jsonify(Resources=resources_list)


    def insertSupplierJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
	rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation:
            dao = ResourcesDAO()
            result = dao.insert(rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation $
            return jsonify(Resources=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

