import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from os.path import basename,exists
    return basename, exists


@app.cell
def _(basename, exists):
    def download(url):
        filename = basename(url)
        if not exists(filename):
            from urllib.request import urlretrieve
            local,_ = urlretrieve(url,filename)
            print(f"Downloaded {local}")
    return (download,)


@app.cell
def _(download):
    download("https://github.com/AllenDowney/ThinkStats/raw/v3/nb/thinkstats.py")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
