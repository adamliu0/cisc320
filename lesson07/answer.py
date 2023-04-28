def student_report(file):
    next(file)
    status_reports = dict()
    for line in file:
        log = line.split()
        studentID = int(log[0])
        actionCode = log[1]
        value = int(log[2])
        timestamp = int(log[3])
        if studentID not in status_reports.keys():
            status_reports[studentID] = {"lowestPID": -1, "latestPID": -1, "avgScore": 0, "scoreCount": 0}
        if actionCode == "P":
            if status_reports[studentID]["lowestPID"] == -1:
                status_reports[studentID]["lowestPID"] = value
            elif value < status_reports[studentID]["lowestPID"]:
                status_reports[studentID]["lowestPID"] = value
            status_reports[studentID]["latestPID"] = value
        elif actionCode == "S":
            status_reports[studentID]["avgScore"] += value
            status_reports[studentID]["scoreCount"] += 1
    return status_reports

def sort_reports(status_reports):
    reports = status_reports.copy()
    for log in reports:
        if reports[log]["scoreCount"] > 0 and reports[log]["lowestPID"] > -1:
            reports[log]["avgScore"] = reports[log]["avgScore"]/reports[log]["scoreCount"]
            del reports[log]["scoreCount"]
        else:
            del reports[log]
    sorted_reports = sorted(reports, key = lambda x: (reports[x]["lowestPID"], reports[x]["latestPID"], reports[x]["avgScore"]))
    ret = []
    for id in sorted_reports:
        ret.append(id)
        ret.append(reports[id]["lowestPID"])
        ret.append(reports[id]["latestPID"])
        ret.append(reports[id]["avgScore"])
    return ret

def solution(file):
    status_reports = student_report(file)
    return sort_reports(status_reports)

if __name__ == "__main__":
    filename = input()
    file = open(filename)
    solution(file)