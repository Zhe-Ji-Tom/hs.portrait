

def get_keywords_by_label(connect):
    labels_keywords_map = {}
    cursor = connect.cursor()
    # 获取工作分类
    cursor.execute("SELECT ID FROM LABELS")
    label_ids = cursor.fetchall()

    for label_id in label_ids:
        cursor.execute("SELECT KEYWORD FROM KEYWORDS WHERE LABEL_ID = %s", label_id)
        keywords = cursor.fetchall()
        keyword_map = {label_id: keywords}
        labels_keywords_map.update(keyword_map)

    connect.commit()
    return labels_keywords_map
