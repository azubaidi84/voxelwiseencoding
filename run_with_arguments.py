import sys
from run import main

#run.py ds002322-download/derivatives output --task alice --skip_bids_validator --participant_label 18 --preprocessing-config lagging_config.json --encoding-config encoding_config.json --detrend --standardize zscore

bids_dir = 'ds002322-download/derivatives'
output_dir = 'output'

# The label(s) of the participant(s) that should be analyzed. The label corresponds to
# sub-<participant_label> from the BIDS spec (so it does not include "sub-"). 
# If this parameter is not provided all subjects should be analyzed. Multiple 
# participants can be specified with a space separated list.
PARTICIPANT_LABEL = '18'
# Whether or not to perform BIDS dataset validation
SKIP_BIDS_VALIDATOR = True
# The label of the preprocessed data to use. Corresponds to label in desc-<label> 
# in the naming of the BOLD NifTIs. If not provided, assumes no derivative label
# is used.
DESC = None
# The task-label to use for training the voxel-wise encoding model. Corresponds 
# to label in task-<label> in BIDS naming.
TASK = 'alice'
# The label of the session to use. Corresponds to label in ses-<label> in the BIDS directory.
SES = None
# show program's version number and exit
VERSION = False
# The label of the stimulus recording to use. Corresponds to label in recording-<label> of the stimulus.
RECORDING = None
# Whether to linearly detrend fMRI data voxel-wise before training encoding models. Default is False.
DETREND = True
# How to voxel-wise standardize fMRI data before training encoding models. Default is no
# standardization, options are zscore for z-scoring and psc for computing percent signal change.
STANDARDIZE = 'zscore'
# Path to the preprocessing config file in JSON format. Parameters in this file 
# will be supplied as keyword arguments to the make_X_Y function.
PREPROCESSING_CONFIG = 'lagging_config.json'
# Path to the encoding config file in JSON format. Parameters in this file will 
# be supplied as keyword arguments to the get_ridge_plus_scores function.
ENCODING_CONFIG = 'encoding_config.json'
# Identifier to be included in the filenames for the encoding model output.
# Use this to differentiate different preprocessing steps or hyperparameters.
IDENTIFIER = None
# Flag to disable masking. This will lead to many non-brain voxels being included.
NO_MASKING = False
# Save preprocessing and model configuration together with model output.
LOG = False

sys.argv.extend([bids_dir, output_dir])
if PARTICIPANT_LABEL is not None:
    sys.argv.extend(['--participant_label', PARTICIPANT_LABEL])
if SKIP_BIDS_VALIDATOR:
    sys.argv.extend(['--skip_bids_validator'])
if DESC is not None:
    sys.argv.extend(['--desc', DESC])
if TASK is not None:
    sys.argv.extend(['--task', TASK])
if SES is not None:
    sys.argv.extend(['--ses', SES])
if VERSION:
    sys.argv.extend(['--version'])
if RECORDING is not None:
    sys.argv.extend(['--recording', RECORDING])
if DETREND:
    sys.argv.extend(['--detrend'])
if STANDARDIZE is not None:
    sys.argv.extend(['--standardize', STANDARDIZE])
if PREPROCESSING_CONFIG is not None:
    sys.argv.extend(['--preprocessing-config', PREPROCESSING_CONFIG])
if ENCODING_CONFIG is not None:
    sys.argv.extend(['--encoding-config', ENCODING_CONFIG])
if IDENTIFIER is not None:
    sys.argv.extend(['--identifier', IDENTIFIER])
if NO_MASKING:
    sys.argv.extend(['--no-masking '])
if LOG:
    sys.argv.extend(['--log'])

main()