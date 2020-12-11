import pandas as pd
import os


def format_date(df):
    fmt = "%Y-%m-%d %H:%M:%S"
    for index in df.index:
        unformatted_created_date = df.loc[index, 'Created Date']
        df.loc[index, 'Created Date'] = pd.to_datetime(unformatted_created_date, format=fmt)

        unformatted_closed_date = df.loc[index, 'Closed Date']
        df.loc[index, 'Closed Date'] = pd.to_datetime(unformatted_closed_date, format=fmt)


def update_current_avg(lst, new_number):
    lst[1] = lst[1] + (new_number - lst[1]) / lst[0]
    lst[0] += 1


def remove_index_from_month_dict(month_dict):
    for key in month_dict.keys():
        month_dict[key] = month_dict[key][1]


def get_monthly_averages(df, zipcode=None):
    month_dict = {k: [1, 0] for k in range(1, 13)}  # Running average is the second number
    for index in df.index:
        if zipcode is not None:
            if df.loc[index, 'Incident Zip'] != zipcode:
                continue
        incident_month = df.loc[index, 'Created Date'].month
        diff = (df.loc[index, 'Closed Date'] - df.loc[index, 'Created Date']).total_seconds() / 3600  # (Hours)
        update_current_avg(month_dict[incident_month], diff)

    remove_index_from_month_dict(month_dict)
    return month_dict


def main():
    data = pd.read_csv(os.path.join("data", "clean.csv.tgz"), compression='gzip',
                       header=None, names=["Created Date", "Closed Date", "Incident Zip"],
                       dtype={"Incident Zip": "str"})
    format_date(data)

    distinct_zipcodes = data['Incident Zip'].unique()

    avg = {'All': get_monthly_averages(df=data)}
    for zipcode in distinct_zipcodes:
        avg[zipcode] = get_monthly_averages(df=data, zipcode=zipcode)

    avg_df = pd.DataFrame(avg)
    avg_df.to_csv(os.path.join('data', 'averages.csv'))


if __name__ == "__main__":
    main()
