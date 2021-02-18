import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def get_movie_data1(urls_list):
    """Get the movie data from its url.

    Arg:
    url: URL link containing movie data. This should be from Rotten Tomatoes
    and in a list.

    Returns:
    df: A dataframe containing movie data."""

    movie_title = []
    score_all_critics = []
    average_rating_all_critics = []
    score_sentiment_all_critics = []
    review_count_all_critics = []
    rating_count_all_critics = []
    liked_count_all_critics = []
    not_liked_count_all_critics = []
    tomatometer_state_all_critics = []
    score_top_critics = []
    average_rating_top_critics = []
    score_sentiment_top_critics = []
    review_count_top_critics = []
    rating_count_top_critics = []
    liked_count_top_critics = []
    not_liked_count_top_critics = []
    tomatometer_state_top_critics = []
    score_audience = []
    average_rating_audience = []
    score_sentiment_audience = []
    review_count_audience = []
    rating_count_audience = []
    liked_count_audience = []
    not_liked_count_audience = []
    tomatometer_state_audience = []
    runtime = []
    release_date = []
    box_office_gross_usa = []
    movie_dictionary = {}

    for movie_url in url_list:
        response = requests.get(movie_url)
        soup = BeautifulSoup(response.content, 'lxml')

        movietitle = soup.title.text[:-len(' - Rotten Tomatoes')]
        movie_title.append(movietitle)

        scores_text = (soup.find_all('script', type=
                                                'text/javascript')[2].string)
        scores_text_lines_list = scores_text.split('\n')
        for line in scores_text_lines_list:
            if 'root.RottenTomatoes.context.scoreInfo' in line:
                scores_data_dict = line
                break
        scores_data_dict = (scores_data_dict.replace('root.RottenTomatoes'
                                        '.context.scoreInfo = ', '').replace('true',
                                        'True').replace('false', 'False').replace('null',
                                        'np.nan')[:-1])
        scores_data_dict = eval(scores_data_dict)

        score_all_critics.append(scores_data_dict['tomatometerAllCritics']['score'])
        average_rating_all_critics.append(scores_data_dict['tomatometerAllCritics']['averageRating'])
        score_sentiment_all_critics.append(scores_data_dict['tomatometerAllCritics']['scoreSentiment'])
        review_count_all_critics.append(scores_data_dict['tomatometerAllCritics']['reviewCount'])
        rating_count_all_critics.append(scores_data_dict['tomatometerAllCritics']['ratingCount'])
        liked_count_all_critics.append(scores_data_dict['tomatometerAllCritics']['likedCount'])
        not_liked_count_all_critics.append(scores_data_dict['tomatometerAllCritics']['notLikedCount'])
        tomatometer_state_all_critics.append(scores_data_dict['tomatometerAllCritics']['tomatometerState'])
        score_top_critics.append(scores_data_dict['tomatometerTopCritics']['score'])
        average_rating_top_critics.append(scores_data_dict['tomatometerTopCritics']['averageRating'])
        score_sentiment_top_critics.append(scores_data_dict['tomatometerTopCritics']['scoreSentiment'])
        review_count_top_critics.append(scores_data_dict['tomatometerTopCritics']['reviewCount'])
        rating_count_top_critics.append(scores_data_dict['tomatometerTopCritics']['ratingCount'])
        liked_count_top_critics.append(scores_data_dict['tomatometerTopCritics']['likedCount'])
        not_liked_count_top_critics.append(scores_data_dict['tomatometerTopCritics']['notLikedCount'])
        tomatometer_state_top_critics.append(scores_data_dict['tomatometerTopCritics']['tomatometerState'])
        score_audience.append(scores_data_dict['audienceAll']['score'])
        average_rating_audience.append(scores_data_dict['audienceAll']['averageRating'])
        score_sentiment_audience.append(scores_data_dict['audienceAll']['scoreSentiment'])
        review_count_audience.append(scores_data_dict['audienceAll']['reviewCount'])
        rating_count_audience.append(scores_data_dict['audienceAll']['ratingCount'])
        liked_count_audience.append(scores_data_dict['audienceAll']['likedCount'])
        not_liked_count_audience.append(scores_data_dict['audienceAll']['notLikedCount'])
        tomatometer_state_audience.append(scores_data_dict['audienceAll']['audienceClass'])

        max_limit = len(soup.find_all('li', class_='meta-row clearfix'))

        for i in[i for i in range(0, max_limit)]:
            li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
            li_descendants = list(li_tag_line.descendants)
            if 'Runtime:' in li_descendants:
                runtime_ = li_descendants[7].split('\n')[1][len('                            '):]
                break
            else:
                runtime_ = np.nan

        runtime.append(runtime_)

        for i in[i for i in range(0, max_limit)]:
            li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
            li_descendants = list(li_tag_line.descendants)
            if 'Box Office (Gross USA):' in li_descendants:
                box_office_gross_usa_ = li_descendants[5]
                break
            else:
                box_office_gross_usa_1 = np.nan
        box_office_gross_usa.append(box_office_gross_usa_)

        for i in[i for i in range(0, max_limit)]:
            li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
            li_descendants = list(li_tag_line.descendants)
            if 'Release Date (Theaters):' in li_descendants:
                release_date_theaters_ = li_descendants[7]
                break
            else:
                release_date_theaters_ = np.nan
        release_date.append(release_date_theaters_)


    movie_dictionary['movie_title'] = movie_title
    movie_dictionary['score_all_critics'] = score_all_critics
    movie_dictionary['average_rating_all_critics'] = average_rating_all_critics
    movie_dictionary['score_sentiment_all_critics'] = score_sentiment_all_critics
    movie_dictionary['review_count_all_critics'] = review_count_all_critics
    movie_dictionary['rating_count_all_critics'] = rating_count_all_critics
    movie_dictionary['liked_count_all_critics'] = liked_count_all_critics
    movie_dictionary['not_liked_count_all_critics'] = not_liked_count_all_critics
    movie_dictionary['tomatometer_state_all_critics'] = tomatometer_state_all_critics
    movie_dictionary['score_top_critics'] = score_top_critics
    movie_dictionary['average_rating_top_critics'] = average_rating_top_critics
    movie_dictionary['score_sentiment_top_critics'] = score_sentiment_top_critics
    movie_dictionary['review_count_top_critics'] = review_count_top_critics
    movie_dictionary['rating_count_top_critics'] = rating_count_top_critics
    movie_dictionary['liked_count_top_critics'] = liked_count_top_critics
    movie_dictionary['not_liked_count_top_critics'] = not_liked_count_top_critics
    movie_dictionary['tomatometer_state_top_critics'] = tomatometer_state_top_critics
    movie_dictionary['score_audience'] = score_audience
    movie_dictionary['average_rating_audience'] = average_rating_audience
    movie_dictionary['score_sentiment_audience'] = score_sentiment_audience
    movie_dictionary['review_count_audience'] = review_count_audience
    movie_dictionary['rating_count_audience'] = rating_count_audience
    movie_dictionary['liked_count_audience'] = liked_count_audience
    movie_dictionary['not_liked_count_audience'] = not_liked_count_audience
    movie_dictionary['tomatometer_state_audience'] = tomatometer_state_audience
    movie_dictionary['runtime'] = runtime
    movie_dictionary['release_date'] = release_date
    movie_dictionary['box_office_gross_usa'] = box_office_gross_usa

    movies_ratings_df = pd.DataFrame.from_dict(movie_dictionary)

    return movies_ratings_df  

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

