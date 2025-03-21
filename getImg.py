import os
import requests
import json

# item.js 파일 불러오기
with open("item.js", encoding="utf-8") as f:
    content = f.read()
    json_str = content.split("=", 1)[1].strip()
    item_list = json.loads(json_str)

# 폴더 만들기
os.makedirs("img/foods", exist_ok=True)

# 이미지 다운로드 및 item["img"] 수정
for item in item_list:
    url = item["img"]
    item_id = item["id"]
    filename = f"{item_id}.png"
    local_path = f"img/foods/{filename}"

    print(f"Downloading {filename}...")
    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(local_path, "wb") as f:
            f.write(r.content)
        # 경로 수정
        item["img"] = local_path
    except Exception as e:
        print(f"⚠️ {url} 다운로드 실패: {e}")

# 수정된 리스트 저장
with open("item_local.js", "w", encoding="utf-8") as f:
    f.write("itemList = " + json.dumps(item_list, ensure_ascii=False, indent=2))
