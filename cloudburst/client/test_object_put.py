from cloudburst.client.common import *

def dag_write(cloudburst, key, size, use_str):
    if use_str:
        new_v = 'a' * size
    else:
        new_v = np.random.random(size)

    start_1 = time.time()
    cloudburst.put_object(key, new_v)
    start_2 = time.time()
    cloudburst.put_object('start1_', start_1)
    cloudburst.put_object('start2_', start_2)
    return [new_v, key]

def dag_read(cloudburst, up_res):
    key = up_res[1]
    end_1 = time.time()
    cloudburst.get_object(key)
    end_2 = time.time()

    cloudburst.put_object('end1_', end_1)
    cloudburst.put_object('end2_', end_2)


OSIZE = 100
iter_num = 4
use_str = True

# suc, err = cloudburst_client.delete_dag('dag_io')
print(f'Test Default with size {OSIZE}')
write_name = 'dag_write_5'
read_name = 'dag_read_5'
dag_write_func = cloudburst_client.register(dag_write, write_name)
dag_read_func = cloudburst_client.register(dag_read, read_name)

dag_name = 'dag_io_4'
functions = [write_name, read_name]
conns = [(write_name, read_name)]
success, error = cloudburst_client.register_dag(dag_name, functions, conns)
print(f'Create dag {dag_name} {success} {error}')

key_n = 'dag3'
arg_map = {write_name: [key_n, OSIZE, use_str]}

elasped_list = []
for _ in range(iter_num):
    print("---")
    a = cloudburst_client.call_dag(dag_name, arg_map).get()
    print("---")
    start1 = cloudburst_client.get_object('start1_')
    start2 = cloudburst_client.get_object('start2_')
    end1 = cloudburst_client.get_object('end1_')
    end2 = cloudburst_client.get_object('end2_')
    elasped_list.append([start1, start2, end1, end2])

print('ephe results. elasped {}'.format(elasped_list))

# suc, err = cloudburst_client.delete_dag(dag_name)