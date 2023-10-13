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
        tasks = r.get("http://localhost/gettasks").json()["tasks"]
        for task in tasks:
            if task["response"] == None:
                with stdoutIO() as s:
                    try:
                        exec(task["code"])
                        res = s.getvalue()
                    except Exception as e:
                        res = str(e)
                    r.post("http://localhost/putresponse", json={"num":tasks.index(task), "response":res})
