# Purpose: This script provides a function to enrich the data using external sources or additional information to make it more valuable for analysis.

def enrich_data(data, demographics):
    """
    Function to enrich data with external demographic information.
    :param data: List of standardized data dictionaries.
    :param demographics: Dictionary mapping user IDs to demographic information.
    :return: List of enriched data dictionaries.
    """
    enriched_data = []

    for record in data:
        user_id = record.get('user_id')
        demographic_info = demographics.get(user_id, {})

        # Add demographic information to each record
        enriched_record = {**record, **demographic_info}
        enriched_data.append(enriched_record)

    return enriched_data
