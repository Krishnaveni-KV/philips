from datetime import datetime
import pytz

# get the standard UTC time
USTZ = pytz.timezone('US/Central')
new =datetime.now(USTZ)

print(new)
