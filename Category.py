import pymysql


def get_tags_by_category(connect):
    tags = {}
    cursor = connect.cursor()
    # 获取工作分类
    cursor.execute("SELECT DISTINCT CATEGORY FROM CATEGORY_SET")
    category_name = cursor.fetchall()

    for name in category_name:
        cursor.execute("SELECT DISTINCT TAG FROM CATEGORY_SET WHERE CATEGORY = %s", name)
        tag = cursor.fetchall()
        tag_map = {name: tag}
        tags.update(tag_map)

    connect.commit()
    return tags
