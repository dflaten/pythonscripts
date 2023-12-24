from state import State

# Start of our states
class Intitating(State):
    """
    Preparing the data for processing.
    """

    def on_event(self, event):
        if event == 'pin_entered':
            return UnlockedState()

        return self


class Preprocessing(State):
    """
    The state which preprocessing of data occurs .
    """

    def on_event(self, event):
        if event == 'device_locked':
            return LockedState()

        return self