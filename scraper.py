import os
import requests
import random
import time
import pandas as pd
import logging
from playwright.sync_api import sync_playwright

def download_video(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        logging.info(f'Downloaded {filename}')
    else:
        logging.error(f'Failed to download {filename}')

def scrape_tiktok_ads(brands_file, progress_callback):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()
        df = pd.read_excel(brands_file)
        ads_data = []

        for idx, row in df.iterrows():
            brand = row['Brand Name']
            progress_callback(f"Opening TikTok Ads site for brand: {brand}")
            page.goto('https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en?period=180&region=US')
            page.wait_for_selector('div.TopadsVideoCard_card__hFsq1.index-mobile_card__vIKWk')
            page.fill(".byted-select-value", brand)
            progress_callback(f"Searching for videos of brand: {brand}")
            page.click('span.CcAutoCompleteInput_completeAppendLabel__E1AFd[data-testid="cc_commonCom_autoComplete_seach"]')
            page.wait_for_timeout(10000)

            progress_callback(f"Looking for videos of the brand: {brand}")

            video_elements_before = page.query_selector_all('div.TopadsVideoCard_card__hFsq1.index-mobile_card__vIKWk a')
            while True:
                count_before = len(video_elements_before)
                page.evaluate("window.scrollTo(0, document.body.scrollHeight - window.innerHeight - 500);")
                time.sleep(random.uniform(3, 6))
                video_elements_after = page.query_selector_all('div.TopadsVideoCard_card__hFsq1.index-mobile_card__vIKWk a')
                count_after = len(video_elements_after)
                if count_after == count_before:
                    break
                video_elements_before = video_elements_after

            video_links = ["https://ads.tiktok.com" + video.get_attribute('href') for video in video_elements_after]
            progress_callback(f"{len(video_links)} videos found for brand: {brand}")

            for vid_idx, link in enumerate(video_links):
                try:
                    progress_callback(f"Processing video {vid_idx+1}/{len(video_links)} for brand: {brand}")
                    page.goto(link)
                    page.wait_for_selector('video')
                    video_url = page.query_selector('video').get_attribute('src')
                    meta_data = page.query_selector_all('div.BasicInfoItem_container__pjw4E.index-mobile_container__2MFvR.TopadsDetailPage_infoItem__vs2lI')
                    industry_name = meta_data[1].query_selector('span.BasicInfoItem_value__psIua').text_content()
                    brand_name = meta_data[3].query_selector('span.BasicInfoItem_value__psIua').text_content()
                    landing_page_elem = meta_data[4].query_selector('a.BasicInfoItem_link__W0k0D')
                    landing_page = landing_page_elem.get_attribute('href') if landing_page_elem else ""
                    ad_caption = meta_data[5].query_selector('span.byted-popper-trigger.byted-popper-trigger-focus.byted-tooltip.BasicInfoItem_foldTextTips__BWOqY').text_content()
                    ad_performance = page.query_selector_all("div.TopadsDetailPage_metricItem__BzCV3")
                    likes = ad_performance[0].query_selector('span.TopadsDetailPage_value__8kWUW').text_content()
                    comments = ad_performance[1].query_selector('span.TopadsDetailPage_value__8kWUW').text_content()
                    shares = ad_performance[2].query_selector('span.TopadsDetailPage_value__8kWUW').text_content()
                    ctr = ad_performance[3].query_selector('span.TopadsDetailPage_value__8kWUW').text_content()
                    budget = ad_performance[4].query_selector('span.TopadsDetailPage_value__8kWUW').text_content()
                    download_video(video_url, f'videos/video_{brand}_{vid_idx+1}.mp4')
                    ads_data.append({
                        'Industry Name': industry_name,
                        'Brand Name': brand_name,
                        'Ad Caption': ad_caption,
                        'Likes': likes,
                        'Comments': comments,
                        'Shares': shares,
                        'CTR': ctr,
                        'Budget': budget,
                        'Video URL': link,
                        'Landing Page': landing_page
                    })
                    progress_callback(f"Downloaded video {vid_idx+1}/{len(video_links)} for brand: {brand}")
                except Exception as e:
                    logging.error(f"Error parsing video link {link}: {e}")
                    progress_callback(f"Error processing video link {link}: {e}")
                    continue
        
        df_output = pd.DataFrame(ads_data)
        df_output.to_excel('tiktok_ads_data.xlsx', index=False)
        browser.close()
