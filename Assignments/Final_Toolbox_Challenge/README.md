# Mapping for suitable houses on Block Island

## Study Area
<img src=https://seewesterly.com/wp-content/uploads/2017/09/blockislandmap.jpg width="200" height="300"><img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZYzIy0qnGkB0maotBjianxeatLDLxiOicgA&usqp=CAU>

## Criteria
### Convenience
- Within 100 meters to the major roads
### Affordability
- Housing prices are below $1,000,000
## Tools
- There are 4 GIS tools in the toolbox for this research

### [XY Table To Point](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/xy-table-to-point.htm)

- This tool displays houses on Block Island using the coordinates in the table

### [Buffer](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm)

- Buffer tool will create a 100-meter buffer zone

### [Intersect](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/intersect.htm)

- This tool creats a new layer of houses in the buffer zone

### [Select](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/select.htm)

- This tool then selects houses within $1,000,000
