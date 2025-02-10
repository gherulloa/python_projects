class TimeInterval:
    def __init__(self, hour: int, minute: int, second: int):
        if not all(isinstance(value, int) for value in (hour, minute, second)):
            raise TypeError("Only integers are accepted")
        if hour > 23 or minute > 59 or second > 59:
            raise ValueError("Invalid time")

        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def __add__(self, other):
        if not isinstance(other, TimeInterval) and not isinstance(other, int):
            raise TypeError("Only TimeInterval or int objects can be added")
        if isinstance(other, TimeInterval):
            total_seconds = (
                self.hour * 3600 + self.minute * 60 + self.second +
                other.hour * 3600 + other.minute * 60 + other.second
            )

            hour = (total_seconds // 3600) % 24
            minute = (total_seconds % 3600) // 60
            second = total_seconds % 60

            return TimeInterval(hour, minute, second)

        elif isinstance(other, int):
            total_seconds = (self.hour * 3600 + self.minute * 60 + self.second) + other
            
            hour = (total_seconds // 3600) % 24
            minute = (total_seconds % 3600) // 60
            second = total_seconds % 60

            return TimeInterval(hour, minute, second)  

    def __sub__(self, other):
        if not isinstance(other, TimeInterval) and not isinstance(other, int):
            raise TypeError("Only TimeInterval or int objects can be subtracted")
        if isinstance(other, TimeInterval):
            total_seconds = (
                (self.hour * 3600 + self.minute * 60 + self.second) - 
                (other.hour * 3600 + other.minute * 60 + other.second)
            )

            if total_seconds < 0:
                raise ValueError("Resulting time interval cannot be negative")
            
            hour = (total_seconds // 3600) % 24
            minute = (total_seconds % 3600) // 60
            second = total_seconds % 60

            return TimeInterval(hour, minute, second)
        elif isinstance(other, int):
            total_seconds = (self.hour * 3600 + self.minute * 60 + self.second) - other

            if total_seconds < 0:
                raise ValueError("Resulting time interval cannot be negative")
            
            hour = (total_seconds // 3600) % 24
            minute = (total_seconds % 3600) // 60
            second = total_seconds % 60

            return TimeInterval(hour, minute, second)
    
    def __mul__(self, num):
        if not isinstance(num, int):
            raise TypeError("Can only multiply by an integer")
        
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second

        total_seconds *= num

        hour = (total_seconds // 3600) % 24
        minute = (total_seconds % 3600) // 60
        second = total_seconds % 60

        return TimeInterval(hour, minute, second)
           
try:
    time = TimeInterval(21, 58, 50)
    time2 = TimeInterval(3, 16, 26)
    print(time + 62)  
    print(time - 62)  
    print(time * 2)  
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")