
import sys
import csv
import facebook
import json
import urllib
import pprint

print('Argument List:', str(sys.argv))

'''
https://gist.github.com/espeed/11114604
'''


def main_routine(arg):

    with open(arg) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

    # token = '622124081310396|fZnzVVTtc7kNn_BrkBdqId5g-h8'
    #
    # graph = facebook.GraphAPI(token)
    # profile = graph.get_object("me")
    # friends = graph.get_connections("me", "friends")
    #
    # friend_list = [friend['name'] for friend in friends['data']]
    #
    # print(friend_list)

    ACCESS_TOKEN = 'EAACEdEose0cBAEO0GJXecEwpY4NzdZCh9qPRD8OZAUF7ODvYm4ouoZCgXPlNAOAN4xGZCKe49TqX3Ctr6hRMgItGSi2VnZCPfbu0lIGcRR1HMqMWZBVpoU3ENIUSgDOXG36JuYPzvbWNRxFTzRNLkRryEtIQhxmrn435COS9ZB0gEx2vzgDjm5uTSHFZCwSXLdAZD'

    # build the URL for the API endpoint
    host = "https://graph.facebook.com"
    path = "/me"
    params = urllib.urlencode({"access_token": ACCESS_TOKEN})

    url = "{host}{path}?{params}".format(host=host, path=path, params=params)

    # open the URL and read the response
    resp = urllib.urlopen(url).read()

    # convert the returned JSON string to a Python datatype
    me = json.loads(resp)

    # display the result
    pprint.pprint(me)



if __name__ == '__main__':

    main_routine(sys.argv[1])


