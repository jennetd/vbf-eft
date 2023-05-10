proc=$1

cmsDriver.py Configuration/GenProduction/python/${proc}-fragment.py --python_filename ${proc}_cfg.py --eventcontent NANOAODGEN \
--customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAOD \
--customise_commands "process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=123\nprocess.rivetProducerHTXS.ProductionMode='VBF'" \
--fileout file:${proc}_123.root --conditions 106X_mcRun2_asymptotic_v13 \
--beamspot Realistic25ns13TeV2016Collision --step LHE,GEN,NANOGEN --geometry DB:Extended --era Run2_2016 --no_exec --mc -n 1000
