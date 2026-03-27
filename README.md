<a href="https://safedep.io"><img src="https://github.com/user-attachments/assets/50a0ebad-6dc8-461c-b86f-b8cc89a89045" align="right" alt="Made at SafeDep badge" /></a>

# revdns

Bulk reverse DNS lookup for IP addresses using [advertools.reverse_dns_lookup](https://advertools.readthedocs.io/en/master/advertools.reverse_dns_lookup.html).

Given a list of IP addresses, resolves hostnames in parallel (up to 600 workers) and outputs a summary table with hostname, aliases, and error details.

## Usage

```bash
pip install advertools
```

```bash
# Print results to console
python revdns.py ips.txt

# Save results to CSV
python revdns.py ips.txt results.csv
```

### Input format

One IP address per line, no spaces:

```
66.249.66.194
66.249.66.91
130.185.74.243
```

### Output

A table with columns: `ip_address`, `count`, `hostname`, `aliaslist`, `ipaddrlist`, `errors`.

## Reference

- [advertools.reverse_dns_lookup documentation](https://advertools.readthedocs.io/en/master/advertools.reverse_dns_lookup.html)

## License

MIT
