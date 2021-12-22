import json

def create_request(header_dict, body_dict):
	"""
	Creates request from passed header and body
	:param header_dict: string of request type
	:param body_dict: dictionary of body
	:return:
	"""
	request_dict = {"header": header_dict, "body": body_dict}
	request_msg = json.dumps(request_dict, indent=2)

	return request_msg
