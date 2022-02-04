# TODO execute matching, get output
# TODO see possibility
import glob
import subprocess
import json
import os
dataset_name = "ENZYMES"
label_num = 6
root_d = "data/{}/result/match_d/".format(dataset_name)
root_q = "data/{}/result/match_q_4_6/".format(dataset_name)
root_result = "data/{}/result/match_result_4_6/".format(dataset_name)
files_d = glob.glob(root_d + "*.graph")
files_q = glob.glob(root_q + "*.graph")

result = []
occ = []

if not os.path.exists(root_result):
    os.makedirs(root_result)
with open(root_result + "motif_stats.output", 'w') as f_stat, \
        open(root_result + "motif_occ.output", 'w') as f_occ:
    for q in files_q:
        file_name = q.replace(root_q, '').replace('.graph', '')
        q_index, freq = file_name.split('_')
        print('processing', file_name)
        result.append({'index': q_index, 'freq': freq})
        for i in range(label_num):
            result[-1]['label_' + str(i)] = 0
            result[-1]['label_' + str(i) + "_net"] = 0
        occ.append({'index': q_index, 'graph_occ_list': []})
        err_flag = False
        for d in files_d:
            file_name = d.replace(root_d, '').replace('.graph', '')
            d_index, label = file_name.split('_')
            command = ["SubgraphMatching/build/matching/SubgraphMatching.out", "-d", d, "-q", q, "-filter", "GQL",
                       "-order", "GQL", "-engine", "LFTJ", "-num", "MAX"]
            try:
                output = subprocess.check_output(command).decode("utf-8")
                lines = output.split("\n")
                for line in lines:
                    if line.startswith('Call Count: '):
                        count = int(line.strip().replace('Call Count: ', ''))
                        if count > 0:
                            result[-1]['label_' + label] += count
                            result[-1]['label_' + label + '_net'] += 1
                            occ[-1]['graph_occ_list'].append([d_index, count])
                        break
            except:
                print('error occurred when processing:', d, q)
                err_flag = True
        if not err_flag:
            pass
        # if result[-1]['label_1_net']:
        #     bias = result[-1]['label_0_net'] / result[-1]['label_1_net']
        # else:
        #     bias = 0
        # result[-1]['bias_net'] = bias
        data_result = json.dumps(result[-1])
        f_stat.write(data_result + "\n")
        data_occ = json.dumps(occ[-1])
        f_occ.write(data_occ + "\n")
