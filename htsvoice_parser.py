# Extract items of HTS voices (or voice.data)
# Useful to get trees and make patches to it. For example, dur and lf0.

def extract_part(file_path, part):
    offsets = {
        # add offsets manually for now.
        "dur": (34044, 124655),
        #"dur": (33684, 123401),
        "lf0": (2295413, 2793993)
        #"lf0": (2298952, 2811210)
    }
    if part not in offsets:
        raise ValueError("Invalid part. Use 'dur' for DURATION_TREE or 'lf0' for STREAM_TREE[LF0].")
    start, end = offsets[part]
    with open(file_path, "rb") as f:
        while True:
            line = f.readline()
            if line.strip() == b"[DATA]":
                break
        data_start = f.tell()
        f.seek(data_start + start)
        data = f.read(end - start)
    return data.decode()

lf0_info = extract_part("24000/voice.data", "lf0")
#dur_info = extract_part("24000/voice.data", "dur")
with open("lf0.inf", "w") as f:
    f.write(lf0_info)