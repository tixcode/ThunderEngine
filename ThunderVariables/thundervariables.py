import random, sys, os, time, json, requests

class ThunderVariables:
	jsdata = {
		"application": {
			"data": {
				"variables": {}
			}
		}
	}

	def SaveThunderVariablesData(sender=os.environ.get("USERNAME")):
		with open('ThunderVariablesData.json', 'w') as outfile:
			json.dump(ThunderVariables.jsdata, outfile)

	def ReadThunderVariablesData(sender=os.environ.get("USERNAME")):
		try:
			with open("ThunderVariablesData.json", 'r') as outfile:
				ThunderVariables.jsdata = json.load(outfile)
		except:
			return None
	
	def ReadJsonFile(fileName: str, sender=os.environ.get("USERNAME")):
		with open(fileName, 'r') as outfile:
			return json.load(outfile)

	def WriteJsonFile(fileName: str, pythonDictionary: dict, sender=os.environ.get("USERNAME")):
		with open(fileName, 'w') as outfile:
			json.dump(pythonDictionary, outfile)

	def isVariable(variableName: str, sender=os.environ.get("USERNAME")):
		if variableName in ThunderVariables.jsdata['application']['data']['variables']:
			return True
		else:
			return False

	def GetVariable(variableName: str, sender=os.environ.get("USERNAME")):
		if (ThunderVariables.isVariable(variableName)):
			return ThunderVariables.jsdata['application']['data']['variables'][variableName]['value']
		else:
			try:
				print('[ERR]: Variable {} dont exists!'.format(variableName))
			except:
				return ''

	def SetVariable(variableName, variableValue, variableType=int, sender=os.environ.get("USERNAME")):
		if (type(variableName) == str):
			if (type(variableValue) == variableType):
				ThunderVariables.jsdata['application']['data']['variables'][variableName] = {'type': f'{variableType}', 'value': variableValue}
			else:
				print("[ERR]: Variable value != {}".format(variableType))
		else:
			print("[ERR]: Variable name != string")