# First prepare parameters you want to pass to the function and then unpack parameters using **

date_filter = (
    {"start_date": some_date} if policy == "policyStart" else {"end_date": some_date}
)

partner_policies = get_partner_policy_details_new(
    partner_id=partner_id, **date_filter
)
