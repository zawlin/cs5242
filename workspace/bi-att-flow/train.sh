#!/bin/sh
python3 -m squad.prepro_nus
python3 -m basic.cli --mode train --noload --len_opt --cluster
