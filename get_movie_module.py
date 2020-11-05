import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd



def get_movie_data(urls_list):
    """Get the movie data from its url.

    Arg:
    url: URL link containing movie data. This should be from Rotten Tomatoes
    and in a list.

    Returns:
    df: A dataframe containing movie data."""

    for i, url in enumerate(urls_list):
        if i == 0:
            # save html file in respone variable
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'lxml')

            # extract scores data as dictionary
            scores_text = (soup.find_all('script', type=
                                        'text/javascript')[2].text)
            scores_text_lines_list = scores_text.split('\n')
            for line in scores_text_lines_list:
                if 'root.RottenTomatoes.context.scoreInfo' in line:
                    scores_data_dict = line
                    break
            scores_data_dict = (scores_data_dict.replace('root.RottenTomatoes'
                                '.context.scoreInfo = ', '').replace('true',
                                'True').replace('false', 'False').replace('null',
                                'np.nan')[:-1])

            # convert dictionary into the first dataframe
            df = (pd.DataFrame.from_dict(eval(scores_data_dict),
                 orient='index').reset_index())

            # extract other movie info and add to the dataframe
            movie_title = soup.title.text[:-len(' - Rotten Tomatoes')]
            df['movie_title'] = pd.Series([movie_title] * len(df['index']))
            release_date_theaters = (soup.find_all('li', class_='meta-row '
                                    'clearfix')[6].contents[3].contents[1].text)
            df['release_date_theaters'] = (pd.Series([release_date_theaters]
                                          * len(df['index'])))
            box_office_gross_usa = soup.find_all('li', class_='meta-row '
                                   'clearfix')[8].contents[3].text
            df['box_office_gross_usa'] = (pd.Series([box_office_gross_usa]
                                         * len(df['index'])))
            runtime = (soup.find_all('li', class_='meta-row clearfix')[9]
                      .contents[3].text.split('\n')[2].replace(' ', ''))
            df['runtime'] = pd.Series([runtime] * len(df['index']))

        else:
            # save html file in respone variable
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'lxml')

            # extract scores data as dictionary
            scores_text = (soup.find_all('script', type=
                                        'text/javascript')[2].text)
            scores_text_lines_list = scores_text.split('\n')
            for line in scores_text_lines_list:
                if 'root.RottenTomatoes.context.scoreInfo' in line:
                    scores_data_dict = line
                    break
            scores_data_dict = (scores_data_dict.replace('root.RottenTomatoes'
                                '.context.scoreInfo = ', '').replace('true',
                                'True').replace('false', 'False').replace('null',
                                'np.nan')[:-1])

            # convert dictionary into the first dataframe
            df1 = (pd.DataFrame.from_dict(eval(scores_data_dict),
                 orient='index').reset_index())

            # extract other movie info and add to the dataframe
            movie_title = soup.title.text[:-len(' - Rotten Tomatoes')]
            df1['movie_title'] = pd.Series([movie_title] * len(df1['index']))
            release_date_theaters = (soup.find_all('li', class_='meta-row '
                                    'clearfix')[6].contents[3].contents[1].text)
            df1['release_date_theaters'] = (pd.Series([release_date_theaters]
                                          * len(df1['index'])))
            box_office_gross_usa = soup.find_all('li', class_='meta-row '
                                   'clearfix')[8].contents[3].text
            df1['box_office_gross_usa'] = (pd.Series([box_office_gross_usa]
                                         * len(df1['index'])))
            runtime = (soup.find_all('li', class_='meta-row clearfix')[9]
                      .contents[3].text.split('\n')[2].replace(' ', ''))
            df1['runtime'] = pd.Series([runtime] * len(df1['index']))

            # combine two dataframes
            df = pd.concat([df, df1], ignore_index = 'True')

    return df
