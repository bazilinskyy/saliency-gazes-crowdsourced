# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
# import matplotlib.pyplot as plt
# import matplotlib._pylab_helpers

import salgazes as sgz

sgz.logs(show_level='info', show_color=True)
logger = sgz.CustomLogger(__name__)  # use custom logger

# Const
SAVE_P = True  # save pickle files with data
LOAD_P = False  # load pickle files with data
SAVE_CSV = True  # load csv files with data
SHOW_OUTPUT = True  # should figures be plotted

if __name__ == '__main__':
    logger.info('Started programme from run.py')