def get_movie_reviews(url_list):
    """Get the movie reviews from its url.

    Arg:
    url: URL link containing movie data. This should be from Rotten Tomatoes
    and in a list.

    Returns:
    df: A dataframe containing movie reviews."""

    reviews = []
    reviews_dictionary = {}
    movie_title = []
    critics_name = []
    review_sentiment = []
    reviews = []
    review_date = []

    for movie_url in url_list:
        for i in [i for i in range(0, 6)]:
            response = requests.get('{}/reviews?type=top_critics&sort=&page={}'.format(movie_url, i))
            soup = BeautifulSoup(response.content, 'lxml')

            for review in soup.find_all('div', class_="row review_table_row"):
                movie_title.append(soup.title.text[:-len(' - Movie Reviews')])
                critics_name.append(list(review.find('div', class_="col-sm-17 col-xs-32 critic_name").descendants)[2])
                if 'fresh' in review.find('div', class_="col-xs-16 review_container").contents[1].attrs['class']:
                    review_sentiment.append('fresh')
                else:
                    review_sentiment.append('rotten')
                reviews.append(str(review.find('div', class_="the_review").string)[len('\r\n                    '):-len('\r\n                ')])
                review_date.append(str(review.find('div', class_="review-date subtle small").string)[len('\r\n                '):-len('\r\n            ')])

    reviews_dictionary["movie_title"], reviews_dictionary["critics_name"], reviews_dictionary["review_sentiment"], reviews_dictionary["review"], reviews_dictionary["review_date"] = movie_title, critics_name, review_sentiment, reviews, review_date
    reviews_df = pd.DataFrame.from_dict(reviews_dictionary)

    return reviews_df
