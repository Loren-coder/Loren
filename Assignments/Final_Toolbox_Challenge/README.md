# Mapping for suitable houses on [Block Island](https://www.google.com/maps/place/Block+Island,+New+Shoreham,+RI+02807/data=!4m2!3m1!1s0x89e5f2c9f8a7cff9:0xa20c27ff7497a9cc?sa=X&ved=2ahUKEwj4nc-xoKTwAhXNnOAKHRkJBMoQ8gEwJ3oECGwQAQ)

## Study Area
<img src=https://seewesterly.com/wp-content/uploads/2017/09/blockislandmap.jpg width="200" height="300"><img src=https://img.marinas.com/v2/c9b356d614491632e62968191fcd3cf0fa5d203f90c705dd6d2d8ef1e489e680.jpg width="500" height="300"><img src=https://ap.rdcpix.com/a2c3e8e5d3e08c5b66cf3fa8b31a1dd3l-m991210866xd-w1020_h770_q80.jpg width="400" height="300">

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
