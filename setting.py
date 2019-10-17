# 请求配置
HEADERS = {
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'Origin': "https://qiye.zhaopingou.com",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'User-Agent': ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"),
    'Content-type': "application/x-www-form-urlencoded",
    'Accept': "multipart/form-data",
    # 'Connection': "keep-alive",
    'Cache-Control': "no-cache",
    'Host': "qiye.zhaopingou.com",
    'cache-control': "no-cache"
}

BASE_URL = 'https://qiye.zhaopingou.com'

# 查询条件配置
DEGREES = {
    '不限': -1,
    '高中/中技/中专': 1,
    '大专': 2,
    '本科': 3,
    '硕士': 4,
    'MBA': 5,
    '博士': 6,
    '及以上': 100,
}

GENDER = {
    '不限': -1,
    '男': 0,
    '女': 1,
}

WORK_YEAR = {
    '不限': -1,
    '无经验': 0,
    '1年': 1,
    '2年': 2,
    '3年': 3,
    '4年': 4,
    '5年': 5,
    '及以上': 100,
}

CITY = {
    '北京市': 1,
    '上海市': 2,
    '深圳市': 3,
    '杭州市': 4,
    '广州市': 5,
    '天津市': 6,
    '重庆市': 53,
    '南京市': 57,
    '郑州市': 111,
    '武汉市': 129,
    '合肥市': 200,
    '长沙市': 235,
    '西安市': 249,
    '成都市': 291,
}

