def analyze_log(filename):
    info_count = 0
    warning_count = 0
    error_count = 0
    total_lines = 0

        try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                total_lines += 1
                if "ERROR" in line:
                    error_count += 1
                elif "WARNING" in line:
                    warning_count += 1
                elif "INFO" in line:
                    info_count += 1
    except FileNotFoundError:
        print("File not found:", filename)
        return

    report = (
        f"Log analysis for: {filename}\n"
        f"Total lines: {total_lines}\n"
        f"INFO: {info_count}\n"
        f"WARNING: {warning_count}\n"
        f"ERROR: {error_count}\n"
    )

    print(report)

    with open("report.txt", "w", encoding="utf-8") as out_file:
        out_file.write(report)
    print("Report saved to report.txt")


if __name__ == "__main__":
    name = input("Enter log file name (press Enter for sample.log): ").strip()
    if name == "":
        name = "sample.log"
    analyze_log(name)