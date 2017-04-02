from .transpyler import transpyler


def run_jupyter():
    """
    Runs a Jupyter shell for Pytugues.
    """

    from transpyler.jupyter import run_jupyter
    run_jupyter(transpyler)


if __name__ == '__main__':
    run_jupyter()
