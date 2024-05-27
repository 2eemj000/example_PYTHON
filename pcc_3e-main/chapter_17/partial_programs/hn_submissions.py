from operator import itemgetter

import requests


# Make an API call and check the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json' # api를 호출할 URL
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json() # 응답객체를 파이썬 리스트로 변환, 이 ID를 이용해 글과 대응하는 딕셔너리 만듦

submission_dicts = [] # 이 딕셔너리를 저장할 빈리스트 만들기
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json" # submission_id의 현재값을 이용해 URL만듦
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = { # 현재 글에 대한 딕셔너리 만듦
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict) # submission_dicts 리스트에 submission_dict 추가

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), # operator모듈의 itemgetter() 함수이용
                            reverse=True) # 함수에 comments키 전달하면 리스트의 각 딕셔너리에서 해당키에 할당된 값 가져옴

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")