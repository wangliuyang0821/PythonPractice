import random

def get_one():
    data_map = {
        "1": "面向对象",
        "2": "JVM性能调优实战 jvm内存结构",
        "3": "JDK、JRE和JVM区别和联系",
        "4": "==和equals比较",
        "5": "final",
        "6": "String、StringBuffer和StringBuilder的区别和使用场景",
        "7": "重载和重写的区别",
        "8": "接口和抽象类的区别",
        "9": "list和set",
        "10": "hashcode和equals",
        "11": "ArrayList和LinkedList的区别",
        "12": "HashMap和HashTable的区别及底层实现 and treeMap",
        "13": "ConcurrentHashMap原理简述，jdk7和jdk8的区别",
        "16": "java类加载器有哪些",
        "17": "双亲委派模型",
        "18": "java中的异常体系",
        "19": "GC如何判断对象可以被回收",
        "20": "线程的生命周期及状态",
        "21": "sleep、wait、join、yield",
        "22": "对线程安全的理解",
        "23": "Thread和Runnable",
        "24": "说说你对守护线程的理解",
        "25": "ThreadLocal的原理和使用场景",
        "26": "ThreadLocal内存泄露的原因，如何避免",
        "27": "并发、并行和串行的区别",
        "28": "并发的三大特性",
        "29": "为什么要使用线程池，参数解释",
        "30": "线程池处理流程",
        "31": "线程池中阻塞队列的作用？为什么是先添加队列而不是先创建最大线程？",
        "32": "线程池的复用原理",
        "33": "scala伴生对象",
        "34": "equals和==区别？为什么重写equals要重写hashcode？"
    }

    keys = list(data_map.keys())
    # Java: size-1，nextInt(len) => [0, len-1)
    random_num = random.randint(0, len(keys) - 1)

    # Java 用的 key 是字符串
    selected_key = keys[random_num]
    print("index:", selected_key)
    return data_map.get(selected_key)

if __name__ == "__main__":
    print(get_one())
