from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.requestName = 'VBF_SMEFTsim_topU3l_NP1_NPNP1'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'VBF_SMEFTsim_topU3l_NP1_NPNP1.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1
config.JobType.pyCfgParams = ['gridpack=../Quad_VBF_SMEFTsim_topU3l_NP1_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz']

config.section_("Data")
config.Data.outputPrimaryDataset = 'VBF_SMEFTsim_topU3l_NP1_NPNP1'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000 #0
NJOBS = 200  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/jdickins/vbf-eft/'
config.Data.publication = True
config.Data.outputDatasetTag = 'VBF_SMEFTsim_topU3l_NP1_NPNP1'

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
