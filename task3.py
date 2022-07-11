def appearance(intervals):
    tutor_on_lesson_intervals = []
    total_sec_interval = 0
    for interval in range(1, len(intervals['tutor']) + 1, 2):
        if intervals['tutor'][interval] in range(intervals['lesson'][0], intervals['lesson'][1]) \
                or intervals['tutor'][interval - 1] in range(intervals['lesson'][0], intervals['lesson'][1]):
            tutor_on_lesson_intervals.append((max(intervals['lesson'][0], intervals['tutor'][interval - 1]),
                                              min(intervals['lesson'][1], intervals['tutor'][interval])))
    pupil_on_lesson_intervals = [(intervals['pupil'][0], intervals['pupil'][1])]
    for pupil_on_lesson in range(3, len(intervals['pupil']) + 1, 2):
        if intervals['pupil'][pupil_on_lesson - 1] \
                not in range(pupil_on_lesson_intervals[-1][0], pupil_on_lesson_intervals[-1][1]):
            pupil_on_lesson_intervals.append((intervals['pupil'][pupil_on_lesson - 1],
                                              intervals['pupil'][pupil_on_lesson]))
        elif intervals['pupil'][pupil_on_lesson] \
                not in range(pupil_on_lesson_intervals[-1][0], pupil_on_lesson_intervals[-1][1]+1):
            pupil_on_lesson_intervals.append(
                (pupil_on_lesson_intervals[-1][1],
                 max(pupil_on_lesson_intervals[-1][1], intervals['pupil'][pupil_on_lesson])))
    for tutor_interval in tutor_on_lesson_intervals:
        for pupil_interval in pupil_on_lesson_intervals:
            if pupil_interval[1] in range(tutor_interval[0], tutor_interval[1]) \
                    or pupil_interval[0] in range(tutor_interval[0], tutor_interval[1]):
                first = max(tutor_interval[0], pupil_interval[0])
                second = min(tutor_interval[1], pupil_interval[1])
            else:
                continue
            total_sec_interval += second - first

    return total_sec_interval
