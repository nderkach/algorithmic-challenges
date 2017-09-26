from itertools import islice

def merge_ranges(ranges):
    ranges.sort()
    merged_meetings = [ranges[0]]
    for cur_meeting_start, cur_meeting_end in islice(ranges, 1, None):
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        if cur_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, cur_meeting_end))
        else:
            merged_meetings.append((cur_meeting_start, cur_meeting_end))
    return merged_meetings


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (3, 10)]))