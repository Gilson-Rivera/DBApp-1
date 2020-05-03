# resources handler

from flask import jsonify
from dao.resources import ResourcesDAO
from dao.resources import FoodDAO
from dao.resources import EquipmentDAO
from dao.resources import MedDevDAO
from dao.resources import MedDAO
from dao.resources import FuelDAO
from dao.resources import ClothingDAO
from dao.resources import WaterDAO

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
        return jsonify(Resources=resources_list)

    def getResourcesByLocation(self, rlocation):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByLocation(rlocation)
        return jsonify(Resources=resources_list)

class FoodHandler(ResourcesHandler):
    def build_Food_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['fid'] = row[7]
        result['fname'] = row[8]
        result['fexpdate'] = row[9]


    def build_Food_attr(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, fid, fname, fexpdate):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        result['fid'] = fid
        result['fname'] = fname
        result['fexpdate'] = fexpdate
        return result

    def getAllFood(self):
        dao = FoodDAO()
        Food_list = dao.getAllFood()
        return jsonify(Food=Food_list)

    def getFoodByID(self, fid):
        dao = FoodDAO()
        result = dao.getFoodByID(fid)
        # if not row:
        #     return jsonify(Error = "Food Not Found"), 404
        # else:
        #     Food = self.build_Food_dict(row)
        return jsonify(Food = result)


    def searchFood(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = FoodDAO()
                Food_list = dao.getFoodByLocation(location)
                # result_list = []
                # for row in Food_list:
                #     result = self.build_Food_dict(row)
                #     result_list.append(row)
                return jsonify(Food=Food_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertFood(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            fname = form['fname']
            fbrand = form['fbrand']
            fexpdate = form['fexpdate']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if fname and fsupplier and fquantity and flocation:
                dao = FoodDAO()
                fid = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                result = self.build_Food_attr(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                return jsonify(Food=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertFoodJson(self, json):
        fname = json['fname']
        fexpdate = json['fexpdate']
        fsupplier = json['fsupplier']
        fbrand = json['fbrand']
        fquantity = json['fquantity']
        flocation = json['flocation']
        if fname and fexpdate and fsupplier and fquantity and flocation:
            dao = FoodDAO()
            result = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
            return jsonify(Food=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteFood(self, fid):
        dao = FoodDAO()
        # if not dao.getFoodByID(fid):
        #     return jsonify(Error = "Food not found."), 404
        # else:
        result =  dao.delete(fid)
        return jsonify(DeleteStatus = result), 200

    def updateFood(self, fid, form):
        dao = FoodDAO()
        if not dao.getFoodByID(fid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getFoodByID(fid)), 201



    def insertSupplierJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation:
            dao = ResourcesDAO()
            result = dao.insert(rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation)
            return jsonify(Resources=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


class FuelHandler(ResourcesHandler):
    def build_fuel_dict(self, row):
        result = {}
        result['fuid'] = row[0]
        result['ftype'] = row[1]
        result['fsupplier'] = row[2]
        result['fquantity'] = row[3]
        result['flocation'] = row[4]

    def build_fuel_attr(self, fuid, ftype, fsupplier, fquantity, flocation):
        result = {}
        result['fuid'] = fuid
        result['ftype'] = ftype
        result['fsupplier'] = fsupplier
        result['fquantity'] = fquantity
        result['flocation'] = flocation
        return result

    def getAllFuel(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        return jsonify(Fuel=fuel_list)

    def getFuelByID(self, fuid):
        dao = FuelDAO()
        result = dao.getFuelByID()
        return jsonify(Fuel=result)

    def searchFuel(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = FuelDAO()
                fuel_list = dao.getFuelByLocation()
                # result_list = []
                # for row in fuel_list:
                #     result = self.build_fuel_dict(row)
                #     result_list.append(row)
                return jsonify(Fuel=fuel_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertFuel(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            # remove fuid later
            # fuid = form['fuid']
            ftype = form['ftype']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if ftype and fsupplier and fquantity and flocation:
                dao = FuelDAO
                fuid = dao.insert(ftype, fsupplier, fquantity, flocation)
                result = self.build_fuel_attr(fuid, ftype, fsupplier, fquantity, flocation)
                return jsonify(Fuel=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertFuelJson(self, json):
        ftype = json['ftype']
        fsupplier = json['fsupplier']
        fquantity = json['fquantity']
        flocation = json['flocation']
        if ftype and fsupplier and fquantity and flocation:
            dao = FuelDAO()
            result = dao.insert(ftype, fsupplier, fquantity, flocation)
            return jsonify(Fuel=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteFuel(self, fuid):
        dao = FuelDAO()
        if not dao.getFuelByID(fuid):
            return jsonify(Error="Fuel not found."), 404
        else:
            dao.delete(fuid)
            return jsonify(DeleteStatus="OK"), 200

    def updateFuel(self, fuid, form):
        dao = FuelDAO()
        if not dao.getFuelByID(fuid):
            return jsonify(Error="Fuel not found."), 404
        else:
            return jsonify(dao.getFuelByID(fuid)), 201


class EquipmentHanlder(ResourcesHandler):
    def build_Equipment_dict(self, row):
        result = {}
        result['eid'] = row[0]
        result['etype'] = row[1]
        result['esupplier'] = row[2]
        result['ebrand'] = row[3]
        result['equantity'] = row[4]
        result['elocation'] = row[5]

    def build_Equipment_attr(self, eid, etype, esupplier, ebrand, equantity, elocation):
        result = {}
        result['eid'] = eid
        result['etype'] = etype
        result['esupplier'] = esupplier
        result['ebrand'] = ebrand
        result['equantity'] = equantity
        result['elocation'] = elocation
        return result

    def getAllEquipment(self):
        dao = EquipmentDAO()
        Equipment_list = dao.getAllEquip()
        return jsonify(Equipment=Equipment_list)

    def getEquipmentByID(self, eid):
        dao = EquipmentDAO()
        result = dao.getEquipByID(eid)
        # if not row:
        #     return jsonify(Error = "Equipment Not Found"), 404
        # else:
        #     Equipment = self.build_Equipment_dict(row)
        return jsonify(Equipment = result)


    def searchEquipment(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = EquipmentDAO()
                equipment_list = dao.getEquipByLocation(location)
                # result_list = []
                # for row in equipment_list:
                #     result = self.build_Equipment_dict(row)
                #     result_list.append(row)
                return jsonify(Equipment=equipment_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertEquipment(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove eid later
            eid = form['eid']
            etype = form['etype']
            ebrand = form['ebrand']
            esupplier = form['esupplier']
            equantity = form['equantity']
            elocation = form['elocation']
            if etype and esupplier and equantity and elocation:
                dao = EquipmentDAO
                eid = dao.insert(eid, etype, esupplier, ebrand, equantity, elocation)
                result = self.build_Equipment_attr(eid, etype, esupplier, ebrand, equantity, elocation)
                return jsonify(Equipment=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertEquipmentJson(self, json):
        eid = json['eid']
        etype = json['etype']
        esupplier = json['esupplier']
        ebrand = json['ebrand']
        equantity = json['equantity']
        elocation = json['elocation']
        if eid and etype and esupplier and equantity and elocation:
            dao = EquipmentDAO()
            result = dao.insert(eid, etype, esupplier, ebrand, equantity, elocation)
            return jsonify(Equipment=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteEquipment(self, eid):
        dao = EquipmentDAO()
        result = dao.delete(eid)
        # if not dao.getEquipByID(eid):
        #     return jsonify(Error = "Equipment not found."), 404
        # else:
        #     dao.delete(eid)
        return jsonify(DeleteStatus = result), 200

    def updateEquipment(self, eid, form):
        dao = EquipmentDAO()
        if not dao.getEquipByID(eid):
            return jsonify(Error="Equiment not found."), 404
        else:
            return jsonify(dao.getEquipByID(eid)), 201

class MedDevHandler(ResourcesHandler):
    def build_MedDev_dict(self, row):
        result = {}
        result['mdid'] = row[0]
        result['mdtype'] = row[1]
        result['mdsupplier'] = row[2]
        result['mdbrand'] = row[3]
        result['mdquantity'] = row[4]
        result['mdlocation'] = row[5]

    def build_MedDev_attr(self, mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation):
        result = {}
        result['mdid'] = mdid
        result['mdtype'] = mdtype
        result['mdsupplier'] = mdsupplier
        result['mdbrand'] = mdbrand
        result['mdquantity'] = mdquantity
        result['mdlocation'] = mdlocation
        return result

    def getAllMedDev(self):
        dao = MedDevDAO()
        MedDev_list = dao.getAllMedDev()
        return jsonify(MedDev=MedDev_list)

    def getMedDevByID(self, mdid):
        dao = MedDevDAO()
        result = dao.getMedDevByID(mdid)
        # if not row:
        #     return jsonify(Error = "MedDev Not Found"), 404
        # else:
        #     MedDev = self.build_MedDev_dict(row)
        return jsonify(MedDev = result)


    def searchMedDev(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = MedDevDAO()
                MedDev_list = dao.getMedDevByLocation(location)
                # result_list = []
                # for row in MedDev_list:
                #     result = self.build_MedDev_dict(row)
                #     result_list.append(row)
                return jsonify(MedDev=MedDev_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertMedDev(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove mdid later
            # mdid = form['mdid']
            mdtype = form['mdtype']
            mdbrand = form['mdbrand']
            mdsupplier = form['mdsupplier']
            mdquantity = form['mdquantity']
            mdlocation = form['mdlocation']
            if mdtype and mdsupplier and mdquantity and mdlocation and mdlocation:
                dao = MedDevDAO()
                mdid = dao.insert(mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
                result = self.build_MedDev_attr(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
                return jsonify(MedDev=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertMedDevJson(self, json):
        mdtype = json['mdtype']
        mdsupplier = json['mdsupplier']
        mdbrand = json['mdbrand']
        mdquantity = json['mdquantity']
        mdlocation = json['mdlocation']
        if mdtype and mdsupplier and mdbrand and mdquantity and mdlocation:
            dao = MedDevDAO()
            result = dao.insert(mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
            return jsonify(MedDev=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMedDev(self, mdid):
        dao = MedDevDAO()
        # if not dao.getMedDevByID(mdid):
        #     return jsonify(Error = "MedDev not found."), 404
        # else:
        result = dao.delete(mdid)
        return jsonify(DeleteStatus = result), 200

    def updateMedDev(self, mdid, form):
        dao = MedDevDAO()
        if not dao.getMedDevByID(mdid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getMedDevByID(mdid)), 201

class MedHandler(ResourcesHandler):
    def build_Med_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['mname'] = row[1]
        result['mexpdate'] = row[2]
        result['msupplier'] = row[3]
        result['mbrand'] = row[4]
        result['mquantity'] = row[5]
        result['mlocation'] = row[6]

    def build_Med_attr(self, mid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
        result = {}
        result['mid'] = mid
        result['mname'] = mname
        result['mexpdate'] = mexpdate
        result['msupplier'] = msupplier
        result['mbrand'] = mbrand
        result['mquantity'] = mquantity
        result['mlocation'] = mlocation
        return result

    def getAllMed(self):
        dao = MedDAO()
        Med_list = dao.getAllMed()
        result_list = []
        for row in Med_list:
            result = self.build_Med_dict(row)
            result_list.append(result)
        return jsonify(Med=Med_list)

    def getMedByID(self, mid):
        dao = MedDAO()
        result = dao.getMedByID(mid)
        # if not row:
        #     return jsonify(Error = "Med Not Found"), 404
        # else:
        #     Med = self.build_Med_dict(row)
        return jsonify(Med = result)


    def searchMed(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = MedDAO()
                Med_list = dao.getMedByLocation(location)
                # result_list = []
                # for row in Med_list:
                #     result = self.build_Med_dict(row)
                #     result_list.append(row)
                return jsonify(Med=Med_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertMed(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove mid later
            mname = form['mname']
            mbrand = form['mbrand']
            mexpdate = form['mexpdate']
            msupplier = form['msupplier']
            mquantity = form['mquantity']
            mlocation = form['mlocation']
            if mname and mexpdate and msupplier and mbrand and mquantity and mlocation:
                dao = MedDAO()
                result = dao.insert(mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
                return jsonify(Med=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertMedJson(self, json):
        mname = json['mname']
        mexpdate = json['mexpdate']
        msupplier = json['msupplier']
        mbrand = json['mbrand']
        mquantity = json['mquantity']
        mlocation = json['mlocation']
        if mname and mexpdate and msupplier and mbrand and mquantity and mlocation:
            dao = MedDAO()
            result = dao.insert(mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
            return jsonify(Med=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMed(self, mid):
        dao = MedDAO()
        result = dao.delete(mid)
        return jsonify(DeleteStatus = result), 200

    def updateMed(self, mid, form):
        dao = MedDAO()
        if not dao.getMedByID(mid):
            return jsonify(Error="Medication not found."), 404
        else:
            return jsonify(dao.getMedByID(mid)), 201

class WaterHandler(ResourcesHandler):
    def build_Water_dict(self, row):
        result = {}
        result['fid'] = row[0]
        result['fname'] = row[1]
        result['fexpdate'] = row[2]
        result['fsupplier'] = row[3]
        result['fbrand'] = row[4]
        result['fquantity'] = row[5]
        result['flocation'] = row[6]

    def build_Water_attr(self, fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation):
        result = {}
        result['fid'] = fid
        result['fname'] = fname
        result['fexpdate'] = fexpdate
        result['fsupplier'] = fsupplier
        result['fbrand'] = fbrand
        result['fquantity'] = fquantity
        result['flocation'] = flocation
        return result

    def getAllWater(self):
        dao = WaterDAO()
        Water_list = dao.getAllWater()
        return jsonify(Water=Water_list)

    def getWaterByID(self, fid):
        dao = WaterDAO()
        result = dao.getWaterByID(fid)
        # if not row:
        #     return jsonify(Error = "Food Not Found"), 404
        # else:
        #     Food = self.build_Food_dict(row)
        return jsonify(Water = result)


    def searchWater(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = FoodDAO()
                Water_list = dao.getWaterByLocation(location)
                # result_list = []
                # for row in Food_list:
                #     result = self.build_Water_dict(row)
                #     result_list.append(row)
                return jsonify(Water=Water_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertWater(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            fname = form['fname']
            fbrand = form['fbrand']
            fexpdate = form['fexpdate']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if fname and fsupplier and fquantity and flocation:
                dao = WaterDAO()
                wid = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                result = self.build_Water_attr(wid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                return jsonify(Water=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertWaterJson(self, json):
        fname = json['fname']
        fexpdate = json['fexpdate']
        fsupplier = json['fsupplier']
        fbrand = json['fbrand']
        fquantity = json['fquantity']
        flocation = json['flocation']
        if fname and fexpdate and fsupplier and fquantity and flocation:
            dao = WaterDAO()
            result = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
            return jsonify(Water=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteWater(self, fid):
        dao = WaterDAO()
        # if not dao.getWaterByID(fid):
        #     return jsonify(Error = "Water not found."), 404
        # else:
        result =  dao.delete(fid)
        return jsonify(DeleteStatus = result), 200

    def updateWater(self, fid, form):
        dao = WaterDAO()
        if not dao.getWaterByID(fid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getWaterByID(fid)), 201



    def insertSupplierJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation:
            dao = ResourcesDAO()
            result = dao.insert(rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation)
            return jsonify(Resources=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

class ClothingHandlers(ResourcesHandler):
    def build_Clothing_dict(self, row):
        result = {}
        result['fid'] = row[0]
        result['fname'] = row[1]
        result['fexpdate'] = row[2]
        result['fsupplier'] = row[3]
        result['fbrand'] = row[4]
        result['fquantity'] = row[5]
        result['flocation'] = row[6]

    def build_Clothing_attr(self, fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation):
        result = {}
        result['fid'] = fid
        result['fname'] = fname
        result['fexpdate'] = fexpdate
        result['fsupplier'] = fsupplier
        result['fbrand'] = fbrand
        result['fquantity'] = fquantity
        result['flocation'] = flocation
        return result

    def getAllClothing(self):
        dao = FoodDAO()
        Food_list = dao.getAllFood()
        return jsonify(Food=Food_list)

    def getClothingByID(self, cid):
        dao = ClothingDAO()
        result = dao.getClothingByID(cid)
        # if not row:
        #     return jsonify(Error = "Clothing Not Found"), 404
        # else:
        #     Food = self.build_Clothing_dict(row)
        return jsonify(Clothing = result)


    def searchClothing(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = ClothingDAO()
                Clothing_list = dao.getClothingByLocation(location)
                # result_list = []
                # for row in Clothing_list:
                #     result = self.build_Clothing_dict(row)
                #     result_list.append(row)
                return jsonify(Clothing=Clothing_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertClothing(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            fname = form['fname']
            fbrand = form['fbrand']
            fexpdate = form['fexpdate']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if fname and fsupplier and fquantity and flocation:
                dao = ClothingDAO()
                fid = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                result = self.build_Clothing_attr(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                return jsonify(Clothing=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertClothingJson(self, json):
        fname = json['fname']
        fexpdate = json['fexpdate']
        fsupplier = json['fsupplier']
        fbrand = json['fbrand']
        fquantity = json['fquantity']
        flocation = json['flocation']
        if fname and fexpdate and fsupplier and fquantity and flocation:
            dao = ClothingDAO()
            result = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
            return jsonify(Clothing=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteClothing(self, fid):
        dao = ClothingDAO()
        # if not dao.getClothingByID(fid):
        #     return jsonify(Error = "Clothing not found."), 404
        # else:
        result =  dao.delete(fid)
        return jsonify(DeleteStatus = result), 200

    def updateClothing(self, fid, form):
        dao = ClothingDAO()
        if not dao.getClothingByID(fid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getClothingByID(fid)), 201



    def insertSupplierJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation:
            dao = ResourcesDAO()
            result = dao.insert(rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation)
            return jsonify(Resources=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400