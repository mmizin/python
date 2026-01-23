# Get fixture name
test_case_name: str = request.node.originalname

# Write/save data into request
request.cls.cleanup = True

api_version = request.node.callspec.params["api_version"]

request.param

payout_payloads = request.getfixturevalue("_setup")

