import json

with open("praktiskais\scores_of_models\jsons\RoBERTa.json", "r") as f:
    roberta = json.load(f)

racc = roberta["Accuracy"]
rpre = roberta["Precision"]
rrec = roberta["Recall"]
rf1 = roberta["F1 Score"]

with open("praktiskais\scores_of_models\jsons\VADER.json", "r") as f:
    vader = json.load(f)

vacc = vader["Accuracy"]
vpre = vader["Precision"]
vrec = vader["Recall"]
vf1 = vader["F1 Score"]

print(racc)
print(rpre)
print(rrec)
print(f"{rf1}\n")

print(vacc)
print(vpre)
print(vrec)
print(f"{vf1}\n")