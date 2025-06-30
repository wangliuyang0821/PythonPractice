import random

def get_one():
    data_map = {
        "1": "留存率 uid,date",
        "2": "连续登陆 uid,date",
        "3": "抖音用户浏览视频日志TableA(date, user_id, video_id),统计2020.03.29观看视频最多的前5个user_id（相同视频要排重）",
        "4": "累计收入  date,value",
        "5": "求平均成绩大于80，且0001课程分数高于0002课程分数的学生id  table(courseid,studentid,name,score)",
        "6": "每天的近7天平均gmv (order_id,user_id,payment_time,gmv)",
        "7": "直播间最大在线人数room_id,user_id,in_time,out_time",
        "8": "首次下单后第二天连续下单的用户比率",
        "9": "会话划分 user_id,pageid,time，超过60s是另一个会话,用sql实现",
        "10": "order left join user, user = 100出现数据倾斜",
        "11": "table:user_id,type,time,计算每个用户的在线时长"
    }

    keys = list(data_map.keys())
    # 注意 Java 中是 size-1, 但 Python randint 是 [a,b] 闭区间，randrange 是 [a,b) 左闭右开
    index = random.randint(0, len(keys) - 1)
    key = keys[index]
    print("index:", key)
    return data_map[key]

# 示例
print(get_one())
