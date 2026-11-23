def analyze_log(filename):
    info_count = 0
    warning_count = 0
    error_count = 0
    total_lines = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    print("Log analysis for:", filename)
    print("Total lines:", total_lines)
    print("INFO:", info_count)
    print("WARNING:", warning_count)
    print("ERROR:", error_count)


analyze_log("sample.log")