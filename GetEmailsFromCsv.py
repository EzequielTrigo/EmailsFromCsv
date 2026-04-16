import pandas as pd

def emailsFromCsv(fileName):
    df = pd.read_csv(fileName, sep=",")
    print("quantity: "+ str(len(df["Email"])))
    return ",".join(df["Email"])

if __name__ == "__main__":
    directory = input("Enter the directory of the csv file: ")
    print(emailsFromCsv(directory))