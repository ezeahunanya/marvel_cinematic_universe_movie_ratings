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

            # extract movie title and add to dataframe
            movie_title = soup.title.text[:-len(' - Rotten Tomatoes')]
            df['movie_title'] = pd.Series([movie_title] * len(df.index))

            max_limit = len(soup.find_all('li', class_='meta-row clearfix'))

            # extract release date and add to dataframe
            for i in[i for i in range(0, max_limit)]:
                li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
                li_descendants = list(li_tag_line.descendants)
                if 'Release Date (Theaters):' in li_descendants:
                    release_date_theaters = li_descendants[7]
                    break
                else:
                    release_date_theaters = np.nan

            df['release_date_theaters'] = (pd.Series([release_date_theaters]
                                                      * len(df.index)))

            # extract runtime and add to dataframe
            for i in[i for i in range(0, max_limit)]:
                li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
                li_descendants = list(li_tag_line.descendants)
                if 'Runtime:' in li_descendants:
                    runtime = li_descendants[7].split('\n')[1]
                    break
                else:
                    runtime = np.nan

            df['runtime'] = pd.Series([runtime] * len(df.index))

            # extract box office info and add to dataframe
            for i in[i for i in range(0, max_limit)]:
                li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
                li_descendants = list(li_tag_line.descendants)
                if 'Box Office (Gross USA):' in li_descendants:
                    box_office_gross_usa = li_descendants[5]
                    break
                else:
                    box_office_gross_usa = np.nan

            df['box_office_gross_usa'] = (pd.Series([box_office_gross_usa]
                                                     * len(df.index)))

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

            # extract movie title and add to dataframe
            movie_title = soup.title.text[:-len(' - Rotten Tomatoes')]
            df1['movie_title'] = pd.Series([movie_title] * len(df1.index))

            max_limit = len(soup.find_all('li', class_='meta-row clearfix'))

            # extract release date and add to dataframe
            for i in[i for i in range(0, max_limit)]:
                li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
                li_descendants = list(li_tag_line.descendants)
                if 'Release Date (Theaters):' in li_descendants:
                    release_date_theaters = li_descendants[7]
                    break
                else:
                    release_date_theaters = np.nan

            df1['release_date_theaters'] = (pd.Series([release_date_theaters]
                                                      * len(df1.index)))

            # extract runtime and add to dataframe
            for i in[i for i in range(0, max_limit)]:
                li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
                li_descendants = list(li_tag_line.descendants)
                if 'Runtime:' in li_descendants:
                    runtime = li_descendants[7].split('\n')[1]
                    break
                else:
                    runtime = np.nan

            df1['runtime'] = pd.Series([runtime] * len(df1.index))

            # extract box office info and add to dataframe
            for i in[i for i in range(0, max_limit)]:
                li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
                li_descendants = list(li_tag_line.descendants)
                if 'Box Office (Gross USA):' in li_descendants:
                    box_office_gross_usa = li_descendants[5]
                    break
                else:
                    box_office_gross_usa = np.nan

            df1['box_office_gross_usa'] = (pd.Series([box_office_gross_usa]
                                                     * len(df1.index)))

            # combine two dataframes
            df = pd.concat([df, df1], ignore_index = 'True')

    return df