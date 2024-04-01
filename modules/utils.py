class Utils:
    def get_headers(token):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'it-IT,it;q=0.9',
            'Authorization': token,
            'Content-Length': '0',
            'Origin': 'https://discord.com',
            'Referer': 'https://discord.com/channels/@me',
            'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
            'X-Debug-Options': 'bugReporterEnabled',
            'X-Discord-Locale': 'it',
            'X-Discord-Timezone': 'Europe/Rome',
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Iml0LUlUIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmVfY3VycmVudCI6Imdvb2dsZSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI4MDM0NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
        }
        return headers
    
    def get_name_items(id):
        if id == "1214340999644446720":
            return "Buster Blade"
        elif id == "1214340999644446721":
            return "Cute Plushie"
        elif id == "1214340999644446722":
            return "Wump Shell"
        elif id == "1214340999644446723":
            return "Speed Boost"
        elif id == "1214340999644446724":
            return "⮕⬆⬇⮕⬆⬇"
        elif id == "1214340999644446725":
            return "Power Helmet"
        elif id == "1214340999644446726":
            return "Quack!!"
        elif id == "1214340999644446727":
            return "OHHHHH BANANA"
        elif id == "1214340999644446728":
            return "Dream Hammer"