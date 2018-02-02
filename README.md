#### Python script to generate a NetCDF mask for IPCC SREX regions ([Seneviratne et al. 2012](https://www.ipcc.ch/pdf/special-reports/srex/SREX-Ch3-Supplement_FINAL.pdf)).

Credits to [regionmask](http://regionmask.readthedocs.io/en/stable/) doing most of the heavy lifting.

---

![IPCC SREX Regions](./IPCC_SREX_Regions.png 'IPCC SREX Regions')

| Region ID | Abbreviation | Longname |
|-----|-----|----|
|  1  | ALA  | Alaska/N.W. Canada |
|  2  | CGI  | Canada/Greenl./Icel. |
|  3  | WNA  | W. North America |
|  4  | CNA  | C. North America |
|  5  | ENA  | E. North America |
|  6  | CAM  | Central America/Mexico |
|  7  | AMZ  | Amazon |
|  8  | NEB  | N.E. Brazil |
|  9  | WSA  | Coast South America |
|  10 |  SSA |  S.E. South America |
|  11 |  NEU |  N. Europe |
|  12 |  CEU |  C. Europe |
|  13 |  MED |  S. Europe/Mediterranean |
|  14 |  SAH |  Sahara |
|  15 |  WAF |  W. Africa |
|  16 |  EAF |  E. Africa |
|  17 |  SAF |  S. Africa |
|  18 |  NAS |  N. Asia |
|  19 |  WAS |  W. Asia |
|  20 |  CAS |  C. Asia |
|  21 |  TIB |  Tibetan Plateau |
|  22 |  EAS |  E. Asia |
|  23 |  SAS |  S. Asia |
|  24 |  SEA |  S.E. Asia |
|  25 |  NAU |  N. Australia |
|  26 |  SAU |  S. Australia/New Zealand |

---

#### Customize resolution (in createSREXnetCDF.py):
```python
## define resolution in degree, e.g. 1.875°
lon_res = 1.875
lat_res = 1.875
```


#### Dependencies:
* [Xarray](http://xarray.pydata.org/en/stable/)
* NumPy
* [regionmask](http://regionmask.readthedocs.io/en/stable/)
