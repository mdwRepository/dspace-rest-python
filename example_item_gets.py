# This software is licenced under the BSD 3-Clause licence
# available at https://opensource.org/licenses/BSD-3-Clause
# and described in the LICENCE file in the root of this project

"""
Example Python 3 application using the dspace.py API client library to demonstrate
various GET functionalities for items in a DSpace 7 repository.
"""
from pprint import pprint

import os
import sys

from dspace_rest_client.client import DSpaceClient
from dspace_rest_client.models import Item

DEFAULT_URL = "https://localhost:8080/server/api"
DEFAULT_USERNAME = "username@test.system.edu"
DEFAULT_PASSWORD = "password"

# UUID of the item to retrieve
ITEM_UUID = "0128787c-6f79-4661-aea4-11635d6fb04f"

# Configuration from environment variables
URL = os.environ.get("DSPACE_API_ENDPOINT", DEFAULT_URL)
USERNAME = os.environ.get("DSPACE_API_USERNAME", DEFAULT_USERNAME)
PASSWORD = os.environ.get("DSPACE_API_PASSWORD", DEFAULT_PASSWORD)

# Instantiate DSpace client
d = DSpaceClient(
    api_endpoint=URL, username=USERNAME, password=PASSWORD, fake_user_agent=True
)

# Authenticate against the DSpace client
authenticated = d.authenticate()
if not authenticated:
    print("Error logging in! Giving up.")
    sys.exit(1)

# Retrieve item by UUID
item = d.get_item(uuid=ITEM_UUID)
if not item:
    print(f"Item with UUID {ITEM_UUID} not found!")
    sys.exit(1)

print("Retrieved Item:")
pprint(item.as_dict())

# Get item metrics
metrics = d.get_item_metrics(item)
print("\nItem Metrics:")
pprint(metrics if metrics else "No metrics available.")

# Get item thumbnail
thumbnail = d.get_item_thumbnail(item)
print("\nItem Thumbnail:")
pprint(thumbnail if thumbnail else "No thumbnail available.")

# Get item owning collection
owning_collection = d.get_item_owning_collection(item)
print("\nOwning Collection:")
pprint(
    owning_collection.as_dict() if owning_collection else "No owning collection found."
)

# Get item mapped collections
mapped_collections = d.get_item_mapped_collections(item)
print("\nMapped Collections:")
pprint(mapped_collections if mapped_collections else "No mapped collections available.")

# Get item relationships
relationships = d.get_item_relationships(item)
print("\nItem Relationships:")
pprint(relationships if relationships else "No relationships found.")

# Get item access status
access_status = d.get_item_access_status(item)
print("\nItem Access Status:")
pprint(access_status if access_status else "No access status available.")
