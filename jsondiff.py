import json
from deepdiff import DeepDiff





def detect_changes(before, after):
    # Convert JSON strings to Python dictionaries
    before_dict = before
    after_dict = after

    # Find the differences between the two dictionaries
    diff = DeepDiff(before_dict, after_dict, ignore_order=True)

    # Extract and print the changes
    added = diff.get("dictionary_item_added", {})
    deleted = diff.get("dictionary_item_removed", {})
    modified = diff.get("values_changed", {})

    changes = {
        "added": added,
        "deleted": deleted,
        "modified": modified
    }

    return changes



# Example usage:
# before_state = '{"name": "John", "age": 25, "city": "New York"}'
# after_state = '{"name": "John", "age": 30, "city": "San Francisco", "new_field": "value"}'
before_state = {
  "id": "50de9259-588b-4b1b-8995-6f29c2959502",
  "created_at": "2023-12-27T21:56:19.028924Z",
  "updated_at": "2023-12-28T19:59:24.114931Z",
  "mpesa_reference": "string",
  "phone_number": "string",
  "amount": 2147483647,
  "paybill_number": "string",
  "account_reference": "string",
  "transaction_reference_data": "{age: 25, city: New York, name: John}",
  "transaction_callback_data": "{}",
  "transaction_query_callback_data": "{}",
  "transaction_status": "PENDING"
}

after_state = {
  "id": "50de9259-588b-4b1b-8995-6f29c2959502",
  "created_at": "2023-12-27T21:56:19.028924Z",
  "updated_at": "2023-12-28T20:02:56.654608Z",
  "mpesa_reference": "string",
  "phone_number": "string",
  "amount": 2147483647,
  "paybill_number": "string",
  "account_reference": "string",
  "transaction_reference_data": "{age: 25, city: New York, name: Hosea}",
  "transaction_callback_data": "{}",
  "transaction_query_callback_data": "{}",
  "transaction_status": "COMPLETED"
}


changes = detect_changes(before_state, after_state)

print("Added:", changes["added"])
print("Deleted:", changes["deleted"])
print("Modified:", changes["modified"])


Added: {}
Deleted: {}
Modified: {
    "root['updated_at']": {
        'new_value': '2023-12-28T19:35:55.222476Z',
        'old_value': '2023-12-27T22:59:02.687298Z'
        },
    "root['mpesa_reference']": {
        'new_value': 'JDMX28011',
        'old_value': 'string'
    },
    "root['paybill_number']": {
        'new_value': '4044053',
        'old_value': 'string'
    }
}


{
   "root['updated_at']":{
      "new_value":"2023-12-28T20:02:56.654608Z",
      "old_value":"2023-12-28T19:59:24.114931Z"
   },
   "root['transaction_reference_data']":{
      "new_value":"{age: 25, city: New York, name: Hosea}",
      "old_value":"{age: 25, city: New York, name: John}"
   },
   "root['transaction_status']":{
      "new_value":"COMPLETED",
      "old_value":"PENDING"
   }
}