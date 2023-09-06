from tqdm import tqdm as _tqdm
from functools import partial

tqdm = partial(_tqdm, dynamic_ncols=True)
