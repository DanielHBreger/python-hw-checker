from pathlib import Path
from zipfile import ZipFile
import sys, subprocess, time

codes = []
seen = []
file_name = input("Enter path to zip file: ")
tests = []
with ZipFile(file_name, "r") as zipobj:
    for entry in zipobj.namelist():
        if entry != "inputs/" and entry.startswith("inputs"):
            if entry[-8:-7] not in seen:
                tests.append(list())
                seen.append(entry[-8:-7])
            inp = zipobj.read(entry)
            output_file = "out" + entry[2:-7] + "out" + entry[-5:]
            output = zipobj.read(output_file)
            tests[int(entry[11:12]) - 1].append((inp, output))

for i in range(len(tests)):
    codes.append(input(f"Enter path to your Q{i+1} python file: "))

runtimes = [list() for _ in tests]
passed_tests = []
failed_tests = []

for i, code in enumerate(codes):
    for j, test_set in enumerate(tests[i]):
        start = time.time()
        p = subprocess.Popen(
            [sys.executable, code], stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
        out = p.communicate(input=test_set[0], timeout=5)[0]
        p.wait(10000)
        end = time.time()
        runtimes[i].append(end-start)
        if out == test_set[1]:
            passed_tests.append(f"Question {i} test {j}")
        else:
            failed_tests.append(f"Question {i} test {j}")

if len(failed_tests) == 0 and len(passed_tests) == sum(map(len, tests)):
    print("All tests pass!")
elif len(failed_tests) > 0:
    for pss in passed_tests:
        print(f"Passed test: {pss}")
    for fail in failed_tests:
        print(f"Failed test: {fail}")
else:
    print("An unexpected error has occcurred.")

print("runtimes:")
for i, q in enumerate(runtimes):
    for j, run in enumerate(q):
        print(f"Q{i+1} test {j+1}: {run:.2f}s")