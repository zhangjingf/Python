import pandas as pd
import cufflinks as cf
import numpy as np
cf.set_config_file(offline=True)
cf.datagen.lines(1, 500).ta_plot(study='sma', periods=[13, 21, 55])