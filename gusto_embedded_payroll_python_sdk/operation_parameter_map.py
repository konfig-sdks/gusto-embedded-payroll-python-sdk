operation_parameter_map = {
    '/v1/companies/{company_uuid}/ach_transactions-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'contractor_payment_uuid'
            },
            {
                'name': 'payroll_uuid'
            },
            {
                'name': 'transaction_type'
            },
            {
                'name': 'payment_direction'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/plaid/processor_token-POST': {
        'parameters': [
            {
                'name': 'owner_type'
            },
            {
                'name': 'owner_id'
            },
            {
                'name': 'processor_token'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/bank_accounts-POST': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'routing_number'
            },
            {
                'name': 'account_number'
            },
            {
                'name': 'account_type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/bank_accounts-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/bank_accounts/{bank_account_uuid}/verify-PUT': {
        'parameters': [
            {
                'name': 'bank_account_uuid'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'deposit_1'
            },
            {
                'name': 'deposit_2'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/partner_managed_companies/{company_uuid}/accept_terms_of_service-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'ip_address'
            },
            {
                'name': 'external_user_id'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/admins-POST': {
        'parameters': [
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/partner_managed_companies-POST': {
        'parameters': [
            {
                'name': 'user'
            },
            {
                'name': 'company'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/finish_onboarding-PUT': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/admins-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/custom_fields-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/onboarding_status-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/partner_managed_companies/{company_uuid}/retrieve_terms_of_service-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/partner_managed_companies/{company_uuid}/migrate-PUT': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'ip_address'
            },
            {
                'name': 'external_user_id'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/company_benefits-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'benefit_type'
            },
            {
                'name': 'active'
            },
            {
                'name': 'responsible_for_employer_taxes'
            },
            {
                'name': 'responsible_for_employee_w2'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/company_benefits/{company_benefit_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/company_benefits/{company_benefit_id}-GET': {
        'parameters': [
            {
                'name': 'company_benefit_id'
            },
            {
                'name': 'with_employee_benefits'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/benefits/{benefit_id}/requirements-GET': {
        'parameters': [
            {
                'name': 'benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/company_benefits/{company_benefit_id}/summary-GET': {
        'parameters': [
            {
                'name': 'company_benefit_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'detailed'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/company_benefits-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'enrollment_count'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/benefits/{benefit_id}-GET': {
        'parameters': [
            {
                'name': 'benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/benefits-GET': {
        'parameters': [
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/company_benefits/{company_benefit_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'company_benefit_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/forms-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/forms/{form_id}-GET': {
        'parameters': [
            {
                'name': 'form_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/forms/{form_id}/pdf-GET': {
        'parameters': [
            {
                'name': 'form_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/forms/{form_id}/sign-PUT': {
        'parameters': [
            {
                'name': 'signature_text'
            },
            {
                'name': 'agree'
            },
            {
                'name': 'signed_by_ip_address'
            },
            {
                'name': 'form_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/sandbox/generate_1099-POST': {
        'parameters': [
            {
                'name': 'contractor_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/forms/{form_id}-GET': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'form_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/forms/{form_id}/pdf-GET': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'form_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/forms-GET': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/bank_accounts-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'routing_number'
            },
            {
                'name': 'account_number'
            },
            {
                'name': 'account_type'
            },
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/payment_method-GET': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/bank_accounts-GET': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/payment_method-PUT': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'version'
            },
            {
                'name': 'type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractor_payments/{contractor_payment_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'contractor_payment_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractor_payments-POST': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'date'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'payment_method'
            },
            {
                'name': 'wage'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'bonus'
            },
            {
                'name': 'reimbursement'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractor_payments/{contractor_payment_uuid}/fund-PUT': {
        'parameters': [
            {
                'name': 'contractor_payment_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractor_payments/{contractor_payment_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'contractor_payment_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractor_payments/{contractor_payment_uuid}/receipt-GET': {
        'parameters': [
            {
                'name': 'contractor_payment_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractor_payments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'group_by_date'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/contractor_payments/preview-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'contractor_payments'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/onboarding_status-PUT': {
        'parameters': [
            {
                'name': 'onboarding_status'
            },
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractors-POST': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'wage_type'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'hourly_rate'
            },
            {
                'name': 'self_onboarding'
            },
            {
                'name': 'email'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'file_new_hire_report'
            },
            {
                'name': 'work_state'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'business_name'
            },
            {
                'name': 'ein'
            },
            {
                'name': 'is_active'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_id}-DELETE': {
        'parameters': [
            {
                'name': 'contractor_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/address-GET': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_id}-GET': {
        'parameters': [
            {
                'name': 'contractor_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractors-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/onboarding_status-GET': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_uuid}/address-PUT': {
        'parameters': [
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'version'
            },
            {
                'name': 'street_1'
            },
            {
                'name': 'street_2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_id}-PUT': {
        'parameters': [
            {
                'name': 'contractor_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'type'
            },
            {
                'name': 'wage_type'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'hourly_rate'
            },
            {
                'name': 'self_onboarding'
            },
            {
                'name': 'email'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'file_new_hire_report'
            },
            {
                'name': 'work_state'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'business_name'
            },
            {
                'name': 'ein'
            },
            {
                'name': 'is_active'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}/add-PUT': {
        'parameters': [
            {
                'name': 'department_uuid'
            },
            {
                'name': 'version'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'contractors'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/departments-POST': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'title'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'department_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/departments-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}-GET': {
        'parameters': [
            {
                'name': 'department_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}/remove-PUT': {
        'parameters': [
            {
                'name': 'department_uuid'
            },
            {
                'name': 'version'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'contractors'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'department_uuid'
            },
            {
                'name': 'title'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/earning_types-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/earning_types/{earning_type_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'earning_type_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/earning_types-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/earning_types/{earning_type_uuid}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'earning_type_uuid'
            },
            {
                'name': 'name'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/home_addresses-POST': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'street_1'
            },
            {
                'name': 'street_2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'courtesy_withholding'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/work_addresses-POST': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'location_uuid'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/home_addresses/{home_address_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'home_address_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/work_addresses/{work_address_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'work_address_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/home_addresses/{home_address_uuid}-GET': {
        'parameters': [
            {
                'name': 'home_address_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/home_addresses-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/work_addresses/{work_address_uuid}-GET': {
        'parameters': [
            {
                'name': 'work_address_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/work_addresses-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/home_addresses/{home_address_uuid}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'home_address_uuid'
            },
            {
                'name': 'street_1'
            },
            {
                'name': 'street_2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'courtesy_withholding'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/work_addresses/{work_address_uuid}-PUT': {
        'parameters': [
            {
                'name': 'work_address_uuid'
            },
            {
                'name': 'version'
            },
            {
                'name': 'location_uuid'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/employee_benefits-POST': {
        'parameters': [
            {
                'name': 'company_benefit_uuid'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'employee_deduction'
            },
            {
                'name': 'deduct_as_percentage'
            },
            {
                'name': 'employee_deduction_annual_maximum'
            },
            {
                'name': 'contribution'
            },
            {
                'name': 'elective'
            },
            {
                'name': 'company_contribution_annual_maximum'
            },
            {
                'name': 'limit_option'
            },
            {
                'name': 'catch_up'
            },
            {
                'name': 'coverage_amount'
            },
            {
                'name': 'coverage_salary_multiplier'
            },
            {
                'name': 'deduction_reduces_taxable_income'
            },
            {
                'name': 'company_contribution'
            },
            {
                'name': 'contribute_as_percentage'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/ytd_benefit_amounts_from_different_company-POST': {
        'parameters': [
            {
                'name': 'tax_year'
            },
            {
                'name': 'ytd_employee_deduction_amount'
            },
            {
                'name': 'ytd_company_contribution_amount'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'benefit_type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employee_benefits/{employee_benefit_id}-DELETE': {
        'parameters': [
            {
                'name': 'employee_benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/employee_benefits-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employee_benefits/{employee_benefit_id}-GET': {
        'parameters': [
            {
                'name': 'employee_benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employee_benefits/{employee_benefit_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'employee_benefit_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'employee_deduction'
            },
            {
                'name': 'deduct_as_percentage'
            },
            {
                'name': 'employee_deduction_annual_maximum'
            },
            {
                'name': 'contribution'
            },
            {
                'name': 'elective'
            },
            {
                'name': 'company_contribution_annual_maximum'
            },
            {
                'name': 'limit_option'
            },
            {
                'name': 'catch_up'
            },
            {
                'name': 'coverage_amount'
            },
            {
                'name': 'deduction_reduces_taxable_income'
            },
            {
                'name': 'coverage_salary_multiplier'
            },
            {
                'name': 'company_contribution'
            },
            {
                'name': 'contribute_as_percentage'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/rehire-POST': {
        'parameters': [
            {
                'name': 'effective_date'
            },
            {
                'name': 'file_new_hire_report'
            },
            {
                'name': 'work_location_uuid'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'employment_status'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/terminations-POST': {
        'parameters': [
            {
                'name': 'effective_date'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'run_termination_payroll'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/terminations-DELETE': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/employment_history-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/rehire-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/terminations-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/rehire-DELETE': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/rehire-PUT': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'file_new_hire_report'
            },
            {
                'name': 'work_location_uuid'
            },
            {
                'name': 'employment_status'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/terminations/{employee_id}-PUT': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'run_termination_payroll'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/sandbox/generate_w2-POST': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/forms-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/forms/{form_id}-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'form_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/forms/{form_id}/pdf-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'form_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/forms/{form_id}/sign-PUT': {
        'parameters': [
            {
                'name': 'signature_text'
            },
            {
                'name': 'agree'
            },
            {
                'name': 'signed_by_ip_address'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'form_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/bank_accounts-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'routing_number'
            },
            {
                'name': 'account_number'
            },
            {
                'name': 'account_type'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/bank_accounts/{bank_account_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'bank_account_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/payment_method-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/bank_accounts-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/payment_method-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'type'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'split_by'
            },
            {
                'name': 'splits'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_uuid}/federal_taxes-GET': {
        'parameters': [
            {
                'name': 'employee_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_uuid}/state_taxes-GET': {
        'parameters': [
            {
                'name': 'employee_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_uuid}/federal_taxes-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'employee_uuid'
            },
            {
                'name': 'filing_status'
            },
            {
                'name': 'extra_withholding'
            },
            {
                'name': 'two_jobs'
            },
            {
                'name': 'dependents_amount'
            },
            {
                'name': 'other_income'
            },
            {
                'name': 'deductions'
            },
            {
                'name': 'w4_data_type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_uuid}/state_taxes-PUT': {
        'parameters': [
            {
                'name': 'states'
            },
            {
                'name': 'employee_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/finish_onboarding-PUT': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/employees-POST': {
        'parameters': [
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'date_of_birth'
            },
            {
                'name': 'email'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'self_onboarding'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}-DELETE': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/custom_fields-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/onboarding_status-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_uuid}/time_off_activities-GET': {
        'parameters': [
            {
                'name': 'employee_uuid'
            },
            {
                'name': 'time_off_type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/employees-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'terminated'
            },
            {
                'name': 'include'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'date_of_birth'
            },
            {
                'name': 'email'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/onboarding_status-PUT': {
        'parameters': [
            {
                'name': 'onboarding_status'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/events-GET': {
        'parameters': [
            {
                'name': 'starting_after_uuid'
            },
            {
                'name': 'resource_uuid'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'event_type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/external_payrolls-POST': {
        'parameters': [
            {
                'name': 'check_date'
            },
            {
                'name': 'payment_period_start_date'
            },
            {
                'name': 'payment_period_end_date'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'external_payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/external_payrolls/tax_liabilities/finish-PUT': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'external_payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/external_payrolls/tax_liabilities-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}/calculate_taxes-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'external_payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/external_payrolls-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/external_payrolls/{external_payroll_id}-PUT': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'external_payroll_id'
            },
            {
                'name': 'replace_fields'
            },
            {
                'name': 'external_payroll_items'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/external_payrolls/tax_liabilities-PUT': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'liability_selections'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/federal_tax_details-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/federal_tax_details-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'legal_name'
            },
            {
                'name': 'ein'
            },
            {
                'name': 'tax_payer_type'
            },
            {
                'name': 'filing_form'
            },
            {
                'name': 'taxable_as_scorp'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/flows-POST': {
        'parameters': [
            {
                'name': 'flow_type'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'entity_uuid'
            },
            {
                'name': 'entity_type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/garnishments-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'court_ordered'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'times'
            },
            {
                'name': 'recurring'
            },
            {
                'name': 'annual_maximum'
            },
            {
                'name': 'pay_period_maximum'
            },
            {
                'name': 'deduct_as_percentage'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/garnishments-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/garnishments/{garnishment_id}-GET': {
        'parameters': [
            {
                'name': 'garnishment_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/garnishments/{garnishment_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'garnishment_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'court_ordered'
            },
            {
                'name': 'times'
            },
            {
                'name': 'recurring'
            },
            {
                'name': 'annual_maximum'
            },
            {
                'name': 'pay_period_maximum'
            },
            {
                'name': 'deduct_as_percentage'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/generated_documents/{document_type}/{request_uuid}-GET': {
        'parameters': [
            {
                'name': 'document_type'
            },
            {
                'name': 'request_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/holiday_pay_policy/add-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/holiday_pay_policy-POST': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'federal_holidays'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/holiday_pay_policy-DELETE': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/holiday_pay_policy-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/paid_holidays-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'year'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/holiday_pay_policy/remove-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/holiday_pay_policy-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'federal_holidays'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/industry_selection-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/industry_selection-PUT': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'naics_code'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'sic_codes'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/oauth/token-POST': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'refresh_token'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/token_info-GET': {
        'parameters': [
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/invoices/{invoice_period}-GET': {
        'parameters': [
            {
                'name': 'invoice_period'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'company_uuids'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}/compensations-POST': {
        'parameters': [
            {
                'name': 'payment_unit'
            },
            {
                'name': 'flsa_status'
            },
            {
                'name': 'job_id'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'adjust_for_minimum_wage'
            },
            {
                'name': 'minimum_wages'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/jobs-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'hire_date'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'state_wc_covered'
            },
            {
                'name': 'state_wc_class_code'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}-DELETE': {
        'parameters': [
            {
                'name': 'job_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/compensations/{compensation_id}-GET': {
        'parameters': [
            {
                'name': 'compensation_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/jobs-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}/compensations-GET': {
        'parameters': [
            {
                'name': 'job_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}-GET': {
        'parameters': [
            {
                'name': 'job_id'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/compensations/{compensation_id}-DELETE': {
        'parameters': [
            {
                'name': 'compensation_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/compensations/{compensation_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'compensation_id'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'payment_unit'
            },
            {
                'name': 'flsa_status'
            },
            {
                'name': 'adjust_for_minimum_wage'
            },
            {
                'name': 'minimum_wages'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'job_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'hire_date'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'state_wc_covered'
            },
            {
                'name': 'state_wc_class_code'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/locations-POST': {
        'parameters': [
            {
                'name': 'phone_number'
            },
            {
                'name': 'street_1'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'street_2'
            },
            {
                'name': 'country'
            },
            {
                'name': 'mailing_address'
            },
            {
                'name': 'filing_address'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/locations/{location_id}-GET': {
        'parameters': [
            {
                'name': 'location_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/locations-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/locations/{location_uuid}/minimum_wages-GET': {
        'parameters': [
            {
                'name': 'location_uuid'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/locations/{location_id}-PUT': {
        'parameters': [
            {
                'name': 'location_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'street_1'
            },
            {
                'name': 'street_2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'country'
            },
            {
                'name': 'mailing_address'
            },
            {
                'name': 'filing_address'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/notifications/{notification_uuid}-GET': {
        'parameters': [
            {
                'name': 'notification_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules/assign-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'hourly_pay_schedule_uuid'
            },
            {
                'name': 'salaried_pay_schedule_uuid'
            },
            {
                'name': 'default_pay_schedule_uuid'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'departments'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules-POST': {
        'parameters': [
            {
                'name': 'frequency'
            },
            {
                'name': 'anchor_pay_date'
            },
            {
                'name': 'anchor_end_of_pay_period'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'day_1'
            },
            {
                'name': 'day_2'
            },
            {
                'name': 'custom_name'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules/assignments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules/{pay_schedule_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'pay_schedule_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_periods-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'payroll_types'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_periods/unprocessed_termination_pay_periods-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules/assignment_preview-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'hourly_pay_schedule_uuid'
            },
            {
                'name': 'salaried_pay_schedule_uuid'
            },
            {
                'name': 'default_pay_schedule_uuid'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'departments'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules/preview-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'anchor_pay_date'
            },
            {
                'name': 'anchor_end_of_pay_period'
            },
            {
                'name': 'day_1'
            },
            {
                'name': 'day_2'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules/{pay_schedule_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'pay_schedule_id'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'anchor_pay_date'
            },
            {
                'name': 'anchor_end_of_pay_period'
            },
            {
                'name': 'day_1'
            },
            {
                'name': 'day_2'
            },
            {
                'name': 'custom_name'
            },
            {
                'name': 'auto_pilot'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/payment_configs-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/payment_configs-PUT': {
        'parameters': [
            {
                'name': 'fast_payment_limit'
            },
            {
                'name': 'payment_speed'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payroll_reversals-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/payrolls/{payroll_uuid}/gross_up-POST': {
        'parameters': [
            {
                'name': 'employee_uuid'
            },
            {
                'name': 'net_pay'
            },
            {
                'name': 'payroll_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}/calculate-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}/cancel-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls-POST': {
        'parameters': [
            {
                'name': 'off_cycle'
            },
            {
                'name': 'off_cycle_reason'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'pay_schedule_uuid'
            },
            {
                'name': 'employee_uuids'
            },
            {
                'name': 'check_date'
            },
            {
                'name': 'withholding_pay_period'
            },
            {
                'name': 'skip_regular_deductions'
            },
            {
                'name': 'fixed_withholding_rate'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'async'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/payrolls/{payroll_id}/generated_documents/printable_payroll_checks-POST': {
        'parameters': [
            {
                'name': 'printing_format'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'starting_check_number'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/payrolls/blockers-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'processing_statuses'
            },
            {
                'name': 'payroll_types'
            },
            {
                'name': 'include'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/payrolls/{payroll_id}/employees/{employee_id}/pay_stub-GET': {
        'parameters': [
            {
                'name': 'payroll_id'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/pay_stubs-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/payrolls/{payroll_uuid}/receipt-GET': {
        'parameters': [
            {
                'name': 'payroll_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}/prepare-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/payrolls/skip-POST': {
        'parameters': [
            {
                'name': 'payroll_type'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'pay_schedule_uuid'
            },
            {
                'name': 'employee_uuids'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}/submit-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}-PUT': {
        'parameters': [
            {
                'name': 'employee_compensations'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/recovery_cases/{recovery_case_uuid}/redebit-PUT': {
        'parameters': [
            {
                'name': 'recovery_case_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/recovery_cases-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/signatories/invite-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'title'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/signatories-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'birthday'
            },
            {
                'name': 'home_address'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/signatories/{signatory_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'signatory_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/signatories-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/signatories/{signatory_uuid}-PUT': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'signatory_uuid'
            },
            {
                'name': 'title'
            },
            {
                'name': 'version'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'birthday'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'home_address'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/tax_requirements/{state}-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'state'
            },
            {
                'name': 'scheduling'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/tax_requirements-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/tax_requirements/{state}-PUT': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'state'
            },
            {
                'name': 'requirement_sets'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/time_off_policies/{time_off_policy_uuid}/add_employees-PUT': {
        'parameters': [
            {
                'name': 'time_off_policy_uuid'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/payrolls/{payroll_id}/employees/{employee_id}/calculate_accruing_time_off_hours-POST': {
        'parameters': [
            {
                'name': 'payroll_id'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'regular_hours_worked'
            },
            {
                'name': 'overtime_hours_worked'
            },
            {
                'name': 'double_overtime_hours_worked'
            },
            {
                'name': 'pto_hours_used'
            },
            {
                'name': 'sick_hours_used'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/time_off_policies-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'policy_type'
            },
            {
                'name': 'accrual_method'
            },
            {
                'name': 'company_uuid'
            },
            {
                'name': 'accrual_rate'
            },
            {
                'name': 'accrual_rate_unit'
            },
            {
                'name': 'paid_out_on_termination'
            },
            {
                'name': 'accrual_waiting_period_days'
            },
            {
                'name': 'carryover_limit_hours'
            },
            {
                'name': 'max_accrual_hours_per_year'
            },
            {
                'name': 'max_hours'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/time_off_policies/{time_off_policy_uuid}/deactivate-PUT': {
        'parameters': [
            {
                'name': 'time_off_policy_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/time_off_policies-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/time_off_policies/{time_off_policy_uuid}-GET': {
        'parameters': [
            {
                'name': 'time_off_policy_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/time_off_policies/{time_off_policy_uuid}/remove_employees-PUT': {
        'parameters': [
            {
                'name': 'time_off_policy_uuid'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/time_off_policies/{time_off_policy_uuid}/balance-PUT': {
        'parameters': [
            {
                'name': 'time_off_policy_uuid'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/time_off_policies/{time_off_policy_uuid}-PUT': {
        'parameters': [
            {
                'name': 'time_off_policy_uuid'
            },
            {
                'name': 'name'
            },
            {
                'name': 'accrual_method'
            },
            {
                'name': 'accrual_rate'
            },
            {
                'name': 'accrual_rate_unit'
            },
            {
                'name': 'paid_out_on_termination'
            },
            {
                'name': 'accrual_waiting_period_days'
            },
            {
                'name': 'carryover_limit_hours'
            },
            {
                'name': 'max_accrual_hours_per_year'
            },
            {
                'name': 'max_hours'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'subscription_types'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}-GET': {
        'parameters': [
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions-GET': {
        'parameters': [
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}/request_verification_token-GET': {
        'parameters': [
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}-PUT': {
        'parameters': [
            {
                'name': 'subscription_types'
            },
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}/verify-PUT': {
        'parameters': [
            {
                'name': 'verification_token'
            },
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
};