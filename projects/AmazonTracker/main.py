# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import scraper
import pandas as pd
import os
import db_handler as duck


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('OS Curdir:', os.curdir)
    print("Before:", os.getcwd())
    os.chdir(os.getcwd() + '/projects/AmazonTracker/data')
    print("After 1:", os.getcwd())

    tracker_id = pd.read_csv('./tracker_id.csv')

    prod_info_db = []
    for tracker in tracker_id.head(3).itertuples():
        prod_info = scraper.readAsin(tracker.url, tracker.asin_id)
        print('Prod info', prod_info)
        prod_info_db.append(prod_info)

    prod_info_df = pd.DataFrame.from_dict(prod_info_db)

    conn = duck.connect('prod_tracker.db')
    duck.create_insert_db(conn, 'prod_tracker', list(prod_info_db[0].keys()), data = prod_info_df)



    print('Scraper end!!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
