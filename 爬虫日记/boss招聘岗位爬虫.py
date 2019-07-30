#抓取boss直聘网深圳地区的python相关工作的招聘信息，并且将招聘信息导入excel表中
#https://www.zhipin.com/c101280600/?query=python&page=1&ka=page-1
#利用requests xlwt xpath lxml



import requests #请求网页
import xlwt  #excel操作
from lxml import etree # xpath

#获取页面
def getPage():
    #请求头    注意若是请求头出错 则会出现ssl验证的失败
    header = {
        "user-agent": "Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/75.0.3770.142 Safari/537.36"

            }
    #创建一个列表放入html
    responses = []
    #循环抓取页码
    for page in range(1,20):
        url = "https://www.zhipin.com/c101280600/?query=python&page="+str(page)
        response = requests.get(url,headers=header).text
        responses.append(response)
        print("第"+str(page)+"页处理完成")
    return str(responses)
#运用xpath处理html 定位
def parse(text):
    html = etree.HTML(text) #初始化 标准化
    #岗位
    jobs = html.xpath('//div[@class="job-title"]/text()')
    #地点
    place = html.xpath('//div[@class="info-primary"]/p/text()[1]')
    #工作经验
    wordyear = html.xpath('//div[@class="info-primary"]/p/text()[2]')
    #学历
    xueli = html.xpath('//div[@class="info-primary"]/p/text()[3]')
    #招聘企业
    company =html.xpath('//div[@class="company-text"]//a/text()')
    #工资
    salary = html.xpath('//div[@class="info-primary"]//span[@class="red"]/text()')
    #zip（）打包为元祖的列表 加上list才能转化为元组的列表
    jobs_data = list(zip(jobs,place,wordyear,xueli,company,salary))
    #第一行加上列名
    jobs_data.insert(0,("岗位","地点","工作经验","学历","招聘企业","薪资"))
    #调用保存为excel的函数
    save_to_excel("python岗位","岗位招聘",jobs_data)
    #保存为excel文件
def save_to_excel(fliename,sheet_name,data):
    f = xlwt.Workbook(encoding="utf-8") #创建一个workbook设置编码
    #第二个参数表示是否可以覆盖单元格 其实是workbook实例化的一个参数，默认值为false
    sheet = f.add_sheet(sheet_name,cell_overwrite_ok=True)

    #enumerate()函数用于将一个可便利的数据对象（如：列表、元组、字符串）
    #组合为一个索引序列
    #同时列出数据和数据下标，一般用在for循环当中

    for row,row_data in enumerate(data): #处理行
        for column,column_data in enumerate(row_data):#处理列
            sheet.write(row,column,str(column_data))
    f.save(fliename+".xls")

if __name__ == '__main__':
    parse(getPage())


