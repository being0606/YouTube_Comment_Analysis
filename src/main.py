from selenium import webdriver
import pandas as pd
import time

def get_comments(url):
    # 웹드라이버 설정 (여기서는 Chrome을 사용)
    driver = webdriver.Chrome("/path/to/chromedriver")

    # 유튜브 영상 페이지로 이동
    driver.get(url)
    
    # 페이지 로드를 기다림
    time.sleep(2)

    # 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # 댓글이 로드될 때까지 기다림
    time.sleep(2)

    # 댓글 요소를 찾음
    comments = driver.find_elements_by_css_selector("#content-text")

    # 데이터 프레임 생성
    df = pd.DataFrame(columns = ['comments'])
    for comment in comments:
        df = df.append({"comments": comment.text}, ignore_index=True)
    
    driver.close()

    return df

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=dU_2RUQzuYo"
    df = get_comments(url)
    print(df)