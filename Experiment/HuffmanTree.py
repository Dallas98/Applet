# Huffman编码

# 树节点类构建
class TreeNode(object):
    def __init__(self, data):
        self.value = data[0]
        self.priority = data[1]
        self.leftChild = None
        self.rightChild = None
        self.code = ""


# 创建树节点队列函数
def creat_node_queue(codes):
    q = []
    for code in codes:
        q.append(TreeNode(code))
    return q


# 为队列添加节点元素，并保证优先度从大到小排列
def add_queue(queue, nodeNew):
    if len(queue) == 0:
        return [nodeNew]
    for i in range(len(queue)):
        if queue[i].priority >= nodeNew.priority:
            return queue[:i] + [nodeNew] + queue[i:]
    return queue + [nodeNew]


# 节点队列类定义
class NodeQueue(object):

    def __init__(self, code):
        self.queue = creat_node_queue(code)
        self.size = len(self.queue)

    def add_node(self, node):
        self.queue = add_queue(self.queue, node)
        self.size += 1

    def pop_node(self):
        self.size -= 1
        return self.queue.pop(0)


# 各个字符在字符串中出现的次数，即计算优先度
def fre_char(string):
    d = {}
    for c in string:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return sorted(d.items(), key=lambda x: x[1])


# 创建哈夫曼树
def creat_huffman_tree(nodeQ):
    while nodeQ.size != 1:
        node1 = nodeQ.pop_node()
        node2 = nodeQ.pop_node()
        r = TreeNode([None, node1.priority + node2.priority])
        r.leftChild = node1
        r.rightChild = node2
        nodeQ.add_node(r)
    return nodeQ.pop_node()


codeDic1 = {}
codeDic2 = {}


# 由哈夫曼树得到哈夫曼编码表
def HuffmanCodeDic(head, x):
    global codeDic, codeList
    if head:
        HuffmanCodeDic(head.leftChild, x + '0')
        head.code += x
        if head.value:
            codeDic2[head.code] = head.value
            codeDic1[head.value] = head.code
        HuffmanCodeDic(head.rightChild, x + '1')


# 字符串编码
def TransEncode(string):
    global codeDic1
    transcode = ""
    for c in string:
        transcode += codeDic1[c]
    return transcode


# 字符串解码
def TransDecode(StringCode):
    global codeDic2
    code = ""
    ans = ""
    for ch in StringCode:
        code += ch
        if code in codeDic2:
            ans += codeDic2[code]
            code = ""
    return ans


# 测试
string = "DRSQWRWESDRQWARESRQSFDRWAEWQDSEFARWESRQDRQAERQDSAEWSQERADSQ"
t = NodeQueue(fre_char(string))
tree = creat_huffman_tree(t)
HuffmanCodeDic(tree, '')
print(codeDic1, '\n', codeDic2)
a = TransEncode(string)
print(a)
aa = TransDecode(a)
# aa=TransDecode('001010100000111010100100101010010100101010010010010001110010100100100100110100010010100110')
print(aa)
print(string == aa)
