import jwt
import requests
import json
from time import time
#
# key='YzmM88nvSlCUXsgfwp08sw'
# sec='E0G3kdbb3D2u9R7ww44NbVsNYSLueyZNGyDr'

# send a request with headers including
# a token and meeting details
def createMeeting(key,sec,da):

    # create a function to generate a token
    # using the pyjwt library
    def generateToken():
        # Enter your API key and your API secret
        API_KEY = str(key)
        API_SEC = str(sec)
        token = jwt.encode(

            # Create a payload of the token containing
            # API Key & expiration time
            {'iss': API_KEY, 'exp': time() + 5000},

            # Secret used to generate token signature
            API_SEC,

            # Specify the hashing alg
            algorithm='HS256'
        )
        return token
    # print(da)

    # create json data for post requests
    meetingdetails = {"topic": "Patient Psychiatrist meeting",
                      "type": 2,
                      "start_time": "2019-06-14T10: 21: 57",
                      "duration": "45",
                      "timezone": "Europe/Madrid",
                      "agenda": "test",

                      "recurrence": {"type": 1,
                                     "repeat_interval": 1
                                     },
                      "settings": {"host_video": "true",
                                   "participant_video": "true",
                                   "join_before_host": "False",
                                   "mute_upon_entry": "False",
                                   "watermark": "true",
                                   "audio": "voip",
                                   "auto_recording": "cloud"
                                   }
                      }


    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))

    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]

    return (f'{join_URL}')

# # run the create meeting function
# createMeeting(key,sec)
