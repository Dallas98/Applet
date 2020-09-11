import pandas as pd
import copy
import datetime


class Flight(object):
    flight_id = 0
    takeoff_time = 0
    landing_time = 0
    plane = 0
    takeoff_airport = ''
    landing_airport = ''
    annotation = ''

    def __init__(self, flight_id, takeoff_time, landing_time, plane, takeoff_airport, landing_airport):
        self.flight_id = flight_id
        self.takeoff_time = takeoff_time
        self.landing_time = landing_time
        self.plane = plane
        self.takeoff_airport = takeoff_airport
        self.landing_airport = landing_airport


class Event(object):
    flight_id = 0
    time = 0
    action = ''
    plane = ''
    airport = ''
    annotation = ''

    def __init__(self, flight_id, time, action, plane, airport):
        self.flight_id = flight_id
        self.time = time
        self.action = action
        self.plane = plane
        self.airport = airport


def get_plane_type(plane_id, df):
    return df[df['飞机尾号'] == plane_id].iloc[0, 1]


def get_future_landing_time_and_airport(log, plane_id):
    time = 0
    flight_id = 0
    for event in log:
        if event.plane == plane_id and event.action == 'takeoff':
            if (event.time > time):
                time = event.time
                flight_id = event.flight_id
    for event in log:
        if event.flight_id == flight_id and event.action == 'landing':
            return event.time, event.airport


def get_takeoff_event(log, flight_id):
    for event in log:
        if (event.flight_id == flight_id and event.action == 'takeoff'):
            return event


def get_landing_event(log, flight_id):
    for event in log:
        if (event.flight_id == flight_id and event.action == 'landing'):
            return event


def get_canceled_event(log, flight_id):
    for event in log:
        if (event.flight_id == flight_id and event.action == 'canceled'):
            return event


def get_duration(plan, flight_id):
    for event in plan:
        if (event.flight_id == flight_id and event.action == 'landing'):
            end = event.time
        if (event.flight_id == flight_id and event.action == 'takeoff'):
            start = event.time
    return end - start - 45 * 60


def if_flight_take_off(log, flight_id):
    for event in log:
        if event.flight_id == flight_id:
            return True
    return False


def from_unix_stamp(stamp):
    stamp -= 60 * 60 * 8
    time = datetime.datetime.fromtimestamp(stamp)
    return time


def key_time(event):
    return event.time


def key_flight_id(event):
    return event.flight_id


def adjust_plan(plan):
    dict = {}
    for event in plan:
        key = str(event.time) + event.action + event.airport
        dict.setdefault(key, 0)
        dict[key] += 1
        if (dict[key] > 5):
            event.time += 10 * 60
        if (event.action == 'takeoff'):
            landing_event = get_landing_event(plan, event.flight_id)
            landing_event.time += 10 * 60
            landing_event.annotation = 'delayed'
        if (event.action == 'landing'):
            take_off_event = get_takeoff_event(plan, event.flight_id)
            take_off_event.time += 10 * 60
            take_off_event.annotation = 'delayed'
        return False
    return True


def get_landing_soon(log, time, airport):
    result = []
    for event in log:
        if event.action == 'landing' and event.airport == airport and event.time > time:
            result.append(event)
    return result


