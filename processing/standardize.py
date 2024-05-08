# Purpose: This script will provide functions to standardize data across different formats and schemas. It ensures uniform data structures for further processing.

def standardize_impressions(impression_data):
    """
    Function to standardize ad impressions data.
    Expected input: a JSON-like dictionary containing impression information.
    """
    standardized_data = {
        'ad_id': impression_data.get('adCreativeId'),
        'user_id': impression_data.get('userId'),
        'timestamp': impression_data.get('timestamp'),
        'website': impression_data.get('website')
    }
    return standardized_data

def standardize_clicks(click_data):
    """
    Function to standardize clicks/conversions data.
    Expected input: a dictionary representing a row from the CSV file.
    """
    standardized_data = {
        'user_id': click_data.get('userID'),
        'campaign_id': click_data.get('adCampaignID'),
        'timestamp': click_data.get('timestamp'),
        'conversion_type': click_data.get('conversionType')
    }
    return standardized_data

def standardize_bids(bid_data):
    """
    Function to standardize bid request data.
    Expected input: a dictionary representing a record from an Avro file.
    """
    standardized_data = {
        'user_id': bid_data.get('user_id'),
        'auction_details': bid_data.get('auction_details'),
        'targeting_criteria': bid_data.get('targeting_criteria'),
        'timestamp': bid_data.get('timestamp')
    }
    return standardized_data
