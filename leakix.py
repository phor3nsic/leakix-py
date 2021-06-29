import requests
import argparse
import sys

headers = {"Accept":"application/json"}

def search_leaks(target):
	url = f"https://leakix.net/search?q={target}&scope=leak"
	req = requests.get(url, headers=headers)
	resp = req.json()
	if resp == None:
		print("[leakix-leak] No Results!")
		sys.exit()

	for x in resp:
		ip = x["ip"]
		port = x["port"]
		plugin = x["plugin"]
		org = x["network"]["organization_name"]

		print(f"[leakix-leak] [plugin:{plugin}] {ip}:{port}")

def search_services(target):
	url = f"https://leakix.net/search?q={target}&scope=service"
	req = requests.get(url, headers=headers)
	resp = req.json()

	if resp == None:
		print("[leakix-service] No Results!")
		sys.exit()
	
	for x in resp:
		ip = x["ip"]
		port = x["port"]
		hostname = x["hostname"]
		software = x["software"]["name"]
		software_version = x["software"]["version"]
		
		print(f"[leakix-service] [hostname: {hostname}] [server: {software} v:{software_version}] {ip}:{port}")

def main():
	parser = argparse.ArgumentParser(add_help=True)
	parser.add_argument("-t", "--target", help="Target ex: (example|example.com)")
	parser.add_argument("-s","--scope", help="Scope to search ex: (leak|service)")
	args = parser.parse_args()

	if args.scope == "service": 
		search_services(args.target)

	if args.scope == "leak":
		search_leaks(args.target)


if __name__ == '__main__':
	main()