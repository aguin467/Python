class Time:

    def _init_(self):
        self.hours = 0
        self.minutes = 0

my_time = Time()
my_time.hours = 7
my_time.minutes = 15


print('%d hours' % my_time.hours, end=' ')
print('and %d minutes' % my_time.minutes)
