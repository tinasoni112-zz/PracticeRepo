def count_past_events(series, timeline):
    import pandas as pd
    past_events = pd.Series(series.index, index = series, name="past_events").sort_index()
    past_timeline_events  = past_events.rolling(timeline).count()
    return past_timeline_events