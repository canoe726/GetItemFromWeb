from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# 아래 링크에 chromedriver.exe 파일 있는지 확인!
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.implicitly_wait(3)

print("getMask.py 0.2ver")
print("* 주의 사항 *")
print("1. 구매하기 클릭시 아이디와 비밀번호를 요구하므로 입력해야함")
print("2. 네이버 결제화면 상태 시 체크카드가 등록 되어 있고, 결제하기 버튼을 클릭시 네이버페이 비밀번호 창이 바로 뜰 경우 사용가능")
print("3. 자동 입력 방지 로그인 이외에는 웹 화면을 건드리면 오류 발생 가능성이 높아짐")
print("4. 연습용 url로 테스트 후 매크로 돌릴 것")
print("5. .zip파일 압축 해제한 후, chromedriver.exe 파일 C 드라이브에 위치 시킬 것")
print()
print("로딩중....")
print()

# 로그인 페이지
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
driver.get(url)

user_id = input("네이버 아이디를 입력하세요 : ")
user_pw = input("네이버 비밀번호를 입력하세요 : ")

# 자동 아이디, 비밀번호 입력
driver.find_element_by_name('id').send_keys(user_id)
driver.find_element_by_name('pw').send_keys(user_pw)

# 로그인 버튼 클릭
login_button = '//*[@id="log.login"]'
driver.find_element_by_xpath(login_button).click()

sleep_time = 20

print()
print("%d초 이내에 비밀번호와 자동 입력 방지 문자를 입력한 후 로그인 하세요"%sleep_time)
print("로딩중....")
print()

# 자동 입력 방지 화면 뜨면 20으로 sleep 시간 조절, 안뜨면 3으로 변경
# 20초 이내에 비밀번호와 자동 입력 방지 문자를 입력한 후 로그인 해야함
time.sleep(sleep_time)

print("이동하길 원하는 페이지를 입력하세요")
print()
print("page 0 : 연습용 url")
print("page 1 : [닥터퓨리] KF94 미세먼지 황사마스크 20매 (개별 낱개포장)")
print("page 2 : [닥터퓨리] KF94 스타일리시 블랙 미세먼지 황사마스크 20매 (개별 낱개포장)")
print("page 3 : [닥터퓨리] KF94 끈조절 블랙 미세먼지 황사마스크 20매 (개별 낱개포장)")
print("page 4 : [닥터퓨리] KF94 끈조절 미세먼지 황사마스크 20매 (개별 낱개포장)")
print("page 5 : [닥터퓨리] KF94 미세먼지 황사마스크 30매 (뽑아쓰는 번들포장)")
print()

page = int(input("페이지 입력 : "))

mode = 0

# 결제 페이지가 나오기 전까지 무한 반복
while(True) :
    # 연습용 url
    if( page == 0 ):
        url = "https://smartstore.naver.com/twinsstore/products/4812576367?NaPm=ct%3Dk7fvf89f%7Cci%3Dshopn%7Ctr%3Dhdlt%7Ctrx%3D2450494%7Chk%3Da7f7badadbd4ee27623938c53059672d4e179f31"
        mode = 1
    
    # 구매 페이지
    
    # [닥터퓨리] KF94 미세먼지 황사마스크 20매 (개별 낱개포장)
    if( page == 1 ):
        url = "https://smartstore.naver.com/mfbshop/products/4072435942"
        mode = 1

    # [닥터퓨리] KF94 스타일리시 블랙 미세먼지 황사마스크 20매 (개별 낱개포장)
    if( page == 2 ):
        url = "https://smartstore.naver.com/mfbshop/products/4680268551"

    # [닥터퓨리] KF94 끈조절 블랙 미세먼지 황사마스크 20매 (개별 낱개포장)
    if( page == 3 ):
        url = "https://smartstore.naver.com/mfbshop/products/4735164530"

    # [닥터퓨리] KF94 끈조절 미세먼지 황사마스크 20매 (개별 낱개포장)
    if( page == 4 ):
        url = "https://smartstore.naver.com/mfbshop/products/4735160554"

    # [닥터퓨리] KF94 미세먼지 황사마스크 30매 (뽑아쓰는 번들포장)
    if( page == 5 ):
        url = "https://smartstore.naver.com/mfbshop/products/4072573492"
        mode = 1

    driver.get(url)
    driver.implicitly_wait(3)

    cur_url = driver.current_url

    if( mode == 0 ) :
        # 수량 조절
        driver.find_element_by_id('cuid_0').send_keys(Keys.BACKSPACE)
        # 구매하고 싶은 수량
        driver.find_element_by_id('cuid_0').send_keys('3')
        driver.implicitly_wait(1)

    if( mode == 1 ) :
        # 드롭다운 메뉴 클릭
        check_menu = '//*[@id="wrap"]/div/div[2]/div[2]/form/fieldset/div[4]/div[1]/ul/li/ul/li/div/div/div'
        driver.find_element_by_xpath(check_menu).click()
        driver.implicitly_wait(1)

        # 아이템 클릭
        # li[2]는 첫번째 아이템, li[3]은 두번재 아이템...
        check_item = '/html/body/div[2]/div/ul/li[2]'
        driver.find_element_by_xpath(check_item).click()
        driver.implicitly_wait(2)

    # 구매하기 버튼 클릭
    buy_button = '//*[@id="wrap"]/div/div[2]/div[2]/form/fieldset/div[4]/div[2]/div[3]/span[1]/a'
    try:
        elem = driver.find_element_by_xpath(buy_button).click()
    except NoSuchElementException:
        print("구매버튼이 활성화 되지 않았음")
        continue

    # while문 탈출을 위해 페이지 이동까지 기다리기
    time.sleep(3)

    # 변경된 페이지 url 얻기
    change_url = driver.current_url
    
    # 결제 페이지로 이동했다면 while문 탈출 후 결제하기
    if( cur_url != change_url ) :
        break

driver.implicitly_wait(1)
# 전체 동의하기 버튼 체크박스 클릭
agree_button = '//*[@id="allAgree"]/span'
driver.find_element_by_xpath(agree_button).click()

# 결제하기 버튼 클릭
pay_button = '//*[@id="orderForm"]/div/div[7]/button'
driver.find_element_by_xpath(pay_button).click()

