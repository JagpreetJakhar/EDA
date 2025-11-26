import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return (pd,)


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
def _():
    return


if __name__ == "__main__":
    app.run()
