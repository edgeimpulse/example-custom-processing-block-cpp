
from pathlib import Path
import sys

ROOT = Path(__file__).parent.parent
sys.path.append(str(ROOT))


from build import eicpp

arr = [ 3, 5, 7, 1 ]

print('min', eicpp.min(arr))
print('max', eicpp.max(arr))
print('avg', eicpp.avg(arr))
