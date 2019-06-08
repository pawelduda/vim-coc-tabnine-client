from subprocess import Popen, PIPE
import json

TABNINE_PATH = 'binaries/1.0.14/x86_64-unknown-linux-gnu/TabNine'
TEST = {"version": "1.0.0", "request": {"Autocomplete": {"before": "Hello H", "after": "", "region_includes_beginning":
                                                         True, "region_includes_end": True, "filename": None}}}
process = Popen(TABNINE_PATH, stdout=PIPE, stdin=PIPE)
print json.dumps(TEST)
process.stdin.write((json.dumps(TEST) + '\n').encode('utf8'))
process.stdin.flush()

output = process.stdout.readline().decode('utf8')
print output
