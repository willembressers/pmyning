# python core packages
from pathlib import Path

# 3rd party packages
import pandas as pd
from opyenxes.data_in.XUniversalParser import XUniversalParser


def read_xes(file_path: Path) -> pd.DataFrame:
    """Reads the given file path into pandas DataFrame.

    Examples:
        >>> import pmyning as pmy
        >>> df = pmy.read_xes(Path("assets/general_example.xes"))

    Parameters
    ----------
    filepath : Path
        The path to the given xes file.

    Returns
    -------
    pd.DataFrame
        _description_

    Raises
    ------
    Exception
        _description_
    """

    # check of the filepath exists
    if not file_path.exists():
        raise Exception("File does not exist")

    # read the file
    xlog = XUniversalParser().parse(file_path)[0]

    # collect the event data here
    events = []

    # loop over the traces
    for xtrace in xlog:
        # loop over the events (in each trace)
        for event in xtrace:
            data = {}

            # add the trace data
            for key, value in xtrace.get_attributes().items():
                data[f"trace:{key}"] = value.get_value()

            # add the event data
            for key, value in event.get_attributes().items():
                data[f"event:{key}"] = value.get_value()

            # add the data to the list
            events.append(data)

    return pd.DataFrame(events)
