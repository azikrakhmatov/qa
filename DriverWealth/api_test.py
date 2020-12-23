import datetime

import requests

from payload import *


def api(user, id, token):
    URI = f"https://api.drivewealth.com/{user}/:{id}/equities"
    header = {
        "Content-Type": "application/json",
        "X-Authorization": f"Bearer {token}"
    }
    r = requests.get(url=URI, headers=header)
    return r.status_code, r.json()


def verify_200_valid_payload():
    # Verifying status 200 code with valid credentials
    status = api('aziz', '123', '123')[0]
    response = api('aziz', '123', '123')[1]
    if status == 200 and len(response) < 0:
        return 'Pass'
    else:
        raise Exception('Status is not equal to 200')


def verify_401_invalid_header(user, id, token):
    URI = f"https://api.drivewealth.com/{user}/:{id}/equities"
    header = {
        "Content-Typeeeee": "application/json",
        "X-Authorizationnnn": f"Bearer {token}"
    }
    r = requests.get(url=URI, headers=header)
    if r.status_code == 401:
        return 'Pass'
    else:
        raise Exception('Status is not equal to 401')


def verify_401_no_token():
    status = api('aziz', '123', '')[0]
    if status == 401:
        return 'Pass'
    else:
        raise Exception('Status is not equal to 401')


def verify_404_invalid_userid():
    status = api('qwer', '123', '')[0]
    if status == 404:
        return 'Pass'
    else:
        raise Exception('Status is not equal to 404')


def verify_429_call_5times_10secs():
    start = datetime.datetime.now()
    status1 = api('aziz', '123', '')[0]
    status2 = api('aziz', '123', '')[0]
    status3 = api('aziz', '123', '')[0]
    status4 = api('aziz', '123', '')[0]
    status5 = api('aziz', '123', '')[0]
    end = datetime.datetime.now()
    if str(start - end) > '10':
        if status5 == 429:
            return 'Pass'
        else:
            raise Exception('Status is not equal to 429')


def verify_500():
    #   Precond: Environment should be down
    status = api('qwer', '123', '')[0]
    if status == 500:
        return 'Pass'
    else:
        raise Exception('Status is not equal to 500')


def verify_504():
    #   Precond: Environment should be slow, Q: How slow it should be?
    status = api('qwer', '123', '')[0]
    if status == 504:
        return 'Pass'
    else:
        raise Exception('Status is not equal to 504')


def schema_validation():
    # Verifying response data
    response = expected  # api('aziz', '123', '123')[1]
    if type(response['userID']) is str \
            and type(response['lastUpdated']) is str \
            and type(response['equityValue']) is float \
            and type(response['equityPositions']) is list:
        for i in response['equityPositions']:
            if type(i['symbol']) is str \
                    and type(i['sharesHeld']) is int or float \
                    and type(i['costBasis']) is int or float \
                    and type(i['marketValue']) is int or float \
                    and type(i['priorClose']) is int or float \
                    and type(i['availableForTradingQty']) is int or float \
                    and type(i['averagePrice']) is int or float \
                    and type(i['marketPrice']) is int or float \
                    and type(i['unrealizedPL']) is int or float \
                    and type(i['unrealizedDayPLPercent']) is int or float \
                    and type(i['unrealizedDayPL']) is int or float:

                print('Pass')
            else:
                raise AssertionError('Types are not matching')


def verify_response_payload():
    exp = expected
    act = actual
    if exp['userID'] == act['userID'] \
            and exp['lastUpdated'] == act['lastUpdated'] \
            and exp['equityValue'] == act['equityValue'] \
            and exp['equityPositions'] == act['equityPositions']:
        for e in exp['equityPositions']:
            for a in act['equityPositions']:
                if e['symbol'] == a['symbol'] \
                        and e['sharesHeld'] == a['sharesHeld'] \
                        and e['costBasis'] == a['costBasis'] \
                        and e['marketValue'] == a['marketValue'] \
                        and e['priorClose'] == a['priorClose'] \
                        and e['availableForTradingQty'] == a['availableForTradingQty'] \
                        and e['averagePrice'] == a['averagePrice'] \
                        and e['marketPrice'] == a['marketPrice'] \
                        and e['unrealizedPL'] == a['unrealizedPL'] \
                        and e['unrealizedDayPLPercent'] == a['unrealizedDayPLPercent'] \
                        and e['unrealizedDayPL'] == a['unrealizedDayPL']:
                    return 'Pass'
                else:
                    raise AssertionError('Payload data is not matching')

