---
title: Eda
marimo-version: 0.16.2
width: medium
---

```python {.marimo}
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
```

```python {.marimo}
import statadict
```

```python {.marimo}
dct_file = "./public/2002FemPreg.dct"
dat_file = "./public/2002FemPreg.dat.gz"
```

```python {.marimo}
from statadict import parse_stata_dict


def read_stata(dct_file, dat_file):
    stata_dict = parse_stata_dict(dct_file)
    resp = pd.read_fwf(
        dat_file,
        names=stata_dict.names,
        colspecs=stata_dict.colspecs,
        compression="gzip",
    )
    return resp
```

```python {.marimo}
preg = read_stata(dct_file, dat_file)
```

```python {.marimo}
preg.shape
```

```python {.marimo}
preg.head(10)
```

```python {.marimo}
preg.columns
```

```python {.marimo}
preg["outcome"].value_counts().sort_index()
```

```python {.marimo}
counts=preg["birthwgt_lb"].value_counts(dropna=False).sort_index()
```

```python {.marimo}
counts
```

```python {.marimo}
counts.loc[0:5]
```

```python {.marimo}
counts.loc[0:5].sum()
```

```python {.marimo}
preg["birthwgt_lb"] = preg["birthwgt_lb"].replace([51, 97, 98, 99], np.nan)
```

```python {.marimo}
preg["agepreg"].mean()
```

```python {.marimo}
preg["agepreg"] /= 100.0
preg["agepreg"].mean()
```

```python {.marimo}
preg["birthwgt_oz"] = preg["birthwgt_oz"].replace([97, 98, 99], np.nan)
```

```python {.marimo}
preg["totalwgt_lb"] = preg["birthwgt_lb"] + preg["birthwgt_oz"] / 16.0
preg["totalwgt_lb"].mean()
```

```python {.marimo}
weights = preg["totalwgt_lb"]
n = weights.count()
n
```

```python {.marimo}
mean = weights.sum() / n
mean
```

```python {.marimo}
squared_deviations = (weights - mean) ** 2
```

```python {.marimo}
squared_deviations
```

```python {.marimo}
var = squared_deviations.sum() / n
var
```

```python {.marimo}
std = np.sqrt(var)
std
```

```python {.marimo}
subset = preg.query("caseid == 10229")
subset.shape
```

```python {.marimo}
subset["outcome"].values
```

### Ex 1.1

```python {.marimo}
preg['birthord'].value_counts(dropna=False).sort_index()
```

### EX 1.2

```python {.marimo}
preg['totalwgt_kg'] = preg['totalwgt_lb']/2.2
```

```python {.marimo}
preg['totalwgt_kg'].mean()
```

```python {.marimo}
preg['totalwgt_kg'].std(ddof=0)
```

### EX1.3

```python {.marimo}
ans = preg.query("caseid==2298")
```

```python {.marimo}
ans['prglngth']
```

```python {.marimo}
ans_2 = preg.query("caseid==5013")
```

```python {.marimo}
ans_2
```

```python {.marimo}
wt=ans_2.query("pregordr==1")
```

```python {.marimo}
wt['totalwgt_lb']
```

```python {.marimo}

```