import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point

# 创建省份和年份的数据
data = {
    'Year': [2000, 2002, 2005, 2008, 2011, 2014, 2017, 2020],
    'Province': ['北京', '上海', '江苏', '浙江', '四川', '广东', '湖南', '陕西'],
    'Coordinates': [(116.4074, 39.9042), (121.4737, 31.2304), (118.7632, 32.0617),
                    (120.1551, 30.2741), (104.0668, 30.6595), (113.2644, 23.1291),
                    (112.9823, 28.1941), (108.9398, 34.3416)]
}

# 创建GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=[Point(xy) for xy in data['Coordinates']])

# 读取中国地图
china_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
china_map = china_map[china_map.name == "China"]

# 绘制地图
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
china_map.plot(ax=ax, color='white', edgecolor='black')
gdf.plot(ax=ax, color='red', marker='o')

# 添加年份标签
for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['Year']):
    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")

plt.title('科学家的中国足迹变化地图')
plt.xlabel('经度')
plt.ylabel('纬度')
plt.grid(True)
plt.show()
