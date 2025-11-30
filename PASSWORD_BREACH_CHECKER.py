def load_breaches():
    with open("BREACHED_PASSWORD.txt", "r") as f:
        return set(line.strip() for line in f)

def check_passwords(passwords, breached_set):
    results = {}
    for pwd in passwords:
        results[pwd] = "BREACHED" if pwd in breached_set else "SAFE"
    return results

if __name__ == "__main__":
    user_input = input("Enter passwords (comma separated): ")
    passwords = [p.strip() for p in user_input.split(",")]

    breached_set = load_breaches()
    results = check_passwords(passwords, breached_set)

    with open("breach_report.txt", "w") as r:
        for pwd, status in results.items():
            r.write(f"{pwd} : {status}\n")

    print("\nScan complete! Results saved to breach_report.txt")