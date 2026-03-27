<a href="https://safedep.io"><img src="https://github.com/user-attachments/assets/50a0ebad-6dc8-461c-b86f-b8cc89a89045" align="right" alt="Made at SafeDep badge" /></a>

# revdns

Bulk reverse DNS lookup for IP addresses using [advertools.reverse_dns_lookup](https://advertools.readthedocs.io/en/master/advertools.reverse_dns_lookup.html).

Given a CSV of IP addresses with frequency counts, resolves hostnames in parallel (up to 600 workers) and outputs a CSV with hostname details — sortable by frequency.

## Usage

```bash
pip install advertools
```

```bash
python revdns.py input.csv result.csv
```

### Input format

CSV with `ip,frequency` per line (no header):

```
66.249.66.194,1500
66.249.66.91,820
130.185.74.243,45
```

### Output

A CSV with columns: `ip`, `frequency`, `hostname`, `aliaslist`, `ipaddrlist`, `errors`.

## Reference

- [advertools.reverse_dns_lookup documentation](https://advertools.readthedocs.io/en/master/advertools.reverse_dns_lookup.html)

## License

MIT
