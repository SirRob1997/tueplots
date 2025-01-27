"""Fontsize settings."""


def icml2022():
    return _from_base(base=10)


def neurips2021():
    return _from_base(base=10)


def aistats2022():
    return _from_base(base=10)


def jmlr2001():
    return _from_base(base=10.95)


def beamer_moml():
    return _from_base(base=10)


def _from_base(*, base=10):
    return {
        "font.size": base - 1,
        "axes.labelsize": base - 1,
        "legend.fontsize": base - 3,
        "xtick.labelsize": base - 3,
        "ytick.labelsize": base - 3,
        "axes.titlesize": base - 1,
    }
