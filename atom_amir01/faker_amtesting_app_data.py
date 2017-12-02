import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','atom_amir01.settings')

import django
django.setup()

##FAKER Script
import random
from amtesting_app.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','News','MarketPlace','Games','Some Topic']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate_data(N=10):

    for entry in range(N):
        #get topics
        mTopic = add_topic()

        #create fake data for topics

        mFakeUrl = fakegen.url()
        mFakeDate = fakegen.date()
        mFakeName = fakegen.company()

        #create web page entry
        webpg = WebPage.objects.get_or_create(topic_name=mTopic,url=mFakeUrl,name=mFakeName)[0]

        #create entry fro AccessRecord
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=mFakeDate)[0]


if __name__ == '__main__':
    print('Populating Records')
    populate_data(30)
    print('Populating Complete')
