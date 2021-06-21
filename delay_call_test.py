from cloudburst.client.client import CloudburstConnection

AWS_FUNC_ELB = 'a03bcf30dc0464116afc2faea44dc393-1972614435.us-east-1.elb.amazonaws.com'

MY_IP = '18.210.27.139'

local = False

if local:
    local_cloud = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
else:
    local_cloud = CloudburstConnection(AWS_FUNC_ELB, MY_IP, local=False)


cloud_sleep = local_cloud.register(lambda _: time.sleep(1), 'sleep01')

for i in range(10):
    local_cloud.exec_func('sleep01',[])
