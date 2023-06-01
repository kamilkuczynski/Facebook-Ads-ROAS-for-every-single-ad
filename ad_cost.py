from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
import pandas as pd
import credentials

my_app_id = credentials.my_app_id
my_app_secret = credentials.my_app_secret
my_access_token = credentials.my_access_token

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_[YOUR_AD_ACCOUNT_ID]')

campaigns = my_account.get_campaigns()

for campaign in campaigns:
    fields = [
        AdsInsights.Field.campaign_id,
        AdsInsights.Field.adset_name,
        AdsInsights.Field.ad_name,
        AdsInsights.Field.impressions,
        AdsInsights.Field.outbound_clicks,
        AdsInsights.Field.spend,
        AdsInsights.Field.website_purchase_roas,
        AdsInsights.Field.purchase_roas,
        AdsInsights.Field.reach,
        AdsInsights.Field.ctr,
        AdsInsights.Field.frequency,
        AdsInsights.Field.cost_per_one_thousand_ad_impression,
        AdsInsights.Field.website_purchase_roas,
        AdsInsights.Field.ad_id,
        AdsInsights.Field.adset_id,
        AdsInsights.Field.campaign_name
    ]

    params = {
        'level': 'ad',
        'time_range': {'since': '2022-07-01', 'until': '2023-04-01'}
    }

    insights = campaign.get_insights(fields=fields, params=params)
    print(insights)

    print('Convert insights data to a pandas dataframe')
    df = pd.DataFrame([data for data in insights])

    # Save data as CSV
    with open('ads_cost.csv', mode='a', encoding='utf-8', newline='') as file:
        df.to_csv(file, index=False)