def to_csv(log, plan, filename):
    log.sort(key=key_flight_id)
    canceled_log = [event for event in log if event.action == 'canceled']
    log = [event for event in log if event.action != 'canceled']

    list = []
    length = len(log)
    i = -1
    lastid = -1
    while (i < length - 1):
        i += 1
        id = log[i].flight_id
        if (id == lastid): continue
        lastid = id
        landing_event = get_landing_event(log, id)
        take_off_event = get_takeoff_event(log, id)
        landing_event_in_plan = get_landing_event(plan, id)
        take_off_event_in_plan = get_takeoff_event(plan, id)
        tmp = []
        tmp.append(log[i].flight_id)  # id
        tmp.append(take_off_event_in_plan.time)  # take off time in plan
        tmp.append(take_off_event.time)  # take off time
        tmp.append(landing_event_in_plan.time)  # landing_time_in_plan
        tmp.append(landing_event.time)  # landing time
        tmp.append(take_off_event.airport)  # take off airport
        tmp.append(landing_event.airport)  # landing airport
        tmp.append(get_plane_type(take_off_event_in_plan.plane, df1))  # plane type in plan
        tmp.append(get_plane_type(take_off_event.plane, df1))  # plane type
        tmp.append(take_off_event_in_plan.plane)  # plane id in plan
        tmp.append(take_off_event.plane)  # plane id
        tmp.append(take_off_event.time - take_off_event_in_plan.time)
        tmp.append(str(from_unix_stamp(take_off_event.time)))
        tmp.append(str(from_unix_stamp(landing_event.time)))
        tmp.append(take_off_event.annotation)
        list.append(tmp)
    length = len(canceled_log)
    i = 0
    while (i < length):
        id = canceled_log[i].flight_id
        landing_event_in_plan = get_landing_event(plan, id)
        take_off_event_in_plan = get_takeoff_event(plan, id)
        tmp = []
        tmp.append(canceled_log[i].flight_id)  # id
        tmp.append(take_off_event_in_plan.time)  # take off time in plan
        tmp.append('canceled')  # take off time
        tmp.append(landing_event_in_plan.time)  # landing_time_in_plan
        tmp.append('canceled')  # landing time
        tmp.append(take_off_event_in_plan.airport)  # take off airport
        tmp.append(landing_event_in_plan.airport)  # landing airport
        tmp.append(get_plane_type(take_off_event_in_plan.plane, df1))  # plane type in plan
        tmp.append('canceled')  # plane type
        tmp.append(take_off_event_in_plan.plane)  # plane id in plan
        tmp.append('canceled')  # plane id
        tmp.append(24 * 60 * 60)
        tmp.append('canceled')
        tmp.append('canceled')
        tmp.append(canceled_log[i].annotation)
        list.append(tmp)
        i += 1
    result_df = pd.DataFrame(list)
    result_df.columns = [u'航班唯一编号', u'起飞时间', u'新起飞时间', u'到达时间 ', u'新到达时间', u'起飞机场', u'到达机场',
                         u'飞机型号', u'新飞机机型号', u'飞机尾号', u'新飞机尾号 ', u'延误时间', u'起飞时间（一般表述）', u'到达时间（一般表述）', u'注释']
    result_df.to_csv(filename, encoding='GBK', index=False)


# 开始
df = pd.read_csv('./miniSchedules.csv', encoding='GBK')
df['飞机尾号'] = df['飞机尾号'].astype('str')
df1 = pd.read_csv('./miniAircrafts.csv', encoding='GBK')
df1 = df1.iloc[:, 0:5]
df1['飞机尾号'] = df1['飞机尾号'].astype('str')

# 初始化
BLIZZARD_START = 1461348000
BLIZZARD_END = 1461358800

tmp = df.iloc[:, 3].values.tolist()
tmp.extend(df.iloc[:, 4].values.tolist())
AIRPORTS = list(set(tmp))

# 初始飞机位置
airplane_dic = {}
events = []
for airport in AIRPORTS:
    airplane_dic[airport] = []

for index, row in df1.iterrows():
    init_airport = row[4]
    plane_id = row[0]
    airplane_dic[init_airport].append(plane_id)

for index, row in df.iterrows():
    # 不能按时起
    if (row[1] > BLIZZARD_START and row[1] < BLIZZARD_END and row[3] == 'OVS'):
        delay = BLIZZARD_END - row[1]
        df.iloc[index, 1] = row[1] + delay
        df.iloc[index, 2] = row[2] + delay
        # 不能按时降
    if (row[2] > BLIZZARD_START and row[2] < BLIZZARD_END and row[4] == 'OVS'):
        delay = BLIZZARD_END - row[2]
        df.iloc[index, 1] = row[1] + delay
        df.iloc[index, 2] = row[2] + delay

# 化为对象

for index, row in df.iterrows():
    take_off_event = Event(row[0], row[1], 'takeoff', str(row[6]), row[3])
    landing_event = Event(row[0], row[2], 'landing', str(row[6]), row[4])
    events.append(take_off_event)
    events.append(landing_event)

# 这样不必考虑 45 分 护的问题
for event in events:
    if (event.action == 'landing'):
        event.time += 45 * 60

