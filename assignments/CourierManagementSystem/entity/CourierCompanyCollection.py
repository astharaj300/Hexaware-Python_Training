
class CourierCompanyCollection:
    def __init__(self):
        self.courier_companies = []

    def add_courier_company(self, courier_company):
        self.courier_companies.append(courier_company)

    def get_courier_companies(self):
        return self.courier_companies

    def add_courier(self, courier):
        for company in self.courier_companies:
            if company.get_company_id() == courier.get_company_id():
                company.add_courier(courier)

    def add_courier_staff(self, courier_staff):
        for company in self.courier_companies:
            if company.get_company_id() == courier_staff.get_company_id():
                company.add_courier_staff(courier_staff)

    def get_couriers(self):
        all_couriers = []
        for company in self.courier_companies:
            all_couriers.extend(company.get_couriers())
        return all_couriers

    def get_courier_staff(self):
        all_courier_staff = []
        for company in self.courier_companies:
            all_courier_staff.extend(company.get_courier_staff())
        return all_courier_staff
