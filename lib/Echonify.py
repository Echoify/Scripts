import sys, os, httplib, json, uuid

mode = os.environ["Echonify-InteractiveMode"]
if mode <> "Advanced":
    raise Exception("Please run the script in Advanced mode!")

localPort = os.environ["Echonify-LocalPort"]
securityToken = os.environ["Echonify-SecurityToken"]

def read():
    try:
        conn = httplib.HTTPConnection("127.0.0.1", localPort)
        headers = {
            "Echonify-SecurityToken": securityToken,
            "Echonify-FlowDirection": "inbound"
        }
        conn.request("GET", "/", headers=headers)
        response = conn.getresponse()
        if response.status <> 200:
            return None
        data = response.read()
        return json.loads(data)
    finally:
        conn.close

def readPlain():
    obj = read()
    dataType = obj["dataType"]
    if dataType in ["text", "markdown", "html"]:
        return obj["plain"]
    else:
        return None

def readFileRef():
    obj = read()
    dataType = obj["dataType"]
    if dataType == "fileref":
        return obj["fileName"]
    else:
        return None

def write(obj):
    try:
        conn = httplib.HTTPConnection("127.0.0.1", localPort)
        headers = {
            "Content-Type": "application/json",
            "Echonify-SecurityToken": securityToken,
            "Echonify-FlowDirection": "outbound"
        }
        data = json.dumps(obj)
        conn.request("POST", "/", data, headers=headers)
        response = conn.getresponse()
        if response.status <> 200:
            return False
        return True
    finally:
        conn.close

def writePlain(plain, dataType="text"):
    obj = {
        "type": "data",
        "dataType": dataType,
        "plain": plain
    }
    return write(obj)

def writeFileRef(fileName):
    obj = {
        "type": "data",
        "dataType": "fileref",
        "fileName": os.path.abspath(fileName)
    }
    return write(obj)

def writeStream(fileName, streamId):
    try:
        conn = httplib.HTTPConnection("127.0.0.1", localPort)
        conn.connect()
        conn.putrequest("POST", "/")
        conn.putheader("Transfer-Encoding", "chunked")
        conn.putheader("Content-Type", "application/octet-stream")
        conn.putheader("Echonify-SecurityToken", securityToken)
        conn.putheader("Echonify-FlowDirection", "outbound")
        conn.putheader("Echonify-StreamId", streamId)
        conn.endheaders()
        with open(fileName, 'rb') as f:
            while True:
                chunk = f.read(2048)
                if not chunk:
                    break
                conn.send("%s\r\n" % hex(len(chunk))[2:])
                conn.send("%s\r\n" % chunk)
        conn.send("0\r\n\r\n")
        response = conn.getresponse()
        if response.status <> 200:
            return False
        return True
    finally:
        conn.close

def writeFile(fileName):
    fileSize = os.stat(fileName).st_size
    _, fileExt = os.path.splitext(fileName)
    streamId = "%s%s" % (str(uuid.uuid4()), fileExt)
    obj = {
        "type": "data",
        "dataType": "file",
        "fileName": os.path.abspath(fileName),
        "streamId": streamId,
        "streamLen": fileSize
    }
    res = write(obj)
    if res is not None:
        return writeStream(fileName, streamId)
    return None
