from cloudburst.client.common import *

def dag_write(cloudburst, key, size, use_str):
    # import time
    new_v = 'a' * size
    cloudburst.put(key, new_v)
    return 2


OSIZE = 100
iter_num = 4
use_str = True

print(f'Test Default with size {OSIZE}')
write_name = 'dag_write_1'

dag_write_func = cloudburst_client.register(dag_write, write_name)


dag_name = 'dag_io_7'
functions = [write_name]
conns = [(write_name)]
success, error = cloudburst_client.register_dag(dag_name, functions, conns)
print(f'Create dag {dag_name} {success} {error}')

key_n = 'dag4'
arg_map = {write_name: [key_n, OSIZE, use_str]}

elasped_list = []
for _ in range(iter_num):
    print("---")
    a = cloudburst_client.call_dag(dag_name, arg_map).get()
    print("---")
    start1 = cloudburst_client.get_object('start1_')
    start2 = cloudburst_client.get_object('start2_')
    # end1 = cloudburst_client.get_object('end1_')
    # end2 = cloudburst_client.get_object('end2_')
    # elasped_list.append([start1, start2, end1, end2])

print('ephe results. elasped {}'.format(elasped_list))

# suc, err = cloudburst_client.delete_dag(dag_name)