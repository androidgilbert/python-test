cities={'bj':"beijing","sjz":"shijiazhuang","sh":"shanghai"}
cities['yt']='yantai'
cities['jn']='jinan'
def find_city(themap,key):
	if key in themap:
		return themap[key]
	else:
		return "not found"
cities['find']=find_city
print cities
# while True:
# 	print "Key?(Enter to quit)",
# 	key=raw_input(">")
# 	if not key:break
# 	city_found=cities['find'](cities,key)
# 	print city_found