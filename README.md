<div align="center">

[![Visit Gusto](./header.png)](https://gusto.com)

# Gusto<a id="gusto"></a>

Welcome to Gusto's Embedded Payroll API documentation!


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Getting Started](#getting-started)
  * [Async](#async)
  * [Raw HTTP Response](#raw-http-response)
  * [Reference](#reference)
    + [`gustoembeddedpayroll.ach_transactions.get_all_for_company`](#gustoembeddedpayrollach_transactionsget_all_for_company)
    + [`gustoembeddedpayroll.bank_accounts.create_from_plaid_token`](#gustoembeddedpayrollbank_accountscreate_from_plaid_token)
    + [`gustoembeddedpayroll.bank_accounts.create_verification_deposits`](#gustoembeddedpayrollbank_accountscreate_verification_deposits)
    + [`gustoembeddedpayroll.bank_accounts.list_company_bank_accounts`](#gustoembeddedpayrollbank_accountslist_company_bank_accounts)
    + [`gustoembeddedpayroll.bank_accounts.verify_micro_deposits`](#gustoembeddedpayrollbank_accountsverify_micro_deposits)
    + [Bank account verification in demo](#bank-account-verification-in-demo)
    + [`gustoembeddedpayroll.companies.accept_terms_of_service`](#gustoembeddedpayrollcompaniesaccept_terms_of_service)
    + [`gustoembeddedpayroll.companies.create_admin`](#gustoembeddedpayrollcompaniescreate_admin)
    + [`gustoembeddedpayroll.companies.create_partner_managed_company`](#gustoembeddedpayrollcompaniescreate_partner_managed_company)
    + [`gustoembeddedpayroll.companies.finish_onboarding`](#gustoembeddedpayrollcompaniesfinish_onboarding)
    + [Approve a company in demo](#approve-a-company-in-demo)
    + [`gustoembeddedpayroll.companies.get_all_admins`](#gustoembeddedpayrollcompaniesget_all_admins)
    + [`gustoembeddedpayroll.companies.get_company`](#gustoembeddedpayrollcompaniesget_company)
    + [`gustoembeddedpayroll.companies.get_custom_fields`](#gustoembeddedpayrollcompaniesget_custom_fields)
    + [`gustoembeddedpayroll.companies.get_onboarding_status`](#gustoembeddedpayrollcompaniesget_onboarding_status)
    + [`gustoembeddedpayroll.companies.get_terms_of_service_status`](#gustoembeddedpayrollcompaniesget_terms_of_service_status)
    + [`gustoembeddedpayroll.companies.migrate_to_embedded_payroll`](#gustoembeddedpayrollcompaniesmigrate_to_embedded_payroll)
    + [`gustoembeddedpayroll.company_benefits.create_benefit`](#gustoembeddedpayrollcompany_benefitscreate_benefit)
    + [`gustoembeddedpayroll.company_benefits.delete_benefit`](#gustoembeddedpayrollcompany_benefitsdelete_benefit)
    + [`gustoembeddedpayroll.company_benefits.get_benefit_by_id`](#gustoembeddedpayrollcompany_benefitsget_benefit_by_id)
    + [`gustoembeddedpayroll.company_benefits.get_benefit_fields_requirements_by_id`](#gustoembeddedpayrollcompany_benefitsget_benefit_fields_requirements_by_id)
    + [`gustoembeddedpayroll.company_benefits.get_benefit_summary_by_id`](#gustoembeddedpayrollcompany_benefitsget_benefit_summary_by_id)
    + [`gustoembeddedpayroll.company_benefits.get_benefits_for_company`](#gustoembeddedpayrollcompany_benefitsget_benefits_for_company)
    + [`gustoembeddedpayroll.company_benefits.get_supported_benefit_by_id`](#gustoembeddedpayrollcompany_benefitsget_supported_benefit_by_id)
    + [`gustoembeddedpayroll.company_benefits.list_supported_benefits`](#gustoembeddedpayrollcompany_benefitslist_supported_benefits)
    + [`gustoembeddedpayroll.company_benefits.update_benefit`](#gustoembeddedpayrollcompany_benefitsupdate_benefit)
    + [`gustoembeddedpayroll.company_forms.get_all_forms`](#gustoembeddedpayrollcompany_formsget_all_forms)
    + [`gustoembeddedpayroll.company_forms.get_form_by_id`](#gustoembeddedpayrollcompany_formsget_form_by_id)
    + [`gustoembeddedpayroll.company_forms.get_pdf_link`](#gustoembeddedpayrollcompany_formsget_pdf_link)
    + [`gustoembeddedpayroll.company_forms.sign_form`](#gustoembeddedpayrollcompany_formssign_form)
    + [`gustoembeddedpayroll.contractor_forms.create1099_form`](#gustoembeddedpayrollcontractor_formscreate1099_form)
    + [`gustoembeddedpayroll.contractor_forms.get_by_id_form`](#gustoembeddedpayrollcontractor_formsget_by_id_form)
    + [`gustoembeddedpayroll.contractor_forms.get_pdf_link`](#gustoembeddedpayrollcontractor_formsget_pdf_link)
    + [`gustoembeddedpayroll.contractor_forms.list_all`](#gustoembeddedpayrollcontractor_formslist_all)
    + [`gustoembeddedpayroll.contractor_payment_method.create_bank_account`](#gustoembeddedpayrollcontractor_payment_methodcreate_bank_account)
    + [`gustoembeddedpayroll.contractor_payment_method.get_contractor_payment_method`](#gustoembeddedpayrollcontractor_payment_methodget_contractor_payment_method)
    + [`gustoembeddedpayroll.contractor_payment_method.list_bank_accounts`](#gustoembeddedpayrollcontractor_payment_methodlist_bank_accounts)
    + [`gustoembeddedpayroll.contractor_payment_method.update_bank_account`](#gustoembeddedpayrollcontractor_payment_methodupdate_bank_account)
    + [`gustoembeddedpayroll.contractor_payments.cancel_payment`](#gustoembeddedpayrollcontractor_paymentscancel_payment)
    + [`gustoembeddedpayroll.contractor_payments.create_payment`](#gustoembeddedpayrollcontractor_paymentscreate_payment)
    + [`gustoembeddedpayroll.contractor_payments.fund_contractor_payment`](#gustoembeddedpayrollcontractor_paymentsfund_contractor_payment)
    + [`gustoembeddedpayroll.contractor_payments.get_single_payment`](#gustoembeddedpayrollcontractor_paymentsget_single_payment)
    + [`gustoembeddedpayroll.contractor_payments.get_single_receipt`](#gustoembeddedpayrollcontractor_paymentsget_single_receipt)
    + [`gustoembeddedpayroll.contractor_payments.get_within_time_period_totals`](#gustoembeddedpayrollcontractor_paymentsget_within_time_period_totals)
    + [`gustoembeddedpayroll.contractor_payments.preview_debit_date`](#gustoembeddedpayrollcontractor_paymentspreview_debit_date)
    + [`gustoembeddedpayroll.contractors.change_onboarding_status`](#gustoembeddedpayrollcontractorschange_onboarding_status)
    + [`gustoembeddedpayroll.contractors.create_new_contractor`](#gustoembeddedpayrollcontractorscreate_new_contractor)
    + [`gustoembeddedpayroll.contractors.delete_contractor`](#gustoembeddedpayrollcontractorsdelete_contractor)
    + [`gustoembeddedpayroll.contractors.get_address`](#gustoembeddedpayrollcontractorsget_address)
    + [`gustoembeddedpayroll.contractors.get_by_id`](#gustoembeddedpayrollcontractorsget_by_id)
    + [`gustoembeddedpayroll.contractors.get_company_contractors`](#gustoembeddedpayrollcontractorsget_company_contractors)
    + [`gustoembeddedpayroll.contractors.get_onboarding_status`](#gustoembeddedpayrollcontractorsget_onboarding_status)
  * [onboarding_status](#onboarding_status)
    + [Admin-facilitated onboarding](#admin-facilitated-onboarding)
    + [Contractor self-onboarding](#contractor-self-onboarding)
  * [onboarding_steps](#onboarding_steps)
    + [`gustoembeddedpayroll.contractors.update_address`](#gustoembeddedpayrollcontractorsupdate_address)
    + [`gustoembeddedpayroll.contractors.update_contractor`](#gustoembeddedpayrollcontractorsupdate_contractor)
    + [`gustoembeddedpayroll.departments.add_people_to_department`](#gustoembeddedpayrolldepartmentsadd_people_to_department)
    + [`gustoembeddedpayroll.departments.create_department`](#gustoembeddedpayrolldepartmentscreate_department)
    + [`gustoembeddedpayroll.departments.delete_department`](#gustoembeddedpayrolldepartmentsdelete_department)
    + [`gustoembeddedpayroll.departments.get_all_with_employees`](#gustoembeddedpayrolldepartmentsget_all_with_employees)
    + [`gustoembeddedpayroll.departments.get_department_by_uuid`](#gustoembeddedpayrolldepartmentsget_department_by_uuid)
    + [`gustoembeddedpayroll.departments.remove_people_from_department`](#gustoembeddedpayrolldepartmentsremove_people_from_department)
    + [`gustoembeddedpayroll.departments.update_department`](#gustoembeddedpayrolldepartmentsupdate_department)
    + [`gustoembeddedpayroll.earning_types.create_custom_earning_type`](#gustoembeddedpayrollearning_typescreate_custom_earning_type)
    + [`gustoembeddedpayroll.earning_types.deactivate_type`](#gustoembeddedpayrollearning_typesdeactivate_type)
    + [`gustoembeddedpayroll.earning_types.get_all`](#gustoembeddedpayrollearning_typesget_all)
    + [`gustoembeddedpayroll.earning_types.update_type`](#gustoembeddedpayrollearning_typesupdate_type)
    + [`gustoembeddedpayroll.employee_addresses.create_home_address`](#gustoembeddedpayrollemployee_addressescreate_home_address)
    + [`gustoembeddedpayroll.employee_addresses.create_work_address`](#gustoembeddedpayrollemployee_addressescreate_work_address)
    + [`gustoembeddedpayroll.employee_addresses.delete_home`](#gustoembeddedpayrollemployee_addressesdelete_home)
    + [`gustoembeddedpayroll.employee_addresses.delete_work_address`](#gustoembeddedpayrollemployee_addressesdelete_work_address)
    + [`gustoembeddedpayroll.employee_addresses.get_home_address`](#gustoembeddedpayrollemployee_addressesget_home_address)
    + [`gustoembeddedpayroll.employee_addresses.get_home_addresses`](#gustoembeddedpayrollemployee_addressesget_home_addresses)
    + [`gustoembeddedpayroll.employee_addresses.get_work_address`](#gustoembeddedpayrollemployee_addressesget_work_address)
    + [`gustoembeddedpayroll.employee_addresses.list_work_addresses`](#gustoembeddedpayrollemployee_addresseslist_work_addresses)
    + [`gustoembeddedpayroll.employee_addresses.update_home_address`](#gustoembeddedpayrollemployee_addressesupdate_home_address)
    + [`gustoembeddedpayroll.employee_addresses.update_work_address`](#gustoembeddedpayrollemployee_addressesupdate_work_address)
    + [`gustoembeddedpayroll.employee_benefits.create_benefit_record`](#gustoembeddedpayrollemployee_benefitscreate_benefit_record)
    + [`gustoembeddedpayroll.employee_benefits.create_ytd_benefit_amounts_from_different_company`](#gustoembeddedpayrollemployee_benefitscreate_ytd_benefit_amounts_from_different_company)
    + [`gustoembeddedpayroll.employee_benefits.delete_by_id`](#gustoembeddedpayrollemployee_benefitsdelete_by_id)
    + [`gustoembeddedpayroll.employee_benefits.get_all_for_employee`](#gustoembeddedpayrollemployee_benefitsget_all_for_employee)
    + [`gustoembeddedpayroll.employee_benefits.get_employee_benefit_by_id`](#gustoembeddedpayrollemployee_benefitsget_employee_benefit_by_id)
    + [`gustoembeddedpayroll.employee_benefits.update_benefit_record`](#gustoembeddedpayrollemployee_benefitsupdate_benefit_record)
    + [`gustoembeddedpayroll.employee_employments.create_rehire`](#gustoembeddedpayrollemployee_employmentscreate_rehire)
    + [`gustoembeddedpayroll.employee_employments.create_termination`](#gustoembeddedpayrollemployee_employmentscreate_termination)
    + [`gustoembeddedpayroll.employee_employments.delete_termination`](#gustoembeddedpayrollemployee_employmentsdelete_termination)
    + [`gustoembeddedpayroll.employee_employments.get_history`](#gustoembeddedpayrollemployee_employmentsget_history)
    + [`gustoembeddedpayroll.employee_employments.get_rehire`](#gustoembeddedpayrollemployee_employmentsget_rehire)
    + [`gustoembeddedpayroll.employee_employments.list_employee_terminations`](#gustoembeddedpayrollemployee_employmentslist_employee_terminations)
    + [`gustoembeddedpayroll.employee_employments.remove_rehire`](#gustoembeddedpayrollemployee_employmentsremove_rehire)
    + [`gustoembeddedpayroll.employee_employments.update_rehire`](#gustoembeddedpayrollemployee_employmentsupdate_rehire)
    + [`gustoembeddedpayroll.employee_employments.update_termination`](#gustoembeddedpayrollemployee_employmentsupdate_termination)
    + [`gustoembeddedpayroll.employee_forms.generate_w2_document`](#gustoembeddedpayrollemployee_formsgenerate_w2_document)
    + [`gustoembeddedpayroll.employee_forms.get_all_employee_forms`](#gustoembeddedpayrollemployee_formsget_all_employee_forms)
    + [`gustoembeddedpayroll.employee_forms.get_form_by_id`](#gustoembeddedpayrollemployee_formsget_form_by_id)
    + [`gustoembeddedpayroll.employee_forms.get_pdf_link`](#gustoembeddedpayrollemployee_formsget_pdf_link)
    + [`gustoembeddedpayroll.employee_forms.sign_form`](#gustoembeddedpayrollemployee_formssign_form)
    + [`gustoembeddedpayroll.employee_payment_method.create_bank_account`](#gustoembeddedpayrollemployee_payment_methodcreate_bank_account)
    + [`gustoembeddedpayroll.employee_payment_method.delete_bank_account`](#gustoembeddedpayrollemployee_payment_methoddelete_bank_account)
    + [`gustoembeddedpayroll.employee_payment_method.get_bank_accounts`](#gustoembeddedpayrollemployee_payment_methodget_bank_accounts)
    + [`gustoembeddedpayroll.employee_payment_method.list_bank_accounts`](#gustoembeddedpayrollemployee_payment_methodlist_bank_accounts)
    + [`gustoembeddedpayroll.employee_payment_method.update_payment_method`](#gustoembeddedpayrollemployee_payment_methodupdate_payment_method)
    + [`gustoembeddedpayroll.employee_tax_setup.get_federal_taxes_by_id`](#gustoembeddedpayrollemployee_tax_setupget_federal_taxes_by_id)
    + [`gustoembeddedpayroll.employee_tax_setup.get_state_taxes`](#gustoembeddedpayrollemployee_tax_setupget_state_taxes)
  * [About filing new hire reports](#about-filing-new-hire-reports)
    + [`gustoembeddedpayroll.employee_tax_setup.update_federal_taxes`](#gustoembeddedpayrollemployee_tax_setupupdate_federal_taxes)
    + [`gustoembeddedpayroll.employee_tax_setup.update_state_taxes`](#gustoembeddedpayrollemployee_tax_setupupdate_state_taxes)
    + [`gustoembeddedpayroll.employees.complete_onboarding`](#gustoembeddedpayrollemployeescomplete_onboarding)
    + [`gustoembeddedpayroll.employees.create_employee`](#gustoembeddedpayrollemployeescreate_employee)
    + [`gustoembeddedpayroll.employees.delete_onboarding_employee`](#gustoembeddedpayrollemployeesdelete_onboarding_employee)
    + [`gustoembeddedpayroll.employees.get_custom_fields`](#gustoembeddedpayrollemployeesget_custom_fields)
    + [`gustoembeddedpayroll.employees.get_employee_by_id`](#gustoembeddedpayrollemployeesget_employee_by_id)
    + [`gustoembeddedpayroll.employees.get_onboarding_status`](#gustoembeddedpayrollemployeesget_onboarding_status)
- [Description](#description)
  * [onboarding_status](#onboarding_status-1)
    + [Admin-facilitated onboarding](#admin-facilitated-onboarding-1)
    + [Employee self-onboarding](#employee-self-onboarding)
  * [onboarding_steps](#onboarding_steps-1)
    + [`gustoembeddedpayroll.employees.get_time_off_activities`](#gustoembeddedpayrollemployeesget_time_off_activities)
    + [`gustoembeddedpayroll.employees.list_company_employees`](#gustoembeddedpayrollemployeeslist_company_employees)
    + [`gustoembeddedpayroll.employees.update_employee`](#gustoembeddedpayrollemployeesupdate_employee)
    + [`gustoembeddedpayroll.employees.update_onboarding_status`](#gustoembeddedpayrollemployeesupdate_onboarding_status)
    + [`gustoembeddedpayroll.events.get30_day_events`](#gustoembeddedpayrolleventsget30_day_events)
    + [`gustoembeddedpayroll.external_payrolls.create_new_payroll`](#gustoembeddedpayrollexternal_payrollscreate_new_payroll)
    + [`gustoembeddedpayroll.external_payrolls.delete_payroll`](#gustoembeddedpayrollexternal_payrollsdelete_payroll)
    + [`gustoembeddedpayroll.external_payrolls.finalize_tax_liabilities`](#gustoembeddedpayrollexternal_payrollsfinalize_tax_liabilities)
    + [`gustoembeddedpayroll.external_payrolls.get_by_id`](#gustoembeddedpayrollexternal_payrollsget_by_id)
    + [`gustoembeddedpayroll.external_payrolls.get_tax_liabilities`](#gustoembeddedpayrollexternal_payrollsget_tax_liabilities)
    + [`gustoembeddedpayroll.external_payrolls.get_tax_suggestions`](#gustoembeddedpayrollexternal_payrollsget_tax_suggestions)
    + [`gustoembeddedpayroll.external_payrolls.list_for_company`](#gustoembeddedpayrollexternal_payrollslist_for_company)
    + [`gustoembeddedpayroll.external_payrolls.update_payroll_items`](#gustoembeddedpayrollexternal_payrollsupdate_payroll_items)
    + [`gustoembeddedpayroll.external_payrolls.update_tax_liabilities`](#gustoembeddedpayrollexternal_payrollsupdate_tax_liabilities)
    + [`gustoembeddedpayroll.federal_tax_details.get_attributes`](#gustoembeddedpayrollfederal_tax_detailsget_attributes)
    + [`gustoembeddedpayroll.federal_tax_details.update_attributes`](#gustoembeddedpayrollfederal_tax_detailsupdate_attributes)
    + [`gustoembeddedpayroll.flows.generate_link`](#gustoembeddedpayrollflowsgenerate_link)
    + [`gustoembeddedpayroll.garnishments.create_garnishment`](#gustoembeddedpayrollgarnishmentscreate_garnishment)
    + [`gustoembeddedpayroll.garnishments.get_employee_garnishments`](#gustoembeddedpayrollgarnishmentsget_employee_garnishments)
    + [`gustoembeddedpayroll.garnishments.get_garnishment`](#gustoembeddedpayrollgarnishmentsget_garnishment)
    + [`gustoembeddedpayroll.garnishments.update_garnishment`](#gustoembeddedpayrollgarnishmentsupdate_garnishment)
    + [`gustoembeddedpayroll.generated_documents.get_document_by_request_uuid`](#gustoembeddedpayrollgenerated_documentsget_document_by_request_uuid)
    + [`gustoembeddedpayroll.holiday_pay_policies.add_employees_to_policy`](#gustoembeddedpayrollholiday_pay_policiesadd_employees_to_policy)
    + [`gustoembeddedpayroll.holiday_pay_policies.create_company_policy`](#gustoembeddedpayrollholiday_pay_policiescreate_company_policy)
    + [`gustoembeddedpayroll.holiday_pay_policies.delete_policy`](#gustoembeddedpayrollholiday_pay_policiesdelete_policy)
    + [`gustoembeddedpayroll.holiday_pay_policies.get_company_policy`](#gustoembeddedpayrollholiday_pay_policiesget_company_policy)
    + [`gustoembeddedpayroll.holiday_pay_policies.preview_company_paid_holidays`](#gustoembeddedpayrollholiday_pay_policiespreview_company_paid_holidays)
    + [`gustoembeddedpayroll.holiday_pay_policies.remove_employees`](#gustoembeddedpayrollholiday_pay_policiesremove_employees)
    + [`gustoembeddedpayroll.holiday_pay_policies.update_policy`](#gustoembeddedpayrollholiday_pay_policiesupdate_policy)
    + [`gustoembeddedpayroll.industry_selection.get_company_industry_selection`](#gustoembeddedpayrollindustry_selectionget_company_industry_selection)
    + [`gustoembeddedpayroll.industry_selection.update_company_industry_selection`](#gustoembeddedpayrollindustry_selectionupdate_company_industry_selection)
    + [`gustoembeddedpayroll.introspection.exchange_refresh_token`](#gustoembeddedpayrollintrospectionexchange_refresh_token)
    + [`gustoembeddedpayroll.introspection.get_current_access_token_info`](#gustoembeddedpayrollintrospectionget_current_access_token_info)
    + [`gustoembeddedpayroll.invoices.get_invoicing_data_for_companies`](#gustoembeddedpayrollinvoicesget_invoicing_data_for_companies)
    + [`gustoembeddedpayroll.jobs_and_compensations.create_compensation`](#gustoembeddedpayrolljobs_and_compensationscreate_compensation)
    + [`gustoembeddedpayroll.jobs_and_compensations.create_job`](#gustoembeddedpayrolljobs_and_compensationscreate_job)
    + [`gustoembeddedpayroll.jobs_and_compensations.delete_job_by_id`](#gustoembeddedpayrolljobs_and_compensationsdelete_job_by_id)
    + [`gustoembeddedpayroll.jobs_and_compensations.get_compensation_by_id`](#gustoembeddedpayrolljobs_and_compensationsget_compensation_by_id)
    + [`gustoembeddedpayroll.jobs_and_compensations.get_employee_jobs`](#gustoembeddedpayrolljobs_and_compensationsget_employee_jobs)
    + [`gustoembeddedpayroll.jobs_and_compensations.get_job_compensations`](#gustoembeddedpayrolljobs_and_compensationsget_job_compensations)
    + [`gustoembeddedpayroll.jobs_and_compensations.get_job_details`](#gustoembeddedpayrolljobs_and_compensationsget_job_details)
    + [`gustoembeddedpayroll.jobs_and_compensations.remove_compensation`](#gustoembeddedpayrolljobs_and_compensationsremove_compensation)
    + [`gustoembeddedpayroll.jobs_and_compensations.update_compensation`](#gustoembeddedpayrolljobs_and_compensationsupdate_compensation)
    + [`gustoembeddedpayroll.jobs_and_compensations.update_job`](#gustoembeddedpayrolljobs_and_compensationsupdate_job)
    + [`gustoembeddedpayroll.locations.create_company_location`](#gustoembeddedpayrolllocationscreate_company_location)
    + [`gustoembeddedpayroll.locations.get_by_id`](#gustoembeddedpayrolllocationsget_by_id)
    + [`gustoembeddedpayroll.locations.get_company_locations`](#gustoembeddedpayrolllocationsget_company_locations)
    + [`gustoembeddedpayroll.locations.get_minimum_wages`](#gustoembeddedpayrolllocationsget_minimum_wages)
    + [`gustoembeddedpayroll.locations.update_location`](#gustoembeddedpayrolllocationsupdate_location)
    + [`gustoembeddedpayroll.notifications.get_details`](#gustoembeddedpayrollnotificationsget_details)
    + [`gustoembeddedpayroll.pay_schedules.assign_employees_to_schedules`](#gustoembeddedpayrollpay_schedulesassign_employees_to_schedules)
    + [`gustoembeddedpayroll.pay_schedules.create_new`](#gustoembeddedpayrollpay_schedulescreate_new)
    + [`gustoembeddedpayroll.pay_schedules.get_assignments`](#gustoembeddedpayrollpay_schedulesget_assignments)
    + [`gustoembeddedpayroll.pay_schedules.get_details`](#gustoembeddedpayrollpay_schedulesget_details)
    + [`gustoembeddedpayroll.pay_schedules.get_pay_periods`](#gustoembeddedpayrollpay_schedulesget_pay_periods)
    + [`gustoembeddedpayroll.pay_schedules.get_unprocessed_termination_pay_periods`](#gustoembeddedpayrollpay_schedulesget_unprocessed_termination_pay_periods)
    + [`gustoembeddedpayroll.pay_schedules.list_for_company`](#gustoembeddedpayrollpay_scheduleslist_for_company)
    + [`gustoembeddedpayroll.pay_schedules.preview_assignments_for_company`](#gustoembeddedpayrollpay_schedulespreview_assignments_for_company)
    + [`gustoembeddedpayroll.pay_schedules.preview_pay_schedule_dates`](#gustoembeddedpayrollpay_schedulespreview_pay_schedule_dates)
    + [`gustoembeddedpayroll.pay_schedules.update_pay_schedule`](#gustoembeddedpayrollpay_schedulesupdate_pay_schedule)
    + [`gustoembeddedpayroll.payment_configs.get_company_payment_configs`](#gustoembeddedpayrollpayment_configsget_company_payment_configs)
    + [`gustoembeddedpayroll.payment_configs.update_company_payment_configs`](#gustoembeddedpayrollpayment_configsupdate_company_payment_configs)
    + [`gustoembeddedpayroll.payrolls.approved_reversals`](#gustoembeddedpayrollpayrollsapproved_reversals)
    + [`gustoembeddedpayroll.payrolls.calculate_gross_up`](#gustoembeddedpayrollpayrollscalculate_gross_up)
    + [`gustoembeddedpayroll.payrolls.calculate_gross_up_0`](#gustoembeddedpayrollpayrollscalculate_gross_up_0)
    + [`gustoembeddedpayroll.payrolls.cancel_payroll_transition`](#gustoembeddedpayrollpayrollscancel_payroll_transition)
    + [`gustoembeddedpayroll.payrolls.create_off_cycle_payroll`](#gustoembeddedpayrollpayrollscreate_off_cycle_payroll)
  * [`off_cycle_reason`](#off_cycle_reason)
    + [`gustoembeddedpayroll.payrolls.delete_unprocessed_payroll`](#gustoembeddedpayrollpayrollsdelete_unprocessed_payroll)
    + [`gustoembeddedpayroll.payrolls.generate_printable_checks`](#gustoembeddedpayrollpayrollsgenerate_printable_checks)
    + [`gustoembeddedpayroll.payrolls.get_all_payroll_blockers`](#gustoembeddedpayrollpayrollsget_all_payroll_blockers)
    + [`gustoembeddedpayroll.payrolls.get_company_payrolls`](#gustoembeddedpayrollpayrollsget_company_payrolls)
    + [`gustoembeddedpayroll.payrolls.get_employee_pay_stub`](#gustoembeddedpayrollpayrollsget_employee_pay_stub)
    + [`gustoembeddedpayroll.payrolls.get_employee_pay_stubs`](#gustoembeddedpayrollpayrollsget_employee_pay_stubs)
    + [`gustoembeddedpayroll.payrolls.get_single_payroll`](#gustoembeddedpayrollpayrollsget_single_payroll)
    + [`gustoembeddedpayroll.payrolls.get_single_receipt`](#gustoembeddedpayrollpayrollsget_single_receipt)
    + [`gustoembeddedpayroll.payrolls.prepare_for_update`](#gustoembeddedpayrollpayrollsprepare_for_update)
    + [`gustoembeddedpayroll.payrolls.skip_payroll`](#gustoembeddedpayrollpayrollsskip_payroll)
    + [`gustoembeddedpayroll.payrolls.submit_payroll`](#gustoembeddedpayrollpayrollssubmit_payroll)
    + [`gustoembeddedpayroll.payrolls.update_payroll_by_id`](#gustoembeddedpayrollpayrollsupdate_payroll_by_id)
    + [`gustoembeddedpayroll.recovery_cases.initiate_redebit`](#gustoembeddedpayrollrecovery_casesinitiate_redebit)
    + [`gustoembeddedpayroll.recovery_cases.list_for_company`](#gustoembeddedpayrollrecovery_caseslist_for_company)
    + [`gustoembeddedpayroll.signatories.create_invite`](#gustoembeddedpayrollsignatoriescreate_invite)
    + [`gustoembeddedpayroll.signatories.create_signatory_with_complete_information`](#gustoembeddedpayrollsignatoriescreate_signatory_with_complete_information)
    + [`gustoembeddedpayroll.signatories.delete_signatory`](#gustoembeddedpayrollsignatoriesdelete_signatory)
    + [`gustoembeddedpayroll.signatories.get_company_signatories`](#gustoembeddedpayrollsignatoriesget_company_signatories)
    + [`gustoembeddedpayroll.signatories.update`](#gustoembeddedpayrollsignatoriesupdate)
    + [`gustoembeddedpayroll.tax_requirements.get_state_requirements`](#gustoembeddedpayrolltax_requirementsget_state_requirements)
    + [Metadata Examples](#metadata-examples)
    + [`gustoembeddedpayroll.tax_requirements.get_states`](#gustoembeddedpayrolltax_requirementsget_states)
    + [`gustoembeddedpayroll.tax_requirements.update_state_taxes`](#gustoembeddedpayrolltax_requirementsupdate_state_taxes)
    + [`gustoembeddedpayroll.time_off_policies.add_employees_to_policy`](#gustoembeddedpayrolltime_off_policiesadd_employees_to_policy)
    + [`gustoembeddedpayroll.time_off_policies.calculate_accruing_time_off_hours`](#gustoembeddedpayrolltime_off_policiescalculate_accruing_time_off_hours)
    + [`gustoembeddedpayroll.time_off_policies.create_policy`](#gustoembeddedpayrolltime_off_policiescreate_policy)
    + [`gustoembeddedpayroll.time_off_policies.deactivate_policy`](#gustoembeddedpayrolltime_off_policiesdeactivate_policy)
    + [`gustoembeddedpayroll.time_off_policies.get_all_policies`](#gustoembeddedpayrolltime_off_policiesget_all_policies)
    + [`gustoembeddedpayroll.time_off_policies.get_policy`](#gustoembeddedpayrolltime_off_policiesget_policy)
    + [`gustoembeddedpayroll.time_off_policies.remove_employees`](#gustoembeddedpayrolltime_off_policiesremove_employees)
    + [`gustoembeddedpayroll.time_off_policies.update_employee_balance`](#gustoembeddedpayrolltime_off_policiesupdate_employee_balance)
    + [`gustoembeddedpayroll.time_off_policies.update_policy`](#gustoembeddedpayrolltime_off_policiesupdate_policy)
    + [`gustoembeddedpayroll.webhooks.create_subscription`](#gustoembeddedpayrollwebhookscreate_subscription)
    + [`gustoembeddedpayroll.webhooks.delete_subscription_by_uuid`](#gustoembeddedpayrollwebhooksdelete_subscription_by_uuid)
    + [`gustoembeddedpayroll.webhooks.get_subscription`](#gustoembeddedpayrollwebhooksget_subscription)
    + [`gustoembeddedpayroll.webhooks.list_subscriptions`](#gustoembeddedpayrollwebhookslist_subscriptions)
    + [`gustoembeddedpayroll.webhooks.request_verification_token`](#gustoembeddedpayrollwebhooksrequest_verification_token)
    + [`gustoembeddedpayroll.webhooks.update_subscription`](#gustoembeddedpayrollwebhooksupdate_subscription)
    + [`gustoembeddedpayroll.webhooks.verify_subscription_token`](#gustoembeddedpayrollwebhooksverify_subscription_token)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Gusto&serviceName=Embedded%20Payroll&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from gusto_embedded_payroll_python_sdk import GustoEmbeddedPayroll, ApiException

gustoembeddedpayroll = GustoEmbeddedPayroll(access_token="YOUR_BEARER_TOKEN")

try:
    # Get all ACH transactions for a company
    get_all_for_company_response = (
        gustoembeddedpayroll.ach_transactions.get_all_for_company(
            company_uuid="company_uuid_example",
            contractor_payment_uuid="string_example",
            payroll_uuid="string_example",
            transaction_type="string_example",
            payment_direction="string_example",
            x_gusto_api_version="2024-03-01",
        )
    )
    print(get_all_for_company_response)
except ApiException as e:
    print("Exception when calling ACHTransactionsApi.get_all_for_company: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from gusto_embedded_payroll_python_sdk import GustoEmbeddedPayroll, ApiException

gustoembeddedpayroll = GustoEmbeddedPayroll(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # Get all ACH transactions for a company
        get_all_for_company_response = (
            await gustoembeddedpayroll.ach_transactions.aget_all_for_company(
                company_uuid="company_uuid_example",
                contractor_payment_uuid="string_example",
                payroll_uuid="string_example",
                transaction_type="string_example",
                payment_direction="string_example",
                x_gusto_api_version="2024-03-01",
            )
        )
        print(get_all_for_company_response)
    except ApiException as e:
        print("Exception when calling ACHTransactionsApi.get_all_for_company: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from gusto_embedded_payroll_python_sdk import GustoEmbeddedPayroll, ApiException

gustoembeddedpayroll = GustoEmbeddedPayroll(access_token="YOUR_BEARER_TOKEN")

try:
    # Get all ACH transactions for a company
    get_all_for_company_response = (
        gustoembeddedpayroll.ach_transactions.raw.get_all_for_company(
            company_uuid="company_uuid_example",
            contractor_payment_uuid="string_example",
            payroll_uuid="string_example",
            transaction_type="string_example",
            payment_direction="string_example",
            x_gusto_api_version="2024-03-01",
        )
    )
    pprint(get_all_for_company_response.body)
    pprint(get_all_for_company_response.headers)
    pprint(get_all_for_company_response.status)
    pprint(get_all_for_company_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ACHTransactionsApi.get_all_for_company: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `gustoembeddedpayroll.ach_transactions.get_all_for_company`<a id="gustoembeddedpayrollach_transactionsget_all_for_company"></a>

Fetches all ACH transactions for a company.

scope: `ach_transactions:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_for_company_response = (
    gustoembeddedpayroll.ach_transactions.get_all_for_company(
        company_uuid="company_uuid_example",
        contractor_payment_uuid="string_example",
        payroll_uuid="string_example",
        transaction_type="string_example",
        payment_direction="string_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### contractor_payment_uuid: `str`<a id="contractor_payment_uuid-str"></a>

The UUID of the contractor payment

##### payroll_uuid: `str`<a id="payroll_uuid-str"></a>

The UUID of the payroll

##### transaction_type: `str`<a id="transaction_type-str"></a>

Used to filter the ACH transactions to only include those with a specific transaction type, such as \"Credit employee pay\".

##### payment_direction: `str`<a id="payment_direction-str"></a>

Used to filter the ACH transactions to only include those with a specific payment direction, either \"credit\" or \"debit\".

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`AchTransactionsGetAllForCompanyResponse`](./gusto_embedded_payroll_python_sdk/pydantic/ach_transactions_get_all_for_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/ach_transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.bank_accounts.create_from_plaid_token`<a id="gustoembeddedpayrollbank_accountscreate_from_plaid_token"></a>

This endpoint creates a new **verified** bank account by using a plaid processor token to retrieve its information.

scope: `plaid_processor:write`

> 📘
> To create a token please use the [plaid api](https://plaid.com/docs/api/processors/#processortokencreate) and select "gusto" as processor.

> 🚧 Warning - Company Bank Accounts
>
> If a default company bank account exists, it will be disabled and the new bank account will replace it as the company's default funding method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_from_plaid_token_response = (
    gustoembeddedpayroll.bank_accounts.create_from_plaid_token(
        owner_type="Company",
        owner_id="string_example",
        processor_token="string_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_type: `str`<a id="owner_type-str"></a>

The owner type of the bank account

##### owner_id: `str`<a id="owner_id-str"></a>

The owner uuid of the bank account

##### processor_token: `str`<a id="processor_token-str"></a>

The Plaid processor token

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BankAccountsCreateFromPlaidTokenRequest`](./gusto_embedded_payroll_python_sdk/type/bank_accounts_create_from_plaid_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BankAccountsCreateFromPlaidTokenResponse`](./gusto_embedded_payroll_python_sdk/pydantic/bank_accounts_create_from_plaid_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/plaid/processor_token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.bank_accounts.create_verification_deposits`<a id="gustoembeddedpayrollbank_accountscreate_verification_deposits"></a>

This endpoint creates a new company bank account.

Upon being created, two verification deposits are automatically sent to the bank account, and the bank account's verification_status is 'awaiting_deposits'. 

When the deposits are successfully transferred, the verification_status changes to 'ready_for_verification', at which point the verify endpoint can be used to verify the bank account.
After successful verification, the bank account's verification_status is 'verified'.

scope: `company_bank_accounts:write`

> 🚧 Warning
>
> If a default bank account exists, it will be disabled and the new bank account will replace it as the company's default funding method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_verification_deposits_response = (
    gustoembeddedpayroll.bank_accounts.create_verification_deposits(
        company_id="company_id_example",
        routing_number="string_example",
        account_number="string_example",
        account_type="Checking",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### routing_number: `str`<a id="routing_number-str"></a>

The bank routing number

##### account_number: `str`<a id="account_number-str"></a>

The bank account number

##### account_type: `str`<a id="account_type-str"></a>

The bank account type

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BankAccountsCreateVerificationDepositsRequest`](./gusto_embedded_payroll_python_sdk/type/bank_accounts_create_verification_deposits_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBankAccount`](./gusto_embedded_payroll_python_sdk/pydantic/company_bank_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/bank_accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.bank_accounts.list_company_bank_accounts`<a id="gustoembeddedpayrollbank_accountslist_company_bank_accounts"></a>

Returns company bank accounts. Currently, we only support a single default bank account per company.

scope: `company_bank_accounts:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_bank_accounts_response = (
    gustoembeddedpayroll.bank_accounts.list_company_bank_accounts(
        company_id="company_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`BankAccountsListCompanyBankAccountsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/bank_accounts_list_company_bank_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/bank_accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.bank_accounts.verify_micro_deposits`<a id="gustoembeddedpayrollbank_accountsverify_micro_deposits"></a>

Verify a company bank account by confirming the two micro-deposits sent to the bank account. Note that the order of the two deposits specified in request parameters does not matter. There's a maximum of 5 verification attempts, after which we will automatically initiate a new set of micro-deposits and require the bank account to be verified with the new micro-deposits.

### Bank account verification in demo<a id="bank-account-verification-in-demo"></a>

We provide the endpoint `POST '/v1/companies/{company_id}/bank_accounts/{bank_account_uuid}/send_test_deposits'` to facilitate bank account verification in the demo environment. This endpoint simulates the micro-deposits transfer and returns them in the response. You can call this endpoint as many times as you wish to retrieve the values of the two micro deposits.

```
  POST '/v1/companies/89771af8-b964-472e-8064-554dfbcb56d9/bank_accounts/ade55e57-4800-4059-9ecd-fa29cfeb6dd2/send_test_deposits'

  {
    "deposit_1": 0.02,
    "deposit_2": 0.42
  }
```

scope: `company_bank_accounts:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_micro_deposits_response = (
    gustoembeddedpayroll.bank_accounts.verify_micro_deposits(
        bank_account_uuid="bank_account_uuid_example",
        company_id="company_id_example",
        deposit_1=3.14,
        deposit_2=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_account_uuid: `str`<a id="bank_account_uuid-str"></a>

The UUID of the bank account

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### deposit_1: `Union[int, float]`<a id="deposit_1-unionint-float"></a>

The dollar amount of the first micro-deposit

##### deposit_2: `Union[int, float]`<a id="deposit_2-unionint-float"></a>

The dollar amount of the second micro-deposit

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BankAccountsVerifyMicroDepositsRequest`](./gusto_embedded_payroll_python_sdk/type/bank_accounts_verify_micro_deposits_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBankAccount`](./gusto_embedded_payroll_python_sdk/pydantic/company_bank_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/bank_accounts/{bank_account_uuid}/verify` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.accept_terms_of_service`<a id="gustoembeddedpayrollcompaniesaccept_terms_of_service"></a>

Accept the Gusto Embedded Payroll's [Terms of Service](https://flows.gusto.com/terms).
The user must have a role in the company in order to accept the Terms of Service.

scope: `terms_of_services:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
accept_terms_of_service_response = (
    gustoembeddedpayroll.companies.accept_terms_of_service(
        email="string_example",
        ip_address="string_example",
        external_user_id="string_example",
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

The user's email address on Gusto. You can retrieve the user's email via company's `/admins`, `/employees`, `/signatories`, and `/contractors` endpoints.

##### ip_address: `str`<a id="ip_address-str"></a>

The IP address of the user who viewed and accepted the Terms of Service.

##### external_user_id: `str`<a id="external_user_id-str"></a>

The user ID on your platform.

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompaniesAcceptTermsOfServiceRequest`](./gusto_embedded_payroll_python_sdk/type/companies_accept_terms_of_service_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesAcceptTermsOfServiceResponse`](./gusto_embedded_payroll_python_sdk/pydantic/companies_accept_terms_of_service_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/partner_managed_companies/{company_uuid}/accept_terms_of_service` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.create_admin`<a id="gustoembeddedpayrollcompaniescreate_admin"></a>

Creates a new admin for a company.
If the email matches an existing user, this will create an admin account for the current user. Otherwise, this will create a new user.

scope: `company_admin:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_admin_response = gustoembeddedpayroll.companies.create_admin(
    first_name="string_example",
    last_name="string_example",
    email="string_example",
    company_id="company_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

The first name of the admin.

##### last_name: `str`<a id="last_name-str"></a>

The last name of the admin.

##### email: `str`<a id="email-str"></a>

The email of the admin for Gusto's system. If the email matches an existing user, this will create an admin account for them.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompaniesCreateAdminRequest`](./gusto_embedded_payroll_python_sdk/type/companies_create_admin_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Admin`](./gusto_embedded_payroll_python_sdk/pydantic/admin.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/admins` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.create_partner_managed_company`<a id="gustoembeddedpayrollcompaniescreate_partner_managed_company"></a>

Create a partner managed company. When you successfully call the API, it does the following:
* Creates a new company in Gusto
* Creates a new user using the provided email if the user does not already exist.
* Makes the user the primary payroll administrator of the new company.

In response, you will receive oauth access tokens for the created company.

IMPORTANT: the returned access and refresh tokens are reserved for this company only. They cannot be used to access other companies AND previously granted tokens cannot be used to access this company.

> 📘 Token Authentication
>
> this endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#retrieving-access-tokens)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_partner_managed_company_response = (
    gustoembeddedpayroll.companies.create_partner_managed_company(
        user={
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "email": "email_example",
        },
        company={
            "name": "name_example",
        },
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user: [`CompaniesCreatePartnerManagedCompanyRequestUser`](./gusto_embedded_payroll_python_sdk/type/companies_create_partner_managed_company_request_user.py)<a id="user-companiescreatepartnermanagedcompanyrequestusergusto_embedded_payroll_python_sdktypecompanies_create_partner_managed_company_request_userpy"></a>


##### company: [`CompaniesCreatePartnerManagedCompanyRequestCompany`](./gusto_embedded_payroll_python_sdk/type/companies_create_partner_managed_company_request_company.py)<a id="company-companiescreatepartnermanagedcompanyrequestcompanygusto_embedded_payroll_python_sdktypecompanies_create_partner_managed_company_request_companypy"></a>


##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompaniesCreatePartnerManagedCompanyRequest`](./gusto_embedded_payroll_python_sdk/type/companies_create_partner_managed_company_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesCreatePartnerManagedCompanyResponse`](./gusto_embedded_payroll_python_sdk/pydantic/companies_create_partner_managed_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/partner_managed_companies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.finish_onboarding`<a id="gustoembeddedpayrollcompaniesfinish_onboarding"></a>

Finalize a given company's onboarding process.

### Approve a company in demo<a id="approve-a-company-in-demo"></a>
After a company is finished onboarding, Gusto requires an additional step to review and approve that company.
In production environments, this step is required for risk-analysis purposes.

We provide the endpoint `PUT '/v1/companies/{company_uuid}/approve'` to facilitate company approvals in the demo environment.

```shell
PUT '/v1/companies/89771af8-b964-472e-8064-554dfbcb56d9/approve'

# Response: Company object, with company_status: 'Approved'
```

scope: `companies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
finish_onboarding_response = gustoembeddedpayroll.companies.finish_onboarding(
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyOnboardingStatus`](./gusto_embedded_payroll_python_sdk/pydantic/company_onboarding_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/finish_onboarding` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.get_all_admins`<a id="gustoembeddedpayrollcompaniesget_all_admins"></a>

Returns a list of all the admins at a company

scope: `company_admin:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_admins_response = gustoembeddedpayroll.companies.get_all_admins(
    company_id="company_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesGetAllAdminsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/companies_get_all_admins_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/admins` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.get_company`<a id="gustoembeddedpayrollcompaniesget_company"></a>

Get a company.         
The employees:read scope is required to return home_address and non-work locations.         
The company_admin:read scope is required to return primary_payroll_admin.         
The signatories:read scope is required to return primary_signatory.         

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_response = gustoembeddedpayroll.companies.get_company(
    company_id="company_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Company`](./gusto_embedded_payroll_python_sdk/pydantic/company.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.get_custom_fields`<a id="gustoembeddedpayrollcompaniesget_custom_fields"></a>

Returns a list of the custom fields of the company. Useful when you need to know the schema of custom fields for an entire company

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_response = gustoembeddedpayroll.companies.get_custom_fields(
    company_id="company_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesGetCustomFieldsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/companies_get_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.get_onboarding_status`<a id="gustoembeddedpayrollcompaniesget_onboarding_status"></a>

Get company's onboarding status.
The data returned helps inform the required onboarding steps and respective completion status.

scope: `company_onboarding_status:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_onboarding_status_response = gustoembeddedpayroll.companies.get_onboarding_status(
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyOnboardingStatus`](./gusto_embedded_payroll_python_sdk/pydantic/company_onboarding_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/onboarding_status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.get_terms_of_service_status`<a id="gustoembeddedpayrollcompaniesget_terms_of_service_status"></a>

Retrieve the user acceptance status of the Gusto Embedded Payroll's [Terms of Service](https://flows.gusto.com/terms).

scope: `terms_of_services:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_terms_of_service_status_response = (
    gustoembeddedpayroll.companies.get_terms_of_service_status(
        email="string_example",
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

The user's email address on Gusto. You can retrieve the user's email via company's `/admins`, `/employees`, `/signatories`, and `/contractors` endpoints.

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompaniesGetTermsOfServiceStatusRequest`](./gusto_embedded_payroll_python_sdk/type/companies_get_terms_of_service_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesGetTermsOfServiceStatusResponse`](./gusto_embedded_payroll_python_sdk/pydantic/companies_get_terms_of_service_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/partner_managed_companies/{company_uuid}/retrieve_terms_of_service` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.companies.migrate_to_embedded_payroll`<a id="gustoembeddedpayrollcompaniesmigrate_to_embedded_payroll"></a>

Migrate an existing Gusto customer to your embedded payroll product.

To use this endpoint, the customer will need to connect their Gusto account to your application using [OAuth2](https://docs.gusto.com/embedded-payroll/docs/oauth2) then view and [accept the Embedded Payroll Terms of Service](https://docs.gusto.com/embedded-payroll/reference/post-partner-managed-companies-company_uuid-accept_terms_of_service).

scope: `partner_managed_companies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
migrate_to_embedded_payroll_response = (
    gustoembeddedpayroll.companies.migrate_to_embedded_payroll(
        email="string_example",
        ip_address="string_example",
        external_user_id="string_example",
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Email of the company signatory who is authorized to accept our [Terms of Service](https://flows.gusto.com/terms) and migration decision. You can retrieve the signatory email from the `GET /v/1/companies/{company_id}/signatories` endpoint.

##### ip_address: `str`<a id="ip_address-str"></a>

The IP address of the signatory who viewed and accepted the Terms of Service.

##### external_user_id: `str`<a id="external_user_id-str"></a>

The signatory's user ID on your platform.

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompaniesMigrateToEmbeddedPayrollRequest`](./gusto_embedded_payroll_python_sdk/type/companies_migrate_to_embedded_payroll_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesMigrateToEmbeddedPayrollResponse`](./gusto_embedded_payroll_python_sdk/pydantic/companies_migrate_to_embedded_payroll_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/partner_managed_companies/{company_uuid}/migrate` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_benefits.create_benefit`<a id="gustoembeddedpayrollcompany_benefitscreate_benefit"></a>

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

scope: `company_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_benefit_response = gustoembeddedpayroll.company_benefits.create_benefit(
    description="string_example",
    company_id="company_id_example",
    benefit_type=3.14,
    active=True,
    responsible_for_employer_taxes=True,
    responsible_for_employee_w2=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

The description of the company benefit.For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like “Kaiser Permanente” or “Blue Cross/ Blue Shield”.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### benefit_type: `Union[int, float]`<a id="benefit_type-unionint-float"></a>

The ID of the benefit to which the company benefit belongs.

##### active: `bool`<a id="active-bool"></a>

Whether this benefit is active for employee participation.

##### responsible_for_employer_taxes: `bool`<a id="responsible_for_employer_taxes-bool"></a>

Whether the employer is subject to pay employer taxes when an employee is on leave. Only applicable to third party sick pay benefits.

##### responsible_for_employee_w2: `bool`<a id="responsible_for_employee_w2-bool"></a>

Whether the employer is subject to file W-2 forms for an employee on leave. Only applicable to third party sick pay benefits.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyBenefitsCreateBenefitRequest`](./gusto_embedded_payroll_python_sdk/type/company_benefits_create_benefit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefit`](./gusto_embedded_payroll_python_sdk/pydantic/company_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/company_benefits` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_benefits.delete_benefit`<a id="gustoembeddedpayrollcompany_benefitsdelete_benefit"></a>

The following must be true in order to delete a company benefit
  - There are no employee benefits associated with the company benefit
  - There are no payroll items associated with the company benefit
  - The benefit is not managed by a Partner or by Gusto (type must be 'External')

scope: `company_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.company_benefits.delete_benefit(
    company_benefit_id="company_benefit_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_benefit_id: `str`<a id="company_benefit_id-str"></a>

The UUID of the company benefit

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_benefits/{company_benefit_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_benefits.get_benefit_by_id`<a id="gustoembeddedpayrollcompany_benefitsget_benefit_by_id"></a>

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

When with_employee_benefits parameter with true value is passed, employee_benefits:read scope is required to return employee_benefits.

scope: `company_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_benefit_by_id_response = gustoembeddedpayroll.company_benefits.get_benefit_by_id(
    company_benefit_id="company_benefit_id_example",
    with_employee_benefits=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_benefit_id: `str`<a id="company_benefit_id-str"></a>

The UUID of the company benefit

##### with_employee_benefits: `bool`<a id="with_employee_benefits-bool"></a>

Whether to return employee benefits associated with the benefit

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefitWithEmployeeBenefits`](./gusto_embedded_payroll_python_sdk/pydantic/company_benefit_with_employee_benefits.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_benefits/{company_benefit_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_benefits.get_benefit_fields_requirements_by_id`<a id="gustoembeddedpayrollcompany_benefitsget_benefit_fields_requirements_by_id"></a>

Returns field requirements for the requested benefit type.

scope: `benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_benefit_fields_requirements_by_id_response = (
    gustoembeddedpayroll.company_benefits.get_benefit_fields_requirements_by_id(
        benefit_id="benefit_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### benefit_id: `str`<a id="benefit_id-str"></a>

The benefit type in Gusto.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`BenefitTypeRequirements`](./gusto_embedded_payroll_python_sdk/pydantic/benefit_type_requirements.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/benefits/{benefit_id}/requirements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_benefits.get_benefit_summary_by_id`<a id="gustoembeddedpayrollcompany_benefitsget_benefit_summary_by_id"></a>

Returns summary benefit data for the requested company benefit id.

Benefits containing PHI are only visible to applications with the `company_benefits:read:phi` scope.

scope: `company_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_benefit_summary_by_id_response = (
    gustoembeddedpayroll.company_benefits.get_benefit_summary_by_id(
        company_benefit_id="company_benefit_id_example",
        start_date="2022-01-01",
        end_date="2022-12-31",
        detailed=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_benefit_id: `str`<a id="company_benefit_id-str"></a>

The UUID of the company benefit

##### start_date: `str`<a id="start_date-str"></a>

The start date for which to retrieve company benefit summary

##### end_date: `str`<a id="end_date-str"></a>

The end date for which to retrieve company benefit summary

##### detailed: `bool`<a id="detailed-bool"></a>

Display employee payroll item summary

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`BenefitSummary`](./gusto_embedded_payroll_python_sdk/pydantic/benefit_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_benefits/{company_benefit_id}/summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_benefits.get_benefits_for_company`<a id="gustoembeddedpayrollcompany_benefitsget_benefits_for_company"></a>

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

Benefits containing PHI are only visible to applications with the `company_benefits:read:phi` scope.

scope: `company_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_benefits_for_company_response = (
    gustoembeddedpayroll.company_benefits.get_benefits_for_company(
        company_id="company_id_example",
        enrollment_count=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### enrollment_count: `bool`<a id="enrollment_count-bool"></a>

Whether to return employee enrollment count

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefitsGetBenefitsForCompanyResponse`](./gusto_embedded_payroll_python_sdk/pydantic/company_benefits_get_benefits_for_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/company_benefits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_benefits.get_supported_benefit_by_id`<a id="gustoembeddedpayrollcompany_benefitsget_supported_benefit_by_id"></a>

Returns a benefit supported by Gusto.

The benefit object in Gusto contains high level information about a particular benefit type and its tax considerations. When companies choose to offer a benefit, they are creating a Company Benefit object associated with a particular benefit.

scope: `benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_supported_benefit_by_id_response = (
    gustoembeddedpayroll.company_benefits.get_supported_benefit_by_id(
        benefit_id="benefit_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### benefit_id: `str`<a id="benefit_id-str"></a>

The benefit type in Gusto.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`SupportedBenefit`](./gusto_embedded_payroll_python_sdk/pydantic/supported_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/benefits/{benefit_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_benefits.list_supported_benefits`<a id="gustoembeddedpayrollcompany_benefitslist_supported_benefits"></a>

Returns all benefits supported by Gusto.

The benefit object in Gusto contains high level information about a particular benefit type and its tax considerations. When companies choose to offer a benefit, they are creating a Company Benefit object associated with a particular benefit.

scope: `benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_supported_benefits_response = (
    gustoembeddedpayroll.company_benefits.list_supported_benefits(
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefitsListSupportedBenefitsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/company_benefits_list_supported_benefits_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/benefits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_benefits.update_benefit`<a id="gustoembeddedpayrollcompany_benefitsupdate_benefit"></a>

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

scope: `company_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_benefit_response = gustoembeddedpayroll.company_benefits.update_benefit(
    version="string_example",
    company_benefit_id="company_benefit_id_example",
    description="string_example",
    active=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### company_benefit_id: `str`<a id="company_benefit_id-str"></a>

The UUID of the company benefit

##### description: `str`<a id="description-str"></a>

The description of the company benefit.For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like “Kaiser Permanente” or “Blue Cross/ Blue Shield”.

##### active: `bool`<a id="active-bool"></a>

Whether this benefit is active for employee participation. Company benefits may only be deactivated if no employees are actively participating.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyBenefitsUpdateBenefitRequest`](./gusto_embedded_payroll_python_sdk/type/company_benefits_update_benefit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefit`](./gusto_embedded_payroll_python_sdk/pydantic/company_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_benefits/{company_benefit_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_forms.get_all_forms`<a id="gustoembeddedpayrollcompany_formsget_all_forms"></a>

Get a list of all company's forms

scope: `company_forms:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_forms_response = gustoembeddedpayroll.company_forms.get_all_forms(
    company_id="company_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyFormsGetAllFormsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/company_forms_get_all_forms_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/forms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_forms.get_form_by_id`<a id="gustoembeddedpayrollcompany_formsget_form_by_id"></a>

Get a company form

scope: `company_forms:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_form_by_id_response = gustoembeddedpayroll.company_forms.get_form_by_id(
    form_id="form_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### form_id: `str`<a id="form_id-str"></a>

The UUID of the form

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Form`](./gusto_embedded_payroll_python_sdk/pydantic/form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/forms/{form_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_forms.get_pdf_link`<a id="gustoembeddedpayrollcompany_formsget_pdf_link"></a>

Get the link to the form PDF

scope: `company_forms:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pdf_link_response = gustoembeddedpayroll.company_forms.get_pdf_link(
    form_id="form_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### form_id: `str`<a id="form_id-str"></a>

The UUID of the form

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`FormPdf`](./gusto_embedded_payroll_python_sdk/pydantic/form_pdf.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/forms/{form_id}/pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.company_forms.sign_form`<a id="gustoembeddedpayrollcompany_formssign_form"></a>

Sign a company form

scope: `company_forms:sign`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sign_form_response = gustoembeddedpayroll.company_forms.sign_form(
    signature_text="string_example",
    agree=True,
    signed_by_ip_address="string_example",
    form_id="form_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### signature_text: `str`<a id="signature_text-str"></a>

The signature

##### agree: `bool`<a id="agree-bool"></a>

whether you agree to sign electronically

##### signed_by_ip_address: `str`<a id="signed_by_ip_address-str"></a>

The IP address of the signatory who signed the form.

##### form_id: `str`<a id="form_id-str"></a>

The UUID of the form

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyFormsSignFormRequest`](./gusto_embedded_payroll_python_sdk/type/company_forms_sign_form_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Form`](./gusto_embedded_payroll_python_sdk/pydantic/form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/forms/{form_id}/sign` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_forms.create1099_form`<a id="gustoembeddedpayrollcontractor_formscreate1099_form"></a>

> 🚧 Demo action
>
> This action is only available in the Demo environment

Generates a 1099 document for testing purposes.

scope: `contractors:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create1099_form_response = gustoembeddedpayroll.contractor_forms.create1099_form(
    contractor_id="string_example",
    year=1,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_id: `str`<a id="contractor_id-str"></a>

The contractor UUID.

##### year: `int`<a id="year-int"></a>

Must be equal to or more recent than 2015. If not specified, defaults to the previous year. 

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorFormsCreate1099FormRequest`](./gusto_embedded_payroll_python_sdk/type/contractor_forms_create1099_form_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Form1099`](./gusto_embedded_payroll_python_sdk/pydantic/form1099.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/sandbox/generate_1099` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_forms.get_by_id_form`<a id="gustoembeddedpayrollcontractor_formsget_by_id_form"></a>

Get a contractor form

scope: `contractor_forms:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_form_response = gustoembeddedpayroll.contractor_forms.get_by_id_form(
    contractor_uuid="contractor_uuid_example",
    form_id="form_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### form_id: `str`<a id="form_id-str"></a>

The UUID of the form

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Form1099`](./gusto_embedded_payroll_python_sdk/pydantic/form1099.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/forms/{form_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_forms.get_pdf_link`<a id="gustoembeddedpayrollcontractor_formsget_pdf_link"></a>

Get the link to the form PDF

scope: `contractor_forms:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pdf_link_response = gustoembeddedpayroll.contractor_forms.get_pdf_link(
    contractor_uuid="contractor_uuid_example",
    form_id="form_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### form_id: `str`<a id="form_id-str"></a>

The UUID of the form

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`FormPdf`](./gusto_embedded_payroll_python_sdk/pydantic/form_pdf.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/forms/{form_id}/pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_forms.list_all`<a id="gustoembeddedpayrollcontractor_formslist_all"></a>

Get a list of all contractor's forms

scope: `contractor_forms:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = gustoembeddedpayroll.contractor_forms.list_all(
    contractor_uuid="contractor_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorFormsListAllResponse`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_forms_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/forms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payment_method.create_bank_account`<a id="gustoembeddedpayrollcontractor_payment_methodcreate_bank_account"></a>

Creates a contractor bank account.

Note: We currently only support one bank account per contractor. Using this endpoint on a contractor who has already
has a bank account will just replace it.

scope: `contractor_payment_methods:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bank_account_response = (
    gustoembeddedpayroll.contractor_payment_method.create_bank_account(
        name="string_example",
        routing_number="string_example",
        account_number="string_example",
        account_type="Checking",
        contractor_uuid="contractor_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### routing_number: `str`<a id="routing_number-str"></a>

##### account_number: `str`<a id="account_number-str"></a>

##### account_type: `str`<a id="account_type-str"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorPaymentMethodCreateBankAccountRequest`](./gusto_embedded_payroll_python_sdk/type/contractor_payment_method_create_bank_account_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContractorBankAccount`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_bank_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/bank_accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payment_method.get_contractor_payment_method`<a id="gustoembeddedpayrollcontractor_payment_methodget_contractor_payment_method"></a>

Fetches a contractor's payment method. A contractor payment method
describes how the payment should be split across the contractor's associated
bank accounts.

scope: `contractor_payment_methods:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_contractor_payment_method_response = (
    gustoembeddedpayroll.contractor_payment_method.get_contractor_payment_method(
        contractor_uuid="contractor_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPaymentMethod`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/payment_method` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payment_method.list_bank_accounts`<a id="gustoembeddedpayrollcontractor_payment_methodlist_bank_accounts"></a>

Returns all contractor bank accounts.

scope: `contractor_payment_methods:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_bank_accounts_response = (
    gustoembeddedpayroll.contractor_payment_method.list_bank_accounts(
        contractor_uuid="contractor_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPaymentMethodListBankAccountsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_payment_method_list_bank_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/bank_accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payment_method.update_bank_account`<a id="gustoembeddedpayrollcontractor_payment_methodupdate_bank_account"></a>

Updates a contractor's payment method. Note that creating a contractor
bank account will also update the contractor's payment method.

scope: `contractor_payment_methods:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_bank_account_response = (
    gustoembeddedpayroll.contractor_payment_method.update_bank_account(
        body=None,
        contractor_uuid="contractor_uuid_example",
        version="string_example",
        type="Direct Deposit",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### type: `str`<a id="type-str"></a>

The payment method type. If type is Direct Deposit, the contractor is required to have a bank account. see [Bank account endpoint](./post-v1-contractors-contractor_uuid-bank_accounts)

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorPaymentMethodUpdateBankAccountRequest`](./gusto_embedded_payroll_python_sdk/type/contractor_payment_method_update_bank_account_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPaymentMethod`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/payment_method` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payments.cancel_payment`<a id="gustoembeddedpayrollcontractor_paymentscancel_payment"></a>

Cancels and deletes a contractor payment. If the contractor payment has already started processing, the payment cannot be cancelled.

scope: `payrolls:run`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.contractor_payments.cancel_payment(
    company_id="company_id_example",
    contractor_payment_id="contractor_payment_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### contractor_payment_id: `str`<a id="contractor_payment_id-str"></a>

The UUID of the contractor payment

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractor_payments/{contractor_payment_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payments.create_payment`<a id="gustoembeddedpayrollcontractor_paymentscreate_payment"></a>

Pay a contractor. Information needed depends on the contractor's wage type (hourly vs fixed)

scope: `payrolls:run`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payment_response = gustoembeddedpayroll.contractor_payments.create_payment(
    contractor_uuid="string_example",
    date="2020-01-01",
    company_id="company_id_example",
    payment_method="Direct Deposit",
    wage=5000,
    hours=40,
    bonus=500,
    reimbursement=20,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The contractor receiving the payment

##### date: `date`<a id="date-date"></a>

The contractor receiving the payment

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payment_method: `str`<a id="payment_method-str"></a>

##### wage: `Union[int, float]`<a id="wage-unionint-float"></a>

If the contractor is on a fixed wage, this is the fixed wage payment for the contractor, regardless of hours worked

##### hours: `Union[int, float]`<a id="hours-unionint-float"></a>

If the contractor is on an hourly wage, this is the number of hours that the contractor worked for the payment

##### bonus: `Union[int, float]`<a id="bonus-unionint-float"></a>

If the contractor is on an hourly wage, this is the bonus the contractor earned

##### reimbursement: `Union[int, float]`<a id="reimbursement-unionint-float"></a>

Reimbursed wages for the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorPaymentsCreatePaymentRequest`](./gusto_embedded_payroll_python_sdk/type/contractor_payments_create_payment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPayment`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_payment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractor_payments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payments.fund_contractor_payment`<a id="gustoembeddedpayrollcontractor_paymentsfund_contractor_payment"></a>

> 🚧 Demo action
>
> This action is only available in the Demo environment

Simulate funding a contractor payment. Funding only occurs automatically in the production environment when bank transactions are generated. Use this action in the demo environment to transition a contractor payment's `status` from `Unfunded` to `Funded`. A `Funded` status is required for generating a contractor payment receipt.

scope: `payrolls:run`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
fund_contractor_payment_response = (
    gustoembeddedpayroll.contractor_payments.fund_contractor_payment(
        contractor_payment_uuid="contractor_payment_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_payment_uuid: `str`<a id="contractor_payment_uuid-str"></a>

The UUID of the contractor payment

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPayment`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_payment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractor_payments/{contractor_payment_uuid}/fund` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payments.get_single_payment`<a id="gustoembeddedpayrollcontractor_paymentsget_single_payment"></a>

Returns a single contractor payments

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_payment_response = (
    gustoembeddedpayroll.contractor_payments.get_single_payment(
        company_id="company_id_example",
        contractor_payment_id="contractor_payment_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### contractor_payment_id: `str`<a id="contractor_payment_id-str"></a>

The UUID of the contractor payment

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPayment`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_payment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractor_payments/{contractor_payment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payments.get_single_receipt`<a id="gustoembeddedpayrollcontractor_paymentsget_single_receipt"></a>

Returns a contractor payment receipt.

Notes:
* Receipts are only available for direct deposit payments and are only available once those payments have been funded.
* Payroll Receipt requests for payrolls which do not have receipts available (e.g. payment by check) will return a 404 status.
* Hour and dollar amounts are returned as string representations of numeric decimals.
* Dollar amounts are represented to the cent.
* If no data has yet be inserted for a given field, it defaults to “0.00” (for fixed amounts).

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_receipt_response = (
    gustoembeddedpayroll.contractor_payments.get_single_receipt(
        contractor_payment_uuid="contractor_payment_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_payment_uuid: `str`<a id="contractor_payment_uuid-str"></a>

The UUID of the contractor payment

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPaymentReceipt`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_payment_receipt.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractor_payments/{contractor_payment_uuid}/receipt` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payments.get_within_time_period_totals`<a id="gustoembeddedpayrollcontractor_paymentsget_within_time_period_totals"></a>

Returns an object containing individual contractor payments, within a given time period, including totals.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_within_time_period_totals_response = (
    gustoembeddedpayroll.contractor_payments.get_within_time_period_totals(
        company_id="company_id_example",
        start_date="2020-01-01",
        end_date="2020-12-31",
        contractor_uuid="string_example",
        group_by_date=True,
        page=3.14,
        per=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### start_date: `str`<a id="start_date-str"></a>

The time period for which to retrieve contractor payments

##### end_date: `str`<a id="end_date-str"></a>

The time period for which to retrieve contractor payments

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor. When specified, will load all payments for that contractor.

##### group_by_date: `bool`<a id="group_by_date-bool"></a>

Display contractor payments results group by check date if set to true.

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPaymentsGetWithinTimePeriodTotalsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_payments_get_within_time_period_totals_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractor_payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractor_payments.preview_debit_date`<a id="gustoembeddedpayrollcontractor_paymentspreview_debit_date"></a>

Returns a debit_date dependent on the ACH payment speed of the company.

If the payment method is Check or Historical payment, the debit_date will be the same as the check_date.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
preview_debit_date_response = (
    gustoembeddedpayroll.contractor_payments.preview_debit_date(
        company_uuid="company_uuid_example",
        contractor_payments=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### contractor_payments: [`ContractorPaymentsPreviewDebitDateRequestContractorPayments`](./gusto_embedded_payroll_python_sdk/type/contractor_payments_preview_debit_date_request_contractor_payments.py)<a id="contractor_payments-contractorpaymentspreviewdebitdaterequestcontractorpaymentsgusto_embedded_payroll_python_sdktypecontractor_payments_preview_debit_date_request_contractor_paymentspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorPaymentsPreviewDebitDateRequest`](./gusto_embedded_payroll_python_sdk/type/contractor_payments_preview_debit_date_request.py)
a list of contractor payments.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPaymentsPreviewDebitDateResponse`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_payments_preview_debit_date_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/contractor_payments/preview` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractors.change_onboarding_status`<a id="gustoembeddedpayrollcontractorschange_onboarding_status"></a>

Updates a contractor's onboarding status.

scope: `contractors:write`

Below is a list of valid onboarding status changes depending on the intended action to be performed on behalf of the contractor.

| Action | current onboarding_status | new onboarding_status |
|:------------------|:------------:|----------:|
| Mark a contractor as self-onboarding | `admin_onboarding_incomplete` | `self_onboarding_not_invited` |
| Invite an employee to self-onboard | `admin_onboarding_incomplete` or `self_onboarding_not_invited` | `self_onboarding_invited` |
| Cancel an employee's self-onboarding | `self_onboarding_invited` or `self_onboarding_not_invited` | `admin_onboarding_incomplete` |
| Review an employee's self-onboarded info | `self_onboarding_started` | `self_onboarding_review` |
| Finish an employee's onboarding | `admin_onboarding_incomplete` or `self_onboarding_review` | `onboarding_completed` |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_onboarding_status_response = (
    gustoembeddedpayroll.contractors.change_onboarding_status(
        onboarding_status="onboarding_completed",
        contractor_uuid="contractor_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### onboarding_status: `str`<a id="onboarding_status-str"></a>

The updated onboarding status for the employee

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorsChangeOnboardingStatusRequest`](./gusto_embedded_payroll_python_sdk/type/contractors_change_onboarding_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContractorOnboardingStatus`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_onboarding_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/onboarding_status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractors.create_new_contractor`<a id="gustoembeddedpayrollcontractorscreate_new_contractor"></a>

Create an individual or business contractor.

scope: `contractors:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_contractor_response = gustoembeddedpayroll.contractors.create_new_contractor(
    body=None,
    company_id="company_id_example",
    type="Individual",
    wage_type="Fixed",
    start_date="2020-01-11",
    hourly_rate="40.0",
    self_onboarding=False,
    email="string_example",
    first_name="string_example",
    last_name="string_example",
    middle_initial="string_example",
    file_new_hire_report=False,
    work_state="string_example",
    ssn="048072888",
    business_name="string_example",
    ein="string_example",
    is_active=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### type: `str`<a id="type-str"></a>

The contractor type.

##### wage_type: `str`<a id="wage_type-str"></a>

The contractor’s wage type. 

##### start_date: `str`<a id="start_date-str"></a>

The day when the contractor will start working for the company. 

##### hourly_rate: `str`<a id="hourly_rate-str"></a>

The contractor’s hourly rate. This attribute is required if the wage_type is `Hourly`.

##### self_onboarding: `bool`<a id="self_onboarding-bool"></a>

Whether the contractor or the payroll admin will complete onboarding in Gusto. Self-onboarding is recommended so that contractors receive Gusto accounts. If self_onboarding is true, then email is required.

##### email: `str`<a id="email-str"></a>

The contractor’s email address.

##### first_name: `str`<a id="first_name-str"></a>

The contractor’s first name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.

##### last_name: `str`<a id="last_name-str"></a>

The contractor’s last name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.

##### middle_initial: `str`<a id="middle_initial-str"></a>

The contractor’s middle initial. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.

##### file_new_hire_report: `bool`<a id="file_new_hire_report-bool"></a>

The boolean flag indicating whether Gusto will file a new hire report for the contractor. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.

##### work_state: `Optional[str]`<a id="work_state-optionalstr"></a>

State where the contractor will be conducting the majority of their work for the company. This value is used when generating the new hire report. This attribute is required for `Individual` contractors if `file_new_hire_report` is true and will be ignored for `Business` contractors.

##### ssn: `str`<a id="ssn-str"></a>

This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors. Social security number is needed to file the annual 1099 tax form.

##### business_name: `str`<a id="business_name-str"></a>

The name of the contractor business. This attribute is required for `Business` contractors and will be ignored for `Individual` contractors.

##### ein: `str`<a id="ein-str"></a>

The employer identification number of the contractor business. This attribute is optional for `Business` contractors and will be ignored for `Individual` contractors.

##### is_active: `bool`<a id="is_active-bool"></a>

The status of the contractor.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorsCreateNewContractorRequest`](./gusto_embedded_payroll_python_sdk/type/contractors_create_new_contractor_request.py)
Create an individual or business contractor.

#### 🔄 Return<a id="🔄-return"></a>

[`Contractor`](./gusto_embedded_payroll_python_sdk/pydantic/contractor.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractors` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractors.delete_contractor`<a id="gustoembeddedpayrollcontractorsdelete_contractor"></a>

A contractor can only be deleted when there are no contractor payments.

scope: `contractors:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.contractors.delete_contractor(
    contractor_id="contractor_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_id: `str`<a id="contractor_id-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractors.get_address`<a id="gustoembeddedpayrollcontractorsget_address"></a>

The address of a contractor is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

scope: `contractors:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_address_response = gustoembeddedpayroll.contractors.get_address(
    contractor_uuid="contractor_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorAddress`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/address` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractors.get_by_id`<a id="gustoembeddedpayrollcontractorsget_by_id"></a>

Get a contractor.

scope: `contractors:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = gustoembeddedpayroll.contractors.get_by_id(
    contractor_id="contractor_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_id: `str`<a id="contractor_id-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Contractor`](./gusto_embedded_payroll_python_sdk/pydantic/contractor.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractors.get_company_contractors`<a id="gustoembeddedpayrollcontractorsget_company_contractors"></a>

Get all contractors, active and inactive, individual and business, for a company.

scope: `contractors:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_contractors_response = (
    gustoembeddedpayroll.contractors.get_company_contractors(
        company_id="company_id_example",
        page=3.14,
        per=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorsGetCompanyContractorsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/contractors_get_company_contractors_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractors.get_onboarding_status`<a id="gustoembeddedpayrollcontractorsget_onboarding_status"></a>

Retrieves a contractor's onboarding status. The data returned helps inform the required onboarding steps and respective completion status.

scope: `contractors:read`

## onboarding_status<a id="onboarding_status"></a>

### Admin-facilitated onboarding<a id="admin-facilitated-onboarding"></a>
| onboarding_status | Description |
|:------------------|------------:|
| `admin_onboarding_incomplete` | Admin needs to enter basic information about the contractor. |
| `admin_onboarding_review` | All information has been completed and admin needs to confirm onboarding. |
| `onboarding_completed` | Contractor has been fully onboarded and verified. |

### Contractor self-onboarding<a id="contractor-self-onboarding"></a>

| onboarding_status | Description |
| --- | ----------- |
| `admin_onboarding_incomplete` | Admin needs to enter basic information about the contractor. |
| `self_onboarding_not_invited` | Admin has the intention to invite the contractor to self-onboard (e.g., marking a checkbox), but the system has not yet sent the invitation. |
| `self_onboarding_invited` | Contractor has been sent an invitation to self-onboard. |
| `self_onboarding_started` | Contractor has started the self-onboarding process. |
| `self_onboarding_review` | Admin needs to review contractors's entered information and confirm onboarding. |
| `onboarding_completed` | Contractor has been fully onboarded and verified. |

## onboarding_steps<a id="onboarding_steps"></a>

| onboarding_steps | Requirement(s) to be completed |
|:-----------------|-------------------------------:|
| `basic_details` | Add individual contractor's first name, last name, social security number or Business name and EIN depending on the contractor type |
| `add_address` | Add contractor address. |
| `compensation_details` | Add contractor compensation. |
| `payment_details` | Set up contractor's direct deposit or set to check. |
| `sign_documents` | Contractor forms (e.g., W9) are generated & signed. |
| `file_new_hire_report` | Contractor new hire report is generated. |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_onboarding_status_response = gustoembeddedpayroll.contractors.get_onboarding_status(
    contractor_uuid="contractor_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorOnboardingStatus`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_onboarding_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/onboarding_status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractors.update_address`<a id="gustoembeddedpayrollcontractorsupdate_address"></a>

The address of a contractor is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

scope: `contractors:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_address_response = gustoembeddedpayroll.contractors.update_address(
    body=None,
    contractor_uuid="contractor_uuid_example",
    version="string_example",
    street_1="string_example",
    street_2="string_example",
    city="string_example",
    state="string_example",
    zip="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### street_1: `str`<a id="street_1-str"></a>

##### street_2: `str`<a id="street_2-str"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorsUpdateAddressRequest`](./gusto_embedded_payroll_python_sdk/type/contractors_update_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContractorAddress`](./gusto_embedded_payroll_python_sdk/pydantic/contractor_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_uuid}/address` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.contractors.update_contractor`<a id="gustoembeddedpayrollcontractorsupdate_contractor"></a>

Update a contractor.

scope: `contractors:write`

> 🚧 Warning
>
> Watch out when changing a contractor's type (when the contractor is finished onboarding). Specifically, changing contractor type can be dangerous since Gusto won’t recognize and file two separate 1099s if they simply change from business to individual

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_contractor_response = gustoembeddedpayroll.contractors.update_contractor(
    body=None,
    contractor_id="contractor_id_example",
    version="string_example",
    type="Individual",
    wage_type="Fixed",
    start_date="2020-01-11",
    hourly_rate="40.0",
    self_onboarding=False,
    email="string_example",
    first_name="string_example",
    last_name="string_example",
    middle_initial="string_example",
    file_new_hire_report=False,
    work_state="string_example",
    ssn="048072888",
    business_name="string_example",
    ein="string_example",
    is_active=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_id: `str`<a id="contractor_id-str"></a>

The UUID of the contractor

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### type: `str`<a id="type-str"></a>

The contractor type.

##### wage_type: `str`<a id="wage_type-str"></a>

The contractor’s wage type. 

##### start_date: `str`<a id="start_date-str"></a>

The day when the contractor will start working for the company. 

##### hourly_rate: `str`<a id="hourly_rate-str"></a>

The contractor’s hourly rate. This attribute is required if the wage_type is `Hourly`.

##### self_onboarding: `bool`<a id="self_onboarding-bool"></a>

Whether the contractor or the payroll admin will complete onboarding in Gusto. Self-onboarding is recommended so that contractors receive Gusto accounts. If self_onboarding is true, then email is required.

##### email: `str`<a id="email-str"></a>

The contractor’s email address.

##### first_name: `str`<a id="first_name-str"></a>

The contractor’s first name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.

##### last_name: `str`<a id="last_name-str"></a>

The contractor’s last name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.

##### middle_initial: `str`<a id="middle_initial-str"></a>

The contractor’s middle initial. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.

##### file_new_hire_report: `bool`<a id="file_new_hire_report-bool"></a>

The boolean flag indicating whether Gusto will file a new hire report for the contractor. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.

##### work_state: `Optional[str]`<a id="work_state-optionalstr"></a>

State where the contractor will be conducting the majority of their work for the company. This value is used when generating the new hire report. This attribute is required for `Individual` contractors if `file_new_hire_report` is true and will be ignored for `Business` contractors.

##### ssn: `str`<a id="ssn-str"></a>

This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors. Social security number is needed to file the annual 1099 tax form.

##### business_name: `str`<a id="business_name-str"></a>

The name of the contractor business. This attribute is required for `Business` contractors and will be ignored for `Individual` contractors.

##### ein: `str`<a id="ein-str"></a>

The employer identification number of the contractor business. This attribute is optional for `Business` contractors and will be ignored for `Individual` contractors.

##### is_active: `bool`<a id="is_active-bool"></a>

The status of the contractor.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorsUpdateContractorRequest`](./gusto_embedded_payroll_python_sdk/type/contractors_update_contractor_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Contractor`](./gusto_embedded_payroll_python_sdk/pydantic/contractor.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.departments.add_people_to_department`<a id="gustoembeddedpayrolldepartmentsadd_people_to_department"></a>

Add employees and contractors to a department

scope: `departments:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_people_to_department_response = (
    gustoembeddedpayroll.departments.add_people_to_department(
        department_uuid="department_uuid_example",
        version="string_example",
        employees=[None],
        contractors=[None],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### employees: [`DepartmentsAddPeopleToDepartmentRequestEmployees`](./gusto_embedded_payroll_python_sdk/type/departments_add_people_to_department_request_employees.py)<a id="employees-departmentsaddpeopletodepartmentrequestemployeesgusto_embedded_payroll_python_sdktypedepartments_add_people_to_department_request_employeespy"></a>

##### contractors: [`DepartmentsAddPeopleToDepartmentRequestContractors`](./gusto_embedded_payroll_python_sdk/type/departments_add_people_to_department_request_contractors.py)<a id="contractors-departmentsaddpeopletodepartmentrequestcontractorsgusto_embedded_payroll_python_sdktypedepartments_add_people_to_department_request_contractorspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsAddPeopleToDepartmentRequest`](./gusto_embedded_payroll_python_sdk/type/departments_add_people_to_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_embedded_payroll_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}/add` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.departments.create_department`<a id="gustoembeddedpayrolldepartmentscreate_department"></a>

Create a department

scope: `departments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_department_response = gustoembeddedpayroll.departments.create_department(
    company_uuid="company_uuid_example",
    title="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### title: `str`<a id="title-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsCreateDepartmentRequest`](./gusto_embedded_payroll_python_sdk/type/departments_create_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_embedded_payroll_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/departments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.departments.delete_department`<a id="gustoembeddedpayrolldepartmentsdelete_department"></a>

Delete a department. You cannot delete a department until all employees and contractors have been removed.

scope: `departments:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.departments.delete_department(
    department_uuid="department_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.departments.get_all_with_employees`<a id="gustoembeddedpayrolldepartmentsget_all_with_employees"></a>

Get all of the departments for a given company with the employees and contractors assigned to that department.

scope: `departments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_with_employees_response = (
    gustoembeddedpayroll.departments.get_all_with_employees(
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsGetAllWithEmployeesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/departments_get_all_with_employees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/departments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.departments.get_department_by_uuid`<a id="gustoembeddedpayrolldepartmentsget_department_by_uuid"></a>

Get a department given the UUID

scope: `departments:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_department_by_uuid_response = (
    gustoembeddedpayroll.departments.get_department_by_uuid(
        department_uuid="department_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_embedded_payroll_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.departments.remove_people_from_department`<a id="gustoembeddedpayrolldepartmentsremove_people_from_department"></a>

Remove employees and contractors from a department

scope: `departments:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_people_from_department_response = (
    gustoembeddedpayroll.departments.remove_people_from_department(
        department_uuid="department_uuid_example",
        version="string_example",
        employees=[None],
        contractors=[None],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### employees: [`DepartmentsRemovePeopleFromDepartmentRequestEmployees`](./gusto_embedded_payroll_python_sdk/type/departments_remove_people_from_department_request_employees.py)<a id="employees-departmentsremovepeoplefromdepartmentrequestemployeesgusto_embedded_payroll_python_sdktypedepartments_remove_people_from_department_request_employeespy"></a>

##### contractors: [`DepartmentsRemovePeopleFromDepartmentRequestContractors`](./gusto_embedded_payroll_python_sdk/type/departments_remove_people_from_department_request_contractors.py)<a id="contractors-departmentsremovepeoplefromdepartmentrequestcontractorsgusto_embedded_payroll_python_sdktypedepartments_remove_people_from_department_request_contractorspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsRemovePeopleFromDepartmentRequest`](./gusto_embedded_payroll_python_sdk/type/departments_remove_people_from_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_embedded_payroll_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}/remove` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.departments.update_department`<a id="gustoembeddedpayrolldepartmentsupdate_department"></a>

Update a department

scope: `departments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_department_response = gustoembeddedpayroll.departments.update_department(
    version="string_example",
    department_uuid="department_uuid_example",
    title="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### title: `str`<a id="title-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsUpdateDepartmentRequest`](./gusto_embedded_payroll_python_sdk/type/departments_update_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_embedded_payroll_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.earning_types.create_custom_earning_type`<a id="gustoembeddedpayrollearning_typescreate_custom_earning_type"></a>

Create a custom earning type.

If an inactive earning type exists with the same name, this will reactivate it instead of creating a new one.

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_custom_earning_type_response = (
    gustoembeddedpayroll.earning_types.create_custom_earning_type(
        name="string_example",
        company_id="company_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the custom earning type.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EarningTypesCreateCustomEarningTypeRequest`](./gusto_embedded_payroll_python_sdk/type/earning_types_create_custom_earning_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EarningType`](./gusto_embedded_payroll_python_sdk/pydantic/earning_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/earning_types` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.earning_types.deactivate_type`<a id="gustoembeddedpayrollearning_typesdeactivate_type"></a>

Deactivate an earning type.

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.earning_types.deactivate_type(
    company_id="company_id_example",
    earning_type_uuid="earning_type_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### earning_type_uuid: `str`<a id="earning_type_uuid-str"></a>

The UUID of the earning type

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/earning_types/{earning_type_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.earning_types.get_all`<a id="gustoembeddedpayrollearning_typesget_all"></a>

A payroll item in Gusto is associated to an earning type to name the type of earning described by the payroll item.

#### Default Earning Type<a id="default-earning-type"></a>
Certain earning types are special because they have tax considerations. Those earning types are mostly the same for every company depending on its legal structure (LLC, Corporation, etc.)

#### Custom Earning Type<a id="custom-earning-type"></a>
Custom earning types are all the other earning types added specifically for a company.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = gustoembeddedpayroll.earning_types.get_all(
    company_id="company_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EarningTypesGetAllResponse`](./gusto_embedded_payroll_python_sdk/pydantic/earning_types_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/earning_types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.earning_types.update_type`<a id="gustoembeddedpayrollearning_typesupdate_type"></a>

Update an earning type.

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_type_response = gustoembeddedpayroll.earning_types.update_type(
    company_id="company_id_example",
    earning_type_uuid="earning_type_uuid_example",
    name="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### earning_type_uuid: `str`<a id="earning_type_uuid-str"></a>

The UUID of the earning type

##### name: `str`<a id="name-str"></a>

The name of the custom earning type.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EarningTypesUpdateTypeRequest`](./gusto_embedded_payroll_python_sdk/type/earning_types_update_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EarningType`](./gusto_embedded_payroll_python_sdk/pydantic/earning_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/earning_types/{earning_type_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.create_home_address`<a id="gustoembeddedpayrollemployee_addressescreate_home_address"></a>

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_home_address_response = (
    gustoembeddedpayroll.employee_addresses.create_home_address(
        employee_id="employee_id_example",
        street_1="string_example",
        street_2="string_example",
        city="string_example",
        state="string_example",
        zip="string_example",
        effective_date="1970-01-01",
        courtesy_withholding=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### street_1: `str`<a id="street_1-str"></a>

##### street_2: `Optional[str]`<a id="street_2-optionalstr"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### courtesy_withholding: `bool`<a id="courtesy_withholding-bool"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeAddressesCreateHomeAddressRequest`](./gusto_embedded_payroll_python_sdk/type/employee_addresses_create_home_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddress`](./gusto_embedded_payroll_python_sdk/pydantic/employee_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/home_addresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.create_work_address`<a id="gustoembeddedpayrollemployee_addressescreate_work_address"></a>

The work address of an employee describes when an employee began working at an associated company location.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_work_address_response = (
    gustoembeddedpayroll.employee_addresses.create_work_address(
        employee_id="employee_id_example",
        location_uuid="string_example",
        effective_date="1970-01-01",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### location_uuid: `str`<a id="location_uuid-str"></a>

Reference to a company location

##### effective_date: `date`<a id="effective_date-date"></a>

Date the employee began working at the company location

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeAddressesCreateWorkAddressRequest`](./gusto_embedded_payroll_python_sdk/type/employee_addresses_create_work_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeWorkAddress`](./gusto_embedded_payroll_python_sdk/pydantic/employee_work_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/work_addresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.delete_home`<a id="gustoembeddedpayrollemployee_addressesdelete_home"></a>

Used for deleting an employee's home address.  Cannot delete the employee's active home address.

scope: `employees:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.employee_addresses.delete_home(
    home_address_uuid="home_address_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### home_address_uuid: `str`<a id="home_address_uuid-str"></a>

The UUID of the home address

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/home_addresses/{home_address_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.delete_work_address`<a id="gustoembeddedpayrollemployee_addressesdelete_work_address"></a>

Used for deleting an employee's work address.  Cannot delete the employee's active work address.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.employee_addresses.delete_work_address(
    work_address_uuid="work_address_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### work_address_uuid: `str`<a id="work_address_uuid-str"></a>

The UUID of the work address

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/work_addresses/{work_address_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.get_home_address`<a id="gustoembeddedpayrollemployee_addressesget_home_address"></a>

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_address_response = gustoembeddedpayroll.employee_addresses.get_home_address(
    home_address_uuid="home_address_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### home_address_uuid: `str`<a id="home_address_uuid-str"></a>

The UUID of the home address

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddress`](./gusto_embedded_payroll_python_sdk/pydantic/employee_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/home_addresses/{home_address_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.get_home_addresses`<a id="gustoembeddedpayrollemployee_addressesget_home_addresses"></a>

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_addresses_response = (
    gustoembeddedpayroll.employee_addresses.get_home_addresses(
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddressesGetHomeAddressesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employee_addresses_get_home_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/home_addresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.get_work_address`<a id="gustoembeddedpayrollemployee_addressesget_work_address"></a>

The work address of an employee is used for payroll tax purposes.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_address_response = gustoembeddedpayroll.employee_addresses.get_work_address(
    work_address_uuid="work_address_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### work_address_uuid: `str`<a id="work_address_uuid-str"></a>

The UUID of the work address

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeWorkAddress`](./gusto_embedded_payroll_python_sdk/pydantic/employee_work_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/work_addresses/{work_address_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.list_work_addresses`<a id="gustoembeddedpayrollemployee_addresseslist_work_addresses"></a>

Returns a list of an employee's work addresses. Each address includes its effective date and a boolean
signifying if it is the currently active work address.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_work_addresses_response = (
    gustoembeddedpayroll.employee_addresses.list_work_addresses(
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddressesListWorkAddressesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employee_addresses_list_work_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/work_addresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.update_home_address`<a id="gustoembeddedpayrollemployee_addressesupdate_home_address"></a>

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_home_address_response = (
    gustoembeddedpayroll.employee_addresses.update_home_address(
        version="string_example",
        home_address_uuid="home_address_uuid_example",
        street_1="string_example",
        street_2="string_example",
        city="string_example",
        state="string_example",
        zip="string_example",
        effective_date="1970-01-01",
        courtesy_withholding=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### home_address_uuid: `str`<a id="home_address_uuid-str"></a>

The UUID of the home address

##### street_1: `str`<a id="street_1-str"></a>

##### street_2: `Optional[str]`<a id="street_2-optionalstr"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### courtesy_withholding: `bool`<a id="courtesy_withholding-bool"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeAddressesUpdateHomeAddressRequest`](./gusto_embedded_payroll_python_sdk/type/employee_addresses_update_home_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddress`](./gusto_embedded_payroll_python_sdk/pydantic/employee_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/home_addresses/{home_address_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_addresses.update_work_address`<a id="gustoembeddedpayrollemployee_addressesupdate_work_address"></a>

The work address of an employee is used for payroll tax purposes.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_work_address_response = (
    gustoembeddedpayroll.employee_addresses.update_work_address(
        work_address_uuid="work_address_uuid_example",
        version="string_example",
        location_uuid="string_example",
        effective_date="1970-01-01",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### work_address_uuid: `str`<a id="work_address_uuid-str"></a>

The UUID of the work address

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### location_uuid: `str`<a id="location_uuid-str"></a>

Reference to a company location

##### effective_date: `date`<a id="effective_date-date"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeAddressesUpdateWorkAddressRequest`](./gusto_embedded_payroll_python_sdk/type/employee_addresses_update_work_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeWorkAddress`](./gusto_embedded_payroll_python_sdk/pydantic/employee_work_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/work_addresses/{work_address_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_benefits.create_benefit_record`<a id="gustoembeddedpayrollemployee_benefitscreate_benefit_record"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

scope: `employee_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_benefit_record_response = (
    gustoembeddedpayroll.employee_benefits.create_benefit_record(
        company_benefit_uuid="string_example",
        employee_id="employee_id_example",
        active=True,
        employee_deduction="0.00",
        deduct_as_percentage=False,
        employee_deduction_annual_maximum="string_example",
        contribution={
            "type": "tiered",
        },
        elective=False,
        company_contribution_annual_maximum="string_example",
        limit_option="string_example",
        catch_up=False,
        coverage_amount="string_example",
        coverage_salary_multiplier="0.00",
        deduction_reduces_taxable_income="unset",
        company_contribution="0.00",
        contribute_as_percentage=False,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_benefit_uuid: `str`<a id="company_benefit_uuid-str"></a>

The UUID of the company benefit.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### active: `bool`<a id="active-bool"></a>

Whether the employee benefit is active.

##### employee_deduction: `str`<a id="employee_deduction-str"></a>

The amount to be deducted, per pay period, from the employee's pay.

##### deduct_as_percentage: `bool`<a id="deduct_as_percentage-bool"></a>

Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll.

##### employee_deduction_annual_maximum: `Optional[str]`<a id="employee_deduction_annual_maximum-optionalstr"></a>

The maximum employee deduction amount per year. A null value signifies no limit.

##### contribution: [`EmployeeBenefitsCreateBenefitRecordRequestContribution`](./gusto_embedded_payroll_python_sdk/type/employee_benefits_create_benefit_record_request_contribution.py)<a id="contribution-employeebenefitscreatebenefitrecordrequestcontributiongusto_embedded_payroll_python_sdktypeemployee_benefits_create_benefit_record_request_contributionpy"></a>


##### elective: `bool`<a id="elective-bool"></a>

Whether the company contribution is elective (aka \\\"matching\\\"). For `tiered`, `elective_amount`, and `elective_percentage` contribution types this is ignored and assumed to be `true`.

##### company_contribution_annual_maximum: `Optional[str]`<a id="company_contribution_annual_maximum-optionalstr"></a>

The maximum company contribution amount per year. A null value signifies no limit.

##### limit_option: `Optional[str]`<a id="limit_option-optionalstr"></a>

Some benefits require additional information to determine their limit. For example, for an HSA benefit, the limit option should be either \\\"Family\\\" or \\\"Individual\\\". For a Dependent Care FSA benefit, the limit option should be either \\\"Joint Filing or Single\\\" or \\\"Married and Filing Separately\\\".

##### catch_up: `bool`<a id="catch_up-bool"></a>

Whether the employee should use a benefit’s \\\"catch up\\\" rate. Only Roth 401k and 401k benefits use this value for employees over 50.

##### coverage_amount: `Optional[str]`<a id="coverage_amount-optionalstr"></a>

The amount that the employee is insured for. Note: company contribution cannot be present if coverage amount is set.

##### coverage_salary_multiplier: `str`<a id="coverage_salary_multiplier-str"></a>

The coverage amount as a multiple of the employee’s salary. Only applicable for Group Term Life benefits. Note: cannot be set if coverage amount is also set.

##### deduction_reduces_taxable_income: `Optional[str]`<a id="deduction_reduces_taxable_income-optionalstr"></a>

Whether the employee deduction reduces taxable income or not. Only valid for Group Term Life benefits. Note: when the value is not \\\"unset\\\", coverage amount and coverage salary multiplier are ignored.

##### company_contribution: `str`<a id="company_contribution-str"></a>

The amount to be paid, per pay period, by the company.

##### contribute_as_percentage: `bool`<a id="contribute_as_percentage-bool"></a>

Whether the company contribution amount should be treated as a percentage to be deducted from each payroll.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeBenefitsCreateBenefitRecordRequest`](./gusto_embedded_payroll_python_sdk/type/employee_benefits_create_benefit_record_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeBenefit`](./gusto_embedded_payroll_python_sdk/pydantic/employee_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/employee_benefits` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_benefits.create_ytd_benefit_amounts_from_different_company`<a id="gustoembeddedpayrollemployee_benefitscreate_ytd_benefit_amounts_from_different_company"></a>

Year-to-date benefit amounts from a different company represents the amount of money added to an employee's plan during a current year, made outside of the current contribution when they were employed at a different company.

This endpoint only supports passing outside contributions for 401(k) benefits.

scope: `employee_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.employee_benefits.create_ytd_benefit_amounts_from_different_company(
    tax_year=2000,
    ytd_employee_deduction_amount="0.00",
    ytd_company_contribution_amount="0.00",
    employee_id="employee_id_example",
    benefit_type=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tax_year: `Union[int, float]`<a id="tax_year-unionint-float"></a>

The tax year for which this amount applies.

##### ytd_employee_deduction_amount: `str`<a id="ytd_employee_deduction_amount-str"></a>

The year-to-date employee deduction made outside the current company.

##### ytd_company_contribution_amount: `str`<a id="ytd_company_contribution_amount-str"></a>

The year-to-date company contribution made outside the current company.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### benefit_type: `Union[int, float]`<a id="benefit_type-unionint-float"></a>

The benefit type supported by Gusto.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeBenefitsCreateYtdBenefitAmountsFromDifferentCompanyRequest`](./gusto_embedded_payroll_python_sdk/type/employee_benefits_create_ytd_benefit_amounts_from_different_company_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/ytd_benefit_amounts_from_different_company` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_benefits.delete_by_id`<a id="gustoembeddedpayrollemployee_benefitsdelete_by_id"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

scope: `employee_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.employee_benefits.delete_by_id(
    employee_benefit_id="employee_benefit_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_benefit_id: `str`<a id="employee_benefit_id-str"></a>

The UUID of the employee benefit.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employee_benefits/{employee_benefit_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_benefits.get_all_for_employee`<a id="gustoembeddedpayrollemployee_benefitsget_all_for_employee"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

Returns an array of all employee benefits for this employee

Benefits containing PHI are only visible to applications with the `employee_benefits:read:phi` scope.

scope: `employee_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_for_employee_response = (
    gustoembeddedpayroll.employee_benefits.get_all_for_employee(
        employee_id="employee_id_example",
        page=3.14,
        per=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeBenefitsGetAllForEmployeeResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employee_benefits_get_all_for_employee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/employee_benefits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_benefits.get_employee_benefit_by_id`<a id="gustoembeddedpayrollemployee_benefitsget_employee_benefit_by_id"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

Benefits containing PHI are only visible to applications with the `employee_benefits:read:phi` scope.

scope: `employee_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_benefit_by_id_response = (
    gustoembeddedpayroll.employee_benefits.get_employee_benefit_by_id(
        employee_benefit_id="employee_benefit_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_benefit_id: `str`<a id="employee_benefit_id-str"></a>

The UUID of the employee benefit.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeBenefit`](./gusto_embedded_payroll_python_sdk/pydantic/employee_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employee_benefits/{employee_benefit_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_benefits.update_benefit_record`<a id="gustoembeddedpayrollemployee_benefitsupdate_benefit_record"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

scope: `employee_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_benefit_record_response = (
    gustoembeddedpayroll.employee_benefits.update_benefit_record(
        version="string_example",
        employee_benefit_id="employee_benefit_id_example",
        active=True,
        employee_deduction="0.00",
        deduct_as_percentage=True,
        employee_deduction_annual_maximum="string_example",
        contribution={
            "type": "amount",
        },
        elective=False,
        company_contribution_annual_maximum="string_example",
        limit_option="string_example",
        catch_up=False,
        coverage_amount="string_example",
        deduction_reduces_taxable_income="unset",
        coverage_salary_multiplier="0.00",
        company_contribution="0.00",
        contribute_as_percentage=False,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### employee_benefit_id: `str`<a id="employee_benefit_id-str"></a>

The UUID of the employee benefit.

##### active: `bool`<a id="active-bool"></a>

Whether the employee benefit is active.

##### employee_deduction: `str`<a id="employee_deduction-str"></a>

The amount to be deducted, per pay period, from the employee's pay.

##### deduct_as_percentage: `bool`<a id="deduct_as_percentage-bool"></a>

Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll.

##### employee_deduction_annual_maximum: `Optional[str]`<a id="employee_deduction_annual_maximum-optionalstr"></a>

The maximum employee deduction amount per year. A null value signifies no limit.

##### contribution: [`EmployeeBenefitsUpdateBenefitRecordRequestContribution`](./gusto_embedded_payroll_python_sdk/type/employee_benefits_update_benefit_record_request_contribution.py)<a id="contribution-employeebenefitsupdatebenefitrecordrequestcontributiongusto_embedded_payroll_python_sdktypeemployee_benefits_update_benefit_record_request_contributionpy"></a>


##### elective: `bool`<a id="elective-bool"></a>

Whether the company contribution is elective (aka \\\"matching\\\"). For `tiered`, `elective_amount`, and `elective_percentage` contribution types this is ignored and assumed to be `true`.

##### company_contribution_annual_maximum: `Optional[str]`<a id="company_contribution_annual_maximum-optionalstr"></a>

The maximum company contribution amount per year. A null value signifies no limit.

##### limit_option: `Optional[str]`<a id="limit_option-optionalstr"></a>

Some benefits require additional information to determine their limit. For example, for an HSA benefit, the limit option should be either \\\"Family\\\" or \\\"Individual\\\". For a Dependent Care FSA benefit, the limit option should be either \\\"Joint Filing or Single\\\" or \\\"Married and Filing Separately\\\".

##### catch_up: `bool`<a id="catch_up-bool"></a>

Whether the employee should use a benefit’s \\\"catch up\\\" rate. Only Roth 401k and 401k benefits use this value for employees over 50.

##### coverage_amount: `Optional[str]`<a id="coverage_amount-optionalstr"></a>

The amount that the employee is insured for. Note: company contribution cannot be present if coverage amount is set.

##### deduction_reduces_taxable_income: `Optional[str]`<a id="deduction_reduces_taxable_income-optionalstr"></a>

Whether the employee deduction reduces taxable income or not. Only valid for Group Term Life benefits. Note: when the value is not \\\"unset\\\", coverage amount and coverage salary multiplier are ignored.

##### coverage_salary_multiplier: `str`<a id="coverage_salary_multiplier-str"></a>

The coverage amount as a multiple of the employee’s salary. Only applicable for Group Term Life benefits. Note: cannot be set if coverage amount is also set.

##### company_contribution: `str`<a id="company_contribution-str"></a>

The amount to be paid, per pay period, by the company.

##### contribute_as_percentage: `bool`<a id="contribute_as_percentage-bool"></a>

Whether the company contribution amount should be treated as a percentage to be deducted from each payroll.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeBenefitsUpdateBenefitRecordRequest`](./gusto_embedded_payroll_python_sdk/type/employee_benefits_update_benefit_record_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeBenefit`](./gusto_embedded_payroll_python_sdk/pydantic/employee_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employee_benefits/{employee_benefit_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_employments.create_rehire`<a id="gustoembeddedpayrollemployee_employmentscreate_rehire"></a>

Rehire is created whenever an employee is scheduled to return to the company.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_rehire_response = gustoembeddedpayroll.employee_employments.create_rehire(
    effective_date="string_example",
    file_new_hire_report=True,
    work_location_uuid="string_example",
    employee_id="employee_id_example",
    employment_status="part_time",
    two_percent_shareholder=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `str`<a id="effective_date-str"></a>

The day when the employee returns to work.

##### file_new_hire_report: `bool`<a id="file_new_hire_report-bool"></a>

The boolean flag indicating whether Gusto will file a new hire report for the employee.

##### work_location_uuid: `str`<a id="work_location_uuid-str"></a>

The uuid of the employee's work location.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### employment_status: `str`<a id="employment_status-str"></a>

The employee's employment status. Supplying an invalid option will set the employment_status to *not_set*.

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RehireBody`](./gusto_embedded_payroll_python_sdk/type/rehire_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Rehire`](./gusto_embedded_payroll_python_sdk/pydantic/rehire.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/rehire` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_employments.create_termination`<a id="gustoembeddedpayrollemployee_employmentscreate_termination"></a>

Terminations are created whenever an employee is scheduled to leave the company. The only things required are an effective date (their last day of work) and whether they should receive their wages in a one-off termination payroll or with the rest of the company.

Note that some states require employees to receive their final wages within 24 hours (unless they consent otherwise,) in which case running a one-off payroll may be the only option.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_termination_response = (
    gustoembeddedpayroll.employee_employments.create_termination(
        effective_date="string_example",
        employee_id="employee_id_example",
        run_termination_payroll=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `str`<a id="effective_date-str"></a>

The employee's last day of work.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### run_termination_payroll: `bool`<a id="run_termination_payroll-bool"></a>

If true, the employee should receive their final wages via an off-cycle payroll. If false, they should receive their final wages on their current pay schedule.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeEmploymentsCreateTerminationRequest`](./gusto_embedded_payroll_python_sdk/type/employee_employments_create_termination_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Termination`](./gusto_embedded_payroll_python_sdk/pydantic/termination.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/terminations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_employments.delete_termination`<a id="gustoembeddedpayrollemployee_employmentsdelete_termination"></a>

Delete an employee termination.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.employee_employments.delete_termination(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/terminations` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_employments.get_history`<a id="gustoembeddedpayrollemployee_employmentsget_history"></a>

Retrieve the employment history for a given employee, which includes termination and rehire.

scope: `employments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_history_response = gustoembeddedpayroll.employee_employments.get_history(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeEmploymentsGetHistoryResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employee_employments_get_history_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/employment_history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_employments.get_rehire`<a id="gustoembeddedpayrollemployee_employmentsget_rehire"></a>

Retrieve an employee's rehire, which contains information on when the employee returns to work.

scope: `employments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_rehire_response = gustoembeddedpayroll.employee_employments.get_rehire(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Rehire`](./gusto_embedded_payroll_python_sdk/pydantic/rehire.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/rehire` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_employments.list_employee_terminations`<a id="gustoembeddedpayrollemployee_employmentslist_employee_terminations"></a>

Terminations are created whenever an employee is scheduled to leave the company. The only things required are an effective date (their last day of work) and whether they should receive their wages in a one-off termination payroll or with the rest of the company.

Note that some states require employees to receive their final wages within 24 hours (unless they consent otherwise,) in which case running a one-off payroll may be the only option.

scope: `employments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employee_terminations_response = (
    gustoembeddedpayroll.employee_employments.list_employee_terminations(
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeEmploymentsListEmployeeTerminationsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employee_employments_list_employee_terminations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/terminations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_employments.remove_rehire`<a id="gustoembeddedpayrollemployee_employmentsremove_rehire"></a>

Delete an employee rehire. An employee rehire cannot be deleted if it's active (past effective date).

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.employee_employments.remove_rehire(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/rehire` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_employments.update_rehire`<a id="gustoembeddedpayrollemployee_employmentsupdate_rehire"></a>

Update an employee's rehire.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_rehire_response = gustoembeddedpayroll.employee_employments.update_rehire(
    body=None,
    employee_id="employee_id_example",
    version="string_example",
    effective_date="string_example",
    file_new_hire_report=True,
    work_location_uuid="string_example",
    employment_status="part_time",
    two_percent_shareholder=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### effective_date: `str`<a id="effective_date-str"></a>

The day when the employee returns to work.

##### file_new_hire_report: `bool`<a id="file_new_hire_report-bool"></a>

The boolean flag indicating whether Gusto will file a new hire report for the employee.

##### work_location_uuid: `str`<a id="work_location_uuid-str"></a>

The uuid of the employee's work location.

##### employment_status: `str`<a id="employment_status-str"></a>

The employee's employment status. Supplying an invalid option will set the employment_status to *not_set*.

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeEmploymentsUpdateRehireRequest`](./gusto_embedded_payroll_python_sdk/type/employee_employments_update_rehire_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Rehire`](./gusto_embedded_payroll_python_sdk/pydantic/rehire.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/rehire` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_employments.update_termination`<a id="gustoembeddedpayrollemployee_employmentsupdate_termination"></a>

Terminations are created whenever an employee is scheduled to leave the company. The only things required are an effective date (their last day of work) and whether they should receive their wages in a one-off termination payroll or with the rest of the company.

Note that some states require employees to receive their final wages within 24 hours (unless they consent otherwise,) in which case running a one-off payroll may be the only option.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_termination_response = (
    gustoembeddedpayroll.employee_employments.update_termination(
        body=None,
        employee_id="employee_id_example",
        version="string_example",
        effective_date="string_example",
        run_termination_payroll=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### effective_date: `str`<a id="effective_date-str"></a>

The employee's last day of work.

##### run_termination_payroll: `bool`<a id="run_termination_payroll-bool"></a>

If true, the employee should receive their final wages via an off-cycle payroll. If false, they should receive their final wages on their current pay schedule.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeEmploymentsUpdateTerminationRequest`](./gusto_embedded_payroll_python_sdk/type/employee_employments_update_termination_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Termination`](./gusto_embedded_payroll_python_sdk/pydantic/termination.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/terminations/{employee_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_forms.generate_w2_document`<a id="gustoembeddedpayrollemployee_formsgenerate_w2_document"></a>

> 🚧 Demo action
>
> This action is only available in the Demo environment

Generates a W2 document for testing purposes.

scope: `employees:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_w2_document_response = (
    gustoembeddedpayroll.employee_forms.generate_w2_document(
        employee_id="string_example",
        year=1,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The employee UUID.

##### year: `int`<a id="year-int"></a>

Must be equal to or more recent than 2015. If not specified, defaults to the previous year. 

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeFormsGenerateW2DocumentRequest`](./gusto_embedded_payroll_python_sdk/type/employee_forms_generate_w2_document_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeFormsGenerateW2DocumentResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employee_forms_generate_w2_document_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/sandbox/generate_w2` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_forms.get_all_employee_forms`<a id="gustoembeddedpayrollemployee_formsget_all_employee_forms"></a>

Get a list of all employee's forms

scope: `employee_forms:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_employee_forms_response = (
    gustoembeddedpayroll.employee_forms.get_all_employee_forms(
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyFormsGetAllFormsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/company_forms_get_all_forms_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/forms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_forms.get_form_by_id`<a id="gustoembeddedpayrollemployee_formsget_form_by_id"></a>

Get an employee form

scope: `employee_forms:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_form_by_id_response = gustoembeddedpayroll.employee_forms.get_form_by_id(
    employee_id="employee_id_example",
    form_id="form_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### form_id: `str`<a id="form_id-str"></a>

The UUID of the form

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Form`](./gusto_embedded_payroll_python_sdk/pydantic/form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/forms/{form_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_forms.get_pdf_link`<a id="gustoembeddedpayrollemployee_formsget_pdf_link"></a>

Get the link to the form PDF

scope: `employee_forms:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pdf_link_response = gustoembeddedpayroll.employee_forms.get_pdf_link(
    employee_id="employee_id_example",
    form_id="form_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### form_id: `str`<a id="form_id-str"></a>

The UUID of the form

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`FormPdf`](./gusto_embedded_payroll_python_sdk/pydantic/form_pdf.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/forms/{form_id}/pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_forms.sign_form`<a id="gustoembeddedpayrollemployee_formssign_form"></a>

Sign a company form

scope: `employee_forms:sign`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sign_form_response = gustoembeddedpayroll.employee_forms.sign_form(
    signature_text="string_example",
    agree=True,
    signed_by_ip_address="string_example",
    employee_id="employee_id_example",
    form_id="form_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### signature_text: `str`<a id="signature_text-str"></a>

The signature

##### agree: `bool`<a id="agree-bool"></a>

whether you agree to sign electronically

##### signed_by_ip_address: `str`<a id="signed_by_ip_address-str"></a>

The IP address of the signatory who signed the form.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### form_id: `str`<a id="form_id-str"></a>

The UUID of the form

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeFormsSignFormRequest`](./gusto_embedded_payroll_python_sdk/type/employee_forms_sign_form_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Form`](./gusto_embedded_payroll_python_sdk/pydantic/form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/forms/{form_id}/sign` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_payment_method.create_bank_account`<a id="gustoembeddedpayrollemployee_payment_methodcreate_bank_account"></a>

Creates an employee bank account. An employee can have multiple
bank accounts. Note that creating an employee bank account will also update
the employee's payment method.

scope: `employee_payment_methods:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bank_account_response = (
    gustoembeddedpayroll.employee_payment_method.create_bank_account(
        name="string_example",
        routing_number="string_example",
        account_number="string_example",
        account_type="Checking",
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### routing_number: `str`<a id="routing_number-str"></a>

##### account_number: `str`<a id="account_number-str"></a>

##### account_type: `str`<a id="account_type-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeePaymentMethodCreateBankAccountRequest`](./gusto_embedded_payroll_python_sdk/type/employee_payment_method_create_bank_account_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeBankAccount`](./gusto_embedded_payroll_python_sdk/pydantic/employee_bank_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/bank_accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_payment_method.delete_bank_account`<a id="gustoembeddedpayrollemployee_payment_methoddelete_bank_account"></a>

Deletes an employee bank account. To update an employee's bank
account details, delete the bank account first and create a new one.

scope: `employee_payment_methods:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.employee_payment_method.delete_bank_account(
    employee_id="employee_id_example",
    bank_account_uuid="bank_account_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### bank_account_uuid: `str`<a id="bank_account_uuid-str"></a>

The UUID of the bank account

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/bank_accounts/{bank_account_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_payment_method.get_bank_accounts`<a id="gustoembeddedpayrollemployee_payment_methodget_bank_accounts"></a>

Fetches an employee's payment method. An employee payment method
describes how the payment should be split across the employee's associated
bank accounts.

scope: `employee_payment_methods:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bank_accounts_response = (
    gustoembeddedpayroll.employee_payment_method.get_bank_accounts(
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeePaymentMethod`](./gusto_embedded_payroll_python_sdk/pydantic/employee_payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/payment_method` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_payment_method.list_bank_accounts`<a id="gustoembeddedpayrollemployee_payment_methodlist_bank_accounts"></a>

Returns all employee bank accounts.

scope: `employee_payment_methods:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_bank_accounts_response = (
    gustoembeddedpayroll.employee_payment_method.list_bank_accounts(
        employee_id="employee_id_example",
        page=3.14,
        per=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeePaymentMethodListBankAccountsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employee_payment_method_list_bank_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/bank_accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_payment_method.update_payment_method`<a id="gustoembeddedpayrollemployee_payment_methodupdate_payment_method"></a>

Updates an employee's payment method. Note that creating an employee
bank account will also update the employee's payment method.

scope: `employee_payment_methods:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_payment_method_response = (
    gustoembeddedpayroll.employee_payment_method.update_payment_method(
        version="string_example",
        type="Direct Deposit",
        employee_id="employee_id_example",
        split_by="Amount",
        splits=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### type: `str`<a id="type-str"></a>

The payment method type. If type is Check, then split_by and splits do not need to be populated. If type is Direct Deposit, split_by and splits are required.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### split_by: `str`<a id="split_by-str"></a>

Describes how the payment will be split. If split_by is Percentage, then the split amounts must add up to exactly 100. If split_by is Amount, then the last split amount must be nil to capture the remainder.

##### splits: [`EmployeePaymentMethodUpdatePaymentMethodRequestSplits`](./gusto_embedded_payroll_python_sdk/type/employee_payment_method_update_payment_method_request_splits.py)<a id="splits-employeepaymentmethodupdatepaymentmethodrequestsplitsgusto_embedded_payroll_python_sdktypeemployee_payment_method_update_payment_method_request_splitspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeePaymentMethodUpdatePaymentMethodRequest`](./gusto_embedded_payroll_python_sdk/type/employee_payment_method_update_payment_method_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeePaymentMethod`](./gusto_embedded_payroll_python_sdk/pydantic/employee_payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/payment_method` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_tax_setup.get_federal_taxes_by_id`<a id="gustoembeddedpayrollemployee_tax_setupget_federal_taxes_by_id"></a>

Get attributes relevant for an employee's federal taxes.

 scope: `employee_federal_taxes:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_federal_taxes_by_id_response = (
    gustoembeddedpayroll.employee_tax_setup.get_federal_taxes_by_id(
        employee_uuid="employee_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_uuid: `str`<a id="employee_uuid-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeFederalTax`](./gusto_embedded_payroll_python_sdk/pydantic/employee_federal_tax.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_uuid}/federal_taxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_tax_setup.get_state_taxes`<a id="gustoembeddedpayrollemployee_tax_setupget_state_taxes"></a>

Get attributes relevant for an employee's state taxes.

The data required to correctly calculate an employee's state taxes varies by both home and work location. This API returns information about each question that must be answered grouped by state. Mostly commonly, an employee lives and works in the same state and will only have questions for a single state. The response contains metadata about each question, the type of answer expected, and the current answer stored in Gusto for that question.

Answers are represented by an array. Today, this array can only be empty or contain exactly one element, but is designed to allow for forward compatibility with effective-dated fields. Until effective dated answers are supported, the `valid_from` and `valid_up_to` must always be `"2010-01-01"` and `null` respectively.

## About filing new hire reports<a id="about-filing-new-hire-reports"></a>
Payroll Admins are responsible for filing a new hire report for each Employee. The `file_new_hire_report` question will only be listed if:
- the `employee.onboarding_status` is one of the following:
  - `admin_onboarding_incomplete`
  - `self_onboarding_awaiting_admin_review`
- that employee's work state requires filing a new hire report

scope: `employee_state_taxes:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_state_taxes_response = gustoembeddedpayroll.employee_tax_setup.get_state_taxes(
    employee_uuid="employee_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_uuid: `str`<a id="employee_uuid-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTaxSetupGetStateTaxesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employee_tax_setup_get_state_taxes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_uuid}/state_taxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_tax_setup.update_federal_taxes`<a id="gustoembeddedpayrollemployee_tax_setupupdate_federal_taxes"></a>

Update attributes relevant for an employee's federal taxes.

scope: `employee_federal_taxes:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_federal_taxes_response = (
    gustoembeddedpayroll.employee_tax_setup.update_federal_taxes(
        version="string_example",
        employee_uuid="employee_uuid_example",
        filing_status="string_example",
        extra_withholding="string_example",
        two_jobs=True,
        dependents_amount="string_example",
        other_income="string_example",
        deductions="string_example",
        w4_data_type="string_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### employee_uuid: `str`<a id="employee_uuid-str"></a>

The UUID of the employee

##### filing_status: `str`<a id="filing_status-str"></a>

##### extra_withholding: `Optional[str]`<a id="extra_withholding-optionalstr"></a>

##### two_jobs: `bool`<a id="two_jobs-bool"></a>

##### dependents_amount: `str`<a id="dependents_amount-str"></a>

##### other_income: `str`<a id="other_income-str"></a>

##### deductions: `str`<a id="deductions-str"></a>

##### w4_data_type: `str`<a id="w4_data_type-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeTaxSetupUpdateFederalTaxesRequest`](./gusto_embedded_payroll_python_sdk/type/employee_tax_setup_update_federal_taxes_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeFederalTax`](./gusto_embedded_payroll_python_sdk/pydantic/employee_federal_tax.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_uuid}/federal_taxes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employee_tax_setup.update_state_taxes`<a id="gustoembeddedpayrollemployee_tax_setupupdate_state_taxes"></a>

Update attributes relevant for an employee's state taxes.

As described for the GET endpoint, the answers must be supplied in the effective-dated format, but currently only a single answer will be accepted - `valid_from` and `valid_up_to` must be `"2010-01-01"` and `null` respectively.

scope: `employee_state_taxes:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_state_taxes_response = (
    gustoembeddedpayroll.employee_tax_setup.update_state_taxes(
        states=[
            {
                "state": "state_example",
            }
        ],
        employee_uuid="employee_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### states: [`EmployeeTaxSetupUpdateStateTaxesRequestStates`](./gusto_embedded_payroll_python_sdk/type/employee_tax_setup_update_state_taxes_request_states.py)<a id="states-employeetaxsetupupdatestatetaxesrequeststatesgusto_embedded_payroll_python_sdktypeemployee_tax_setup_update_state_taxes_request_statespy"></a>

##### employee_uuid: `str`<a id="employee_uuid-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeTaxSetupUpdateStateTaxesRequest`](./gusto_embedded_payroll_python_sdk/type/employee_tax_setup_update_state_taxes_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTaxSetupGetStateTaxesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employee_tax_setup_get_state_taxes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_uuid}/state_taxes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.complete_onboarding`<a id="gustoembeddedpayrollemployeescomplete_onboarding"></a>

This endpoint is currently supported but will eventually be deprecated; please use `/v1/employees/{employee_id}/onboarding_status` instead.

Call this endpoint as the very last step of employee onboarding to complete their onboarding. When successful, the employee's `onboarded` attribute will be updated to true, indicating that they can be included in company's payrolls.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_onboarding_response = gustoembeddedpayroll.employees.complete_onboarding(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./gusto_embedded_payroll_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/finish_onboarding` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.create_employee`<a id="gustoembeddedpayrollemployeescreate_employee"></a>

Create an employee.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_employee_response = gustoembeddedpayroll.employees.create_employee(
    first_name="string_example",
    last_name="string_example",
    company_id="company_id_example",
    middle_initial="string_example",
    date_of_birth="string_example",
    email="string_example",
    ssn="048072888",
    self_onboarding=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### middle_initial: `str`<a id="middle_initial-str"></a>

##### date_of_birth: `str`<a id="date_of_birth-str"></a>

##### email: `str`<a id="email-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### self_onboarding: `bool`<a id="self_onboarding-bool"></a>

If true, employee is expected to self-onboard. If false, payroll admin is expected to enter in the employee's onboarding information

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesCreateEmployeeRequest`](./gusto_embedded_payroll_python_sdk/type/employees_create_employee_request.py)
Create an employee.

#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./gusto_embedded_payroll_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.delete_onboarding_employee`<a id="gustoembeddedpayrollemployeesdelete_onboarding_employee"></a>

Use this endpoint to delete an employee who is in onboarding. Deleting
an onboarded employee is not allowed. Please check out the Terminations api
if you need to terminate an onboarded employee.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.employees.delete_onboarding_employee(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.get_custom_fields`<a id="gustoembeddedpayrollemployeesget_custom_fields"></a>

Returns a list of the employee's custom fields.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_response = gustoembeddedpayroll.employees.get_custom_fields(
    employee_id="employee_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetCustomFieldsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employees_get_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.get_employee_by_id`<a id="gustoembeddedpayrollemployeesget_employee_by_id"></a>

Get an employee.

scope: `employees:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_by_id_response = gustoembeddedpayroll.employees.get_employee_by_id(
    employee_id="employee_id_example",
    include="all_compensations",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### include: `str`<a id="include-str"></a>

Include the requested attribute(s) in each employee response, multiple options are comma separated. Available options: - all_compensations: Include all effective dated compensations for each job instead of only the current compensation - custom_fields: Include employees' custom fields

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./gusto_embedded_payroll_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.get_onboarding_status`<a id="gustoembeddedpayrollemployeesget_onboarding_status"></a>

# Description<a id="description"></a>
Retrieves an employee's onboarding status. The data returned helps inform the required onboarding steps and respective completion status.

scope: `employees:read`

## onboarding_status<a id="onboarding_status"></a>

### Admin-facilitated onboarding<a id="admin-facilitated-onboarding"></a>
| onboarding_status | Description |
|:------------------|------------:|
| `admin_onboarding_incomplete` | Admin needs to complete the full employee-onboarding. |
| `onboarding_completed` | Employee has been fully onboarded and verified. |

### Employee self-onboarding<a id="employee-self-onboarding"></a>
| onboarding_status | Description |
|:------------------|------------:|
| `admin_onboarding_incomplete` | Admin needs to enter basic information about the employee. |
| `self_onboarding_pending_invite` | Admin has the intention to invite the employee to self-onboard (e.g., marking a checkbox), but the system has not yet sent the invitation. |
| `self_onboarding_invited` | Employee has been sent an invitation to self-onboard. |
| `self_onboarding_invited_started` | Employee has started the self-onboarding process. |
| `self_onboarding_invited_overdue` | Employee's start date has passed, and employee has still not completed self-onboarding. |
| `self_onboarding_completed_by_employee` | Employee has completed entering in their information. The status should be updated via API to "self_onboarding_awaiting_admin_review" from here, once the Admin has started reviewing. |
| `self_onboarding_awaiting_admin_review` | Admin has started to verify the employee's information. |
| `onboarding_completed` | Employee has been fully onboarded and verified. |

## onboarding_steps<a id="onboarding_steps"></a>

| onboarding_steps | Requirement(s) to be completed |
|:-----------------|-------------------------------:|
| `personal_details` | Add employee's first name, last name, email, date of birth, social security number |
| `compensation_details` | Associate employee to a job & compensation. |
| `add_work_address` | Add employee work address. |
| `add_home_address` | Add employee home address. |
| `federal_tax_setup` | Set up federal tax withholdings. |
| `state_tax_setup` | Set up state tax withholdings. |
| `direct_deposit_setup` | (optional) Set up employee's direct deposit. |
| `employee_form_signing` | Employee forms (e.g., W4, direct deposit authorization) are generated & signed. |
| `file_new_hire_report` | File a new hire report for this employee. |
| `admin_review` | Admin reviews & confirms employee details (only required for Employee self-onboarding) |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_onboarding_status_response = gustoembeddedpayroll.employees.get_onboarding_status(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeOnboardingStatus`](./gusto_embedded_payroll_python_sdk/pydantic/employee_onboarding_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/onboarding_status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.get_time_off_activities`<a id="gustoembeddedpayrollemployeesget_time_off_activities"></a>

Get employee time off activities.

scope: `employee_time_off_activities:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_off_activities_response = (
    gustoembeddedpayroll.employees.get_time_off_activities(
        employee_uuid="employee_uuid_example",
        time_off_type="time_off_type_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_uuid: `str`<a id="employee_uuid-str"></a>

The UUID of the employee

##### time_off_type: `str`<a id="time_off_type-str"></a>

The time off type name you want to query data for. ex: 'sick' or 'vacation'

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffActivity`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_activity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_uuid}/time_off_activities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.list_company_employees`<a id="gustoembeddedpayrollemployeeslist_company_employees"></a>

Get all of the employees, onboarding, active and terminated, for a given company.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_employees_response = gustoembeddedpayroll.employees.list_company_employees(
    company_id="company_id_example",
    terminated=True,
    include="all_compensations",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### terminated: `bool`<a id="terminated-bool"></a>

Filters employees by the provided boolean

##### include: `str`<a id="include-str"></a>

Include the requested attribute(s) in each employee response, multiple options are comma separated. Available options: - all_compensations: Include all effective dated compensations for each job instead of only the current compensation - custom_fields: Include employees' custom fields

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesListCompanyEmployeesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/employees_list_company_employees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.update_employee`<a id="gustoembeddedpayrollemployeesupdate_employee"></a>

Update an employee.

scope: `employees:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employee_response = gustoembeddedpayroll.employees.update_employee(
    version="string_example",
    employee_id="employee_id_example",
    first_name="string_example",
    middle_initial="string_example",
    last_name="string_example",
    date_of_birth="string_example",
    email="string_example",
    ssn="048072888",
    two_percent_shareholder=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### first_name: `str`<a id="first_name-str"></a>

##### middle_initial: `str`<a id="middle_initial-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### date_of_birth: `str`<a id="date_of_birth-str"></a>

##### email: `str`<a id="email-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdateEmployeeRequest`](./gusto_embedded_payroll_python_sdk/type/employees_update_employee_request.py)
Update an employee.

#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./gusto_embedded_payroll_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.employees.update_onboarding_status`<a id="gustoembeddedpayrollemployeesupdate_onboarding_status"></a>

scope: `employees:manage`

Updates an employee's onboarding status.
Below is a list of valid onboarding status changes depending on the intended action to be performed on behalf of the employee.

| Action | current onboarding_status | new onboarding_status |
|:------------------|:------------:|----------:|
| Mark an employee as self-onboarding | `admin_onboarding_incomplete` | `self_onboarding_pending_invite` |
| Invite an employee to self-onboard | `admin_onboarding_incomplete` or `self_onboarding_pending_invite` | `self_onboarding_invited` |
| Cancel an employee's self-onboarding | `self_onboarding_invited` or `self_onboarding_pending_invite` | `admin_onboarding_incomplete` |
| Review an employee's self-onboarded info | `self_onboarding_completed_by_employee` | `self_onboarding_awaiting_admin_review` |
| Finish an employee's onboarding | `admin_onboarding_incomplete` or `self_onboarding_awaiting_admin_review` | `onboarding_completed` |

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_onboarding_status_response = (
    gustoembeddedpayroll.employees.update_onboarding_status(
        onboarding_status="string_example",
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### onboarding_status: `str`<a id="onboarding_status-str"></a>

The updated onboarding status for the employee

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdateOnboardingStatusRequest`](./gusto_embedded_payroll_python_sdk/type/employees_update_onboarding_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeOnboardingStatus`](./gusto_embedded_payroll_python_sdk/pydantic/employee_onboarding_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/onboarding_status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.events.get30_day_events`<a id="gustoembeddedpayrolleventsget30_day_events"></a>

Fetch all events, going back up to 30 days, that your partner application has the required scopes for. Note that a partner does NOT have to have verified webhook subscriptions in order to utilize this endpoint.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `events:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get30_day_events_response = gustoembeddedpayroll.events.get30_day_events(
    starting_after_uuid="string_example",
    resource_uuid="string_example",
    limit="string_example",
    event_type="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### starting_after_uuid: `str`<a id="starting_after_uuid-str"></a>

A cursor for pagination. Returns all events occuring after the specified UUID (exclusive)

##### resource_uuid: `str`<a id="resource_uuid-str"></a>

The UUID of the company. If not specified, will return all events for all companies.

##### limit: `str`<a id="limit-str"></a>

Limits the number of objects returned in a single response, between 1 and 100. The default is 25

##### event_type: `str`<a id="event_type-str"></a>

A string containing the exact event name (e.g. `employee.created`), or use a wildcard match to filter for a group of events (e.g. `employee.*`, `*.created`, `notification.*.created` etc.)

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EventsGet30DayEventsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/events_get30_day_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.external_payrolls.create_new_payroll`<a id="gustoembeddedpayrollexternal_payrollscreate_new_payroll"></a>

Creates a new external payroll for the company.

scope: `external_payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_payroll_response = gustoembeddedpayroll.external_payrolls.create_new_payroll(
    check_date="string_example",
    payment_period_start_date="string_example",
    payment_period_end_date="string_example",
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### check_date: `str`<a id="check_date-str"></a>

External payroll's check date.

##### payment_period_start_date: `str`<a id="payment_period_start_date-str"></a>

External payroll's pay period start date.

##### payment_period_end_date: `str`<a id="payment_period_end_date-str"></a>

External payroll's pay period end date.

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExternalPayrollsCreateNewPayrollRequest`](./gusto_embedded_payroll_python_sdk/type/external_payrolls_create_new_payroll_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExternalPayroll`](./gusto_embedded_payroll_python_sdk/pydantic/external_payroll.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/external_payrolls` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.external_payrolls.delete_payroll`<a id="gustoembeddedpayrollexternal_payrollsdelete_payroll"></a>

Delete an external payroll.

scope: `external_payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.external_payrolls.delete_payroll(
    company_uuid="company_uuid_example",
    external_payroll_id="external_payroll_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### external_payroll_id: `str`<a id="external_payroll_id-str"></a>

The UUID of the external payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.external_payrolls.finalize_tax_liabilities`<a id="gustoembeddedpayrollexternal_payrollsfinalize_tax_liabilities"></a>

Finalizes tax liabilities for a company. All external payrolls edit action will be disabled.

scope: `external_payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.external_payrolls.finalize_tax_liabilities(
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/external_payrolls/tax_liabilities/finish` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.external_payrolls.get_by_id`<a id="gustoembeddedpayrollexternal_payrollsget_by_id"></a>

Get an external payroll for a given company.

scope: `external_payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = gustoembeddedpayroll.external_payrolls.get_by_id(
    company_uuid="company_uuid_example",
    external_payroll_id="external_payroll_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### external_payroll_id: `str`<a id="external_payroll_id-str"></a>

The UUID of the external payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ExternalPayroll`](./gusto_embedded_payroll_python_sdk/pydantic/external_payroll.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.external_payrolls.get_tax_liabilities`<a id="gustoembeddedpayrollexternal_payrollsget_tax_liabilities"></a>

Get tax liabilities from aggregate external payrolls for a company.

scope: `external_payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tax_liabilities_response = (
    gustoembeddedpayroll.external_payrolls.get_tax_liabilities(
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ExternalPayrollsGetTaxLiabilitiesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/external_payrolls_get_tax_liabilities_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/external_payrolls/tax_liabilities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.external_payrolls.get_tax_suggestions`<a id="gustoembeddedpayrollexternal_payrollsget_tax_suggestions"></a>

Get tax suggestions for an external payroll. Earnings and/or benefits
data must be saved prior to the calculation in order to retrieve accurate
tax calculation.

scope: `external_payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tax_suggestions_response = (
    gustoembeddedpayroll.external_payrolls.get_tax_suggestions(
        company_uuid="company_uuid_example",
        external_payroll_id="external_payroll_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### external_payroll_id: `str`<a id="external_payroll_id-str"></a>

The UUID of the external payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ExternalPayrollsGetTaxSuggestionsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/external_payrolls_get_tax_suggestions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}/calculate_taxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.external_payrolls.list_for_company`<a id="gustoembeddedpayrollexternal_payrollslist_for_company"></a>

Get an external payroll for a given company.

scope: `external_payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_company_response = gustoembeddedpayroll.external_payrolls.list_for_company(
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ExternalPayrollsListForCompanyResponse`](./gusto_embedded_payroll_python_sdk/pydantic/external_payrolls_list_for_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/external_payrolls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.external_payrolls.update_payroll_items`<a id="gustoembeddedpayrollexternal_payrollsupdate_payroll_items"></a>

Update an external payroll with a list of external payroll items

scope: `external_payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_payroll_items_response = (
    gustoembeddedpayroll.external_payrolls.update_payroll_items(
        company_uuid="company_uuid_example",
        external_payroll_id="external_payroll_id_example",
        replace_fields=True,
        external_payroll_items=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### external_payroll_id: `str`<a id="external_payroll_id-str"></a>

The UUID of the external payroll

##### replace_fields: `bool`<a id="replace_fields-bool"></a>

Patch update external payroll items when set to true, otherwise it will overwrite the previous changes.

##### external_payroll_items: [`ExternalPayrollsUpdatePayrollItemsRequestExternalPayrollItems`](./gusto_embedded_payroll_python_sdk/type/external_payrolls_update_payroll_items_request_external_payroll_items.py)<a id="external_payroll_items-externalpayrollsupdatepayrollitemsrequestexternalpayrollitemsgusto_embedded_payroll_python_sdktypeexternal_payrolls_update_payroll_items_request_external_payroll_itemspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExternalPayrollsUpdatePayrollItemsRequest`](./gusto_embedded_payroll_python_sdk/type/external_payrolls_update_payroll_items_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExternalPayroll`](./gusto_embedded_payroll_python_sdk/pydantic/external_payroll.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.external_payrolls.update_tax_liabilities`<a id="gustoembeddedpayrollexternal_payrollsupdate_tax_liabilities"></a>

Update tax liabilities for a company.

scope: `external_payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_tax_liabilities_response = (
    gustoembeddedpayroll.external_payrolls.update_tax_liabilities(
        company_uuid="company_uuid_example",
        liability_selections=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### liability_selections: [`ExternalPayrollsUpdateTaxLiabilitiesRequestLiabilitySelections`](./gusto_embedded_payroll_python_sdk/type/external_payrolls_update_tax_liabilities_request_liability_selections.py)<a id="liability_selections-externalpayrollsupdatetaxliabilitiesrequestliabilityselectionsgusto_embedded_payroll_python_sdktypeexternal_payrolls_update_tax_liabilities_request_liability_selectionspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExternalPayrollsUpdateTaxLiabilitiesRequest`](./gusto_embedded_payroll_python_sdk/type/external_payrolls_update_tax_liabilities_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExternalPayrollsGetTaxLiabilitiesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/external_payrolls_get_tax_liabilities_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/external_payrolls/tax_liabilities` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.federal_tax_details.get_attributes`<a id="gustoembeddedpayrollfederal_tax_detailsget_attributes"></a>

Fetches attributes relevant for a company's federal taxes.

scope: `company_federal_taxes:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attributes_response = gustoembeddedpayroll.federal_tax_details.get_attributes(
    company_id="company_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`FederalTaxDetails`](./gusto_embedded_payroll_python_sdk/pydantic/federal_tax_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/federal_tax_details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.federal_tax_details.update_attributes`<a id="gustoembeddedpayrollfederal_tax_detailsupdate_attributes"></a>

Updates attributes relevant for a company's federal taxes.
This information is required is to onboard a company for use with Gusto Embedded Payroll.

scope: `company_federal_taxes:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_attributes_response = gustoembeddedpayroll.federal_tax_details.update_attributes(
    version="string_example",
    company_id="company_id_example",
    legal_name="string_example",
    ein="string_example",
    tax_payer_type="C-Corporation",
    filing_form="string_example",
    taxable_as_scorp=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### legal_name: `str`<a id="legal_name-str"></a>

The legal name of the company

##### ein: `str`<a id="ein-str"></a>

The EIN of of the company

##### tax_payer_type: `str`<a id="tax_payer_type-str"></a>

What type of tax entity the company is

##### filing_form: `str`<a id="filing_form-str"></a>

The form used by the company for federal tax filing. One of: - 941 (Quarterly federal tax return) - 944 (Annual federal tax return)

##### taxable_as_scorp: `bool`<a id="taxable_as_scorp-bool"></a>

Whether this company should be taxed as an S-Corporation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FederalTaxDetailsUpdateAttributesRequest`](./gusto_embedded_payroll_python_sdk/type/federal_tax_details_update_attributes_request.py)
Attributes related to federal tax details that can be updated via this endpoint include:

#### 🔄 Return<a id="🔄-return"></a>

[`FederalTaxDetails`](./gusto_embedded_payroll_python_sdk/pydantic/federal_tax_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/federal_tax_details` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.flows.generate_link`<a id="gustoembeddedpayrollflowsgenerate_link"></a>

Generate a link to access a pre-built workflow in Gusto white-label UI. For security, all generated flows will expire within 1 hour of inactivity or 24 hours from creation time, whichever comes first.

scope: `flows:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_link_response = gustoembeddedpayroll.flows.generate_link(
    flow_type="string_example",
    company_uuid="company_uuid_example",
    entity_uuid="string_example",
    entity_type="Company",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### flow_type: `str`<a id="flow_type-str"></a>

flow type

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### entity_uuid: `str`<a id="entity_uuid-str"></a>

UUID of the target entity applicable to the flow. This field is optional for company flows, please refer to the flow_types table above for more details.

##### entity_type: `str`<a id="entity_type-str"></a>

the type of target entity applicable to the flow. This field is optional for company flows, please refer to the flow_types table above for more details.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FlowsGenerateLinkRequest`](./gusto_embedded_payroll_python_sdk/type/flows_generate_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Flow`](./gusto_embedded_payroll_python_sdk/pydantic/flow.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/flows` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.garnishments.create_garnishment`<a id="gustoembeddedpayrollgarnishmentscreate_garnishment"></a>

Garnishments, or employee deductions, are fixed amounts or percentages deducted from an employee’s pay. They can be deducted a specific number of times or on a recurring basis. Garnishments can also have maximum deductions on a yearly or per-pay-period bases. Common uses for garnishments are court-ordered payments for child support or back taxes. Some companies provide loans to their employees that are repaid via garnishments.

scope: `garnishments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_garnishment_response = gustoembeddedpayroll.garnishments.create_garnishment(
    description="string_example",
    amount="string_example",
    court_ordered=True,
    employee_id="employee_id_example",
    active=True,
    times=1,
    recurring=False,
    annual_maximum="string_example",
    pay_period_maximum="string_example",
    deduct_as_percentage=False,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

The description of the garnishment.

##### amount: `float`<a id="amount-float"></a>

The amount of the garnishment. Either a percentage or a fixed dollar amount. Represented as a float, e.g. \\\"8.00\\\".

##### court_ordered: `bool`<a id="court_ordered-bool"></a>

Whether the garnishment is court ordered.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### active: `bool`<a id="active-bool"></a>

Whether or not this garnishment is currently active.

##### times: `Optional[int]`<a id="times-optionalint"></a>

The number of times to apply the garnishment. Ignored if recurring is true.

##### recurring: `bool`<a id="recurring-bool"></a>

Whether the garnishment should recur indefinitely.

##### annual_maximum: `Optional[float]`<a id="annual_maximum-optionalfloat"></a>

The maximum deduction per annum. A null value indicates no maximum. Represented as a float, e.g. \\\"200.00\\\".

##### pay_period_maximum: `Optional[float]`<a id="pay_period_maximum-optionalfloat"></a>

The maximum deduction per pay period. A null value indicates no maximum. Represented as a float, e.g. \\\"16.00\\\".

##### deduct_as_percentage: `bool`<a id="deduct_as_percentage-bool"></a>

Whether the amount should be treated as a percentage to be deducted per pay period.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GarnishmentsCreateGarnishmentRequest`](./gusto_embedded_payroll_python_sdk/type/garnishments_create_garnishment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Garnishment`](./gusto_embedded_payroll_python_sdk/pydantic/garnishment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/garnishments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.garnishments.get_employee_garnishments`<a id="gustoembeddedpayrollgarnishmentsget_employee_garnishments"></a>

Garnishments, or employee deductions, are fixed amounts or percentages deducted from an employee’s pay. They can be deducted a specific number of times or on a recurring basis. Garnishments can also have maximum deductions on a yearly or per-pay-period bases. Common uses for garnishments are court-ordered payments for child support or back taxes. Some companies provide loans to their employees that are repaid via garnishments.

scope: `garnishments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_garnishments_response = (
    gustoembeddedpayroll.garnishments.get_employee_garnishments(
        employee_id="employee_id_example",
        page=3.14,
        per=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`GarnishmentsGetEmployeeGarnishmentsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/garnishments_get_employee_garnishments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/garnishments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.garnishments.get_garnishment`<a id="gustoembeddedpayrollgarnishmentsget_garnishment"></a>

Garnishments, or employee deductions, are fixed amounts or percentages deducted from an employee’s pay. They can be deducted a specific number of times or on a recurring basis. Garnishments can also have maximum deductions on a yearly or per-pay-period bases. Common uses for garnishments are court-ordered payments for child support or back taxes. Some companies provide loans to their employees that are repaid via garnishments.

scope: `garnishments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_garnishment_response = gustoembeddedpayroll.garnishments.get_garnishment(
    garnishment_id="garnishment_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### garnishment_id: `str`<a id="garnishment_id-str"></a>

The UUID of the garnishment

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Garnishment`](./gusto_embedded_payroll_python_sdk/pydantic/garnishment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/garnishments/{garnishment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.garnishments.update_garnishment`<a id="gustoembeddedpayrollgarnishmentsupdate_garnishment"></a>

Garnishments, or employee deductions, are fixed amounts or percentages deducted from an employee’s pay. They can be deducted a specific number of times or on a recurring basis. Garnishments can also have maximum deductions on a yearly or per-pay-period bases. Common uses for garnishments are court-ordered payments for child support or back taxes. Some companies provide loans to their employees that are repaid via garnishments.

scope: `garnishments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_garnishment_response = gustoembeddedpayroll.garnishments.update_garnishment(
    version="string_example",
    garnishment_id="garnishment_id_example",
    description="string_example",
    active=True,
    amount="string_example",
    court_ordered=True,
    times=1,
    recurring=False,
    annual_maximum="string_example",
    pay_period_maximum="string_example",
    deduct_as_percentage=False,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### garnishment_id: `str`<a id="garnishment_id-str"></a>

The UUID of the garnishment

##### description: `str`<a id="description-str"></a>

The description of the garnishment.

##### active: `bool`<a id="active-bool"></a>

Whether or not this garnishment is currently active.

##### amount: `float`<a id="amount-float"></a>

The amount of the garnishment. Either a percentage or a fixed dollar amount. Represented as a float, e.g. \\\"8.00\\\".

##### court_ordered: `bool`<a id="court_ordered-bool"></a>

Whether the garnishment is court ordered.

##### times: `Optional[int]`<a id="times-optionalint"></a>

The number of times to apply the garnishment. Ignored if recurring is true.

##### recurring: `bool`<a id="recurring-bool"></a>

Whether the garnishment should recur indefinitely.

##### annual_maximum: `Optional[float]`<a id="annual_maximum-optionalfloat"></a>

The maximum deduction per annum. A null value indicates no maximum. Represented as a float, e.g. \\\"200.00\\\".

##### pay_period_maximum: `Optional[float]`<a id="pay_period_maximum-optionalfloat"></a>

The maximum deduction per pay period. A null value indicates no maximum. Represented as a float, e.g. \\\"16.00\\\".

##### deduct_as_percentage: `bool`<a id="deduct_as_percentage-bool"></a>

Whether the amount should be treated as a percentage to be deducted per pay period.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GarnishmentsUpdateGarnishmentRequest`](./gusto_embedded_payroll_python_sdk/type/garnishments_update_garnishment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Garnishment`](./gusto_embedded_payroll_python_sdk/pydantic/garnishment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/garnishments/{garnishment_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.generated_documents.get_document_by_request_uuid`<a id="gustoembeddedpayrollgenerated_documentsget_document_by_request_uuid"></a>

Get a generated document given the request_uuid. The response will include the generation request's status and, if complete, the relevant document urls.

scope: `generated_documents:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_document_by_request_uuid_response = (
    gustoembeddedpayroll.generated_documents.get_document_by_request_uuid(
        document_type="document_type_example",
        request_uuid="request_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### document_type: `str`<a id="document_type-str"></a>

the type of document being generated

##### request_uuid: `str`<a id="request_uuid-str"></a>

The UUID of the Generated Document Request

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`GeneratedDocument`](./gusto_embedded_payroll_python_sdk/pydantic/generated_document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/generated_documents/{document_type}/{request_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.holiday_pay_policies.add_employees_to_policy`<a id="gustoembeddedpayrollholiday_pay_policiesadd_employees_to_policy"></a>

Add employees to a company's holiday pay policy

scope: `holiday_pay_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_employees_to_policy_response = (
    gustoembeddedpayroll.holiday_pay_policies.add_employees_to_policy(
        version="string_example",
        company_uuid="company_uuid_example",
        employees=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### employees: [`HolidayPayPoliciesAddEmployeesToPolicyRequestEmployees`](./gusto_embedded_payroll_python_sdk/type/holiday_pay_policies_add_employees_to_policy_request_employees.py)<a id="employees-holidaypaypoliciesaddemployeestopolicyrequestemployeesgusto_embedded_payroll_python_sdktypeholiday_pay_policies_add_employees_to_policy_request_employeespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HolidayPayPoliciesAddEmployeesToPolicyRequest`](./gusto_embedded_payroll_python_sdk/type/holiday_pay_policies_add_employees_to_policy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HolidayPayPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/holiday_pay_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/holiday_pay_policy/add` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.holiday_pay_policies.create_company_policy`<a id="gustoembeddedpayrollholiday_pay_policiescreate_company_policy"></a>

Create a holiday pay policy for a company

scope: `holiday_pay_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_company_policy_response = (
    gustoembeddedpayroll.holiday_pay_policies.create_company_policy(
        company_uuid="company_uuid_example",
        federal_holidays={},
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### federal_holidays: [`HolidayPayPoliciesCreateCompanyPolicyRequestFederalHolidays`](./gusto_embedded_payroll_python_sdk/type/holiday_pay_policies_create_company_policy_request_federal_holidays.py)<a id="federal_holidays-holidaypaypoliciescreatecompanypolicyrequestfederalholidaysgusto_embedded_payroll_python_sdktypeholiday_pay_policies_create_company_policy_request_federal_holidayspy"></a>


##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HolidayPayPoliciesCreateCompanyPolicyRequest`](./gusto_embedded_payroll_python_sdk/type/holiday_pay_policies_create_company_policy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HolidayPayPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/holiday_pay_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/holiday_pay_policy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.holiday_pay_policies.delete_policy`<a id="gustoembeddedpayrollholiday_pay_policiesdelete_policy"></a>

Delete a company's holiday pay policy

scope: `holiday_pay_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.holiday_pay_policies.delete_policy(
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/holiday_pay_policy` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.holiday_pay_policies.get_company_policy`<a id="gustoembeddedpayrollholiday_pay_policiesget_company_policy"></a>

Get a company's holiday pay policy

scope: `holiday_pay_policies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_policy_response = (
    gustoembeddedpayroll.holiday_pay_policies.get_company_policy(
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`HolidayPayPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/holiday_pay_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/holiday_pay_policy` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.holiday_pay_policies.preview_company_paid_holidays`<a id="gustoembeddedpayrollholiday_pay_policiespreview_company_paid_holidays"></a>

Preview a company's paid holidays

scope: `holiday_pay_policies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
preview_company_paid_holidays_response = (
    gustoembeddedpayroll.holiday_pay_policies.preview_company_paid_holidays(
        company_uuid="company_uuid_example",
        year="string_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### year: `str`<a id="year-str"></a>

If a year is passed, paid holidays for that year will be returned. Otherwise, paid holidays for the next three years will be returned.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HolidayPayPoliciesPreviewCompanyPaidHolidaysRequest`](./gusto_embedded_payroll_python_sdk/type/holiday_pay_policies_preview_company_paid_holidays_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaidHolidays`](./gusto_embedded_payroll_python_sdk/pydantic/paid_holidays.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/paid_holidays` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.holiday_pay_policies.remove_employees`<a id="gustoembeddedpayrollholiday_pay_policiesremove_employees"></a>

Remove employees from a company's holiday pay policy

scope: `holiday_pay_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_employees_response = gustoembeddedpayroll.holiday_pay_policies.remove_employees(
    version="string_example",
    company_uuid="company_uuid_example",
    employees=[{}],
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### employees: [`HolidayPayPoliciesRemoveEmployeesRequestEmployees`](./gusto_embedded_payroll_python_sdk/type/holiday_pay_policies_remove_employees_request_employees.py)<a id="employees-holidaypaypoliciesremoveemployeesrequestemployeesgusto_embedded_payroll_python_sdktypeholiday_pay_policies_remove_employees_request_employeespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HolidayPayPoliciesRemoveEmployeesRequest`](./gusto_embedded_payroll_python_sdk/type/holiday_pay_policies_remove_employees_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HolidayPayPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/holiday_pay_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/holiday_pay_policy/remove` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.holiday_pay_policies.update_policy`<a id="gustoembeddedpayrollholiday_pay_policiesupdate_policy"></a>

Update a company's holiday pay policy

scope: `holiday_pay_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_policy_response = gustoembeddedpayroll.holiday_pay_policies.update_policy(
    version="string_example",
    company_uuid="company_uuid_example",
    federal_holidays={},
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### federal_holidays: [`HolidayPayPoliciesUpdatePolicyRequestFederalHolidays`](./gusto_embedded_payroll_python_sdk/type/holiday_pay_policies_update_policy_request_federal_holidays.py)<a id="federal_holidays-holidaypaypoliciesupdatepolicyrequestfederalholidaysgusto_embedded_payroll_python_sdktypeholiday_pay_policies_update_policy_request_federal_holidayspy"></a>


##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HolidayPayPoliciesUpdatePolicyRequest`](./gusto_embedded_payroll_python_sdk/type/holiday_pay_policies_update_policy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HolidayPayPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/holiday_pay_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/holiday_pay_policy` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.industry_selection.get_company_industry_selection`<a id="gustoembeddedpayrollindustry_selectionget_company_industry_selection"></a>

Get industry selection for the company.

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_industry_selection_response = (
    gustoembeddedpayroll.industry_selection.get_company_industry_selection(
        company_id="company_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Industry`](./gusto_embedded_payroll_python_sdk/pydantic/industry.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/industry_selection` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.industry_selection.update_company_industry_selection`<a id="gustoembeddedpayrollindustry_selectionupdate_company_industry_selection"></a>

Update the company industry selection by passing in industry classification codes: [NAICS code](https://www.naics.com), [SICS code](https://siccode.com/) and industry title. Our UI is leveraging [Middesk API](https://docs.middesk.com/reference/introduction) to determine industry classification codes.

scope: `companies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_company_industry_selection_response = (
    gustoembeddedpayroll.industry_selection.update_company_industry_selection(
        title="string_example",
        naics_code="string_example",
        company_id="company_id_example",
        sic_codes=["string_example"],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Industry title

##### naics_code: `str`<a id="naics_code-str"></a>

North American Industry Classification System (NAICS) is used to classify businesses with a six digit number based on the primary type of work the business performs

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### sic_codes: [`IndustrySelectionUpdateCompanyIndustrySelectionRequestSicCodes`](./gusto_embedded_payroll_python_sdk/type/industry_selection_update_company_industry_selection_request_sic_codes.py)<a id="sic_codes-industryselectionupdatecompanyindustryselectionrequestsiccodesgusto_embedded_payroll_python_sdktypeindustry_selection_update_company_industry_selection_request_sic_codespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IndustrySelectionUpdateCompanyIndustrySelectionRequest`](./gusto_embedded_payroll_python_sdk/type/industry_selection_update_company_industry_selection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Industry`](./gusto_embedded_payroll_python_sdk/pydantic/industry.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/industry_selection` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.introspection.exchange_refresh_token`<a id="gustoembeddedpayrollintrospectionexchange_refresh_token"></a>

Exchange a refresh token for a new access token.

The previous `refresh_token` will be revoked on the first usage of the new `access_token`.

The `expires_in` value is provided in seconds from when the `access_token` was generated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
exchange_refresh_token_response = (
    gustoembeddedpayroll.introspection.exchange_refresh_token(
        client_id="string_example",
        client_secret="string_example",
        refresh_token="string_example",
        grant_type="string_example",
        redirect_uri="string_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

Your client id

##### client_secret: `str`<a id="client_secret-str"></a>

Your client secret

##### refresh_token: `str`<a id="refresh_token-str"></a>

The `refresh_token` being exchanged for an access token code

##### grant_type: `str`<a id="grant_type-str"></a>

this should be the literal string 'refresh_token'

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The redirect URI you set up via the Developer Portal

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntrospectionExchangeRefreshTokenRequest`](./gusto_embedded_payroll_python_sdk/type/introspection_exchange_refresh_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Authentication`](./gusto_embedded_payroll_python_sdk/pydantic/authentication.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.introspection.get_current_access_token_info`<a id="gustoembeddedpayrollintrospectionget_current_access_token_info"></a>

Returns scope and resource information associated with the current access token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_access_token_info_response = (
    gustoembeddedpayroll.introspection.get_current_access_token_info(
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`IntrospectionGetCurrentAccessTokenInfoResponse`](./gusto_embedded_payroll_python_sdk/pydantic/introspection_get_current_access_token_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/token_info` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.invoices.get_invoicing_data_for_companies`<a id="gustoembeddedpayrollinvoicesget_invoicing_data_for_companies"></a>

Retrieve data for active companies used to calculate invoices for Gusto Embedded Payroll. A company is considered active for an invoice period if they are an active partner managed company, have run payroll or created contractor payments since becoming a partner managed company, and are not suspended at any point during the invoice period.  This endpoint forces pagination, with 100 results returned at a time. You can learn more about our pagination here: [pagination guide](https://docs.gusto.com/embedded-payroll/docs/pagination) 

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#retrieving-access-tokens)

scope: `invoices:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_invoicing_data_for_companies_response = (
    gustoembeddedpayroll.invoices.get_invoicing_data_for_companies(
        invoice_period="2020-01",
        page=3.14,
        per=3.14,
        company_uuids="string_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_period: `str`<a id="invoice_period-str"></a>

The month we are calculating the invoice for. Must be in YYYY-MM format

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### company_uuids: `str`<a id="company_uuids-str"></a>

Filter companies returned in the active_companies response, will return an error if company not active during provided invoice period. i.e. `?company_uuids=781922d8-e780-4b6b-bf74-ee303166d022,bbbca930-7322-491c-ba7f-98707a52a9c5`

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`InvoiceData`](./gusto_embedded_payroll_python_sdk/pydantic/invoice_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/invoices/{invoice_period}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.create_compensation`<a id="gustoembeddedpayrolljobs_and_compensationscreate_compensation"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_compensation_response = (
    gustoembeddedpayroll.jobs_and_compensations.create_compensation(
        payment_unit="Hour",
        flsa_status="Nonexempt",
        job_id="job_id_example",
        rate="string_example",
        effective_date="string_example",
        adjust_for_minimum_wage=True,
        minimum_wages=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_unit: `str`<a id="payment_unit-str"></a>

The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.

##### flsa_status: [`FlsaStatusType`](./gusto_embedded_payroll_python_sdk/type/flsa_status_type.py)<a id="flsa_status-flsastatustypegusto_embedded_payroll_python_sdktypeflsa_status_typepy"></a>

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### rate: `str`<a id="rate-str"></a>

The dollar amount paid per payment unit.

##### effective_date: `str`<a id="effective_date-str"></a>

The date when the compensation takes effect.

##### adjust_for_minimum_wage: `bool`<a id="adjust_for_minimum_wage-bool"></a>

Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees.

##### minimum_wages: [`JobsAndCompensationsCreateCompensationRequestMinimumWages`](./gusto_embedded_payroll_python_sdk/type/jobs_and_compensations_create_compensation_request_minimum_wages.py)<a id="minimum_wages-jobsandcompensationscreatecompensationrequestminimumwagesgusto_embedded_payroll_python_sdktypejobs_and_compensations_create_compensation_request_minimum_wagespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsAndCompensationsCreateCompensationRequest`](./gusto_embedded_payroll_python_sdk/type/jobs_and_compensations_create_compensation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Compensation`](./gusto_embedded_payroll_python_sdk/pydantic/compensation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}/compensations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.create_job`<a id="gustoembeddedpayrolljobs_and_compensationscreate_job"></a>

Create a job.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_job_response = gustoembeddedpayroll.jobs_and_compensations.create_job(
    title="string_example",
    hire_date="string_example",
    employee_id="employee_id_example",
    two_percent_shareholder=True,
    state_wc_covered=True,
    state_wc_class_code="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The job title

##### hire_date: `str`<a id="hire_date-str"></a>

The date when the employee was hired or rehired for the job.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee owns at least 2% of the company.

##### state_wc_covered: `bool`<a id="state_wc_covered-bool"></a>

Whether this job is eligible for workers' compensation coverage in the state of Washington (WA).

##### state_wc_class_code: `str`<a id="state_wc_class_code-str"></a>

The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsAndCompensationsCreateJobRequest`](./gusto_embedded_payroll_python_sdk/type/jobs_and_compensations_create_job_request.py)
Create a job.

#### 🔄 Return<a id="🔄-return"></a>

[`Job`](./gusto_embedded_payroll_python_sdk/pydantic/job.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/jobs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.delete_job_by_id`<a id="gustoembeddedpayrolljobs_and_compensationsdelete_job_by_id"></a>

Deletes a specific job that an employee holds.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.jobs_and_compensations.delete_job_by_id(
    job_id="job_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.get_compensation_by_id`<a id="gustoembeddedpayrolljobs_and_compensationsget_compensation_by_id"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`.

scope: `jobs:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compensation_by_id_response = (
    gustoembeddedpayroll.jobs_and_compensations.get_compensation_by_id(
        compensation_id="compensation_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### compensation_id: `str`<a id="compensation_id-str"></a>

The UUID of the compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Compensation`](./gusto_embedded_payroll_python_sdk/pydantic/compensation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/compensations/{compensation_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.get_employee_jobs`<a id="gustoembeddedpayrolljobs_and_compensationsget_employee_jobs"></a>

Get all of the jobs that an employee holds.

scope: `jobs:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_jobs_response = (
    gustoembeddedpayroll.jobs_and_compensations.get_employee_jobs(
        employee_id="employee_id_example",
        page=3.14,
        per=3.14,
        include="all_compensations",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### include: `str`<a id="include-str"></a>

Available options: - all_compensations: Include all effective dated compensations for each job instead of only the current compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`JobsAndCompensationsGetEmployeeJobsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/jobs_and_compensations_get_employee_jobs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.get_job_compensations`<a id="gustoembeddedpayrolljobs_and_compensationsget_job_compensations"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`. By default the API returns only the current compensation - see the `include` query parameter for retrieving all compensations.

Note: Currently the API does not support creating multiple compensations per job - creating a compensation with the same `job_uuid` as another will fail with a relevant error.

Use `flsa_status` to determine if an employee is eligible for overtime.

scope: `jobs:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_compensations_response = (
    gustoembeddedpayroll.jobs_and_compensations.get_job_compensations(
        job_id="job_id_example",
        page=3.14,
        per=3.14,
        include="all_compensations",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### include: `str`<a id="include-str"></a>

Available options: - all_compensations: Include all effective dated compensations for each job instead of only the current compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`JobsAndCompensationsGetJobCompensationsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/jobs_and_compensations_get_job_compensations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}/compensations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.get_job_details`<a id="gustoembeddedpayrolljobs_and_compensationsget_job_details"></a>

Get a job.

scope: `jobs:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_details_response = gustoembeddedpayroll.jobs_and_compensations.get_job_details(
    job_id="job_id_example",
    include="all_compensations",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### include: `str`<a id="include-str"></a>

Available options: - all_compensations: Include all effective dated compensations for the job instead of only the current compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Job`](./gusto_embedded_payroll_python_sdk/pydantic/job.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.remove_compensation`<a id="gustoembeddedpayrolljobs_and_compensationsremove_compensation"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`. This endpoint deletes a compensation for a job that hasn't been processed on payroll.

scope: `jobs:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.jobs_and_compensations.remove_compensation(
    compensation_id="compensation_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### compensation_id: `str`<a id="compensation_id-str"></a>

The UUID of the compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/compensations/{compensation_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.update_compensation`<a id="gustoembeddedpayrolljobs_and_compensationsupdate_compensation"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_compensation_response = (
    gustoembeddedpayroll.jobs_and_compensations.update_compensation(
        version="string_example",
        compensation_id="compensation_id_example",
        rate="string_example",
        payment_unit="Hour",
        flsa_status="Nonexempt",
        adjust_for_minimum_wage=True,
        minimum_wages=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### compensation_id: `str`<a id="compensation_id-str"></a>

The UUID of the compensation

##### rate: `str`<a id="rate-str"></a>

The dollar amount paid per payment unit.

##### payment_unit: `str`<a id="payment_unit-str"></a>

The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.

##### flsa_status: [`FlsaStatusType`](./gusto_embedded_payroll_python_sdk/type/flsa_status_type.py)<a id="flsa_status-flsastatustypegusto_embedded_payroll_python_sdktypeflsa_status_typepy"></a>

##### adjust_for_minimum_wage: `bool`<a id="adjust_for_minimum_wage-bool"></a>

Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees.

##### minimum_wages: [`JobsAndCompensationsUpdateCompensationRequestMinimumWages`](./gusto_embedded_payroll_python_sdk/type/jobs_and_compensations_update_compensation_request_minimum_wages.py)<a id="minimum_wages-jobsandcompensationsupdatecompensationrequestminimumwagesgusto_embedded_payroll_python_sdktypejobs_and_compensations_update_compensation_request_minimum_wagespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsAndCompensationsUpdateCompensationRequest`](./gusto_embedded_payroll_python_sdk/type/jobs_and_compensations_update_compensation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Compensation`](./gusto_embedded_payroll_python_sdk/pydantic/compensation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/compensations/{compensation_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.jobs_and_compensations.update_job`<a id="gustoembeddedpayrolljobs_and_compensationsupdate_job"></a>

Update a job.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_job_response = gustoembeddedpayroll.jobs_and_compensations.update_job(
    version="string_example",
    job_id="job_id_example",
    title="string_example",
    hire_date="string_example",
    two_percent_shareholder=True,
    state_wc_covered=True,
    state_wc_class_code="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### title: `str`<a id="title-str"></a>

The job title

##### hire_date: `str`<a id="hire_date-str"></a>

The date when the employee was hired or rehired for the job.

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee owns at least 2% of the company.

##### state_wc_covered: `bool`<a id="state_wc_covered-bool"></a>

Whether this job is eligible for workers' compensation coverage in the state of Washington (WA).

##### state_wc_class_code: `str`<a id="state_wc_class_code-str"></a>

The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsAndCompensationsUpdateJobRequest`](./gusto_embedded_payroll_python_sdk/type/jobs_and_compensations_update_job_request.py)
Update a job.

#### 🔄 Return<a id="🔄-return"></a>

[`Job`](./gusto_embedded_payroll_python_sdk/pydantic/job.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.locations.create_company_location`<a id="gustoembeddedpayrolllocationscreate_company_location"></a>

Company locations represent all addresses associated with a company. These can be filing addresses, mailing addresses, and/or work locations; one address may serve multiple, or all, purposes.

Since all company locations are subsets of locations, retrieving or updating an individual record should be done via the locations endpoints.

scope: `companies.write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_company_location_response = (
    gustoembeddedpayroll.locations.create_company_location(
        phone_number="0480728880",
        street_1="string_example",
        city="string_example",
        state="string_example",
        zip="string_example",
        company_id="company_id_example",
        street_2="string_example",
        country="USA",
        mailing_address=True,
        filing_address=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### street_1: `str`<a id="street_1-str"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### street_2: `Optional[str]`<a id="street_2-optionalstr"></a>

##### country: `str`<a id="country-str"></a>

##### mailing_address: `bool`<a id="mailing_address-bool"></a>

Specify if this location is the company's mailing address.

##### filing_address: `bool`<a id="filing_address-bool"></a>

Specify if this location is the company's filing address.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationsCreateCompanyLocationRequest`](./gusto_embedded_payroll_python_sdk/type/locations_create_company_location_request.py)
Create a company location.

#### 🔄 Return<a id="🔄-return"></a>

[`Location`](./gusto_embedded_payroll_python_sdk/pydantic/location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/locations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.locations.get_by_id`<a id="gustoembeddedpayrolllocationsget_by_id"></a>

Get a location.

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = gustoembeddedpayroll.locations.get_by_id(
    location_id="location_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_id: `str`<a id="location_id-str"></a>

The UUID of the location

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Location`](./gusto_embedded_payroll_python_sdk/pydantic/location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/locations/{location_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.locations.get_company_locations`<a id="gustoembeddedpayrolllocationsget_company_locations"></a>

Company locations represent all addresses associated with a company. These can be filing addresses, mailing addresses, and/or work locations; one address may serve multiple, or all, purposes.

Since all company locations are subsets of locations, retrieving or updating an individual record should be done via the locations endpoints.

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_locations_response = gustoembeddedpayroll.locations.get_company_locations(
    company_id="company_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsGetCompanyLocationsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/locations_get_company_locations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.locations.get_minimum_wages`<a id="gustoembeddedpayrolllocationsget_minimum_wages"></a>

Get minimum wages for a location

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_minimum_wages_response = gustoembeddedpayroll.locations.get_minimum_wages(
    location_uuid="location_uuid_example",
    effective_date="2020-01-31",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_uuid: `str`<a id="location_uuid-str"></a>

The UUID of the location

##### effective_date: `str`<a id="effective_date-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsGetMinimumWagesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/locations_get_minimum_wages_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/locations/{location_uuid}/minimum_wages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.locations.update_location`<a id="gustoembeddedpayrolllocationsupdate_location"></a>

Update a location.

scope: `companies.write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_location_response = gustoembeddedpayroll.locations.update_location(
    body=None,
    location_id="location_id_example",
    version="string_example",
    phone_number="0480728880",
    street_1="string_example",
    street_2="string_example",
    city="string_example",
    state="string_example",
    zip="string_example",
    country="string_example",
    mailing_address=True,
    filing_address=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_id: `str`<a id="location_id-str"></a>

The UUID of the location

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### phone_number: `str`<a id="phone_number-str"></a>

##### street_1: `str`<a id="street_1-str"></a>

##### street_2: `Optional[str]`<a id="street_2-optionalstr"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### country: `str`<a id="country-str"></a>

##### mailing_address: `bool`<a id="mailing_address-bool"></a>

For a company location, specify if this location is the company's mailing address. A company has a single mailing address, so this designation will override any previous selection.

##### filing_address: `bool`<a id="filing_address-bool"></a>

For a company location, specify if this location is the company's filing address. A company has a single filing address, so this designation will override any previous selection.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationsUpdateLocationRequest`](./gusto_embedded_payroll_python_sdk/type/locations_update_location_request.py)
Update a location

#### 🔄 Return<a id="🔄-return"></a>

[`Location`](./gusto_embedded_payroll_python_sdk/pydantic/location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/locations/{location_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.notifications.get_details`<a id="gustoembeddedpayrollnotificationsget_details"></a>

Upon receiving a notification webhook event, use this endpoint to fetch the notification's details. The notification details include basic suggested content that can help you build notifications in your platform.

Note: partners are responsible for the delivery and any custom state management of notifications in their application. Refer to our [partner notification guide](https://docs.gusto.com/embedded-payroll/docs/partner-notifications) for more details.

If the notification UUID is not found, the response will be 404 Not Found. If the notification's supporting data is no longer valid, the response will be 422 Unprocessable Entity.

scope: `notifications:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = gustoembeddedpayroll.notifications.get_details(
    notification_uuid="notification_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### notification_uuid: `str`<a id="notification_uuid-str"></a>

The UUID of the notification

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Notification`](./gusto_embedded_payroll_python_sdk/pydantic/notification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/notifications/{notification_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.assign_employees_to_schedules`<a id="gustoembeddedpayrollpay_schedulesassign_employees_to_schedules"></a>

This endpoints assigns employees to specified pay schedules based on the pay schedule type.

scope: `pay_schedules:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.pay_schedules.assign_employees_to_schedules(
    type="single",
    company_id="company_id_example",
    hourly_pay_schedule_uuid="string_example",
    salaried_pay_schedule_uuid="string_example",
    default_pay_schedule_uuid="string_example",
    employees=[{}],
    departments=[{}],
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

The pay schedule assignment type.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### hourly_pay_schedule_uuid: `str`<a id="hourly_pay_schedule_uuid-str"></a>

Pay schedule for hourly employees.

##### salaried_pay_schedule_uuid: `str`<a id="salaried_pay_schedule_uuid-str"></a>

Pay schedule for salaried employees.

##### default_pay_schedule_uuid: `str`<a id="default_pay_schedule_uuid-str"></a>

Default pay schedule for employees.

##### employees: [`PayScheduleAssignmentBodyEmployees`](./gusto_embedded_payroll_python_sdk/type/pay_schedule_assignment_body_employees.py)<a id="employees-payscheduleassignmentbodyemployeesgusto_embedded_payroll_python_sdktypepay_schedule_assignment_body_employeespy"></a>

##### departments: [`PayScheduleAssignmentBodyDepartments`](./gusto_embedded_payroll_python_sdk/type/pay_schedule_assignment_body_departments.py)<a id="departments-payscheduleassignmentbodydepartmentsgusto_embedded_payroll_python_sdktypepay_schedule_assignment_body_departmentspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayScheduleAssignmentBody`](./gusto_embedded_payroll_python_sdk/type/pay_schedule_assignment_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules/assign` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.create_new`<a id="gustoembeddedpayrollpay_schedulescreate_new"></a>

If a company does not have any pay schedules, this endpoint will create a single pay schedule and assign it to all employees. This is a common use case during company onboarding.

If a company has an existing active pay schedule and want to support multiple pay schedules, this endpoint will create a pay schedule that is not assigned to any employee.

Be sure to **[check state laws](https://www.dol.gov/agencies/whd/state/payday)** to know what schedule is right for your customers.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = gustoembeddedpayroll.pay_schedules.create_new(
    frequency="Every week",
    anchor_pay_date="2020-05-15",
    anchor_end_of_pay_period="2020-05-08",
    company_id="company_id_example",
    day_1=1,
    day_2=1,
    custom_name="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### frequency: `str`<a id="frequency-str"></a>

The frequency that employees on this pay schedule are paid with Gusto.

##### anchor_pay_date: `str`<a id="anchor_pay_date-str"></a>

The first date that employees on this pay schedule are paid with Gusto.

##### anchor_end_of_pay_period: `str`<a id="anchor_end_of_pay_period-str"></a>

The last date of the first pay period. This can be the same date as the anchor pay date.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### day_1: `Optional[int]`<a id="day_1-optionalint"></a>

An integer between 1 and 31 indicating the first day of the month that employees are paid. This field is only relevant for pay schedules with the “Twice per month” and “Monthly” frequencies. It will be null for pay schedules with other frequencies.

##### day_2: `Optional[int]`<a id="day_2-optionalint"></a>

An integer between 1 and 31 indicating the second day of the month that employees are paid. This field is the second pay date for pay schedules with the \\\"Twice per month\\\" frequency. For semi-monthly pay schedules, set this field to 31. For months shorter than 31 days, we will set the second pay date to the last day of the month. It will be null for pay schedules with other frequencies.

##### custom_name: `str`<a id="custom_name-str"></a>

A custom pay schedule name, defaults to the pay frequency description.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaySchedulesCreateNewRequest`](./gusto_embedded_payroll_python_sdk/type/pay_schedules_create_new_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedule`](./gusto_embedded_payroll_python_sdk/pydantic/pay_schedule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.get_assignments`<a id="gustoembeddedpayrollpay_schedulesget_assignments"></a>

This endpoint returns the current pay schedule assignment for a company, with pay schedule and employee/department mappings depending on the pay schedule type.

scope: `pay_schedules:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_assignments_response = gustoembeddedpayroll.pay_schedules.get_assignments(
    company_id="company_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayScheduleAssignment`](./gusto_embedded_payroll_python_sdk/pydantic/pay_schedule_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules/assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.get_details`<a id="gustoembeddedpayrollpay_schedulesget_details"></a>

The pay schedule object in Gusto captures the details of when employees work and when they should be paid. A company can have multiple pay schedules.

scope: `pay_schedules:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = gustoembeddedpayroll.pay_schedules.get_details(
    company_id="company_id_example",
    pay_schedule_id="pay_schedule_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### pay_schedule_id: `str`<a id="pay_schedule_id-str"></a>

The UUID of the pay schedule

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedule`](./gusto_embedded_payroll_python_sdk/pydantic/pay_schedule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules/{pay_schedule_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.get_pay_periods`<a id="gustoembeddedpayrollpay_schedulesget_pay_periods"></a>

Pay periods are the foundation of payroll. Compensation, time & attendance, taxes, and expense reports all rely on when they happened. To begin submitting information for a given payroll, we need to agree on the time period.

By default, this endpoint returns pay periods starting from 6 months ago to the date today.  Use the `start_date` and `end_date` parameters to change the scope of the response.  End dates can be up to 3 months in the future and there is no limit on start dates.

Starting in version '2023-04-01', the eligible_employees attribute was removed from the response.  The eligible employees for a payroll are determined by the employee_compensations returned from the payrolls#prepare endpoint.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_periods_response = gustoembeddedpayroll.pay_schedules.get_pay_periods(
    company_id="company_id_example",
    start_date="2020-01-01",
    end_date="2020-01-31",
    payroll_types="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### start_date: `str`<a id="start_date-str"></a>

##### end_date: `str`<a id="end_date-str"></a>

##### payroll_types: `str`<a id="payroll_types-str"></a>

regular and/or transition. Multiple options are comma separated. The default is regular pay periods if nothing is passed in.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedulesGetPayPeriodsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/pay_schedules_get_pay_periods_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_periods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.get_unprocessed_termination_pay_periods`<a id="gustoembeddedpayrollpay_schedulesget_unprocessed_termination_pay_periods"></a>

When a payroll admin terminates an employee and selects "Dismissal Payroll" as the employee's final payroll, their last pay period will appear on the list.

This endpoint returns the unprocessed pay periods for past and future terminated employees in a given company.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unprocessed_termination_pay_periods_response = (
    gustoembeddedpayroll.pay_schedules.get_unprocessed_termination_pay_periods(
        company_id="company_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedulesGetUnprocessedTerminationPayPeriodsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/pay_schedules_get_unprocessed_termination_pay_periods_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_periods/unprocessed_termination_pay_periods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.list_for_company`<a id="gustoembeddedpayrollpay_scheduleslist_for_company"></a>

The pay schedule object in Gusto captures the details of when employees work and when they should be paid. A company can have multiple pay schedules.

scope: `pay_schedules:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_company_response = gustoembeddedpayroll.pay_schedules.list_for_company(
    company_id="company_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedulesListForCompanyResponse`](./gusto_embedded_payroll_python_sdk/pydantic/pay_schedules_list_for_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.preview_assignments_for_company`<a id="gustoembeddedpayrollpay_schedulespreview_assignments_for_company"></a>

This endpoints returns the employee changes, including pay period and transition pay periods, for changing the pay schedule.

scope: `pay_schedules:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
preview_assignments_for_company_response = (
    gustoembeddedpayroll.pay_schedules.preview_assignments_for_company(
        type="single",
        company_id="company_id_example",
        hourly_pay_schedule_uuid="string_example",
        salaried_pay_schedule_uuid="string_example",
        default_pay_schedule_uuid="string_example",
        employees=[{}],
        departments=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

The pay schedule assignment type.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### hourly_pay_schedule_uuid: `str`<a id="hourly_pay_schedule_uuid-str"></a>

Pay schedule for hourly employees.

##### salaried_pay_schedule_uuid: `str`<a id="salaried_pay_schedule_uuid-str"></a>

Pay schedule for salaried employees.

##### default_pay_schedule_uuid: `str`<a id="default_pay_schedule_uuid-str"></a>

Default pay schedule for employees.

##### employees: [`PayScheduleAssignmentBodyEmployees`](./gusto_embedded_payroll_python_sdk/type/pay_schedule_assignment_body_employees.py)<a id="employees-payscheduleassignmentbodyemployeesgusto_embedded_payroll_python_sdktypepay_schedule_assignment_body_employeespy"></a>

##### departments: [`PayScheduleAssignmentBodyDepartments`](./gusto_embedded_payroll_python_sdk/type/pay_schedule_assignment_body_departments.py)<a id="departments-payscheduleassignmentbodydepartmentsgusto_embedded_payroll_python_sdktypepay_schedule_assignment_body_departmentspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayScheduleAssignmentBody`](./gusto_embedded_payroll_python_sdk/type/pay_schedule_assignment_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayScheduleAssignmentPreview`](./gusto_embedded_payroll_python_sdk/pydantic/pay_schedule_assignment_preview.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules/assignment_preview` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.preview_pay_schedule_dates`<a id="gustoembeddedpayrollpay_schedulespreview_pay_schedule_dates"></a>

Provides a preview of a pay schedule with the specified parameters

scope: `pay_schedules:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
preview_pay_schedule_dates_response = (
    gustoembeddedpayroll.pay_schedules.preview_pay_schedule_dates(
        company_id="company_id_example",
        frequency="Every week",
        anchor_pay_date="2020-05-15",
        anchor_end_of_pay_period="2020-05-08",
        day_1=1,
        day_2=1,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### frequency: `str`<a id="frequency-str"></a>

The frequency that employees on this pay schedule are paid with Gusto.

##### anchor_pay_date: `str`<a id="anchor_pay_date-str"></a>

The first date that employees on this pay schedule are paid with Gusto.

##### anchor_end_of_pay_period: `str`<a id="anchor_end_of_pay_period-str"></a>

The last date of the first pay period. This can be the same date as the anchor pay date.

##### day_1: `int`<a id="day_1-int"></a>

An integer between 1 and 31 indicating the first day of the month that employees are paid. This field is only relevant for pay schedules with the “Twice per month” and “Monthly” frequencies. It will be null for pay schedules with other frequencies.

##### day_2: `int`<a id="day_2-int"></a>

An integer between 1 and 31 indicating the second day of the month that employees are paid. This field is the second pay date for pay schedules with the \"Twice per month\" frequency. For semi-monthly pay schedules, set this field to 31. For months shorter than 31 days, we will set the second pay date to the last day of the month. It will be null for pay schedules with other frequencies.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedulesPreviewPayScheduleDatesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/pay_schedules_preview_pay_schedule_dates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules/preview` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.pay_schedules.update_pay_schedule`<a id="gustoembeddedpayrollpay_schedulesupdate_pay_schedule"></a>

Updates a pay schedule.

scope: `pay_schedules:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_pay_schedule_response = gustoembeddedpayroll.pay_schedules.update_pay_schedule(
    version="string_example",
    company_id="company_id_example",
    pay_schedule_id="pay_schedule_id_example",
    frequency="Every week",
    anchor_pay_date="2020-05-15",
    anchor_end_of_pay_period="2020-05-08",
    day_1=1,
    day_2=1,
    custom_name="string_example",
    auto_pilot=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### pay_schedule_id: `str`<a id="pay_schedule_id-str"></a>

The UUID of the pay schedule

##### frequency: `str`<a id="frequency-str"></a>

The frequency that employees on this pay schedule are paid with Gusto.

##### anchor_pay_date: `str`<a id="anchor_pay_date-str"></a>

The first date that employees on this pay schedule are paid with Gusto.

##### anchor_end_of_pay_period: `str`<a id="anchor_end_of_pay_period-str"></a>

The last date of the first pay period. This can be the same date as the anchor pay date.

##### day_1: `Optional[int]`<a id="day_1-optionalint"></a>

An integer between 1 and 31 indicating the first day of the month that employees are paid. This field is only relevant for pay schedules with the “Twice per month” and “Monthly” frequencies. It will be null for pay schedules with other frequencies.

##### day_2: `Optional[int]`<a id="day_2-optionalint"></a>

An integer between 1 and 31 indicating the second day of the month that employees are paid. This field is the second pay date for pay schedules with the \\\"Twice per month\\\" frequency. For semi-monthly pay schedules, set this field to 31. For months shorter than 31 days, we will set the second pay date to the last day of the month. It will be null for pay schedules with other frequencies.

##### custom_name: `str`<a id="custom_name-str"></a>

A custom pay schedule name.

##### auto_pilot: `bool`<a id="auto_pilot-bool"></a>

With Autopilot® enabled, payroll will run automatically one day before your payroll deadlines.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaySchedulesUpdatePayScheduleRequest`](./gusto_embedded_payroll_python_sdk/type/pay_schedules_update_pay_schedule_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedule`](./gusto_embedded_payroll_python_sdk/pydantic/pay_schedule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules/{pay_schedule_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payment_configs.get_company_payment_configs`<a id="gustoembeddedpayrollpayment_configsget_company_payment_configs"></a>

Get payment speed for the company and fast payment limit (1-day is only applicable to partners that opt in).

scope: `company_payment_configs:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_payment_configs_response = (
    gustoembeddedpayroll.payment_configs.get_company_payment_configs(
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentConfigs`](./gusto_embedded_payroll_python_sdk/pydantic/payment_configs.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/payment_configs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payment_configs.update_company_payment_configs`<a id="gustoembeddedpayrollpayment_configsupdate_company_payment_configs"></a>

Update payment speed and fast payment limit for a company. At least one of `payment_speed` or `fast_payment_limit` parameters is required. 1-day option is only applicable to partners that opt in.

scope: `company_payment_configs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_company_payment_configs_response = (
    gustoembeddedpayroll.payment_configs.update_company_payment_configs(
        fast_payment_limit="string_example",
        payment_speed="1-day",
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fast_payment_limit: `str`<a id="fast_payment_limit-str"></a>

Fast payment limit. This limit is an aggregate of all fast payrolls amount.

##### payment_speed: `str`<a id="payment_speed-str"></a>

Gusto Embedded supports three payment speeds (1-day, 2-day, and 4-day). For next-day payments, funds are deposited in your team's bank account by the end of the next business day. Most people will see the funds arrive the next afternoon, but payments may arrive as late as the end of the business day.

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentConfigsUpdateCompanyPaymentConfigsRequest`](./gusto_embedded_payroll_python_sdk/type/payment_configs_update_company_payment_configs_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentConfigs`](./gusto_embedded_payroll_python_sdk/pydantic/payment_configs.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/payment_configs` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.approved_reversals`<a id="gustoembeddedpayrollpayrollsapproved_reversals"></a>

Returns all approved Payroll Reversals for a Company.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
approved_reversals_response = gustoembeddedpayroll.payrolls.approved_reversals(
    company_id="company_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollReversal`](./gusto_embedded_payroll_python_sdk/pydantic/payroll_reversal.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payroll_reversals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.calculate_gross_up`<a id="gustoembeddedpayrollpayrollscalculate_gross_up"></a>

Calculates gross up earnings for an employee's payroll, given net earnings. This endpoint is only applicable to off-cycle unprocessed payrolls.

The gross up amount must then be mapped to the corresponding fixed compensation earning type to get the correct payroll amount. For example, for bonus off-cycles, the gross up amount should be set with the Bonus earning type in the payroll `fixed_compensations` field.

scope: `payrolls:run`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calculate_gross_up_response = gustoembeddedpayroll.payrolls.calculate_gross_up(
    employee_uuid="string_example",
    net_pay="string_example",
    payroll_uuid="payroll_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_uuid: `str`<a id="employee_uuid-str"></a>

Employee UUID

##### net_pay: `str`<a id="net_pay-str"></a>

Employee net earnings

##### payroll_uuid: `str`<a id="payroll_uuid-str"></a>

The UUID of the payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayrollsCalculateGrossUpRequest`](./gusto_embedded_payroll_python_sdk/type/payrolls_calculate_gross_up_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GrossUpPay`](./gusto_embedded_payroll_python_sdk/pydantic/gross_up_pay.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payrolls/{payroll_uuid}/gross_up` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.calculate_gross_up_0`<a id="gustoembeddedpayrollpayrollscalculate_gross_up_0"></a>

Performs calculations for taxes, benefits, and deductions for an unprocessed payroll. The calculated payroll details provide a preview of the actual values that will be used when the payroll is run.

This calculation is asynchronous and a successful request responds with a 202 HTTP status. To view the details of the calculated payroll, use the GET /v1/companies/{company_id}/payrolls/{payroll_id} endpoint with *include=taxes,benefits,deductions* params.
In v2023-04-01, *show_calculation=true* is no longer required.

If the company is blocked from running payroll due to issues like incomplete setup, missing information or other compliance issues, the response will be 422 Unprocessable Entity with a categorization of the blockers as described in the error responses.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.payrolls.calculate_gross_up_0(
    company_id="company_id_example",
    payroll_id="payroll_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}/calculate` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.cancel_payroll_transition`<a id="gustoembeddedpayrollpayrollscancel_payroll_transition"></a>

Transitions a `processed` payroll back to the `unprocessed` state. A payroll can be canceled if it meets both criteria:
- `processed` is true
- Current time is earlier than 3:30pm PT on the payroll_deadline

scope: `payrolls:run`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_payroll_transition_response = (
    gustoembeddedpayroll.payrolls.cancel_payroll_transition(
        company_id="company_id_example",
        payroll_id="payroll_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Payroll`](./gusto_embedded_payroll_python_sdk/pydantic/payroll.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}/cancel` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.create_off_cycle_payroll`<a id="gustoembeddedpayrollpayrollscreate_off_cycle_payroll"></a>

Creates a new, unprocessed, off-cycle payroll.

## `off_cycle_reason`<a id="off_cycle_reason"></a>
- External benefits and deductions will be included when the `off_cycle_reason` is set to `Correction`.
- All benefits and deductions are blocked when the `off_cycle_reason` is set to `Bonus`.

scope: `payrolls:run`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_off_cycle_payroll_response = (
    gustoembeddedpayroll.payrolls.create_off_cycle_payroll(
        off_cycle=True,
        off_cycle_reason="Bonus",
        start_date="string_example",
        end_date="string_example",
        company_id="company_id_example",
        pay_schedule_uuid="string_example",
        employee_uuids=["string_example"],
        check_date="string_example",
        withholding_pay_period="Every week",
        skip_regular_deductions=True,
        fixed_withholding_rate=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### off_cycle: `bool`<a id="off_cycle-bool"></a>

Whether it is an off cycle payroll.

##### off_cycle_reason: `str`<a id="off_cycle_reason-str"></a>

An off cycle payroll reason. Select one from the following list.

##### start_date: `str`<a id="start_date-str"></a>

Pay period start date.

##### end_date: `str`<a id="end_date-str"></a>

Pay period end date.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### pay_schedule_uuid: `str`<a id="pay_schedule_uuid-str"></a>

A pay schedule is required for Transition from old pay schedule payroll to identify the matching transition pay period.

##### employee_uuids: [`PayrollsCreateOffCyclePayrollRequestEmployeeUuids`](./gusto_embedded_payroll_python_sdk/type/payrolls_create_off_cycle_payroll_request_employee_uuids.py)<a id="employee_uuids-payrollscreateoffcyclepayrollrequestemployeeuuidsgusto_embedded_payroll_python_sdktypepayrolls_create_off_cycle_payroll_request_employee_uuidspy"></a>

##### check_date: `str`<a id="check_date-str"></a>

Payment date.

##### withholding_pay_period: `str`<a id="withholding_pay_period-str"></a>

The payment schedule tax rate the payroll is based on

##### skip_regular_deductions: `bool`<a id="skip_regular_deductions-bool"></a>

Block regular deductions and contributions for this payroll.

##### fixed_withholding_rate: `bool`<a id="fixed_withholding_rate-bool"></a>

Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayrollsCreateOffCyclePayrollRequest`](./gusto_embedded_payroll_python_sdk/type/payrolls_create_off_cycle_payroll_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayrollPrepared`](./gusto_embedded_payroll_python_sdk/pydantic/payroll_prepared.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.delete_unprocessed_payroll`<a id="gustoembeddedpayrollpayrollsdelete_unprocessed_payroll"></a>

This endpoint allows you to delete an **unprocessed** payroll.

By default the payroll and associated data is deleted synchronously. To request an asynchronous delete, use the `async=true` query parameter. In both cases validation of ability to delete will be performed and an Unprocessable Entity error will be returned if the payroll is not able to be deleted. A successful synchronous delete will return `204/No Content`. When a payroll has been enqueued for asynchronous deletion, `202/Accepted` will be returned.

scope: `payrolls:run`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.payrolls.delete_unprocessed_payroll(
    company_id="company_id_example",
    payroll_id="payroll_id_example",
    _async=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### _async: `bool`<a id="_async-bool"></a>

When true, request an asynchronous delete of the payroll.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.generate_printable_checks`<a id="gustoembeddedpayrollpayrollsgenerate_printable_checks"></a>

This endpoint initiates the generation of employee checks for the payroll specified by payroll_id. A generation status and corresponding generated document request_uuid will be returned. Use the generated document GET endpoint with document_type: `printable_payroll_checks` and request_uuid to poll the check generation process and retrieve the generated check URL upon completion.

scope: `generated_documents:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_printable_checks_response = (
    gustoembeddedpayroll.payrolls.generate_printable_checks(
        printing_format="string_example",
        payroll_id="payroll_id_example",
        starting_check_number=1,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### printing_format: `str`<a id="printing_format-str"></a>

The type of check stock being printed. Check this [link](https://support.gusto.com/article/999877761000000/Pay-your-team-by-check) for more info on check types

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### starting_check_number: `int`<a id="starting_check_number-int"></a>

The starting check number for the checks being generated

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayrollsGeneratePrintableChecksRequest`](./gusto_embedded_payroll_python_sdk/type/payrolls_generate_printable_checks_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayrollCheck`](./gusto_embedded_payroll_python_sdk/pydantic/payroll_check.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payrolls/{payroll_id}/generated_documents/printable_payroll_checks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.get_all_payroll_blockers`<a id="gustoembeddedpayrollpayrollsget_all_payroll_blockers"></a>

Returns a list of reasons that prevent the company from running payrolls. See the [payroll blockers guide](https://docs.gusto.com/embedded-payroll/docs/payroll-blockers) for a complete list of reasons.

The list is empty if there are no payroll blockers.

scope: `payrolls:run`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_payroll_blockers_response = (
    gustoembeddedpayroll.payrolls.get_all_payroll_blockers(
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollsGetAllPayrollBlockersResponse`](./gusto_embedded_payroll_python_sdk/pydantic/payrolls_get_all_payroll_blockers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/payrolls/blockers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.get_company_payrolls`<a id="gustoembeddedpayrollpayrollsget_company_payrolls"></a>

Returns a list of payrolls for a company. You can change the payrolls returned by updating the processing_status, payroll_types, start_date, & end_date params.

By default, will return processed, regular payrolls for the past 6 months.

Notes:
* Dollar amounts are returned as string representations of numeric decimals, are represented to the cent.
* end_date can be at most 3 months in the future and start_date and end_date can't be more than 1 year apart.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_payrolls_response = gustoembeddedpayroll.payrolls.get_company_payrolls(
    company_id="company_id_example",
    processing_statuses="unprocessed",
    payroll_types="regular",
    include="totals",
    start_date="string_example",
    end_date="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### processing_statuses: `str`<a id="processing_statuses-str"></a>

Whether to include processed and/or unprocessed payrolls in the response, defaults to processed, for multiple attributes comma separate the values, i.e. `?processing_statuses=processed,unprocessed`

##### payroll_types: `str`<a id="payroll_types-str"></a>

Whether to include regular and/or off_cycle payrolls in the response, defaults to regular, for multiple attributes comma separate the values, i.e. `?payroll_types=regular,off_cycle`

##### include: `str`<a id="include-str"></a>

Include the requested attribute in the response. In v2023-04-01 totals are no longer included by default. For multiple attributes comma separate the values, i.e. `?include=totals,payroll_status_meta`

##### start_date: `str`<a id="start_date-str"></a>

Return payrolls whose pay period is after the start date

##### end_date: `str`<a id="end_date-str"></a>

Return payrolls whose pay period is before the end date

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollsGetCompanyPayrollsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/payrolls_get_company_payrolls_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.get_employee_pay_stub`<a id="gustoembeddedpayrollpayrollsget_employee_pay_stub"></a>

Get an employee's pay stub for the specified payroll. By default, an application/pdf response will be returned. No other content types are currently supported, but may be supported in the future.

scope: `pay_stubs:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.payrolls.get_employee_pay_stub(
    payroll_id="payroll_id_example",
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payrolls/{payroll_id}/employees/{employee_id}/pay_stub` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.get_employee_pay_stubs`<a id="gustoembeddedpayrollpayrollsget_employee_pay_stubs"></a>

Get an employee's pay stubs

scope: `pay_stubs:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_pay_stubs_response = gustoembeddedpayroll.payrolls.get_employee_pay_stubs(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollsGetEmployeePayStubsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/payrolls_get_employee_pay_stubs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/pay_stubs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.get_single_payroll`<a id="gustoembeddedpayrollpayrollsget_single_payroll"></a>

Returns a payroll. If payroll is calculated or processed, will return employee_compensations and totals.

Notes:
* Hour and dollar amounts are returned as string representations of numeric decimals.
* Hours are represented to the thousands place; dollar amounts are represented to the cent.
* Every eligible compensation is returned for each employee. If no data has yet be inserted for a given field, it defaults to “0.00” (for fixed amounts) or “0.000” (for hours ).
* When include parameter with benefits value is passed, employee_benefits:read scope is required to return benefits
  * Benefits containing PHI are only visible with the `employee_benefits:read:phi` scope

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_payroll_response = gustoembeddedpayroll.payrolls.get_single_payroll(
    company_id="company_id_example",
    payroll_id="payroll_id_example",
    include="benefits",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### include: `str`<a id="include-str"></a>

Include the requested attribute in the response, for multiple attributes comma separate the values, i.e. `?include=benefits,deductions,taxes`

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Payroll`](./gusto_embedded_payroll_python_sdk/pydantic/payroll.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.get_single_receipt`<a id="gustoembeddedpayrollpayrollsget_single_receipt"></a>

Returns a payroll receipt.

Notes:
* Hour and dollar amounts are returned as string representations of numeric decimals.
* Dollar amounts are represented to the cent.
* If no data has yet be inserted for a given field, it defaults to “0.00” (for fixed amounts).

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_receipt_response = gustoembeddedpayroll.payrolls.get_single_receipt(
    payroll_uuid="payroll_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payroll_uuid: `str`<a id="payroll_uuid-str"></a>

The UUID of the payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollReceipt`](./gusto_embedded_payroll_python_sdk/pydantic/payroll_receipt.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payrolls/{payroll_uuid}/receipt` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.prepare_for_update`<a id="gustoembeddedpayrollpayrollsprepare_for_update"></a>

This endpoint will build the payroll and get it ready for making updates. This includes adding/removing eligible employees from the Payroll and updating the check_date, payroll_deadline, and payroll_status_meta dates & times.

Notes:
 * Will null out calculated_at & totals if a payroll has already been calculated.
 * Will return the version param used for updating the payroll

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
prepare_for_update_response = gustoembeddedpayroll.payrolls.prepare_for_update(
    company_id="company_id_example",
    payroll_id="payroll_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollPrepared`](./gusto_embedded_payroll_python_sdk/pydantic/payroll_prepared.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}/prepare` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.skip_payroll`<a id="gustoembeddedpayrollpayrollsskip_payroll"></a>

Submits a $0 payroll for employees associated with the pay schedule to skip payroll. This submission is asynchronous and a successful request responds with a 202 HTTP status. Upon success, the payroll is transitioned to the `processed` state.

If the company is blocked from running payroll due to issues like incomplete setup, missing information or other compliance issues, the response will be 422 Unprocessable Entity with a categorization of the blockers as described in the error responses.

scope: `payrolls:run`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.payrolls.skip_payroll(
    payroll_type="Regular",
    company_uuid="company_uuid_example",
    start_date="string_example",
    end_date="string_example",
    pay_schedule_uuid="string_example",
    employee_uuids=["string_example"],
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payroll_type: `str`<a id="payroll_type-str"></a>

Payroll type

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### start_date: `str`<a id="start_date-str"></a>

Pay period start date

##### end_date: `str`<a id="end_date-str"></a>

Pay period end date

##### pay_schedule_uuid: `str`<a id="pay_schedule_uuid-str"></a>

The UUID of the pay schedule

##### employee_uuids: [`PayrollsSkipPayrollRequestEmployeeUuids`](./gusto_embedded_payroll_python_sdk/type/payrolls_skip_payroll_request_employee_uuids.py)<a id="employee_uuids-payrollsskippayrollrequestemployeeuuidsgusto_embedded_payroll_python_sdktypepayrolls_skip_payroll_request_employee_uuidspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayrollsSkipPayrollRequest`](./gusto_embedded_payroll_python_sdk/type/payrolls_skip_payroll_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/payrolls/skip` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.submit_payroll`<a id="gustoembeddedpayrollpayrollssubmit_payroll"></a>

Submits an unprocessed payroll to be calculated and run. This submission is asynchronous and a successful request responds with a 202 HTTP status. Upon success, transitions the payroll to the `processed` state.

If the company is blocked from running payroll due to issues like incomplete setup, missing information or other compliance issues, the response will be 422 Unprocessable Entity with a categorization of the blockers as described in the error responses.

scope: `payrolls:run`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.payrolls.submit_payroll(
    company_id="company_id_example",
    payroll_id="payroll_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}/submit` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.payrolls.update_payroll_by_id`<a id="gustoembeddedpayrollpayrollsupdate_payroll_by_id"></a>

This endpoint allows you to update information for one or more employees for a specific **unprocessed** payroll.  You can think of the **unprocessed**
payroll object as a template of fields that you can update.  You cannot modify the structure of the payroll object through this endpoint, only values
of the fields included in the payroll.  If you do not include specific employee compensations or fixed/hourly compensations in your request body, they
will not be removed from the payroll.

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_payroll_by_id_response = gustoembeddedpayroll.payrolls.update_payroll_by_id(
    employee_compensations=[
        {
            "payment_method": "Direct Deposit",
        }
    ],
    company_id="company_id_example",
    payroll_id="payroll_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_compensations: [`PayrollsUpdatePayrollByIdRequestEmployeeCompensations`](./gusto_embedded_payroll_python_sdk/type/payrolls_update_payroll_by_id_request_employee_compensations.py)<a id="employee_compensations-payrollsupdatepayrollbyidrequestemployeecompensationsgusto_embedded_payroll_python_sdktypepayrolls_update_payroll_by_id_request_employee_compensationspy"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayrollsUpdatePayrollByIdRequest`](./gusto_embedded_payroll_python_sdk/type/payrolls_update_payroll_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayrollPrepared`](./gusto_embedded_payroll_python_sdk/pydantic/payroll_prepared.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.recovery_cases.initiate_redebit`<a id="gustoembeddedpayrollrecovery_casesinitiate_redebit"></a>

After resolving the underlying bank error, initiate a redebit for an open recovery case. This submission is asynchronous and a successful request responds with a 202 HTTP status.

It may take up to four business days for the ACH debit to process; in the meantime, the status of the recovery case will be in the `initiated_redebit` state. When funds are successfully redebited, the recovery case is transitioned to the `recovered` state.

If the company has exceeded maximum redebit attempts, or if the recovery case is not in a redebitable state, the response will be 422 Unprocessable Entity.

scope: `recovery_cases:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.recovery_cases.initiate_redebit(
    recovery_case_uuid="recovery_case_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recovery_case_uuid: `str`<a id="recovery_case_uuid-str"></a>

The UUID of the recovery case

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/recovery_cases/{recovery_case_uuid}/redebit` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.recovery_cases.list_for_company`<a id="gustoembeddedpayrollrecovery_caseslist_for_company"></a>

Fetch all recovery cases for a company.

scope: `recovery_cases:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_company_response = gustoembeddedpayroll.recovery_cases.list_for_company(
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`RecoveryCasesListForCompanyResponse`](./gusto_embedded_payroll_python_sdk/pydantic/recovery_cases_list_for_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/recovery_cases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.signatories.create_invite`<a id="gustoembeddedpayrollsignatoriescreate_invite"></a>

Create a signatory with minimal information. This signatory can be invited to provide more information through the `PUT /v1/companies/{company_uuid}/signatories/{signatory_uuid}` endpoint. This will start the identity verification process and allow the signatory to be verified to sign documents.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_invite_response = gustoembeddedpayroll.signatories.create_invite(
    email="string_example",
    company_uuid="company_uuid_example",
    title="string_example",
    first_name="string_example",
    last_name="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### title: `str`<a id="title-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SignatoriesCreateInviteRequest`](./gusto_embedded_payroll_python_sdk/type/signatories_create_invite_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Signatory`](./gusto_embedded_payroll_python_sdk/pydantic/signatory.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/signatories/invite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.signatories.create_signatory_with_complete_information`<a id="gustoembeddedpayrollsignatoriescreate_signatory_with_complete_information"></a>

Create a company signatory with complete information.
A signatory can legally sign forms once the identity verification process is successful.

scope: `signatories:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_signatory_with_complete_information_response = (
    gustoembeddedpayroll.signatories.create_signatory_with_complete_information(
        title="string_example",
        ssn="string_example",
        first_name="string_example",
        last_name="string_example",
        email="string_example",
        phone="string_example",
        birthday="string_example",
        home_address={
            "street_1": "street_1_example",
            "city": "city_example",
            "state": "state_example",
            "zip": "zip_example",
        },
        company_uuid="company_uuid_example",
        middle_initial="string_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email: `str`<a id="email-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### birthday: `str`<a id="birthday-str"></a>

##### home_address: [`SignatoriesCreateSignatoryWithCompleteInformationRequestHomeAddress`](./gusto_embedded_payroll_python_sdk/type/signatories_create_signatory_with_complete_information_request_home_address.py)<a id="home_address-signatoriescreatesignatorywithcompleteinformationrequesthomeaddressgusto_embedded_payroll_python_sdktypesignatories_create_signatory_with_complete_information_request_home_addresspy"></a>


##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### middle_initial: `str`<a id="middle_initial-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SignatoriesCreateSignatoryWithCompleteInformationRequest`](./gusto_embedded_payroll_python_sdk/type/signatories_create_signatory_with_complete_information_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Signatory`](./gusto_embedded_payroll_python_sdk/pydantic/signatory.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/signatories` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.signatories.delete_signatory`<a id="gustoembeddedpayrollsignatoriesdelete_signatory"></a>

Delete a company signatory.

scope: `signatories:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.signatories.delete_signatory(
    company_uuid="company_uuid_example",
    signatory_uuid="signatory_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### signatory_uuid: `str`<a id="signatory_uuid-str"></a>

The UUID of the signatory

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/signatories/{signatory_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.signatories.get_company_signatories`<a id="gustoembeddedpayrollsignatoriesget_company_signatories"></a>

Returns company signatories. Currently we only support a single signatory per company.

scope: `signatories:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_signatories_response = (
    gustoembeddedpayroll.signatories.get_company_signatories(
        company_uuid="company_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`SignatoriesGetCompanySignatoriesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/signatories_get_company_signatories_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/signatories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.signatories.update`<a id="gustoembeddedpayrollsignatoriesupdate"></a>

Update a signatory that has been either invited or created. If the signatory has been created with minimal information through the `POST /v1/companies/{company_uuid}/signatories/invite` endpoint, then the first update must contain all attributes specified in the request body in order to start the identity verification process.

scope: `signatories:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = gustoembeddedpayroll.signatories.update(
    company_uuid="company_uuid_example",
    signatory_uuid="signatory_uuid_example",
    title="string_example",
    version="string_example",
    first_name="string_example",
    middle_initial="string_example",
    last_name="string_example",
    phone="string_example",
    birthday="string_example",
    ssn="string_example",
    home_address={},
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### signatory_uuid: `str`<a id="signatory_uuid-str"></a>

The UUID of the signatory

##### title: `str`<a id="title-str"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the versioning guide for information on how to use this field.

##### first_name: `str`<a id="first_name-str"></a>

##### middle_initial: `str`<a id="middle_initial-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### birthday: `str`<a id="birthday-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### home_address: [`SignatoriesUpdateRequestHomeAddress`](./gusto_embedded_payroll_python_sdk/type/signatories_update_request_home_address.py)<a id="home_address-signatoriesupdaterequesthomeaddressgusto_embedded_payroll_python_sdktypesignatories_update_request_home_addresspy"></a>


##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SignatoriesUpdateRequest`](./gusto_embedded_payroll_python_sdk/type/signatories_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Signatory`](./gusto_embedded_payroll_python_sdk/pydantic/signatory.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/signatories/{signatory_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.tax_requirements.get_state_requirements`<a id="gustoembeddedpayrolltax_requirementsget_state_requirements"></a>

Get all tax requirements for a given state.

### Metadata Examples<a id="metadata-examples"></a>

```json select
{
  "type": "select",
  "options": [
    { "label": "Semiweekly",  value: "Semi-weekly" },
    { "label": "Monthly",  value: "Monthly" },
    { "label": "Quarterly",  value: "Quarterly" },
  ]
}
```
```json radio
{
  "type": "radio",
  "options": [
    { "label": "No, we cannot reimburse",  value: false, short_label: "Not Reimbursable" },
    { "label": "Yes, we can reimburse",  value: true, short_label: "Reimbursable" },
  ]
}
```
```json account_number
{
  "type": "account_number",
  "mask": "######-##',
  "prefix": null
}
```
```json tax_rate
{
  "type": "tax_rate",
  "validation": {
    "type": "min_max",
    "min": "0.0004",
    "max": "0.081"
  }
}
```

scope: `company_tax_requirements:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_state_requirements_response = (
    gustoembeddedpayroll.tax_requirements.get_state_requirements(
        company_uuid="company_uuid_example",
        state="state_example",
        scheduling=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### state: `str`<a id="state-str"></a>

2-letter US state abbreviation

##### scheduling: `bool`<a id="scheduling-bool"></a>

When true, return \"new\" requirement sets with valid `effective_from` dates that are available to save new effective dated values.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`TaxRequirementsState`](./gusto_embedded_payroll_python_sdk/pydantic/tax_requirements_state.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/tax_requirements/{state}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.tax_requirements.get_states`<a id="gustoembeddedpayrolltax_requirementsget_states"></a>

Returns objects describing the states that have tax requirements for the company

scope: `company_tax_requirements:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_states_response = gustoembeddedpayroll.tax_requirements.get_states(
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`TaxRequirementsGetStatesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/tax_requirements_get_states_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/tax_requirements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.tax_requirements.update_state_taxes`<a id="gustoembeddedpayrolltax_requirementsupdate_state_taxes"></a>

Update State Tax Requirements

scope: `company_tax_requirements:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.tax_requirements.update_state_taxes(
    company_uuid="company_uuid_example",
    state="state_example",
    requirement_sets=[
        {
            "key": "registrations",
            "state": "GA",
        }
    ],
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### state: `str`<a id="state-str"></a>

2-letter US state abbreviation

##### requirement_sets: [`TaxRequirementsUpdateStateTaxesRequestRequirementSets`](./gusto_embedded_payroll_python_sdk/type/tax_requirements_update_state_taxes_request_requirement_sets.py)<a id="requirement_sets-taxrequirementsupdatestatetaxesrequestrequirementsetsgusto_embedded_payroll_python_sdktypetax_requirements_update_state_taxes_request_requirement_setspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaxRequirementsUpdateStateTaxesRequest`](./gusto_embedded_payroll_python_sdk/type/tax_requirements_update_state_taxes_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/tax_requirements/{state}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.time_off_policies.add_employees_to_policy`<a id="gustoembeddedpayrolltime_off_policiesadd_employees_to_policy"></a>

Add employees to a time off policy. Employees are required to have at least one job to be added to a time off policy. Accepts starting balances for non-unlimited policies

scope: `time_off_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_employees_to_policy_response = (
    gustoembeddedpayroll.time_off_policies.add_employees_to_policy(
        time_off_policy_uuid="time_off_policy_uuid_example",
        employees=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_policy_uuid: `str`<a id="time_off_policy_uuid-str"></a>

The UUID of the company time off policy

##### employees: [`TimeOffPoliciesAddEmployeesToPolicyRequestEmployees`](./gusto_embedded_payroll_python_sdk/type/time_off_policies_add_employees_to_policy_request_employees.py)<a id="employees-timeoffpoliciesaddemployeestopolicyrequestemployeesgusto_embedded_payroll_python_sdktypetime_off_policies_add_employees_to_policy_request_employeespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffPoliciesAddEmployeesToPolicyRequest`](./gusto_embedded_payroll_python_sdk/type/time_off_policies_add_employees_to_policy_request.py)
A list of employee objects containing the employee uuid

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off_policies/{time_off_policy_uuid}/add_employees` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.time_off_policies.calculate_accruing_time_off_hours`<a id="gustoembeddedpayrolltime_off_policiescalculate_accruing_time_off_hours"></a>

Returns a list of accruing time off for each time off policy associated with the employee.

Factors affecting the accrued hours:
  * the time off policy accrual method (whether they get pay per hour worked, per hour paid, with / without overtime, accumulate time off based on pay period / calendar year / anniversary)
  * how many hours of work during this pay period
  * how many hours of PTO / sick hours taken during this pay period (for per hour paid policies only)
  * company pay schedule frequency (for per pay period)

If none of the parameters is passed in, the accrued time off hour will be 0.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calculate_accruing_time_off_hours_response = (
    gustoembeddedpayroll.time_off_policies.calculate_accruing_time_off_hours(
        payroll_id="payroll_id_example",
        employee_id="employee_id_example",
        regular_hours_worked=3.14,
        overtime_hours_worked=3.14,
        double_overtime_hours_worked=3.14,
        pto_hours_used=3.14,
        sick_hours_used=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### regular_hours_worked: `Union[int, float]`<a id="regular_hours_worked-unionint-float"></a>

regular hours worked in this pay period

##### overtime_hours_worked: `Union[int, float]`<a id="overtime_hours_worked-unionint-float"></a>

overtime hours worked in this pay period

##### double_overtime_hours_worked: `Union[int, float]`<a id="double_overtime_hours_worked-unionint-float"></a>

double overtime hours worked in this pay period

##### pto_hours_used: `Union[int, float]`<a id="pto_hours_used-unionint-float"></a>

paid time off hours used in this pay period

##### sick_hours_used: `Union[int, float]`<a id="sick_hours_used-unionint-float"></a>

sick hours used in this pay period

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffPoliciesCalculateAccruingTimeOffHoursRequest`](./gusto_embedded_payroll_python_sdk/type/time_off_policies_calculate_accruing_time_off_hours_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPoliciesCalculateAccruingTimeOffHoursResponse`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_policies_calculate_accruing_time_off_hours_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payrolls/{payroll_id}/employees/{employee_id}/calculate_accruing_time_off_hours` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.time_off_policies.create_policy`<a id="gustoembeddedpayrolltime_off_policiescreate_policy"></a>

Create a time off policy

scope: `time_off_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_policy_response = gustoembeddedpayroll.time_off_policies.create_policy(
    name="test policy3",
    policy_type="sick",
    accrual_method="unlimited",
    company_uuid="company_uuid_example",
    accrual_rate="string_example",
    accrual_rate_unit="string_example",
    paid_out_on_termination=True,
    accrual_waiting_period_days=1,
    carryover_limit_hours="string_example",
    max_accrual_hours_per_year="string_example",
    max_hours="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the time off policy

##### policy_type: `str`<a id="policy_type-str"></a>

Type of the time off policy. Currently only \\\"vacation\\\" and \\\"sick\\\" are supported

##### accrual_method: `str`<a id="accrual_method-str"></a>

Accrual method of the time off policy

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### accrual_rate: `float`<a id="accrual_rate-float"></a>

The rate at which the time off hours will accrue for an employee on the policy. Represented as a float, e.g. \\\"40.0\\\".

##### accrual_rate_unit: `float`<a id="accrual_rate_unit-float"></a>

The number of hours an employee has to work or be paid for to accrue the number of hours set in the accrual rate. Only used for hourly policies (per_hour_paid, per_hour_paid_no_overtime, per_hour_work, per_hour_worked_no_overtime). Represented as a float, e.g. \\\"40.0\\\".

##### paid_out_on_termination: `bool`<a id="paid_out_on_termination-bool"></a>

Boolean representing if an employees accrued time off hours will be paid out on termination

##### accrual_waiting_period_days: `int`<a id="accrual_waiting_period_days-int"></a>

Number of days before an employee on the policy will begin accruing time off hours

##### carryover_limit_hours: `float`<a id="carryover_limit_hours-float"></a>

The max number of hours and employee can carryover from one year to the next

##### max_accrual_hours_per_year: `float`<a id="max_accrual_hours_per_year-float"></a>

The max number of hours and employee can accrue in a year

##### max_hours: `float`<a id="max_hours-float"></a>

The max number of hours an employee can accrue

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffPoliciesCreatePolicyRequest`](./gusto_embedded_payroll_python_sdk/type/time_off_policies_create_policy_request.py)
Requires a policy name, a policy_type, and an accrual_method

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/time_off_policies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.time_off_policies.deactivate_policy`<a id="gustoembeddedpayrolltime_off_policiesdeactivate_policy"></a>

Deactivate a time off policy

scope: `time_off_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_policy_response = gustoembeddedpayroll.time_off_policies.deactivate_policy(
    time_off_policy_uuid="time_off_policy_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_policy_uuid: `str`<a id="time_off_policy_uuid-str"></a>

The UUID of the company time off policy

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off_policies/{time_off_policy_uuid}/deactivate` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.time_off_policies.get_all_policies`<a id="gustoembeddedpayrolltime_off_policiesget_all_policies"></a>

Get all time off policies for a company

scope: `time_off_policies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_policies_response = gustoembeddedpayroll.time_off_policies.get_all_policies(
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPoliciesGetAllPoliciesResponse`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_policies_get_all_policies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/time_off_policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.time_off_policies.get_policy`<a id="gustoembeddedpayrolltime_off_policiesget_policy"></a>

Get a time off policy

scope: `time_off_policies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_response = gustoembeddedpayroll.time_off_policies.get_policy(
    time_off_policy_uuid="time_off_policy_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_policy_uuid: `str`<a id="time_off_policy_uuid-str"></a>

The UUID of the company time off policy

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off_policies/{time_off_policy_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.time_off_policies.remove_employees`<a id="gustoembeddedpayrolltime_off_policiesremove_employees"></a>

Remove employees from a time off policy

scope: `time_off_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_employees_response = gustoembeddedpayroll.time_off_policies.remove_employees(
    time_off_policy_uuid="time_off_policy_uuid_example",
    employees=[{}],
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_policy_uuid: `str`<a id="time_off_policy_uuid-str"></a>

The UUID of the company time off policy

##### employees: [`TimeOffPoliciesRemoveEmployeesRequestEmployees`](./gusto_embedded_payroll_python_sdk/type/time_off_policies_remove_employees_request_employees.py)<a id="employees-timeoffpoliciesremoveemployeesrequestemployeesgusto_embedded_payroll_python_sdktypetime_off_policies_remove_employees_request_employeespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffPoliciesRemoveEmployeesRequest`](./gusto_embedded_payroll_python_sdk/type/time_off_policies_remove_employees_request.py)
A list of employee objects containing the employee uuid

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off_policies/{time_off_policy_uuid}/remove_employees` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.time_off_policies.update_employee_balance`<a id="gustoembeddedpayrolltime_off_policiesupdate_employee_balance"></a>

Updates time off hours balances for employees for a time off policy

scope: `time_off_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employee_balance_response = (
    gustoembeddedpayroll.time_off_policies.update_employee_balance(
        time_off_policy_uuid="time_off_policy_uuid_example",
        employees=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_policy_uuid: `str`<a id="time_off_policy_uuid-str"></a>

The UUID of the company time off policy

##### employees: [`TimeOffPoliciesUpdateEmployeeBalanceRequestEmployees`](./gusto_embedded_payroll_python_sdk/type/time_off_policies_update_employee_balance_request_employees.py)<a id="employees-timeoffpoliciesupdateemployeebalancerequestemployeesgusto_embedded_payroll_python_sdktypetime_off_policies_update_employee_balance_request_employeespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffPoliciesUpdateEmployeeBalanceRequest`](./gusto_embedded_payroll_python_sdk/type/time_off_policies_update_employee_balance_request.py)
A list of employee objects containing the employee uuid and time off hours balance

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off_policies/{time_off_policy_uuid}/balance` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.time_off_policies.update_policy`<a id="gustoembeddedpayrolltime_off_policiesupdate_policy"></a>

Update a time off policy

scope: `time_off_policies:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_policy_response = gustoembeddedpayroll.time_off_policies.update_policy(
    time_off_policy_uuid="time_off_policy_uuid_example",
    name="test policy3",
    accrual_method="per_calendar_year",
    accrual_rate="120.0",
    accrual_rate_unit="string_example",
    paid_out_on_termination=True,
    accrual_waiting_period_days=1,
    carryover_limit_hours="string_example",
    max_accrual_hours_per_year="string_example",
    max_hours="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_policy_uuid: `str`<a id="time_off_policy_uuid-str"></a>

The UUID of the company time off policy

##### name: `str`<a id="name-str"></a>

Name of the time off policy

##### accrual_method: `str`<a id="accrual_method-str"></a>

Accrual method of the time off policy

##### accrual_rate: `float`<a id="accrual_rate-float"></a>

The rate at which the time off hours will accrue for an employee on the policy. Represented as a float, e.g. \\\"40.0\\\".

##### accrual_rate_unit: `float`<a id="accrual_rate_unit-float"></a>

The number of hours an employee has to work or be paid for to accrue the number of hours set in the accrual rate. Only used for hourly policies (per_hour_paid, per_hour_paid_no_overtime, per_hour_work, per_hour_worked_no_overtime). Represented as a float, e.g. \\\"40.0\\\".

##### paid_out_on_termination: `bool`<a id="paid_out_on_termination-bool"></a>

Boolean representing if an employees accrued time off hours will be paid out on termination

##### accrual_waiting_period_days: `int`<a id="accrual_waiting_period_days-int"></a>

Number of days before an employee on the policy will begin accruing time off hours

##### carryover_limit_hours: `float`<a id="carryover_limit_hours-float"></a>

The max number of hours and employee can carryover from one year to the next

##### max_accrual_hours_per_year: `float`<a id="max_accrual_hours_per_year-float"></a>

The max number of hours and employee can accrue in a year

##### max_hours: `float`<a id="max_hours-float"></a>

The max number of hours an employee can accrue

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffPoliciesUpdatePolicyRequest`](./gusto_embedded_payroll_python_sdk/type/time_off_policies_update_policy_request.py)
Can update any attributes of the time off policy except policy_type, is_active, complete & employees

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPolicy`](./gusto_embedded_payroll_python_sdk/pydantic/time_off_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off_policies/{time_off_policy_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.webhooks.create_subscription`<a id="gustoembeddedpayrollwebhookscreate_subscription"></a>

Create a webhook subscription to receive events of the specified subscription_types whenever there is a state change.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_subscription_response = gustoembeddedpayroll.webhooks.create_subscription(
    url="string_example",
    subscription_types=["string_example"],
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

##### subscription_types: [`WebhooksCreateSubscriptionRequestSubscriptionTypes`](./gusto_embedded_payroll_python_sdk/type/webhooks_create_subscription_request_subscription_types.py)<a id="subscription_types-webhookscreatesubscriptionrequestsubscriptiontypesgusto_embedded_payroll_python_sdktypewebhooks_create_subscription_request_subscription_typespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksCreateSubscriptionRequest`](./gusto_embedded_payroll_python_sdk/type/webhooks_create_subscription_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./gusto_embedded_payroll_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.webhooks.delete_subscription_by_uuid`<a id="gustoembeddedpayrollwebhooksdelete_subscription_by_uuid"></a>

Deletes the Webhook Subscription associated with the provided UUID.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.webhooks.delete_subscription_by_uuid(
    webhook_subscription_uuid="webhook_subscription_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.webhooks.get_subscription`<a id="gustoembeddedpayrollwebhooksget_subscription"></a>

Returns the Webhook Subscription associated with the provided UUID.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_subscription_response = gustoembeddedpayroll.webhooks.get_subscription(
    webhook_subscription_uuid="webhook_subscription_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./gusto_embedded_payroll_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.webhooks.list_subscriptions`<a id="gustoembeddedpayrollwebhookslist_subscriptions"></a>

Returns all webhook subscriptions associated with the provided Partner API token.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_subscriptions_response = gustoembeddedpayroll.webhooks.list_subscriptions(
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksListSubscriptionsResponse`](./gusto_embedded_payroll_python_sdk/pydantic/webhooks_list_subscriptions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.webhooks.request_verification_token`<a id="gustoembeddedpayrollwebhooksrequest_verification_token"></a>

Request that the webhook subscription `verification_token` be POSTed to the Subscription URL.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoembeddedpayroll.webhooks.request_verification_token(
    webhook_subscription_uuid="webhook_subscription_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}/request_verification_token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.webhooks.update_subscription`<a id="gustoembeddedpayrollwebhooksupdate_subscription"></a>

Updates the Webhook Subscription associated with the provided UUID.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_subscription_response = gustoembeddedpayroll.webhooks.update_subscription(
    subscription_types=["string_example"],
    webhook_subscription_uuid="webhook_subscription_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_types: [`WebhooksUpdateSubscriptionRequestSubscriptionTypes`](./gusto_embedded_payroll_python_sdk/type/webhooks_update_subscription_request_subscription_types.py)<a id="subscription_types-webhooksupdatesubscriptionrequestsubscriptiontypesgusto_embedded_payroll_python_sdktypewebhooks_update_subscription_request_subscription_typespy"></a>

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksUpdateSubscriptionRequest`](./gusto_embedded_payroll_python_sdk/type/webhooks_update_subscription_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./gusto_embedded_payroll_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoembeddedpayroll.webhooks.verify_subscription_token`<a id="gustoembeddedpayrollwebhooksverify_subscription_token"></a>

When a webhook subscription is created, a `verification_token` is POSTed to the registered webhook subscription URL. This `verify` endpoint needs to be called with `verification_token` before webhook events can be sent to the registered webhook URL.

Use the /v1/webhook_subscriptions/{webhook_subscription_uuid}/request_verification_token API to resend the `verification_token` to the Subscriber.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_subscription_token_response = (
    gustoembeddedpayroll.webhooks.verify_subscription_token(
        verification_token="string_example",
        webhook_subscription_uuid="webhook_subscription_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### verification_token: `str`<a id="verification_token-str"></a>

The token POSTed to the Subscription URL.

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksVerifySubscriptionTokenRequest`](./gusto_embedded_payroll_python_sdk/type/webhooks_verify_subscription_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./gusto_embedded_payroll_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}/verify` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
