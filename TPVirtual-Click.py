#!/Users/david/.pyenv/shims/python

import os,sys,subprocess,re,time,glob

# The Script tries to determine the directory for the qz app installation automatically below. If
# that fails, set it here. Find the subdirectory in ~/Library/Containers that contains 
#
# "Data/Library/Caches/org.cagnulein.qdomyoszwift" 
# 
# Then replace "RandomString with that subdirectory (which is random string), and uncomment (remove)
# the '#' before MY_QZ_APPDIR.
#
# MY_QZ_APPDIR ='/Users/david/Library/Containers/RandomString'
# 
# Let's try and find the installation directory of qdomyoszwift automagically.
# If this doesn't work, change it above.
#

def shiftUp():
        cmd = """
        osascript <<EOF
        tell application "TPVirtual"
                activate
                tell application "System Events" to keystroke "="
        end tell
        EOF
        """
        os.system(cmd)

def shiftDown():
        cmd = """
        osascript <<EOF
        tell application "TPVirtual"
                activate
                tell application "System Events" to keystroke "-"
        end tell
        EOF
        """
        os.system(cmd)

def watch(fn, words):
    fp = open(fn, 'r')
    first_time = True
    while True:
        new = fp.readline()
        # Once all lines are read this just returns ''
        # until the file changes and a new line appears

        if new:
            if first_time is False:
                for word in words:
                    if word in new:
                        yield (word, new)
        else:
            first_time = False
            time.sleep(0.5)

# Main

try: 
    MY_QZ_APPDIR
except NameError:
    qz_appdir_string = subprocess.check_output('find ~/Library/Containers |grep qdomyoszwift | head -1 | cut -d / -f 6', shell=True, text=True).rstrip()

    if qz_appdir_string != "":
        MY_QZ_APPDIR=os.getenv('HOME') + "/Library/Containers/" + qz_appdir_string
    else:
        print("Couldn't find QZ App Directory")
        sys.exit(1)


# Cleanup old debug log files of QZ. WARNING: Don't do this if you need those around!
logdir = MY_QZ_APPDIR + '/Data/Documents/'

try:
    logfiles = list(filter(os.path.isfile, glob.glob(logdir + "*")))
    for f in logfiles: 
        os.remove(f)
except:
    print("No old logs to delete")

launch_qz = "open -a /Applications/qdomyoszwift.app"
launch_iv = "open -W /Applications/TPVirtual-Launcher.app"

os.system(launch_qz)
#os.system(launch_iv)

log_found = False

while log_found is False:
    try:
        new_logfiles = list(filter(os.path.isfile, glob.glob(logdir + "*.log")))
        new_logfiles.sort(key=lambda x: os.path.getmtime(x))
        fn = new_logfiles[-1] 
        log_found = True
    except:
        print("Waiting for log...")
        time.sleep(10)


pattern = re.compile("setGears (\-*\d+)$")

old_gear = 0
new_gear = 0

print("Getting ready to ride...")
os.system(launch_iv)

try:
    words = ['setGears']
    for hit_word, hit_sentence in watch(fn, words):
        for match in pattern.finditer(hit_sentence):
            new_gear = int(match.groups()[0])
            if new_gear > old_gear and new_gear < 20:
                print("shift UP")
                shiftUp()
                old_gear = new_gear
            elif new_gear < old_gear and new_gear > -7:
                print("shift DOWN")
                shiftDown()
                old_gear = new_gear
except(KeyboardInterrupt):
    print("Shutting Down...")
    os.system("killall -3 qdomyoszwift")
    sys.exit(0)

