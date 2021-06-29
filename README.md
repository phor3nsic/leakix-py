# Leakix-py

> Python client for: https://leakix.net/

```
Usage: leakix.py [-h] [-t TARGET] [-s SCOPE]

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target ex: (example|example.com)
  -s SCOPE, --scope SCOPE
                        Scope to search ex: (leak|service)

```
### Service
```
python3 leakix.py -t hackerone.com -s service

[leakix-service] [hostname: 54.90.143.110] [server: nginx v:1.18.0] 54.90.143.110:80
[leakix-service] [hostname: 50.19.94.149] [server: nginx v:] 50.19.94.149:80
[leakix-service] [hostname: 104.243.33.133] [server: Apache v:2.4.29] 104.243.33.133:443
[leakix-service] [hostname: 50.112.145.7] [server: nginx v:1.18.0] 50.112.145.7:80
[leakix-service] [hostname: 13.212.177.96] [server: nginx v:1.18.0] 13.212.177.96:80
[leakix-service] [hostname: 54.209.1.179] [server: nginx v:1.18.0] 54.209.1.179:80
[leakix-service] [hostname: 44.239.74.213] [server: nginx v:1.18.0] 44.239.74.213:80

```

### Leak

```
python3 leakix.py -t example.com -s leak

[leakix-leak] [plugin:PhpInfoHttpPlugin] 94.103.152.112:443
[leakix-leak] [plugin:PhpInfoHttpPlugin] 51.141.49.218:443
[leakix-leak] [plugin:PhpInfoHttpPlugin] 160.16.109.67:443
[leakix-leak] [plugin:PhpInfoHttpPlugin] 173.209.56.51:443
[leakix-leak] [plugin:PhpInfoHttpPlugin] 34.197.50.30:80
[leakix-leak] [plugin:PhpInfoHttpPlugin] 175.126.82.116:443
```