# 按时间排序
events.sort(key=key_time)
result = []
# 开始处理
print("start")
index = -1
for event in events:
    if (index % 100 == 0):
        print(str(index) + '/' + str(len(events)))
    index += 1
    id = event.flight_id
    time = event.time
    airport = event.airport
    plane_in_plan = event.plane
    action = event.action
    duration = get_duration(events, id)
    plane_type = df1[df1['飞机尾号'] == plane_in_plan].iloc[0, 1]
    earlist = df1[df1['飞机尾号'] == plane_in_plan].iloc[0, 2]
    latest = df1[df1['飞机尾号'] == plane_in_plan].iloc[0, 3]
    if event.action == 'landing' and if_flight_take_off(result, id):
        if ('-' + plane_in_plan) in airplane_dic[airport]:
            airplane_dic[airport].remove('-' + plane_in_plan)
        else:
            airplane_dic[airport].append(plane_in_plan)
        continue

    substitute_list = []
    tmp = get_future_landing_time_and_airport(result, plane_in_plan)
    landing_soon = get_landing_soon(result, time, airport)

    if (tmp == None):
        for p in landing_soon:
            substitute_list.append('*' + p.plane)
    elif (tmp[1] != airport):
        for p in landing_soon:
            substitute_list.append('*' + p.plane)
    else:
        future_landing_time = tmp[0]
        for p in landing_soon:
            if p.time < future_landing_time:
                substitute_list.append('*' + p.plane)

    for plane in airplane_dic[airport]:
        if (plane[0] == '-'): continue
        _earlist = df1[df1['飞机尾号'] == plane].iloc[0, 2]
        _latest = df1[df1['飞机尾号'] == plane].iloc[0, 3]
        _plane_type = df1[df1['飞机尾号'] == plane].iloc[0, 1]
        if (time >= _earlist and time + duration <= _latest):
            substitute_list.append(plane)

    # 按计划起
    if plane_in_plan in airplane_dic[airport]:
        event.annotation = 'as plan'
        landing_event = get_landing_event(events, id)
        landing_event.annotation = 'as plan'
        tmp = copy.deepcopy(event)
        result.append(tmp)
        tmp = copy.deepcopy(landing_event)
        result.append(tmp)
        airplane_dic[airport].remove(plane_in_plan)
    # 替飞
    elif len(substitute_list) > 0:
        substitute = substitute_list[0]
        flag = 1 if substitute[0] == '*' else 0
        substitute = substitute[1:] if flag == 1 else substitute
        tmp = copy.deepcopy(event)
        tmp.plane = substitute
        tmp.annotation = 'substitute'
        result.append(tmp)
        landing_event = get_landing_event(events, id)
        tmp = copy.deepcopy(landing_event)
        tmp.plane = substitute
        tmp.annotation = 'substitute'
        result.append(tmp)
        if flag == 0:
            airplane_dic[airport].remove(substitute)
        else:
            airplane_dic[airport].append('-' + substitute)
        tmp = sorted(events[index + 1:], key=key_time)
        events[index + 1:] = tmp
    # 或取消
    else:
        landing_time, landing_airport = get_future_landing_time_and_airport(result, plane_in_plan)
        destination_landing_time = landing_time + duration

        if (landing_time - time <= 60 * 60 * 5 and landing_airport == airport and not (
                landing_time > BLIZZARD_START and landing_time < BLIZZARD_END) \
                and destination_landing_time - 45 * 60 < latest and landing_time > earlist):
            tmp = copy.deepcopy(event)
            tmp.time = landing_time
            tmp.annotation = 'delayed'
            result.append(tmp)
            landing_event = get_landing_event(events, id)
            tmp = copy.deepcopy(landing_event)
            tmp.time += landing_time - time
            tmp.annotation = 'delayed'
            result.append(tmp)
            airplane_dic[airport].append('-' + plane_in_plan)
        else:
            result.append(Event(id, event.time, 'canceled', event.plane, ''))

for event in result:
    if (event.action == 'landing'):
        event.time -= 45 * 60

for event in events:
    if (event.action == 'landing'):
        event.time -= 45 * 60

result.sort(key=key_time)

# 处理 道
while (not adjust_plan(result)):
    pass

result.sort(key=key_time)

# 输出
for event in result:
    print('flight id ' + str(event.flight_id) + ' ' + str(event.action) + ' at ' + str(
        from_unix_stamp(event.time)) + '(unix stamp:' \
          + str(event.time) + ')' + ' in ' + str(event.airport) + '. plane: ' + str(
        event.plane) + ', ' + event.annotation)
    df = pd.read_csv('./miniSchedules.csv', encoding='GBK')
    df['飞机尾号'] = df['飞机尾号'].astype('str')
    events = []
    for index, row in df.iterrows():
        take_off_event = Event(row[0], row[1], 'takeoff', str(row[6]), row[3])
        landing_event = Event(row[0], row[2], 'landing', str(row[6]), row[4])
        events.append(take_off_event)
        events.append(landing_event)
    to_csv(result, events, './result.csv')
