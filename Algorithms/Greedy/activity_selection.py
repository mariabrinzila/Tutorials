def activity_selection(activities):
    """
    :param activities: the array of possible activities containing (start_time, finish_time) tuples
    :return: the array of activities a person can perform so that they perform a maximum number of
        activities
    """
    # Sort the activities array based on the finish time
    # In ascending order, so as many activities as possible can be selected
    activities.sort(key=lambda a: a[1])

    # The first activity to be selected is by default the first one in the sorted array of activities
    selected_activities = [activities[0]]
    activities_number = len(activities)

    # Traverse the sorted activities array and always choose the local optimal solution
    # Local optimal solution <=> an activity that starts after the lastly added one has finished
    for i in range(1, activities_number):
        activity = activities[i]
        start = activity[0]
        last_activity_finish = selected_activities[len(selected_activities) - 1][1]

        if last_activity_finish <= start:
            selected_activities.append(activity)

    return selected_activities
