import sys
import advertools as adv

def main():
    if len(sys.argv) < 2:
        print("Usage: python revdns.py <ip_list.txt> [output.csv]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    with open(input_file) as f:
        ip_list = [line.strip() for line in f if line.strip()]

    print(f"Loaded {len(ip_list)} IPs from {input_file}")

    result = adv.reverse_dns_lookup(ip_list)
    print(result.to_string())

    if output_file:
        result.to_csv(output_file, index=False)
        print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    main()
