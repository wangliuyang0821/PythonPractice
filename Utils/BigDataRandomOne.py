import random

def get_one():
    data_map = {
        "1": "HashMap的数据结构是什么？如何实现的？和hashtable、ConcurrentHashMap的区别？",
        "2": "ArrayList是如何实现的，ArrayList和LinkedList的区别？ArrayList如何实现扩容?",
        "3": "synchronized和volatile的使用方法和区别",
        "4": "Hbase读写基本流程",
        "5": "乐观锁与悲观锁",
        "6": "理解spark中的job、stage、task",
        "7": "kafka的消息传递方式",
        "8": "Spark的driver和executor",
        "9": "Java虚拟机",
        "10": "接口和抽象类有什么区别",
        "11": "List、set、map之间的区别是什么",
        "12": "spark mapreduce和hive mapreduce的区别，以及spark的优势与缺点",
        "13": "mapreduce过程",
        "14": "spark执行流程",
        "15": "维度建模",
        "16": "zookeeper选举",
        "17": "Lock与synchronized有以下区别",
        "18": "kafka如何保证数据不丢失",
        "19": "kafka零拷贝",
        "20": "spark内存模型",
        "21": "HDFS读写数据流程",
        "22": "namenode的作用",
        "23": "HBase的HMaster的作用",
        "24": "HDFS再上传文件的时候，如果其中一个块突然损坏了怎么办",
        "25": "order by和sort by的区别 cluster by和distribute by的区别",
        "26": "spark partition分区策略",
        "27": "Flink架构",
        "28": "spark shuffle调优；shuffle的过程；什么决定shufflemaptask和shufflereducetask的个数；shufflegroup的作用",
        "29": "写入tidb性能优化",
        "30": "spark rdd的五大特性",
        "31": "flink checkpoint的对齐",
        "32": "rebalance与rescale的区别",
        "33": "Flink 从checkpoint恢复，并行度改变后，状态重分配",
        "34": "spark shuffle",
        "35": "Flink checkpoint 与 Spark checkpoint有什么区别或优势",
        "36": "对于迟到数据是怎么处理的",
        "37": "Flink 集群有哪些角色？各自有什么作用",
        "38": "Flink 资源管理中 Task Slot 的概念",
        "39": "Flink 的重启策略",
        "40": "如果下级存储不支持事务，Flink 怎么保证 exactly-once",
        "41": "Flink 是如何处理反压的",
        "42": "Flink 中的状态存储",
        "43": "简单说一下 hadoop 和 Spark 的 shuffle 相同和差异？",
        "44": "RDD 的弹性表现在哪几点",
        "45": "介绍一下 join 操作优化经验",
        "46": "Hive 中的压缩格式 TextFile、SequenceFile、RCfile 、ORCfile各有什么区别？",
        "47": "宽窄依赖",
        "48": "添加维度不回刷数据",
        "49": "scala伴生对象",
        "50": "flink内存模型",
        "51": "kafka rebalance",
        "52": "cache和persist是action算子吗？会懒执行嘛？",
        "53": "内存只有256M，有两个10G的文件，从这两个文件中找出相同的数字？",
        "54": "clickhouse为什么快",
        "55": "spark sql group by 优化，添加哪些参数",
        "56": "范式建模和维度建模的区别",
        "57": "hdfs小文件解决方式，hive和spark",
        "58": "app下沉到dws的标准",
        "59": "dwd的几种类型以及其作用",
        "60": "doris的查询优化有那些方式",
        "61": "flink一致性是什么，如何实现",
        "62": "spark中group by和reduceby的区别",
        "63": "spark中coalesce和repartition的区别"
    }

    # 和 Java 一样：size-1, 然后随机 [0, len-1] 的整数
    keys = list(data_map.keys())
    random_num = random.randint(0, len(keys) - 1)

    content = data_map[str(random_num + 1)] if str(random_num + 1) in data_map else None
    print("index:", random_num + 1)
    return content

#4,12,14,15,19,20,21,25 ,28,33,46,50,51,55,56,57
if __name__ == "__main__":
    print(get_one())
