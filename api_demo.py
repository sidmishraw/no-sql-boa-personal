# api_demo.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-03-03 20:33:26
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-03-03 22:55:40


__author__ = 'sidmishraw'


'''
This script will generate the sample data from the New York Times APIs.
'''

# Python standard library imports
from urllib.request import urlopen
from json import dumps
from json import loads
from pprint import pprint



__NYT_API_BASE_PATH__ = 'http://api.nytimes.com/svc/'

# default api key
# I'd recommend use your own api key for this script
__API_KEY__ = 'c9e169f173f34249a02bc0aff8d50fb9'



def archives_api(year = 2000, month = 4):
  '''
  Calls the NYT archives API and generates the sample dataset inside `nyt_archives.json`.
  Takes year and month as the arguments.

  :param: year `int` - Default value = 2000 - The year of the archives
  :param: month `int` - Default value = 4 - The month of the archives

  :return: `None`
  '''

  url_string = '{base_url}archive/v1/{year}/{month}.json?api-key={api_key}'.format(\
    base_url = __NYT_API_BASE_PATH__, year = year, month = month, api_key = __API_KEY__)

  json_string = None

  with urlopen(url_string) as archive_res:
    json_string = archive_res.read()

  with open('nyt_archives.json', 'wb') as op_file:
    op_file.write(json_string)

  return




def movie_reviews_api(offset = 0):
  '''
  Fetches all the movie reviews and writes them to nyt_movie_reviews.json file.
  This is paginated and needs an offset to pull in that
  page's reviews; offset needs to be a multiple of 20.

  For eg - 
  http://api.nytimes.com/svc/movies/v2/reviews/\
  all.json?api-key=c9e169f173f34249a02bc0aff8d50fb9&offset=200

  :param: offset `int` - Default value = 0 - The offset for fetching the reviews. Needs to be a
  multiple of 20.

  :return: `None`
  '''

  # since for some reason v1 is not supported for this API
  # going with v2 instead
  version = 'v2'

  url_string = '{base_url}movies/{version}/reviews/all.json?api-key={api_key}&offset={offset}'.format(\
    base_url = __NYT_API_BASE_PATH__, version = version, api_key = __API_KEY__, offset = offset)

  json_string = None

  with urlopen(url_string) as movies_res:
    json_string = movies_res.read()

  with open('nyt_movie_reviews.json', 'wb') as op_file:
    op_file.write(json_string)

  return




def movie_critics_api(offset = 0):
  '''
  Fetches all the movie critics and writes them to nyt_movie_critics.json file.
  This is paginated and needs an offset to pull in that
  page's critics; offset needs to be a multiple of 20.

  For eg - 
  http://api.nytimes.com/svc/movies/v2/\
  critics/all.json?api-key=c9e169f173f34249a02bc0aff8d50fb9&offset=200

  :param: offset `int` - Default value = 0 - The offset for fetching the critics. Needs to be a
  multiple of 20.

  :return: `None`
  '''

  # since for some reason v1 is not supported for this API
  # going with v2 instead
  version = 'v2'

  url_string = '{base_url}movies/{version}/critics/all.json?api-key={api_key}&offset={offset}'.\
  format(base_url = __NYT_API_BASE_PATH__, version = version, api_key = __API_KEY__, offset = offset)

  json_string = None

  with urlopen(url_string) as movies_res:
    json_string = movies_res.read()

  with open('nyt_movie_critics.json', 'wb') as op_file:
    op_file.write(json_string)

  return




def books_list_api(genre = 'e-book-fiction'):
  '''
  Fetches the books from NYT's book reviews given the genre and the writes them to 
  nyt_books_list.json file.
  The genre needs to be fetched from GET_lists-names.json API call to NYT.

  :param: genre `str` - The genre or list name from NYT

  :return: `None`
  '''

  #going with v3 as mentioned in the documentation
  version = 'v3'

  url_string = '{base_url}books/{version}/lists.json?api-key={api_key}&list={list_name}'.\
  format(base_url = __NYT_API_BASE_PATH__, version = version, api_key = __API_KEY__,\
    list_name = genre)

  json_string = None

  with urlopen(url_string) as books_list_res:
    json_string = books_list_res.read()

  with open('nyt_books_list.json', 'wb') as op_file:
    op_file.write(json_string)

  return




if __name__ == '__main__':
  archives_api()
  movie_reviews_api()
  movie_critics_api()
  books_list_api()


