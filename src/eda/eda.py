import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import scipy
    import marimo as mo
    return mo, np, pd


@app.cell
def _():
    import statadict
    return


@app.cell
def _():
    dct_file = "./public/2002FemPreg.dct"
    dat_file = "./public/2002FemPreg.dat.gz"
    return dat_file, dct_file


@app.cell
def _(pd):
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
    return (read_stata,)


@app.cell
def _(dat_file, dct_file, read_stata):
    preg = read_stata(dct_file, dat_file)
    return (preg,)


@app.cell
def _(preg):
    preg.shape
    return


@app.cell
def _(preg):
    preg.head(10)
    return


@app.cell
def _(preg):
    preg.columns
    return


@app.cell
def _(preg):
    preg["outcome"].value_counts().sort_index()
    return


@app.cell
def _(preg):
    counts=preg["birthwgt_lb"].value_counts(dropna=False).sort_index()
    return (counts,)


@app.cell
def _(counts):
    counts
    return


@app.cell
def _(counts):
    counts.loc[0:5]
    return


@app.cell
def _(counts):
    counts.loc[0:5].sum()
    return


@app.cell
def _(np, preg):
    preg["birthwgt_lb"] = preg["birthwgt_lb"].replace([51, 97, 98, 99], np.nan)
    return


@app.cell
def _(preg):
    preg["agepreg"].mean()
    return


@app.cell
def _(preg):
    preg["agepreg"] /= 100.0
    preg["agepreg"].mean()
    return


@app.cell
def _(np, preg):
    preg["birthwgt_oz"] = preg["birthwgt_oz"].replace([97, 98, 99], np.nan)
    return


@app.cell
def _(preg):
    preg["totalwgt_lb"] = preg["birthwgt_lb"] + preg["birthwgt_oz"] / 16.0
    preg["totalwgt_lb"].mean()
    return


@app.cell
def _(preg):
    weights = preg["totalwgt_lb"]
    n = weights.count()
    n
    return n, weights


@app.cell
def _(n, weights):
    mean = weights.sum() / n
    mean
    return (mean,)


@app.cell
def _(mean, weights):
    squared_deviations = (weights - mean) ** 2
    return (squared_deviations,)


@app.cell
def _(squared_deviations):
    squared_deviations
    return


@app.cell
def _(n, squared_deviations):
    var = squared_deviations.sum() / n
    var
    return (var,)


@app.cell
def _(np, var):
    std = np.sqrt(var)
    std
    return


@app.cell
def _(preg):
    subset = preg.query("caseid == 10229")
    subset.shape
    return (subset,)


@app.cell
def _(subset):
    subset["outcome"].values
    return


@app.cell
def _(mo):
    mo.md(r"""### Ex 1.1""")
    return


@app.cell
def _(preg):
    preg['birthord'].value_counts(dropna=False).sort_index()
    return


@app.cell
def _(mo):
    mo.md(r"""### EX 1.2""")
    return


@app.cell
def _(preg):
    preg['totalwgt_kg'] = preg['totalwgt_lb']/2.2
    return


@app.cell
def _(preg):
    preg['totalwgt_kg'].mean()
    return


@app.cell
def _(preg):
    preg['totalwgt_kg'].std(ddof=0)
    return


@app.cell
def _(mo):
    mo.md(r"""### EX1.3""")
    return


@app.cell
def _(preg):
    ans = preg.query("caseid==2298")
    return (ans,)


@app.cell
def _(ans):
    ans['prglngth']
    return


@app.cell
def _(preg):
    ans_2 = preg.query("caseid==5013")
    return (ans_2,)


@app.cell
def _(ans_2):
    ans_2
    return


@app.cell
def _(ans_2):
    wt=ans_2.query("pregordr==1")
    return (wt,)


@app.cell
def _(wt):
    wt['totalwgt_lb']
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
