from utils import stats
import numpy as np
from configs.configs import config
pred = np.load('../pred_'+config.mode+'_main3.npy')
true = np.load('../true_'+config.mode+'_main3.npy')
stats(pred, true, 0.2992)
