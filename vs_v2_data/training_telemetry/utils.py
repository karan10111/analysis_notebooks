import json


def get_per_epoch_files(audio_paths_file, epoch, num_batches_in_epoch=10000):
    audio_used = []
    with open(audio_paths_file) as apf:
        line = apf.readline()
        cnt = 1
        while line:
            cnt += 1
            info = json.loads(line)
            gstep = info["GSTEP"]
            paths = info["paths"]
            if gstep < epoch * num_batches_in_epoch:
                audio_used.extend(paths)
            line = apf.readline()
    return audio_used

