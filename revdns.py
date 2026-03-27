import sys
import pandas as pd
import advertools as adv

def main():
    if len(sys.argv) < 3:
        print("Usage: python revdns.py <input.csv> <output.csv>")
        print("Input CSV format: ip,frequency (no header)")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    df_input = pd.read_csv(input_file, header=None, names=["ip", "frequency"])
    print(f"Loaded {len(df_input)} IPs from {input_file}")

    unique_ips = df_input["ip"].unique().tolist()
    result = adv.reverse_dns_lookup(unique_ips)

    merged = df_input.merge(result, left_on="ip", right_on="ip_address", how="left")
    merged = merged[["ip", "frequency", "hostname", "aliaslist", "ipaddrlist", "errors"]]

    print(merged.to_string(index=False))

    merged.to_csv(output_file, index=False)
    print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    main()
