from pathlib import Path

import pandas as pd
import intake
import xarray as xr

app_dir = Path(__file__).parent

#test dataset
temp = xr.open_dataset(app_dir / 'time_series_temp_test.nc'
)



#here is where the variables will be changed

# Open original collection description file: CESM1 LENS
cat_url = "https://ncar-cesm-lens.s3-us-west-2.amazonaws.com/catalogs/aws-cesm1-le.json"
# open the catalog using the intake function
col = intake.open_esm_datastore(cat_url)
# Get more detailed: search for monthly output for the 20th century and RCP8.5 
col_ocntemp = col.search(
    frequency=["monthly"],
    component="ocn",
    variable="TEMP",
    experiment=["20C", "RCP85"],  # ("HIST" is the 1850-1919 period, which is only in the first ensemble member, and "20C" is 1920-2005 which is common across all the other members) 
)
# Load catalog entries for subset into a dictionary of xarray datasets
dsets = col_ocntemp.to_dataset_dict(
    zarr_kwargs={"consolidated": True}, storage_options={"anon": True}
)
ds_20C = dsets["ocn.20C.monthly"]


#Note: we need to replace the information in this .py doc with getting the data from the cesm server.
#we can do this later and see if it is easily replacable.