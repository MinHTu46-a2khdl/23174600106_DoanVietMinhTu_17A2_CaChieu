van_ban = """
       I have many friends but Amit is my best friend
       He is my classmate and neighbor also
       He always stood first in the class
       He is very helpful
       He is smart and good looking
       He always keeps himself neat and clean
       He is honest and hardworking. He respects elders
       He is very punctual and disciplined. He helps me in my study
       I love him very much """
tu_dem = {tu: van_ban.split().count(tu) for tu in set(van_ban.split())}
tu_max,tu_min = max(tu_dem, key=tu_dem.get),min(tu_dem, key=tu_dem.get)

print(f"""
Từ xuất hiện nhiều nhất: '{tu_max}' với {tu_dem[tu_max]} lần.
Từ xuất hiện ít nhất: '{tu_min}' với {tu_dem[tu_min]} lần.""")