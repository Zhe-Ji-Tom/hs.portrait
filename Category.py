import pymysql


def get_tags_by_category():
    tags = {}
    connect = pymysql.connect('localhost', user='root', passwd='root', db='test')
    cursor = connect.cursor()
    # 获取工作分类
    category_name = cursor.execute("SELECT DISTINCT CATEGORY FROM CATEGORY_SET")

    for name in category_name:
        tag = cursor.execute("SELECT DISTINCT TAG FRIN CATEGORT_SET WHERE CATEGORY = %s", name)
        tag_map = {name: tag}
        tags.update(tag_map)

    return tags
