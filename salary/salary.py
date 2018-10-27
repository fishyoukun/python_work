# -*- coding: utf-8 -*-
"""
Created on Sat Sep 01 15:51:09 2018

@author: KYou
"""
from __future__ import division

# salary informtion
base_salary = 23000
transport = 250
meal = 400

insurance_low = 4279  # 社保下限
insurance_high = 21396  # 社保上限
tax_start_point = [3500, 5000]
# insurance for employee
insurance_table_employee = {'endowment insurance': 0.08,
                            'medical insurance': 0.02,
                            'unemployment insurance': 0.005,
                            'maternity insurance': 0.0,
                            'employment injury insurance': 0.0,
                            'housing fund': 0.07}
# insurance for employer
insurance_table_employer = {'endowment insurance': 0.20,
                            'medical insurance': 0.10,
                            'unemployment insurance': 0.01,
                            'maternity insurance': 0.01,
                            'employment injury insurance': 0.005,
                            'housing fund': 0.07}
# old tax table
tax_table = [[{'taxable income': 1500, 'tax rate': 0.03, 'deduction': 0},
              {'taxable income': 4500, 'tax rate': 0.10, 'deduction': 105},
              {'taxable income': 9000, 'tax rate': 0.20, 'deduction': 555},
              {'taxable income': 35000, 'tax rate': 0.25, 'deduction': 1005},
              {'taxable income': 55000, 'tax rate': 0.30, 'deduction': 2755},
              {'taxable income': 80000, 'tax rate': 0.35, 'deduction': 5505},
              {'taxable income': 999999999999, 'tax rate': 0.45, 'deduction': 13505}],
# new tax table
             [{'taxable income': 3000, 'tax rate': 0.03, 'deduction': 0},
              {'taxable income': 12000, 'tax rate': 0.10, 'deduction': 210},
              {'taxable income': 25000, 'tax rate': 0.20, 'deduction': 1410},
              {'taxable income': 35000, 'tax rate': 0.25, 'deduction': 2660},
              {'taxable income': 55000, 'tax rate': 0.30, 'deduction': 4410},
              {'taxable income': 80000, 'tax rate': 0.35, 'deduction': 7160},
              {'taxable income': 999999999999, 'tax rate': 0.45, 'deduction': 15160}]]

salary_total = base_salary + transport + meal
if salary_total < insurance_low:
    salary_apply = insurance_low
elif salary_total > insurance_high:
    salary_apply = insurance_high
else:
    salary_apply = salary_total

salary_insurance_employee = salary_apply * (insurance_table_employee['endowment insurance']
                                            + insurance_table_employee['medical insurance']
                                            + insurance_table_employee['unemployment insurance']
                                            + insurance_table_employee['maternity insurance']
                                            + insurance_table_employee['employment injury insurance']
                                            + insurance_table_employee['housing fund']
                                            )

salary_insurance_employer = salary_apply * (insurance_table_employer['endowment insurance']
                                            + insurance_table_employer['medical insurance']
                                            + insurance_table_employer['unemployment insurance']
                                            + insurance_table_employer['maternity insurance']
                                            + insurance_table_employer['employment injury insurance']
                                            + insurance_table_employer['housing fund']
                                            )

salary_employer_offer = base_salary + transport + meal + salary_insurance_employer
salary_taxable = [0.0, 0.0]
for method in range(0, 2):
    salary_taxable[method] = salary_total - salary_insurance_employee - tax_start_point[method]

final_tax_rate = [0.0, 0.0]
final_deduction = [0.0, 0.0]
for method in range(0, 2):
    for i in range(0, len(tax_table[method])):
        if salary_taxable[method] < tax_table[method][i]['taxable income']:
            final_tax_rate[method] = tax_table[method][i]['tax rate']
            final_deduction[method] = tax_table[method][i]['deduction']
            break

tax = [0.0, 0.0]
salary_final = [0, 0]
salary_efficency = [0,0]
for method in range(0, 2):
    tax[method] = salary_taxable[method] * final_tax_rate[method] - final_deduction[method]
for method in range(0, 2):
    salary_final[method] = salary_taxable[method] - tax[method] + tax_start_point[method]
    salary_efficency[method] = salary_final[method] / salary_employer_offer

print '*******************calc result*************************'
print '* salary insurance = ', salary_insurance_employee
print '* employer insurance = ', salary_insurance_employer
print '* salary_employer_offer = ', salary_employer_offer
print '******************************************************** '
for method in range(0, 2):
    if method == 0:
        print '* old tax situation'
    else:
        print '* new tax situation'
    print '* final tax rate   = ', final_tax_rate[method]
    print '* salary taxable   = ', salary_taxable[method]
    print '* salary tax       = ', tax[method]
    print '* salary final     = ', salary_final[method]
    print '* salary_efficency = ',round (salary_efficency[method]*100, 2),'%'
    print '******************************************************** '
print '* new salary - old salary = ', salary_final[1] - salary_final[0]
print '********************* over ******************************* '
