#!/usr/bin/env python
from rich import print
from typer import Typer
# from requests_html import HTMLSession
from crtsh import crtshAPI
# add cross ref to https://bgp.tools
# https://bgp.tools/prefix/12.34.56.0/24#whois for all resolved addrs


app = Typer()

@app.command()
def domains(domains:list[str]):
	"""get one or more subdomains"""
	ret = set()
	for d in domains:
		results = crtshAPI().search(d)
		# print(results)
		for el in results:
			# print(el.get)
			try:
				ret.add(el.get('common_name','').strip())
				ret.add(el.get('name_value','').strip())
			except BaseException as e:
				print(f"Exception for {d}:", e)
	# print(ret)
	for el in ret: 
		print(el)

# @app.command()
# def 

if __name__ == '__main__':
	app()