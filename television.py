class Television:
    MIN_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3

    def __init__(self):
        self._status, self._muted = False, False
        self._volume, self._channel = self.MIN_VOLUME, self.MIN_CHANNEL
    def power(self):
        self._status = not self._status
    def mute(self):
        if self._status:
            self._muted = not self._muted
    def channel_up(self):
        if self._status:
            self._channel += 1
            if self._channel > self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL
    def channel_down(self):
        if self._status:
            self._channel -= 1
            if self._channel < self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
    def volume_up(self):
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < self.MAX_VOLUME:
                self._volume += 1
    def volume_down(self):
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        return f'Power = {self._status}, Channel = {self._channel}, Volume = {0 if self._muted else self._volume}'