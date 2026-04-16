import pandas as pd

def emailsFromCsv(fileName):
    df = pd.read_csv(fileName, sep=",")
    return ",".join(df["Email"])

print(emailsFromCsv("A10.csv"))
