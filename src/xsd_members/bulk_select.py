from models import MemberProfile

import StringIO
import csv

token_name='names'

def get_some_objects(list):
    return MemberProfile.objects.filter(pk__in=list)
def parse_token_data(request_post):
    f = StringIO.StringIO(request_post[token_name])
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        user_ids=row
    return user_ids

def get_bulk_members(request):
    user_ids=parse_token_data(request.GET)
    members=get_some_objects(user_ids)
    return members
