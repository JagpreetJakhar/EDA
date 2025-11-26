import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    return (pd,)


@app.cell
def _():
    import statadict
    import scipy
    return


@app.cell
def _():
    dct_file = "./public/2002FemPreg.dct"
    dat_file = "./public/2002FemPreg.dat.gz"
    return


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
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
