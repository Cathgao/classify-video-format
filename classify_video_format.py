import os, sys, subprocess, json, shutil
from subprocess import call

workpath = sys.path[0]

def move_file(codec,filename):
    if not os.path.exists(codec):
        os.mkdir(codec)
    source_file = os.path.join(workpath, filename)
    dest_file = os.path.join(workpath,codec,filename)
    shutil.move(source_file, dest_file)

def probe_file(filename):
    cmnd = ['ffprobe', '-show_streams', '-select_streams', 'v', '-print_format', 'json', '-loglevel', 'quiet', filename]
    p = subprocess.Popen(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err =  p.communicate()
    data = json.loads(out)
    try:
        codec = data["streams"][0]["codec_name"]
    except:
        return
    move_file(codec,filename)



def recursive_listdir(path):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            probe_file(file)
        # elif os.path.isdir(file_path):
        #     yield from recursive_listdir(file_path)
            
recursive_listdir(workpath)
