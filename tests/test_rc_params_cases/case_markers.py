"""Test cases for markers."""

from tueplots import markers


def case_markers_with_edge_default():
    return markers.with_edge()


def case_markers_with_edge_custom():
    return markers.with_edge(edgecolor="green", edgewidth=1.0)


def case_markers_inverted_default():
    return markers.inverted()


def case_markers_inverted_custom():
    return markers.inverted(facecolor="green", edgewidth=1.0)
