import pandas as pd


def main():
    data = pd.read_csv('stocks.csv')

    for index, row in data.iterrows():

        PE_Ratio = row['Price'] / row['Earnings Per Share']
        PB_Ratio = row['Price'] / row[' Book Value']

        data.at[index, 'PE Ratio'] = round(PE_Ratio, 2)
        data.at[index, 'PB Ratio'] = round(PB_Ratio, 2)

    interested_columns = ['Company Name', 'PE Ratio', 'PB Ratio']

    data[interested_columns].to_csv('Output.csv', index=False)



if __name__ == '__main__':
    main()


