import os, json, requests
import pprint

pypath = os.path.dirname(os.path.realpath(__file__))
fields = [
    "file_name",
    "cases.submitter_id",
    ]
fields = ",".join(fields)

# cases_endpt = "https://api.gdc.cancer.gov/files"
cases_endpt = "https://api.gdc.cancer.gov/files"

with open(pypath + "/../json/filter-Ctrl-RNAseq.json", 'r') as f:
        filters = json.load(f)

params = {
    "filters": json.dumps(filters),
    "fields": fields,
    "format": "JSON",
    "size": "10000" #HACK: modificar si los casos superan los hints
    }

response = requests.get(cases_endpt, params = params)
jdata = json.loads(response.content.decode("utf-8"))
nhits = len(jdata["data"]["hits"])
print "Controles con RNAseq: ", nhits
f = open("cases.txt", "w")
for i in jdata["data"]["hits"]:
	f.write(i["cases"][0]["submitter_id"] + '-\n')	