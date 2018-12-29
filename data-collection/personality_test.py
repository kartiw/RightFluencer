"""
The example returns a JSON response whose content is the same as that in
  ../resources/personality-v3-expect2.txt
"""


from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username='XX',
    password='XX')

with open('profile.txt') as \
        profile_json:
    profile = personality_insights.profile(
        profile_json.read(), content_type='text/plain',
        raw_scores=True, consumption_preferences=True)

    print(json.dumps(profile, indent=2))
