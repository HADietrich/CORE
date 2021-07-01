import pandas as pd
import xlrd


class CostLine:
    def __init__(self, row_values, task, labor_profile):
        self.task_id = task.task_id
        self.labor_id = labor_profile.id
        self.year = "2022"
        self.pma = task.pma
        self.pe = task.pe
        self.funding_profile = task.funding_profile
        self.type = task.type
        self.WUC = task.WUC
        self.product_category = task.product_category
        self.product = task.product
        self.task_description = task.task_description
        self.product_count = task.product_count
        self.location = row_values[17]
        self.org_commercial = "Undefined"
        self.hours = int(row_values[35]) * int(1920)
        self.work_years = row_values[35]
        self.labor_rate = labor_profile.labor_rate
        self.labor_cost = self.labor_rate * self.work_years
        self.other_cost = row_values[32]
        self.flat_rate_costs = row_values[33]
        self.total_cost = self.other_cost + self.flat_rate_costs + self.labor_rate * self.work_years

class CostLines:
    def __init__(self):
        self.task_ids = []
        self.labor_ids = []
        self.years = []
        self.pmas = []
        self.pes = []
        self.funding_profiles = []
        self.types = []
        self.WUCS = []
        self.product_categories = []
        self.products = []
        self.task_descriptions = []
        self.product_counts = []
        self.locations = []
        self.org_commercial = []
        self.hours = []
        self.work_years = []
        self.labor_rates = []
        self.labor_costs = []
        self.other_costs = []
        self.flat_rate_costs = []
        self.total_costs = []

    def add_cost_line(self, cost_line):
        self.task_ids.append(cost_line.task_id)
        self.labor_ids.append(cost_line.labor_id)
        self.years.append(cost_line.year)
        self.pmas.append(cost_line.pma)
        self.pes.append(cost_line.pe)
        self.funding_profiles.append(cost_line.funding_profile)
        self.types.append(cost_line.type)
        self.WUCS.append(cost_line.WUC)
        self.product_categories.append(cost_line.product_category)
        self.products.append(cost_line.product)
        self.task_descriptions.append(cost_line.task_description)
        self.product_counts.append(cost_line.product_count)
        self.locations.append(cost_line.location)
        self.org_commercial.append(cost_line.org_commercial)
        self.hours.append(cost_line.hours)
        self.work_years.append(cost_line.work_years)
        self.labor_rates.append(cost_line.labor_rate)
        self.labor_costs.append(cost_line.labor_cost)
        self.other_costs.append(cost_line.other_cost)
        self.flat_rate_costs.append(cost_line.flat_rate_costs)
        self.total_costs.append(cost_line.total_cost)

    def create_dataframe(self):
        dataframe = pd.DataFrame({
            "TaskID": self.task_ids,
            "LaborID": self.labor_ids,
            "Year": self.years,
            "PMA": self.pmas,
            "PE": self.pes,
            "FundingProfile": self.funding_profiles,
            "Type": self.types,
            "WUC": self.WUCS,
            "ProductCategory": self.product_categories,
            "Product": self.products,
            "Description of Task": self.task_descriptions,
            "Product Count": self.product_counts,
            "Location": self.locations,
            "Organic/Commercial": self.org_commercial,
            "Hours": self.hours,
            "Work Years": self.work_years,
            "Labor Rate": self.labor_rates,
            "Labor Cost": self.labor_costs,
            "Other Costs": self.other_costs,
            "Flat Rate Costs": self.flat_rate_costs,
            "Total Cost": self.total_costs
        })
        return dataframe