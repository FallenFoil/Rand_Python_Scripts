import pandas as pd

csv = pd.read_csv("contas.csv", ",")

csv = csv.drop(['httpRealm', 'formActionOrigin', 'guid', 'timeCreated', 'timeLastUsed', 'timePasswordChanged'], axis=1)

csv.to_csv("new_contas.csv", index=False)