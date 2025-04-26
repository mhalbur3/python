class Television:
    """ A television class with power, channel, volume, and mute """
    MIN_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Default settings for television"""
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL
    def power(self) -> None:
        """Toggle for the power status"""
        self._status = not self._status
    def mute(self) -> None:
        """Toggle for the mute"""
        if self._status:
            self._muted = not self._muted
    def channel_up(self) -> None:
        """Channel number increase"""
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)
    def channel_down(self) -> None:
        """Channel number decrease"""
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)
    def volume_up(self) -> None:
        """Volume increases and then unmutes."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < self.MAX_VOLUME:
                self._volume += 1
    def volume_down(self) -> None:
        """Volume decreases and then unmutes."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """Returns the TV's current state, with volume starting with zero when muted"""
        vol_display = 0 if self._muted else self._volume
        return f'Power = {self._status}, Channel = {self._channel}, Volume = {vol_display}'